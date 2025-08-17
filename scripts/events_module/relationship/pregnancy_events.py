import random
from random import choice, randint
from typing import Dict, List, Union, Optional

import i18n

from scripts.cat.cats import Cat
from scripts.cat.enums import CatAge, CatGroup, CatRank, CatSocial
from scripts.cat.names import names, Name
from scripts.cat_relations.relationship import Relationship, RelType
from scripts.clan_package.settings import get_clan_setting
from scripts.event_class import Single_Event
from scripts.events_module.short.condition_events import Condition_Events
from scripts.game_structure import constants
from scripts.game_structure import game
from scripts.game_structure.localization import load_lang_resource
from scripts.utility import (
    create_new_cat,
    get_highest_romantic_relation,
    event_text_adjust,
    get_personality_compatibility,
    change_relationship_values,
    find_alive_cats_with_rank,
    adjust_list_text,
)


class Pregnancy_Events:
    """All events which are related to pregnancy such as kitting and defining who are the parents."""

    biggest_family = {}
    PREGNANT_STRINGS: Optional[Dict[str, Union[List, Dict[str, List]]]] = {}
    currently_loaded_lang: str = None

    @staticmethod
    def rebuild_strings():
        if Pregnancy_Events.currently_loaded_lang == i18n.config.get("locale"):
            return
        Pregnancy_Events.PREGNANT_STRINGS = load_lang_resource(
            "conditions/pregnancy.json"
        )
        Pregnancy_Events.currently_loaded_lang = i18n.config.get("locale")

    @staticmethod
    def set_biggest_family():
        """Gets the biggest family of the clan."""
        biggest_family = None
        for cat in Cat.all_cats.values():
            ancestors = cat.get_relatives()
            if not biggest_family:
                biggest_family = ancestors
                biggest_family.append(cat.ID)
            elif len(biggest_family) < len(ancestors) + 1:
                biggest_family = ancestors
                biggest_family.append(cat.ID)
        Pregnancy_Events.biggest_family = biggest_family

    @staticmethod
    def biggest_family_is_big():
        """Returns if the current biggest family is big enough to 'activates' additional inbreeding counters."""

        living_cats = len(
            [i for i in Cat.all_cats.values() if i.status.alive_in_player_clan]
        )
        return len(Pregnancy_Events.biggest_family) > (living_cats / 10)

    @staticmethod
    def handle_pregnancy_age(clan):
        """Increase the moon for each pregnancy in the pregnancy dictionary"""
        for pregnancy_key in clan.pregnancy_data.keys():
            clan.pregnancy_data[pregnancy_key]["moons"] += 1

    @staticmethod
    def handle_having_kits(cat, clan):
        """Handles pregnancy of a cat."""
        if not clan:
            return

        if not Pregnancy_Events.biggest_family:
            Pregnancy_Events.set_biggest_family()

        # Handles if a cat is already pregnant
        if cat.ID in clan.pregnancy_data:
            moons = clan.pregnancy_data[cat.ID]["moons"]
            if moons == 1:
                Pregnancy_Events.handle_one_moon_pregnant(cat, clan)
                return
            if moons >= 2:
                if "pregnant" in cat.injuries:
                    Pregnancy_Events.handle_two_moon_pregnant(cat, clan)
                    # events.ceremony_accessory = True
                    return
                else:
                    second_parent_id = clan.pregnancy_data[cat.ID]["second_parent"]
                    second_parent = Cat.all_cats.get(second_parent_id)
                    Pregnancy_Events.handle_adoption(cat, second_parent, clan)
                    return

        if cat.status.is_outsider:
            return

        # Handle birth cooldown outside of the check_if_can_have_kits function, so it only happens once
        # for each cat.
        if cat.birth_cooldown > 0:
            cat.birth_cooldown -= 1

        # Check if they can have kits.
        can_have_kits = Pregnancy_Events.check_if_can_have_kits(
            cat, get_clan_setting("single parentage"), get_clan_setting("affair")
        )
        if not can_have_kits:
            return

        false_preg = 0
        #Determine if a cat will have a false pregnancy
        if get_clan_setting("pregnancy turmoil"):
            odds = constants.CONFIG["pregnancy"]["false_pregnancy_chance"]
            if "infertile" in cat.permanent_condition:
                odds = int(odds / 1.5)
            false_preg = random.randint(1, odds)

        # DETERMINE THE SECOND PARENT
        # check if there is a cat in the clan for the second parent
        second_parent, is_affair = Pregnancy_Events.get_second_parent(cat, clan)

        # check if the second_parent is not none and if they also can have kits
        can_have_kits, kits_are_adopted = Pregnancy_Events.check_second_parent(
            cat,
            second_parent,
            get_clan_setting("single parentage"),
            get_clan_setting("affair"),
            get_clan_setting("inter-species birth"),
            get_clan_setting("same sex birth"),
            get_clan_setting("same sex adoption"),
        )
        if second_parent:
            if not can_have_kits:
                return
        else:
            if not get_clan_setting("single parentage"):
                return

        chance = Pregnancy_Events.get_balanced_kit_chance(
            cat, second_parent, is_affair, clan
        )

        if not int(random.random() * chance):
            # If you've reached here - congrats, kits!
            if false_preg == 1:
                Pregnancy_Events.handle_zero_moon_false(cat, second_parent, clan)
            if kits_are_adopted:
                Pregnancy_Events.handle_adoption(cat, second_parent, clan)
            else:
                Pregnancy_Events.handle_zero_moon_pregnant(cat, second_parent, clan)

    # ---------------------------------------------------------------------------- #
    #                                 handle events                                #
    # ---------------------------------------------------------------------------- #

    @staticmethod
    def handle_adoption(cat: Cat, other_cat=None, clan=game.clan):
        """Handle if the there is no pregnancy but the pair triggered kits chance."""
        if other_cat and (
            not other_cat.status.alive_in_player_clan or other_cat.birth_cooldown > 0
        ):
            return

        if cat.ID in clan.pregnancy_data:
            if "faux pregnant" not in cat.injuries:
                return

        if other_cat and other_cat.ID in clan.pregnancy_data:
            return

        # Gather adoptive parents, to feed into the
        # get kits function.
        adoptive_parents = [cat.ID]
        cats_involved = [cat.ID]

        if other_cat:
            adoptive_parents.append(other_cat.ID)

        for _m in cat.mate:
            if _m not in adoptive_parents:
                adoptive_parents.append(_m)

        if other_cat:
            for _m in other_cat.mate:
                if _m not in adoptive_parents:
                    adoptive_parents.append(_m)

        amount = Pregnancy_Events.get_amount_of_kits(cat)
        kits = Pregnancy_Events.get_kits(
            amount, None, None, clan, adoptive_parents=adoptive_parents
        )

        insert = i18n.t("conditions.pregnancy.kit_amount", count=amount)

        # choose event string
        # TODO: currently they don't choose which 'mate' is the 'blood' parent or not
        # change or leaf as it is?
        Pregnancy_Events.rebuild_strings()
        events = Pregnancy_Events.PREGNANT_STRINGS
        event_list = []
        if not cat.outside and other_cat is None:
            event_list.append(choice(events["adoption"]["unmated_parent"]))
        elif other_cat.ID in cat.mate and not other_cat.dead and not other_cat.outside:
            cats_involved.append(other_cat.ID)
            event_list.append(choice(events["adoption"]["two_parents"]))
        elif other_cat.ID in cat.mate and other_cat.dead or other_cat.outside:
            cats_involved.append(other_cat.ID)
            event_list.append(choice(events["adoption"]["dead_mate"]))
        elif len(cat.mate) < 1 and len(other_cat.mate) < 1 and not other_cat.dead:
            cats_involved.append(other_cat.ID)
            event_list.append(choice(events["adoption"]["both_unmated"]))
        elif (
            len(cat.mate) > 0 and other_cat.ID not in cat.mate and not other_cat.dead
        ) or (len(other_cat.mate) > 0 and cat.ID not in other_cat.mate and not other_cat.dead
        ):
            cats_involved.append(other_cat.ID)
            event_list.append(choice(events["adoption"]["affair"]))
        else:
            event_list.append(choice(events["adoption"]["unmated_parent"]))

        if clan.game_mode != "classic" and not cat.dead and "faux pregnant" in cat.injuries:
            cat.injuries.pop("faux pregnant")
                
        print_event = " ".join(event_list)
        print_event = print_event.replace("{insert}", insert)

        print_event = event_text_adjust(Cat, print_event, main_cat=cat, random_cat=other_cat, clan=game.clan)

        cats_involved = {"m_c": cat}
        if other_cat:
            cats_involved["r_c"] = other_cat
        for kit in kits:
            kit.thought = "hardcoded.new_kit_thought"
            kit.thought = event_text_adjust(Cat, kit.thought, random_cat=cat)

        # Normally, birth cooldown is only applied to cat who gave birth
        # However, if we don't apply birth cooldown to adoption, we get
        # too much adoption, since adoptive couples are using the increased two-parent
        # kits chance. We will only apply it to "cat" in this case
        # which is enough to stop the couple from adopting about within
        # the window.
        cat.birth_cooldown = constants.CONFIG["pregnancy"]["birth_cooldown"]

        game.cur_events_list.append(
            Single_Event(print_event, "birth_death", cat_dict=cats_involved)
        )

    @staticmethod
    def handle_zero_moon_false(cat: Cat, other_cat=None, clan=game.clan):
        """Handles if the cat is having a false pregnancy"""
        if other_cat and (
            other_cat.dead or other_cat.outside or other_cat.birth_cooldown > 0
        ):
            return

        if cat.ID in clan.pregnancy_data:
            return

        if other_cat and other_cat.ID in clan.pregnancy_data:
            return

        # additional save for no kit setting, since we(I) don't want them rolling for it.
        if (cat and (cat.no_kits or cat.neutered)) or (other_cat and (other_cat.no_kits or other_cat.neutered)):
            return
        
        if not get_clan_setting("same sex birth") and cat.gender == "male":
            return

        Pregnancy_Events.rebuild_strings()
        
        clan.pregnancy_data[cat.ID] = {
            "second_parent": str(other_cat.ID) if other_cat else None,
            "moons": 0,
            "amount": 0,
        }

        text = choice(Pregnancy_Events.PREGNANT_STRINGS["false_preg announcement"])
        if clan.game_mode != "classic":
            severity = random.choices(["minor", "major"], [10, 1], k=1)
            cat.get_injured("faux pregnant", severity=severity[0])
            text += choice(Pregnancy_Events.PREGNANT_STRINGS[f"{severity[0]}_severity"])
        text = event_text_adjust(Cat, text, main_cat=cat, clan=game.clan)

        game.cur_events_list.append(Single_Event(text, "birth_death", cat.ID))
        return   

    @staticmethod
    def handle_zero_moon_pregnant(cat: Cat, other_cat=None, clan=game.clan):
        """Handles if the cat is zero moons pregnant."""
        if other_cat and (
            not other_cat.status.alive_in_player_clan or other_cat.birth_cooldown > 0
        ):
            return

        if cat.ID in clan.pregnancy_data:
            return

        if other_cat and other_cat.ID in clan.pregnancy_data:
            return

        # additional save for no kit setting
        if (cat and (cat.no_kits or cat.neutered)) or (other_cat and (other_cat.no_kits or other_cat.neutered)):
            return

        # Null Cats will only Adopt
        if (cat and cat.gender == "null") or (other_cat and other_cat.gender == "null"):
            return

        Pregnancy_Events.rebuild_strings()

        if get_clan_setting("same sex birth"):
            # 50/50 for single cats to get pregnant or just bring a litter back
            if not other_cat and random.randint(0, 1):
                amount = Pregnancy_Events.get_amount_of_kits(cat)
                stillborn_chance = 0

                if get_clan_setting("pregnancy turmoil"):
                    if amount <= 3:
                        stillborn_chance = constants.CONFIG["pregnancy"]["stillborn_chances"]["tiny"]
                    elif amount <= 6:
                        stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["small"]
                    elif amount <= 9:
                        stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["large"]
                    elif amount <= 14:
                        stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["huge"]
                    else:
                        stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["ridiculous"]
                stillborn_count = 0
                kits = Pregnancy_Events.get_kits(amount, cat, None, clan)
                for kit in kits:
                    if random.random() <= stillborn_chance:
                        kit.dead = True
                        History.add_death(kit, str(kit.name) + " was stillborn.")
                        kits.remove(kit)
                        stillborn_count += 1

                print_event = i18n.t(
                    choice(Pregnancy_Events.PREGNANT_STRINGS["birth"]["affair_outsider"]),
                    insert=i18n.t("conditions.pregnancy.kit_amount", count=amount),
                )
                cats_involved = [cat.ID]
                cat_dict = {"m_c": cat}
                for kit in kits:
                    cats_involved.append(kit.ID)
                
                if stillborn_count != 0:
                    print_event += i18n.t(
                        "conditions.pregnancy.pregnant_stillbirth",
                        name=cat.name,
                        insert=i18n.t("conditions.pregnancy.stillborn_amount", count=stillborn_count),
                    )
                    cat.get_ill("grief stricken", event_triggered=True)  
                    
                print_event = event_text_adjust(Cat, print_event, main_cat=cat, clan=game.clan)
                game.cur_events_list.append(
                    Single_Event(
                        print_event, "birth_death", cats_involved, cat_dict=cat_dict
                    )
                )
                return

            # same sex birth enables all cats to get pregnant,
            # therefore the main cat will be used, regarding of gender
            clan.pregnancy_data[cat.ID] = {
                "second_parent": str(other_cat.ID) if other_cat else None,
                "moons": 0,
                "amount": 0,
            }
            text = choice(Pregnancy_Events.PREGNANT_STRINGS["announcement"])
            severity = random.choices(["minor", "major"], [3, 1], k=1)
            cat.get_injured("pregnant", severity=severity[0])
            text += choice(Pregnancy_Events.PREGNANT_STRINGS[f"{severity[0]}_severity"])

            text = event_text_adjust(Cat, text, main_cat=cat, clan=clan)
            game.cur_events_list.append(
                Single_Event(text, "birth_death", cat.ID, cat_dict={"m_c": cat})
            )
        else:
            if not other_cat and cat.gender == "male":
                amount = Pregnancy_Events.get_amount_of_kits(cat)
                stillborn_chance = 0

                if get_clan_setting("pregnancy turmoil"):
                    if amount <= 3:
                        stillborn_chance = constants.CONFIG["pregnancy"]["stillborn_chances"]["tiny"]
                    elif amount <= 6:
                        stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["small"]
                    elif amount <= 9:
                        stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["large"]
                    elif amount <= 14:
                        stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["huge"]
                    else:
                        stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["ridiculous"]
                stillborn_count = 0
                kits = Pregnancy_Events.get_kits(amount, cat, None, clan)
                for kit in kits:
                    if random.random() <= stillborn_chance:
                        kit.dead = True
                        History.add_death(kit, str(kit.name) + " was stillborn.")
                        kits.remove(kit)
                        stillborn_count += 1

                print_event = i18n.t(
                    choice(Pregnancy_Events.PREGNANT_STRINGS["birth"]["affair_outsider"]),
                    insert=i18n.t("conditions.pregnancy.kit_amount", count=amount),
                )
                cats_involved = [cat.ID]
                cat_dict = {"m_c": cat}
                for kit in kits:
                    cats_involved.append(kit.ID)
                
                if stillborn_count != 0:
                    print_event += i18n.t(
                        "conditions.pregnancy.pregnant_stillbirth",
                        name=cat.name,
                        insert=i18n.t("conditions.pregnancy.stillborn_amount", count=stillborn_count),
                    )
                    cat.get_ill("grief stricken", event_triggered=True)  
                    
                print_event = event_text_adjust(Cat, print_event, main_cat=cat, clan=game.clan)
                game.cur_events_list.append(
                    Single_Event(
                        print_event, "birth_death", cats_involved, cat_dict=cat_dict
                    )
                )
                return
            if not other_cat and cat.gender == 'intersex': 
            #Intersex cats result will be determined by their intersex condition if they have one. 
                if cat.permanent_condition != ["mosaicism", "aneuploidy", "excess testosterone", "testosterone deficiency"]:
                    if random.randint(0,1):
                        amount = Pregnancy_Events.get_amount_of_kits(cat)
                        stillborn_chance = 0

                        if get_clan_setting("pregnancy turmoil"):
                            if amount <= 3:
                                stillborn_chance = constants.CONFIG["pregnancy"]["stillborn_chances"]["tiny"]
                            elif amount <= 6:
                                stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["small"]
                            elif amount <= 9:
                                stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["large"]
                            elif amount <= 14:
                                stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["huge"]
                            else:
                                stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["ridiculous"]
                        stillborn_count = 0
                        kits = Pregnancy_Events.get_kits(amount, cat, None, clan)
                        for kit in kits:
                            if random.random() <= stillborn_chance:
                                kit.dead = True
                                History.add_death(kit, str(kit.name) + " was stillborn.")
                                kits.remove(kit)
                                stillborn_count += 1

                        print_event = i18n.t(
                            choice(Pregnancy_Events.PREGNANT_STRINGS["birth"]["affair_outsider"]),
                            insert=i18n.t("conditions.pregnancy.kit_amount", count=amount),
                        )
                        cats_involved = [cat.ID]
                        cat_dict = {"m_c": cat}
                        for kit in kits:
                            cats_involved.append(kit.ID)
                        
                        if stillborn_count != 0:
                            print_event += i18n.t(
                                "conditions.pregnancy.pregnant_stillbirth",
                                name=cat.name,
                                insert=i18n.t("conditions.pregnancy.stillborn_amount", count=stillborn_count),
                            )
                            cat.get_ill("grief stricken", event_triggered=True)  
                            
                        print_event = event_text_adjust(Cat, print_event, main_cat=cat, clan=game.clan)
                        game.cur_events_list.append(
                            Single_Event(
                                print_event, "birth_death", cats_involved, cat_dict=cat_dict
                            )
                        )
                        return
                    clan.pregnancy_data[cat.ID] = {
                        "second_parent": str(other_cat.ID) if other_cat else None,
                        "moons": 0,
                        "amount": 0,
                    }
                    text = choice(Pregnancy_Events.PREGNANT_STRINGS["announcement"])
                    severity = random.choices(["minor", "major"], [3, 1], k=1)
                    cat.get_injured("pregnant", severity=severity[0])
                    text += choice(Pregnancy_Events.PREGNANT_STRINGS[f"{severity[0]}_severity"])

                    text = event_text_adjust(Cat, text, main_cat=cat, clan=clan)
                    game.cur_events_list.append(
                        Single_Event(text, "birth_death", cat.ID, cat_dict={"m_c": cat})
                    )
                    return

                elif cat.permanent_condition in ["mosaicism", "testosterone deficiency"]:
                    amount = Pregnancy_Events.get_amount_of_kits(cat)
                    stillborn_chance = 0

                    if get_clan_setting("pregnancy turmoil"):
                        if amount <= 3:
                            stillborn_chance = constants.CONFIG["pregnancy"]["stillborn_chances"]["tiny"]
                        elif amount <= 6:
                            stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["small"]
                        elif amount <= 9:
                            stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["large"]
                        elif amount <= 14:
                            stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["huge"]
                        else:
                            stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["ridiculous"]
                    stillborn_count = 0
                    kits = Pregnancy_Events.get_kits(amount, cat, None, clan)
                    for kit in kits:
                        if random.random() <= stillborn_chance:
                            kit.dead = True
                            History.add_death(kit, str(kit.name) + " was stillborn.")
                            kits.remove(kit)
                            stillborn_count += 1

                    print_event = i18n.t(
                        choice(Pregnancy_Events.PREGNANT_STRINGS["birth"]["affair_outsider"]),
                        insert=i18n.t("conditions.pregnancy.kit_amount", count=amount),
                    )
                    cats_involved = [cat.ID]
                    cat_dict = {"m_c": cat}
                    for kit in kits:
                        cats_involved.append(kit.ID)
                    
                    if stillborn_count != 0:
                        print_event += i18n.t(
                            "conditions.pregnancy.pregnant_stillbirth",
                            name=cat.name,
                            insert=i18n.t("conditions.pregnancy.stillborn_amount", count=stillborn_count),
                        )
                        cat.get_ill("grief stricken", event_triggered=True)  
                        
                    print_event = event_text_adjust(Cat, print_event, main_cat=cat, clan=game.clan)
                    game.cur_events_list.append(
                        Single_Event(
                            print_event, "birth_death", cats_involved, cat_dict=cat_dict
                        )
                    )
                    return
                else:
                    clan.pregnancy_data[cat.ID] = {
                        "second_parent": str(other_cat.ID) if other_cat else None,
                        "moons": 0,
                        "amount": 0,
                    }
                    text = choice(Pregnancy_Events.PREGNANT_STRINGS["announcement"])
                    severity = random.choices(["minor", "major"], [3, 1], k=1)
                    cat.get_injured("pregnant", severity=severity[0])
                    text += choice(Pregnancy_Events.PREGNANT_STRINGS[f"{severity[0]}_severity"])

                    text = event_text_adjust(Cat, text, main_cat=cat, clan=clan)
                    game.cur_events_list.append(
                        Single_Event(text, "birth_death", cat.ID, cat_dict={"m_c": cat})
                    )
                    return                    
            # if the other cat is afab and the current cat is amab, make the afab cat pregnant
            pregnant_cat = cat
            second_parent = other_cat
            if (
                cat.gender == "male"
                and other_cat is not None
                and other_cat.gender == "female"
            ):
                pregnant_cat = other_cat
                second_parent = cat
            elif (
                cat.gender == "male" 
                and other_cat is not None 
                and other_cat.gender == "intersex"
            ):
                if other_cat.permanent_condition != ["mosaicism", "testosterone deficiency"]:
                    pregnant_cat = other_cat
                    second_parent = cat                  
                else:
                    return
            elif (
                cat.gender == "intersex" 
                and other_cat is not None 
                and other_cat.gender == "female"
            ):
                if cat.permanent_condition != ["aneuploidy", "excess testosterone"]:
                    pregnant_cat = other_cat
                    second_parent = cat                 
                else:
                    return
            elif (
                cat.gender == "intersex" 
                and other_cat is not None 
                and other_cat.gender == "intersex"
            ):
                if other_cat.permanent_condition != ["mosaicism", "testosterone deficiency"] and cat.permanent_condition != ["aneuploidy", "excess testosterone"]:
                    pregnant_cat = other_cat
                    second_parent = cat
                else:
                    return
            elif (
                "mosaicism" in cat.permanent_condition
                and other_cat is not None
                and other_cat.gender == "female"
            ):
                pregnant_cat = other_cat
                second_parent = cat

            clan.pregnancy_data[pregnant_cat.ID] = {
                "second_parent": str(second_parent.ID) if second_parent else None,
                "moons": 0,
                "amount": 0,
            }

            text = choice(Pregnancy_Events.PREGNANT_STRINGS["announcement"])
            severity = random.choices(["minor", "major"], [3, 1], k=1)
            pregnant_cat.get_injured("pregnant", severity=severity[0])
            text += choice(Pregnancy_Events.PREGNANT_STRINGS[f"{severity[0]}_severity"])
            text = event_text_adjust(Cat, text, main_cat=pregnant_cat, clan=clan)
            game.cur_events_list.append(
                Single_Event(
                    text, "birth_death", pregnant_cat.ID, cat_dict={"m_c": cat}
                )
            )

    @staticmethod
    def handle_one_moon_pregnant(cat: Cat, clan=game.clan):
        """Handles if the cat is one moon pregnant."""
        if cat.ID not in clan.pregnancy_data.keys():
            return

        # if the pregnant cat killed meanwhile, delete it from the dictionary
        if cat.dead:
            del clan.pregnancy_data[cat.ID]
            return

        amount = Pregnancy_Events.get_amount_of_kits(cat)
        text = "This should not appear (pregnancy_events.py)"

        # add the amount to the pregnancy dict
        clan.pregnancy_data[cat.ID]["amount"] = amount

        # if the cat is outside of the clan, they won't guess how many kits they will have
        if cat.status.is_outsider:
            return

        if "faux pregnant" in cat.injuries:
            if cat.gender == "male":
                failure = constants.CONFIG["pregnancy"]["failed_adopt"]["male"]
            elif cat.gender == "female":
                failure = constants.CONFIG["pregnancy"]["failed_adopt"]["female"]
            else:
                failure = constants.CONFIG["pregnancy"]["failed_adopt"]["intersex"]                

            if random.random() <= failure:
                text = choice(Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["empty_nest"])
                cat.injuries.pop("faux pregnant")
                cat.get_ill("grief stricken", event_triggered=True)             
            else:    
                text = choice(Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["adoption_announce"])            

            text = event_text_adjust(Cat, text, main_cat=cat, clan=game.clan)
            game.cur_events_list.append(Single_Event(text, "birth_death", cat.ID))
            return

        thinking_amount = random.choices(
            ["correct", "incorrect", "unsure", "exact"], [3, 5, 3, 2], k=1
        )
        if amount <= constants.CONFIG["pregnancy"]["small_litter"]:
            correct_guess = "small"
        elif amount >= constants.CONFIG["pregnancy"]["huge_litter"]:
            correct_guess = "huge"
        else:
            correct_guess = "large"

        Pregnancy_Events.rebuild_strings()

        if thinking_amount[0] == "correct":
            if correct_guess == "small":
                text = choice(Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["small_litter"])
            elif correct_guess == "huge":
                text = choice(Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["huge_litter"])
            else:
                text = choice(Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["large_litter"])
        elif thinking_amount[0] == "incorrect":
            if correct_guess == "small":
                text = choice(Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["large_litter"] + 
                        Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["huge_litter"])              
            elif correct_guess == "huge":
                text = choice(Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["large_litter"] + 
                        Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["small_litter"] + 
                        Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["single_kitten"])                    
            else:
                text = choice(Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["huge_litter"] + 
                        Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["small_litter"] + 
                        Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["single_kitten"])      
        elif thinking_amount[0] == "exact":
            thinking_amount = choice([amount - random.randint(1, 6), amount, amount + random.randint(1, 6)])
            if thinking_amount < 1:
                thinking_amount = 1
            if thinking_amount == 1:
                text = Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["single_kitten"]    
            else:
                text = i18n.t(
                                "conditions.pregnancy.pregnant_exact",
                                name=cat.name,
                                insert=i18n.t("conditions.pregnancy.kit_amount", count=thinking_amount),
                            )
        else:
            text = choice(Pregnancy_Events.PREGNANT_STRINGS["litter_guesses"]["unsure_litter_guess"])

        try:
            if cat.injuries["pregnant"]["severity"] == "minor":
                cat.injuries["pregnant"]["severity"] = "major"
                text += choice(Pregnancy_Events.PREGNANT_STRINGS["major_severity"])
        except:
            print("Is this an old save? Cat does not have the pregnant condition")

        text = event_text_adjust(Cat, text, main_cat=cat, clan=game.clan)
        game.cur_events_list.append(
            Single_Event(text, "birth_death", cat_dict={"m_c": cat})
        )

    @staticmethod
    def handle_two_moon_pregnant(cat: Cat, clan=game.clan):
        """Handles if the cat is two moons pregnant."""
        if cat.ID not in clan.pregnancy_data.keys():
            return

        # if the pregnant cat is killed meanwhile, delete it from the dictionary
        if cat.dead:
            del clan.pregnancy_data[cat.ID]
            return

        involved_cats = [cat.ID]
        cat_dict = {"m_c": cat}

        kits_amount = clan.pregnancy_data[cat.ID]["amount"]
        if (
            kits_amount == 0
        ):  # safety check, sometimes pregnancies were ending up with 0 due to save rollbacks
            kits_amount = 1

        if get_clan_setting("pregnancy turmoil"):
            turmoil = random.randint(1, 100)
            if turmoil <= 20:
                cat.get_injured("turmoiled litter", event_triggered=True)
            if kits_amount <= 3:
                stillborn_chance = constants.CONFIG["pregnancy"]["stillborn_chances"]["tiny"]
            elif kits_amount <= 6:
                stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["small"]
            elif kits_amount <= 9:
                stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["large"]
            elif kits_amount <= 14:
                stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["huge"]
            else:
                stillborn_chance = game.config["pregnancy"]["stillborn_chances"]["ridiculous"]

        kits = Pregnancy_Events.get_kits(kits_amount, cat, None, clan)
        stillborn_count = 0
        for kit in kits:
            if random.random() <= stillborn_chance:
                kit.dead = True
                History.add_death(kit, str(kit.name) + " was stillborn.")
                kits.remove(kit)
                stillborn_count += 1

        other_cat_id = clan.pregnancy_data[cat.ID]["second_parent"]
        other_cat = Cat.all_cats.get(other_cat_id)

        kits = Pregnancy_Events.get_kits(kits_amount, cat, other_cat, clan)
        kits_amount = len(kits)
        Pregnancy_Events.set_biggest_family()

        # delete the cat out of the pregnancy dictionary
        del clan.pregnancy_data[cat.ID]

        if cat.status.is_outsider:
            for kit in kits:
                kit.status.generate_new_status(
                    age=kit.age, social=cat.status.social, group=cat.status.group
                )
                kit.backstory = "outsider1"

                if cat.status.is_exiled(CatGroup.PLAYER_CLAN):
                    name = choice(names.names_dict["normal_prefixes"])
                    kit.name = Name(prefix=name, suffix="", cat=kit)

                if other_cat and not other_cat.status.is_outsider:
                    kit.backstory = "outsider2"

                if cat.status.is_outsider and not cat.status.is_exiled(
                    CatGroup.PLAYER_CLAN
                ):
                    kit.backstory = "outsider3"
                kit.relationships = {}
                kit.create_one_relationship(cat)

        insert = i18n.t("conditions.pregnancy.kit_amount", count=kits_amount)

        # Since cat has given birth, apply the birth cooldown.
        cat.birth_cooldown = constants.CONFIG["pregnancy"]["birth_cooldown"]

        # choose event string
        # TODO: currently they don't choose which 'mate' is the 'blood' parent or not
        # change or leaf as it is?
        Pregnancy_Events.rebuild_strings()
        events = Pregnancy_Events.PREGNANT_STRINGS
        event_list = []
        if not cat.status.is_outsider and other_cat is None:
            event_list.append(choice(events["birth"]["unmated_parent"]))
        elif cat.status.is_outsider:
            adding_text = choice(events["birth"]["outside_alone"])
            if other_cat and not other_cat.status.is_outsider:
                adding_text = choice(events["birth"]["outside_in_clan"])
            event_list.append(adding_text)
        elif other_cat.ID in cat.mate and other_cat.status.alive_in_player_clan:
            involved_cats.append(other_cat.ID)
            cat_dict["r_c"] = other_cat
            event_list.append(choice(events["birth"]["two_parents"]))
        elif (
            other_cat.ID in cat.mate and other_cat.dead or other_cat.status.is_outsider
        ):
            involved_cats.append(other_cat.ID)
            cat_dict["r_c"] = other_cat
            # TODO: this seems odd, outsider mates are also treated as dead?
            event_list.append(choice(events["birth"]["dead_mate"]))
        elif len(cat.mate) < 1 and len(other_cat.mate) < 1 and not other_cat.dead:
            involved_cats.append(other_cat.ID)
            cat_dict["r_c"] = other_cat
            event_list.append(choice(events["birth"]["both_unmated"]))
        elif (
            len(cat.mate) > 0 and other_cat.ID not in cat.mate and not other_cat.dead
        ) or (
            len(other_cat.mate) > 0
            and cat.ID not in other_cat.mate
            and not other_cat.dead
        ):
            involved_cats.append(other_cat.ID)
            cat_dict["r_c"] = other_cat
            event_list.append(choice(events["birth"]["affair"]))
            if len(cat.mate) > 0:
                event_list.append(choice(events["birth"]["affair_mated"]))
        else:
            event_list.append(choice(events["birth"]["unmated_parent"]))

        involved_cats += [k.ID for k in kits]

        if clan.game_mode != "classic":
            try:
                death_chance = cat.injuries["pregnant"]["mortality"]
            except:
                death_chance = 40
        else:
            death_chance = 40
        if not int(
            random.random() * death_chance
        ):  # chance for a cat to die during childbirth
            possible_events = events["birth"]["death"]
            # just makin sure meds aren't mentioned if they aren't around or if they are a parent
            meds = find_alive_cats_with_rank(
                Cat, [CatRank.MEDICINE_CAT, CatRank.MEDICINE_APPRENTICE], sort=True
            )
            mate_is_med = [mate_id for mate_id in cat.mate if mate_id in meds]
            if not meds or cat in meds or len(mate_is_med) > 0:
                for event in possible_events:
                    if CatRank.MEDICINE_CAT in event:
                        possible_events.remove(event)

            if cat.status.is_outsider:
                possible_events = events["birth"]["outside_death"]
            if game.clan.leader_lives > 1 and cat.status.is_leader:
                possible_events = events["birth"]["lead_death"]
            event_list.append(choice(possible_events))

            if cat.status.is_leader:
                clan.leader_lives -= 1
                cat.die()
                death_event = i18n.t("conditions.pregnancy.leader_kitting_death")
            else:
                cat.die()
                death_event = i18n.t(
                    "conditions.pregnancy.kitting_death", name=cat.name
                )
            cat.history.add_death(death_text=death_event)
        elif (
            not cat.status.is_outsider
        ):  # if cat doesn't die, give recovering from birth
            cat.get_injured("recovering from birth", event_triggered=True)
            if "blood loss" in cat.injuries:
                if cat.status.is_leader:
                    death_event = i18n.t(
                        "conditions.pregnancy.leader_kitting_death_severe"
                    )
                else:
                    death_event = i18n.t(
                        "conditions.pregnancy.kitting_death_harsh", name=cat.name
                    )
                cat.history.add_possible_history("blood loss", death_text=death_event)
                possible_events = events["birth"]["difficult_birth"]
                # just makin sure meds aren't mentioned if they aren't around or if they are a parent
                meds = find_alive_cats_with_rank(
                    Cat, [CatRank.MEDICINE_CAT, CatRank.MEDICINE_APPRENTICE]
                )
                mate_is_med = [mate_id for mate_id in cat.mate if mate_id in meds]
                if not meds or cat in meds or len(mate_is_med) > 0:
                    for event in possible_events:
                        if CatRank.MEDICINE_CAT in event:
                            possible_events.remove(event)

                event_list.append(choice(possible_events))
        if not cat.dead:
            # If they are dead in childbirth above, all condition are cleared anyway.
            try:
                cat.injuries.pop("pregnant")
            except:
                print(
                    "Is this an old save? Your cat didn't have the pregnant condition!"
                )
        print_event = " ".join(event_list)
        print_event = print_event.replace("{insert}", insert)

        print_event = event_text_adjust(
            Cat, print_event, main_cat=cat, random_cat=other_cat, clan=game.clan
        )

        if stillborn_count != 0:
            print_event += i18n.t(
                "conditions.pregnancy.pregnant_stillbirth",
                name=cat.name,
                insert=i18n.t("conditions.pregnancy.stillborn_amount", count=stillborn_count),
            )
            cat.get_ill("grief stricken", event_triggered=True)  

        # display event
        game.cur_events_list.append(
            Single_Event(
                print_event, ["health", "birth_death"], involved_cats, cat_dict=cat_dict
            )
        )

    # ---------------------------------------------------------------------------- #
    #                          check if event is triggered                         #
    # ---------------------------------------------------------------------------- #

    @staticmethod
    def check_intersex_conditions(cat: Cat,
                               second_parent: Cat,
                               same_sex_adoption: bool):

        # all of this is only run if same sex is OFF
        if "chimerism" in cat.permanent_condition or "chimerism" in second_parent.permanent_condition:
            if cat.gender == second_parent.gender:
                if cat.gender == 'intersex':
                    return True, False
                elif not same_sex_adoption:
                    return False, False
                else:
                    return True, True
            else:
                return True, False
            
        elif "mosaicism" in cat.permanent_condition:
            if cat.gender == "male" and second_parent.gender != "female":
                    return True, True
            elif cat.gender == "female" and second_parent.gender != "female":
                return True, False
            elif cat.gender == "intersex":
                if second_parent.permanent_condition in ["mosaicism", "excess testosterone"]:
                    return True, False
                elif second_parent.gender == "female":
                    return True, False
                else:
                    if not same_sex_adoption:
                        return False, False
                    else:
                        return True, True
            else:
                if not same_sex_adoption:
                    return False, False
                else:
                    return True, True

        elif "aneuploidy" in cat.permanent_condition:   
            if "testosterone deficiency" in second_parent.permanent_condition:
                return True, False
            elif second_parent.gender == "male":
                return True, False
            else:
                if not same_sex_adoption:
                    return False, False
                else:
                    return True, True

        elif "testosterone deficiency" in cat.permanent_condition:
            if cat.gender in ["male", "intersex"] and second_parent.gender != "male":
                if second_parent.permanent_condition in ["aneuploidy", "excess testosterone"]:
                    return True, False
                elif not same_sex_adoption:
                    return False, False
                else:
                    return True, True
            else:
                if not same_sex_adoption:
                    return False, False
                else:
                    return True, True

        elif "excess testosterone" in cat.permanent_condition:
            if cat.gender in ["female", "intersex"] and second_parent.gender != "female":
                if "testosterone deficiency" in second_parent.permanent_condition:
                    return True, False
                elif not same_sex_adoption:
                    return False, False
                else:
                    return True, True
            else:
                if not same_sex_adoption:
                    return False, False
                else:
                    return True, True

        return False, False

    @staticmethod
    def check_if_can_have_kits(cat, single_parentage, allow_affair):
        """Check if the given cat can have kits, see for age, birth-cooldown and so on."""
        if not cat:
            return False

        if cat.birth_cooldown > 0:
            return False

        if "recovering from birth" in cat.injuries:
            return False

        # decide chances of having kits, and if it's possible at all.
        # Including - age, dead statis, having kits turned off.
        not_correct_age = (
            cat.age in [CatAge.NEWBORN, CatAge.KITTEN, CatAge.ADOLESCENT]
            or cat.moons < 15
        )
        if not_correct_age or cat.no_kits or cat.dead or cat.neutered:
            return False

        # check for mate
        if len(cat.mate) > 0:
            for mate_id in cat.mate:
                if mate_id not in cat.all_cats:
                    print(
                        f"WARNING: {cat.name}  has an invalid mate # {mate_id}. This has been unset."
                    )
                    cat.mate.remove(mate_id)

        # If the "single parentage setting in on, we should only allow cats that have mates to have kits.
        if not single_parentage and len(cat.mate) < 1 and not allow_affair:
            return False

        # check for the no_breed species tag
        species_dict = game.species["species"]
        if any("no_breed" in tag for tag in species_dict[cat.species]):
            print("no breed tag")
            return False

        # if function reaches this point, having kits is possible
        return True

    @staticmethod
    def check_second_parent(
        cat: Cat,
        second_parent: Cat,
        single_parentage: bool,
        allow_affair: bool,
        inter_species: bool,
        same_sex_birth: bool,
        same_sex_adoption: bool,
    ):
        """
        This checks to see if the chosen second parent and CAT can have kits. It assumes CAT can have kits.
        returns:
        parent can have kits, kits are adopted
        """
        species_dict = game.species["species"]

        # Checks for second parent alone:
        if not Pregnancy_Events.check_if_can_have_kits(
            second_parent, single_parentage, allow_affair
        ):
            return False, False

        if cat.gender == "null" or second_parent.gender == "null":
            return True, True

        if cat.neutered or second_parent.neutered:
            return False, False
            
        if "infertile" in cat.permanent_condition or "infertile" in second_parent.permanent_condition:
            infertile_kits = random.randint(1, 10)
            if infertile_kits != 1:
                return True, True

        # check for exclusive and different breed tags
        if not inter_species:
            if (
                (
                    (
                    any("exc_breed" in tag for tag in species_dict[cat.species])
                    or any("exc_breed" in tag for tag in species_dict[second_parent.species])
                    )
                    and cat.species != second_parent.species
                )
                or (
                    (
                    any("diff_breed" in tag for tag in species_dict[cat.species])
                    or any("diff_breed" in tag for tag in species_dict[second_parent.species])
                    )
                    and cat.species == second_parent.species
                    )
                ):
                return False, True

        if (
            cat.permanent_condition in ["chimerism", "mosaicism", "aneuploidy", "excess testosterone", "testosterone deficiency"]
            or second_parent.permanent_condition in ["chimerism", "mosaicism", "aneuploidy", "excess testosterone", "testosterone deficiency"]
        ) and not same_sex_birth:
            return Pregnancy_Events.check_intersex_conditions(cat, second_parent, same_sex_adoption)  

        # Check to see if the pair can have kits.
        if cat.gender == second_parent.gender:
            if cat.gender == 'intersex':
                return True, False
            if same_sex_birth:
                return True, False
            elif not same_sex_adoption:
                return False, False
            else:
                return True, True


        return True, False

    # ---------------------------------------------------------------------------- #
    #                               getter functions                               #
    # ---------------------------------------------------------------------------- #

    @staticmethod
    def get_second_parent(cat, clan):
        """
        Return the second parent of a cat, which will have kits.
        Also returns a bool that is true if an affair was triggered.
        """
        samesex = get_clan_setting("same sex birth")
        allow_affair = get_clan_setting("affair")
        mate = None

        # randomly select a mate of given cat
        if len(cat.mate) > 0:
            mate = choice(cat.mate)
            mate = cat.fetch_cat(mate)

        # if the sex does matter, choose the best solution to allow kits
        if not samesex and mate and mate.gender == cat.gender:
            opposite_mate = [
                cat.fetch_cat(mate_id)
                for mate_id in cat.mate
                if cat.fetch_cat(mate_id).gender != cat.gender
            ]
            if len(opposite_mate) > 0:
                mate = choice(opposite_mate)

        if not allow_affair:
            # if affairs setting is OFF, second parent (mate) will be returned
            return mate, False

        # get relationships to influence the affair chance
        mate_relation = None
        if mate and mate.ID in cat.relationships:
            mate_relation = cat.relationships[mate.ID]
        elif mate:
            mate_relation = cat.create_one_relationship(mate)

        # LOVE AFFAIR
        # Handle love affair chance.
        affair_partner = Pregnancy_Events.determine_love_affair(
            cat, mate, mate_relation, samesex
        )
        if affair_partner:
            return affair_partner, True

        # RANDOM AFFAIR
        chance = constants.CONFIG["pregnancy"]["random_affair_chance"]
        special_affair = False
        if len(cat.mate) <= 0:
            # Special random affair check only for unmated cats. For this check, only
            # other unmated cats can be the affair partner.
            chance = constants.CONFIG["pregnancy"]["unmated_random_affair_chance"]
            special_affair = True

        # 'buff' affairs if the current biggest family is big + this cat doesn't belong there
        if not Pregnancy_Events.biggest_family:
            Pregnancy_Events.set_biggest_family()

        if (
            Pregnancy_Events.biggest_family_is_big()
            and cat.ID not in Pregnancy_Events.biggest_family
        ):
            chance = int(chance * 0.8)

            # "regular" random affair
        if not int(random.random() * chance):
            possible_affair_partners = [
                i
                for i in Cat.all_cats_list
                if i.is_potential_mate(cat, for_love_interest=True)
                and (samesex or i.gender != cat.gender)
                and i.ID not in cat.mate
            ]
            if special_affair:
                possible_affair_partners = [
                    c for c in possible_affair_partners if len(c.mate) < 1
                ]

            # even it is a random affair, the cats should not hate each other or something like that
            p_affairs = []
            if len(possible_affair_partners) > 0:
                for p_affair in possible_affair_partners:
                    if p_affair.ID in cat.relationships:
                        p_rel = cat.relationships[p_affair.ID]
                        if not p_rel.opposite_relationship:
                            p_rel.link_relationship()
                        p_rel_opp = p_rel.opposite_relationship
                        if p_rel_opp.like < -20 and p_rel.like < -20:
                            p_affairs.append(p_affair)
            possible_affair_partners = p_affairs

            if len(possible_affair_partners) > 0:
                chosen_affair = choice(possible_affair_partners)
                return chosen_affair, True

        return mate, False

    @staticmethod
    def determine_love_affair(cat, mate, mate_relation, samesex):
        """
        Function to handle everything around love affairs.
        Will return a second parent if a love affair is triggerd, and none otherwise.
        """

        highest_romantic_relation = get_highest_romantic_relation(
            cat.relationships.values(), exclude_mate=True, potential_mate=True
        )

        if mate and highest_romantic_relation:
            # Love affair calculation when the cat has a mate
            chance_love_affair = Pregnancy_Events.get_love_affair_chance(
                mate_relation, highest_romantic_relation
            )
            if not chance_love_affair or not int(random.random() * chance_love_affair):
                if samesex or cat.gender != highest_romantic_relation.cat_to.gender:
                    return highest_romantic_relation.cat_to
        elif highest_romantic_relation:
            # Love affair change if the cat doesn't have a mate:
            chance_love_affair = Pregnancy_Events.get_unmated_love_affair_chance(
                highest_romantic_relation
            )
            if not chance_love_affair or not int(random.random() * chance_love_affair):
                if samesex or cat.gender != highest_romantic_relation.cat_to.gender:
                    return highest_romantic_relation.cat_to

        return None

    @staticmethod
    def get_kits(
        kits_amount, cat=None, other_cat=None, clan=game.clan, adoptive_parents=None
    ):
        """Create some amount of kits
        No parents are specified, it will create a blood parents for all the
        kits to be related to. They may be dead or alive, but will always be outside
        the clan."""
        all_kitten = []
        if not adoptive_parents:
            adoptive_parents = []

        # First, just a check: If we have no cat, but an other_cat was provided,
        # swap other_cat to cat:
        # This way, we can ensure that if only one parent is provided,
        # it's cat, not other_cat.
        # And if cat is None, we know that no parents were provided.
        if other_cat and not cat:
            cat = other_cat
            other_cat = None

        blood_parent = None
        par2species = None

        ##### SELECT BACKSTORY #####
        if cat and "pregnant" in cat.injuries:
            backstory = choice(["halfclan1", "outsider_roots1"])
        elif cat:
            backstory = choice(["halfclan2", "outsider_roots2"])
        else:  # cat is adopted
            backstory = choice(["abandoned1", "abandoned2", "abandoned3", "abandoned4"])
        ###########################

        ##### ADOPTIVE PARENTS #####
        # First, gather all the mates of the provided bio parents to be added
        # as adoptive parents.
        all_adoptive_parents = []
        birth_parents = [i.ID for i in (cat, other_cat) if i]
        for _par in (cat, other_cat):
            if not _par:
                continue
            for _m in _par.mate:
                if _m not in birth_parents and _m not in all_adoptive_parents:
                    all_adoptive_parents.append(_m)

        # Then, add any additional adoptive parents that were provided passed directly into the
        # function.
        for _m in adoptive_parents:
            if _m not in all_adoptive_parents:
                all_adoptive_parents.append(_m)

        # Generate a par2species in case par2 is None, so all littermates have same species inheritance weights
        species_list = (list(game.species["species"])).copy()
        weights = game.species["ran_weights"].copy()

        for species in species_list:
            if cat:
                if (
                    any("no_breed" in tag for tag in game.species["species"][species])
                    or any("exc_breed" in tag for tag in game.species["species"][species]) and species != cat.species
                    or any("diff_breed" in tag for tag in game.species["species"][species]) and species == cat.species
                    ):
                    weights.pop((species_list.index(species)))
                    species_list.remove(species)
            else:
                if (
                    any("no_breed" in tag for tag in game.species["species"][species])
                    ):
                    weights.pop((species_list.index(species)))
                    species_list.remove(species)

        par2species = random.choices(species_list, weights=weights, k=1)[0]

        #############################

        #### GENERATE THE KITS ######
        for kit in range(kits_amount):
            if not cat:
                # No parents provided, give a blood parent - this is an adoption.
                if not blood_parent:
                    # Generate a blood parent if we haven't already.
                    outsider_parent = random.randint(0, 10)
                    if outsider_parent == 0:
                        thought = i18n.t(
                            "conditions.pregnancy.half_blood_kitting_live_thought",
                            count=kits_amount,
                        )
                        blood_parent = create_new_cat(
                            Cat,
                            original_social=random.choice((CatSocial.LONER, CatSocial.KITTYPET)),
                            alive=True,
                            thought=thought,
                            moons=randint(15, 120),
                            species=par2species,
                            outside=True,
                        )[0]
                    else:
                        thought = i18n.t(
                            "conditions.pregnancy.half_blood_kitting_thought",
                            count=kits_amount,
                        )
                        blood_parent = create_new_cat(
                            Cat,
                            original_social=random.choice((CatSocial.LONER, CatSocial.KITTYPET)),
                            alive=False,
                            thought=thought,
                            moons=randint(15, 120),
                            species=par2species,
                            outside=True,
                        )[0]
                    blood_parent.thought = thought

                kit = Cat(parent1=blood_parent.ID, par2species=par2species, moons=0, backstory=backstory)

            elif cat and other_cat:
                # Two parents provided
                # The cat that gave birth is always parent1 so there is no need to check gender
                kit = Cat(parent1=cat.ID, parent2=other_cat.ID, moons=0)
                kit.thought = i18n.t("hardcoded.new_kit_thought", name=str(cat.name))
                kit.thought = event_text_adjust(Cat, kit.thought, random_cat=cat)
            else:
                # A one blood parent litter is the only option left.
                kit = Cat(parent1=cat.ID, par2species=par2species, moons=0, backstory=backstory)
                kit.thought = i18n.t("hardcoded.new_kit_thought", name=str(cat.name))
                kit.thought = event_text_adjust(Cat, kit.thought, random_cat=cat)

            # Prevent duplicate prefixes in the same litter
            while kit.name.prefix in [kitty.name.prefix for kitty in all_kitten]:
                kit.name = Name("newborn")

            all_kitten.append(kit)
            # adoptive parents are set at the end, when everything else is decided

            # remove scars
            kit.pelt.scars.clear()

            # try to give them a permanent condition. 1/90 chance
            # don't delete the game.clan condition, this is needed for a test
            if game.clan and not int(
                random.random()
                * constants.CONFIG["cat_generation"]["base_permanent_condition"]
            ):
                kit.congenital_condition(kit)
                for condition in kit.permanent_condition:
                    if kit.permanent_condition[condition] == "born without a leg":
                        kit.pelt.scars.append("NOPAW")
                    elif kit.permanent_condition[condition] == "born without a tail":
                        kit.pelt.scars.append("NOTAIL")
                Condition_Events.handle_already_disabled(kit)

            # create and update relationships
            for cat_id in clan.clan_cats:
                if cat_id == kit.ID:
                    continue
                the_cat = Cat.all_cats.get(cat_id)
                if the_cat.dead or the_cat.status.is_outsider:
                    continue
                if the_cat.ID in kit.get_parents():
                    if "turmoiled litter" in the_cat.injuries:
                        parent_to_kit = constants.CONFIG["new_cat"]["parent_debuff"][
                            "parent_to_kit"
                        ]
                        y = random.randrange(0, 15)
                        start_relation = Relationship(the_cat, kit, False, True)
                        start_relation.like = parent_to_kit[RelType.LIKE] - y
                        start_relation.comfort = parent_to_kit[RelType.COMFORT] - y
                        start_relation.respect = parent_to_kit[RelType.RESPECT] - y
                        start_relation.trust = parent_to_kit[RelType.TRUST] - y
                        the_cat.relationships[kit.ID] = start_relation

                    else:
                        parent_to_kit = constants.CONFIG["new_cat"]["parent_buff"][
                            "parent_to_kit"
                        ]
                        y = random.randrange(0, 15)
                        start_relation = Relationship(the_cat, kit, False, True)
                        start_relation.like = parent_to_kit[RelType.LIKE] + y
                        start_relation.comfort = parent_to_kit[RelType.COMFORT] + y
                        start_relation.respect = parent_to_kit[RelType.RESPECT] + y
                        start_relation.trust = parent_to_kit[RelType.TRUST] + y
                        the_cat.relationships[kit.ID] = start_relation

                    kit_to_parent = constants.CONFIG["new_cat"]["parent_buff"][
                        "kit_to_parent"
                    ]
                    y = random.randrange(0, 15)
                    start_relation = Relationship(kit, the_cat, False, True)
                    start_relation.like += kit_to_parent[RelType.LIKE] + y
                    start_relation.comfort = kit_to_parent[RelType.COMFORT] + y
                    start_relation.respect = kit_to_parent[RelType.RESPECT] + y
                    start_relation.trust = kit_to_parent[RelType.TRUST] + y
                    kit.relationships[the_cat.ID] = start_relation
                else:
                    the_cat.relationships[kit.ID] = Relationship(the_cat, kit)
                    kit.relationships[the_cat.ID] = Relationship(kit, the_cat)

            #### REMOVE ACCESSORY ######
            kit.pelt.accessory = []
            clan.add_cat(kit)

            #### GIVE HISTORY ######
            kit.history.add_beginning(clan_born=bool(cat))

        # check other cats of Clan for siblings
        for kitten in all_kitten:
            # update/buff the relationship towards the siblings
            for second_kitten in all_kitten:
                y = random.randrange(0, 10)
                if second_kitten.ID == kitten.ID:
                    continue
                kitten.relationships[second_kitten.ID].like += 20 + y
                kitten.relationships[second_kitten.ID].comfort += 10 + y
                kitten.relationships[second_kitten.ID].trust += 10 + y

            kitten.create_inheritance_new_cat()  # Calculate inheritance.

        # check if the possible adoptive cat is not already in the family tree and
        # add them as adoptive parents if not
        final_adoptive_parents = []
        for adoptive_p in all_adoptive_parents:
            if adoptive_p not in all_kitten[0].inheritance.all_involved:
                final_adoptive_parents.append(adoptive_p)

        # Add the adoptive parents.
        for kit in all_kitten:
            kit.adoptive_parents = final_adoptive_parents
            kit.inheritance.update_inheritance()
            kit.inheritance.update_all_related_inheritance()

            # update relationship for adoptive parents
            for parent_id in final_adoptive_parents:
                parent = Cat.fetch_cat(parent_id)
                if parent:
                    kit_to_parent = constants.CONFIG["new_cat"]["parent_buff"][
                        "kit_to_parent"
                    ]
                    parent_to_kit = constants.CONFIG["new_cat"]["parent_buff"][
                        "parent_to_kit"
                    ]
                    change_relationship_values(
                        cats_from=[kit],
                        cats_to=[parent],
                        **kit_to_parent,
                    )
                    change_relationship_values(
                        cats_from=[parent],
                        cats_to=[kit],
                        **parent_to_kit,
                    )

        return all_kitten

    @staticmethod
    def get_amount_of_kits(cat):
        """Get the amount of kits which will be born."""
        min_kits = constants.CONFIG["pregnancy"]["min_kits"]
        max_kits = constants.CONFIG["pregnancy"]["max_kits"]    
        
        tiny_litter = [random.randint(min_kits, 3)] * constants.CONFIG["pregnancy"]["tiny_litter_possibility"][cat.age.value]
        small_litter = [random.randint(4, 6)] * constants.CONFIG["pregnancy"]["small_litter_possibility"][cat.age.value]
        large_litter = [random.randint(7, 9)] * constants.CONFIG["pregnancy"]["large_litter_possibility"][cat.age.value]
        huge_litter = [random.randint(10, 14)] * constants.CONFIG["pregnancy"]["huge_litter_possibility"][cat.age.value]
        ridiculous_litter = [random.randint(15, max_kits)] * constants.CONFIG["pregnancy"]["ridiculous_litter_possibility"][cat.age.value]

        amount = choice(tiny_litter + small_litter + large_litter + huge_litter + ridiculous_litter)

        return amount

    # ---------------------------------------------------------------------------- #
    #                                  get chances                                 #
    # ---------------------------------------------------------------------------- #

    @staticmethod
    def get_love_affair_chance(
        mate_relation: Relationship, affair_relation: Relationship
    ):
        """Looks into the current values and calculate the chance of having kits with the affair cat.
        The lower, the more likely they will have affairs. This function should only be called when mate
        and affair_cat are not the same.

        Returns:
            integer (number)
        """
        if not mate_relation.opposite_relationship:
            mate_relation.link_relationship()

        if not affair_relation.opposite_relationship:
            affair_relation.link_relationship()

        average_mate_love = (
            mate_relation.romance + mate_relation.opposite_relationship.romance
        ) / 2
        average_affair_love = (
            affair_relation.romance + affair_relation.opposite_relationship.romance
        ) / 2

        difference = average_mate_love - average_affair_love

        if difference < 0:
            # If the average love between affair partner is greater than the average love between the mate
            affair_chance = 10
            difference = -difference

            if difference > 30:
                affair_chance -= 7
            elif difference > 20:
                affair_chance -= 6
            elif difference > 15:
                affair_chance -= 5
            elif difference > 10:
                affair_chance -= 4

        elif difference > 0:
            # If the average love between the mate is greater than the average relationship between the affair
            affair_chance = 30

            if difference > 30:
                affair_chance += 8
            elif difference > 20:
                affair_chance += 5
            elif difference > 15:
                affair_chance += 3
            elif difference > 10:
                affair_chance += 5

        else:
            # For difference = 0 or some other weird stuff
            affair_chance = 15

        return affair_chance

    @staticmethod
    def get_unmated_love_affair_chance(relation: Relationship):
        """Get the "love affair" change when neither the cat nor the highest romantic relation have a mate"""

        if not relation.opposite_relationship:
            relation.link_relationship()

        affair_chance = 15
        average_romantic_love = (
            relation.romance + relation.opposite_relationship.romance
        ) / 2

        if average_romantic_love > 50:
            affair_chance -= 12
        elif average_romantic_love > 40:
            affair_chance -= 10
        elif average_romantic_love > 30:
            affair_chance -= 7
        elif average_romantic_love > 10:
            affair_chance -= 5

        return affair_chance

    @staticmethod
    def get_balanced_kit_chance(
        first_parent: Cat, second_parent: Cat, affair, clan
    ) -> int:
        """Returns a chance based on different values."""
        # Now that the second parent is determined, we can calculate the balanced chance for kits
        # get the chance for pregnancy
        inverse_chance = constants.CONFIG["pregnancy"]["primary_chance_unmated"]
        if len(first_parent.mate) > 0 and not affair:
            inverse_chance = constants.CONFIG["pregnancy"]["primary_chance_mated"]

        # SETTINGS
        # - decrease inverse chance if only mated pairs can have kits
        if not get_clan_setting("single parentage"):
            inverse_chance = int(inverse_chance * 0.7)

        # - decrease inverse chance if affairs are not allowed
        if not get_clan_setting("affair"):
            inverse_chance = int(inverse_chance * 0.7)

        # CURRENT CAT AMOUNT
        # - increase the inverse chance if the clan is bigger
        living_cats = len(
            [i for i in Cat.all_cats.values() if i.status.alive_in_player_clan]
        )
        if living_cats < 10:
            inverse_chance = int(inverse_chance * 0.5)
        elif living_cats > 30:
            inverse_chance = int(inverse_chance * (living_cats / 30))

        # COMPATIBILITY
        # - decrease / increase depending on the compatibility
        if second_parent:
            comp = get_personality_compatibility(first_parent, second_parent)
            if comp is not None:
                buff = 0.85
                if not comp:
                    buff += 0.3
                inverse_chance = int(inverse_chance * buff)

        # RELATIONSHIP
        # - decrease the inverse chance if the cats are going along well
        if second_parent:
            # get the needed relationships
            if second_parent.ID in first_parent.relationships:
                second_parent_relation = first_parent.relationships[second_parent.ID]
                if not second_parent_relation.opposite_relationship:
                    second_parent_relation.link_relationship()
            else:
                second_parent_relation = first_parent.create_one_relationship(
                    second_parent
                )

            average_romantic_love = (
                second_parent_relation.romance
                + second_parent_relation.opposite_relationship.romance
            ) / 2
            average_comfort = (
                second_parent_relation.comfort
                + second_parent_relation.opposite_relationship.comfort
            ) / 2
            average_trust = (
                second_parent_relation.trust
                + second_parent_relation.opposite_relationship.trust
            ) / 2

            if average_romantic_love >= 85:
                inverse_chance -= int(inverse_chance * 0.3)
            elif average_romantic_love >= 55:
                inverse_chance -= int(inverse_chance * 0.2)
            elif average_romantic_love >= 35:
                inverse_chance -= int(inverse_chance * 0.1)

            if average_comfort >= 85:
                inverse_chance -= int(inverse_chance * 0.3)
            elif average_comfort >= 55:
                inverse_chance -= int(inverse_chance * 0.2)
            elif average_comfort >= 35:
                inverse_chance -= int(inverse_chance * 0.1)

            if average_trust >= 85:
                inverse_chance -= int(inverse_chance * 0.3)
            elif average_trust >= 55:
                inverse_chance -= int(inverse_chance * 0.2)
            elif average_trust >= 35:
                inverse_chance -= int(inverse_chance * 0.1)

        # AGE
        # - decrease the inverse chance if the whole clan is really old
        avg_age = int(sum((cat.moons for cat in Cat.all_cats.values())) / living_cats)
        if avg_age > 80:
            inverse_chance = int(inverse_chance * 0.8)

        # 'INBREED' counter
        # - increase inverse chance if one of the current cats belongs in the biggest family
        if not Pregnancy_Events.biggest_family:  # set the family if not already
            Pregnancy_Events.set_biggest_family()

        if (
            first_parent.ID in Pregnancy_Events.biggest_family
            or second_parent
            and second_parent.ID in Pregnancy_Events.biggest_family
        ):
            inverse_chance = int(inverse_chance * 1.7)

        # - decrease inverse chance if the current family is small
        if len(first_parent.get_relatives(get_clan_setting("second cousin mates"))) < (
            living_cats / 15
        ):
            inverse_chance = int(inverse_chance * 0.7)

        # - decrease inverse chance single parents if settings allow an biggest family is huge
        settings_allow = not second_parent and not get_clan_setting("single parentage")
        if settings_allow and Pregnancy_Events.biggest_family_is_big():
            inverse_chance = int(inverse_chance * 0.9)

        return inverse_chance
