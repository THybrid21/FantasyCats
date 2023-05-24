import random
from random import choice, randint

# Alphabetical !! yea !!
from .pelts import (
    black_colours,
    blue_eyes,
    brown_colours,
    choose_pelt,
    colour_categories,
    exotic,
    eye_colours,
    ginger_colours,
    green_eyes,
    high_white,
    little_white,
    mid_white,
    mostly_white,
    pelt_categories,
    pelt_length,
    plain,
    plant_accessories,
    point_markings,
    scars1,
    scars3,
    spotted,
    tabbies,
    tortiebases,
    torties,
    vit,
    white_colours,
    wild_accessories,
    yellow_eyes,
    pelt_colours,
    tortiepatterns,
    sphynx,
    cream_colours,
    grey_colours,
    blue_colours,
    green_colours,
    purple_colours,
    yellow_colours,
    pride_colours,
    skin_sprites,
    albino_sprites,
    melanistic_sprites,
    skin_categories,
    mono_eyes,
    purple_eyes,
    chromatic_eyes,
    sus_eyes,
    sus_blue,
    sus_chrome,
    sus_yellow,
    sus_green,
    sus_mono,
    sus_purple,
    sparkle_cats
    )
from scripts.cat.sprites import Sprites
from scripts.game_structure.game_essentials import game


# ---------------------------------------------------------------------------- #
#                                init functions                                #
# ---------------------------------------------------------------------------- #


def init_eyes(cat):
    if cat.eye_colour:
        return   
    else:
        par1 = None
        par2 = None
        if cat.parent1 is None:
            cat.eye_colour = choice(eye_colours + sus_eyes)
        elif cat.parent2 is None:
            par1 = cat.all_cats[cat.parent1]
            cat.eye_colour = choice([par1.eye_colour, choice(eye_colours + sus_eyes)])
        else:
            par1 = cat.all_cats[cat.parent1]
            par2 = cat.all_cats[cat.parent2]
            cat.eye_colour = choice([par1.eye_colour, par2.eye_colour, choice(eye_colours + sus_eyes)])
        num = game.config["cat_generation"]["base_heterochromia"]
        if cat.white_patches in [high_white, mostly_white, 'FULLWHITE'] or cat.pelt.colour == 'WHITE':
            num = num - 90
        if cat.white_patches == 'FULLWHITE' or cat.pelt.colour == 'WHITE':
            num -= 10
        if par1:
            if par1.eye_colour2:
                num -= 10
        if par2:
            if par2.eye_colour2:
                num -= 10
        if num < 0:
            num = 1
        hit = randint(0, num)
        if hit == 0:
            if cat.eye_colour in yellow_eyes:
                eye_choice = choice([blue_eyes, green_eyes, purple_eyes, mono_eyes, chromatic_eyes])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in blue_eyes:
                eye_choice = choice([yellow_eyes, green_eyes, purple_eyes, mono_eyes, chromatic_eyes])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in green_eyes:
                eye_choice = choice([yellow_eyes, blue_eyes, purple_eyes, mono_eyes, chromatic_eyes])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in purple_eyes:
                eye_choice = choice([yellow_eyes, blue_eyes, green_eyes, mono_eyes, chromatic_eyes])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in mono_eyes:
                eye_choice = choice([yellow_eyes, blue_eyes, green_eyes, purple_eyes, chromatic_eyes])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in chromatic_eyes:
                eye_choice = choice([yellow_eyes, blue_eyes, green_eyes, purple_eyes, mono_eyes])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in sus_yellow:
                eye_choice = choice([sus_blue, sus_green, sus_purple, sus_mono, sus_chrome])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in sus_blue:
                eye_choice = choice([sus_yellow, sus_green, sus_purple, sus_mono, sus_chrome])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in sus_green:
                eye_choice = choice([sus_yellow, sus_blue, sus_purple, sus_mono, sus_chrome])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in sus_purple:
                eye_choice = choice([sus_yellow, sus_blue, sus_green, sus_mono, sus_chrome])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in sus_mono:
                eye_choice = choice([sus_yellow, sus_blue, sus_green, sus_purple, sus_chrome])
                cat.eye_colour2 = choice(eye_choice)
            elif cat.eye_colour in sus_chrome:
                eye_choice = choice([sus_yellow, sus_blue, sus_green, sus_purple, sus_mono])
                cat.eye_colour2 = choice(eye_choice)


def pelt_inheritance(cat, parents: tuple):
    # setting parent pelt categories
    #We are using a set, since we don't need this to be ordered, and sets deal with removing duplicates.
    par_peltlength = set()
    par_peltcolours = set()
    par_peltnames = set()
    par_pelts = []
    par_white = []
    for p in parents:
        if p:
            # Gather pelt color.
            par_peltcolours.add(p.pelt.colour)

             # Gather pelt length
            par_peltlength.add(p.pelt.length)

            # Gather pelt name
            if p.pelt.name in torties:
                par_peltnames.add(p.tortiebase.capitalize())
            else:
                par_peltnames.add(p.pelt.name)

            # Gather exact pelts, for direct inheritance.
            par_pelts.append(p.pelt)

            # Gather if they have white in their pelt.
            par_white.append(p.pelt.white)
        else:
            # If order for white patches to work correctly, we also want to randomly generate a "pelt_white"
            # for each "None" parent (missing or unknown parent)
            par_white.append(bool(random.getrandbits(1)))

            # Append None
            # Gather pelt color.
            par_peltcolours.add(None)
            par_peltlength.add(None)
            par_peltnames.add(None)

    # If this list is empty, something went wrong.
    if not par_peltcolours:
        print("Error - no parents: pelt randomized")
        randomize_pelt(cat)
        return

    # There is a 1/10 chance for kits to have the exact same pelt as one of their parents
    if not randint(0, game.config["cat_generation"]["direct_inheritance"]):  # 1/10 chance
        selected = choice(par_pelts)
        cat.pelt = choose_pelt(selected.colour, selected.white, selected.name,
                               selected.length)
        return

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT
    # ------------------------------------------------------------------------------------------------------------#

    # Determine pelt.
    weights = [0, 0, 0, 0, 0]  #Weights for each pelt group. It goes: (tabbies, spotted, plain, exotic, sparkle_cats)
    for p_ in par_peltnames:
        if p_ in tabbies:
            add_weight = (50, 10, 5, 7, 1)
        elif p_ in spotted:
            add_weight = (10, 50, 5, 5, 1)
        elif p_ in plain:
            add_weight = (5, 5, 50, 2, 0)
        elif p_ in exotic:
            add_weight = (15, 15, 5, 45, 1)
        elif p_ in sparkle_cats:
            add_weight = (15, 15, 10, 25, 45)
        elif p_ is None:  # If there is at least one unknown parent, a None will be added to the set.
            add_weight = (35, 20, 30, 15, 2)
        else:
            add_weight = (0, 0, 0, 0, 0)

        for x in range(0, len(weights)):
            weights[x] += add_weight[x]

    #A quick check to make sure all the weights aren't 0
    if all([x == 0 for x in weights]):
        weights = [1, 1, 1, 1, 1]

    # Now, choose the pelt category and pelt. The extra 0 is for the tortie pelts,
    chosen_pelt = choice(
        random.choices(pelt_categories, weights=weights + [0], k = 1)[0]
    )

    # Tortie chance
    tortie_chance_f = game.config["cat_generation"]["base_female_tortie"]  # There is a default chance for female tortie
    tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
    for p_ in par_pelts:
        if p_.name in torties:
            tortie_chance_f = int(tortie_chance_f / 2)
            tortie_chance_m = tortie_chance_m - 1
            break

    # Determine tortie:
    if cat.gender == "female":
        torbie = random.getrandbits(tortie_chance_f) == 1
    else:
        torbie = random.getrandbits(tortie_chance_m) == 1

    chosen_tortie_base = None
    if torbie:
        # If it is tortie, the chosen pelt above becomes the base pelt.
        chosen_tortie_base = chosen_pelt
        if chosen_tortie_base in ["TwoColour", "SingleColour"]:
            chosen_tortie_base = "Single"
        if chosen_tortie_base in ["FalseSolid", "FalseTwo"]:
            chosen_tortie_base = "FalseSolid"
        if chosen_tortie_base in ["Wolf", "WolfBicolour"]:
            chosen_tortie_base = "Wolf" 
        chosen_tortie_base = chosen_tortie_base.lower()
        chosen_pelt = random.choice(torties)

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT COLOUR
    # ------------------------------------------------------------------------------------------------------------#
    # Weights for each colour group. It goes: (cream, ginger, black, grey, white, brown, 
        #blue, yellow, purple, green, pride)
    weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for p_ in par_peltcolours:
        if p_ in cream_colours:
            add_weight = (40, 20, 0, 0, 0, 10, 0, 5, 5, 2, 1)
        if p_ in ginger_colours:
            add_weight = (20, 40, 0, 0, 0, 10, 0, 0, 5, 0, 5)
        elif p_ in black_colours:
            add_weight = (0, 0, 40, 20, 2, 5, 5, 0, 0, 0, 1)
        elif p_ in grey_colours:
            add_weight = (0, 0, 10, 40, 10, 2, 5, 0, 0, 1, 1)
        elif p_ in white_colours:
            add_weight = (2, 0, 5, 20, 40, 0, 5, 2, 0, 1, 1)
        elif p_ in brown_colours:
            add_weight = (5, 10, 5, 2, 0, 35, 0, 5, 0, 1, 1)
        elif p_ in blue_colours:
            add_weight = (0, 0, 20, 20, 20, 0, 25, 0, 2, 0, 5)
        elif p_ in yellow_colours:
            add_weight = (10, 0, 0, 0, 10, 20, 0, 25, 0, 5, 5)
        elif p_ in purple_colours:
            add_weight = (20, 20, 0, 0, 0, 0, 0, 5, 25, 0, 5)
        elif p_ in green_colours:
            add_weight = (2, 0, 0, 1, 1, 1, 0, 5, 0, 35, 5)
        elif p_ in pride_colours:
            add_weight = (1, 5, 1, 1, 1, 1, 5, 5, 5, 5, 45)
        elif p_ is None:
            add_weight = (40, 40, 40, 40, 40, 40, 2, 2, 2, 15, 5)
        else:
            add_weight = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        for x in range(0, len(weights)):
            weights[x] += add_weight[x]

        # A quick check to make sure all the weights aren't 0
        if all([x == 0 for x in weights]):
            weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    chosen_pelt_color = choice(random.choices(colour_categories, weights=weights, k=1)[0])

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT LENGTH
    # ------------------------------------------------------------------------------------------------------------#

    weights = [0, 0, 0]  # Weights for each length. It goes (short, medium, long)
    for p_ in par_peltlength:
        if p_ == "short":
            add_weight = (50, 10, 2)
        elif p_ == "medium":
            add_weight = (25, 50, 25)
        elif p_ == "long":
            add_weight = (2, 10, 50)
        elif p_ is None:
            add_weight = (10, 10, 10)
        else:
            add_weight = (0, 0, 0)

        for x in range(0, len(weights)):
            weights[x] += add_weight[x]

    # A quick check to make sure all the weights aren't 0
    if all([x == 0 for x in weights]):
        weights = [1, 1, 1]

    chosen_pelt_length = random.choices(pelt_length, weights=weights, k=1)[0]

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT WHITE
    # ------------------------------------------------------------------------------------------------------------#

    # There is 94 percentage points that can be added by
    # parents having white. If we have more than two, this
    # will keep that the same.
    percentage_add_per_parent = int(94 / len(par_white))
    chance = 3
    for p_ in par_white:
        if p_:
            chance += percentage_add_per_parent

    chosen_white = random.randint(1, 100) <= chance

    # Adjustments to pelt chosen based on if the pelt has white in it or not.
    if chosen_pelt in ["TwoColour", "SingleColour"]:
        if chosen_white:
            chosen_pelt = "TwoColour"
        else:
            chosen_pelt = "SingleColour"
    elif chosen_pelt in ["FalseTwo", "FalseSolid"]:
        if chosen_white:
            chosen_pelt = "FalseTwo"
        else:
            chosen_white = "FalseSolid"        
    elif chosen_pelt == "Calico":
        if not chosen_white:
            chosen_pelt = "Tortie"

    # SET THE PELT
    cat.pelt = choose_pelt(chosen_pelt_color, chosen_white, chosen_pelt, chosen_pelt_length)
    cat.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.


def randomize_pelt(cat):
    # ------------------------------------------------------------------------------------------------------------#
    #   PELT
    # ------------------------------------------------------------------------------------------------------------#

    # Determine pelt.
    chosen_pelt = choice(
        random.choices(pelt_categories, weights=(35, 20, 30, 15, 1, 0), k=1)[0]
    )

    # Tortie chance
    # There is a default chance for female tortie, slightly increased for completely random generation.
    tortie_chance_f = game.config["cat_generation"]["base_female_tortie"] - 1
    tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
    if cat.gender == "female":
        torbie = random.getrandbits(tortie_chance_f) == 1
    else:
        torbie = random.getrandbits(tortie_chance_m) == 1

    chosen_tortie_base = None
    if torbie:
        # If it is tortie, the chosen pelt above becomes the base pelt.
        chosen_tortie_base = chosen_pelt
        if chosen_tortie_base in ["TwoColour", "SingleColour"]:
            chosen_tortie_base = "Single"
        elif chosen_tortie_base in ["FalseSolid", "FalseTwo"]:
            chosen_tortie_base = "FalseSolid"
        elif chosen_tortie_base in ["Wolf", "WolfBiColour"]:
            chosen_tortie_base = "Wolf"
        chosen_tortie_base = chosen_tortie_base.lower()
        chosen_pelt = random.choice(torties)

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT COLOUR
    # ------------------------------------------------------------------------------------------------------------#

    chosen_pelt_color = choice(random.choices(colour_categories, weights=(30, 45, 40, 30, 25, 45, 15, 15, 10, 25, 2), k=1)[0])

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT LENGTH
    # ------------------------------------------------------------------------------------------------------------#


    chosen_pelt_length = random.choice(pelt_length)

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT WHITE
    # ------------------------------------------------------------------------------------------------------------#


    chosen_white = random.randint(1, 100) <= 40

    # Adjustments to pelt chosen based on if the pelt has white in it or not.
    if chosen_pelt in ["TwoColour", "SingleColour"]:
        if chosen_white:
            chosen_pelt = "TwoColour"
        else:
            chosen_white = "SingleColour"
    elif chosen_pelt in ["FalseTwo", "FalseSolid"]:
        if chosen_white:
            chosen_pelt = "FalseTwo"
        else:
            chosen_white = "FalseSolid"
    elif chosen_pelt in ["Wolf", "WolfBiColour"]:
        if chosen_white:
            chosen_pelt = "WolfBiColour"
        else:
            chosen_white = "Wolf"
    elif chosen_pelt == "Calico":
        if not chosen_white:
            chosen_pelt = "Tortie"

    cat.pelt = choose_pelt(chosen_pelt_color, chosen_white, chosen_pelt, chosen_pelt_length)
    cat.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.


def init_pelt(cat):
    if cat.pelt is not None:
        return cat.pelt
    else:
        # Grab Parents
        par1 = None
        par2 = None
        if cat.parent1 in cat.all_cats:
            par1 = cat.all_cats[cat.parent1]
        if cat.parent2 in cat.all_cats:
            par2 = cat.all_cats[cat.parent2]

        if par1 or par2:
            #If the cat has parents, use inheritance to decide pelt.
            pelt_inheritance(cat, (par1, par2))
        else:
            randomize_pelt(cat)


def init_sprite(cat):
    if cat.pelt is None:
        init_pelt(cat)
    cat.cat_sprites = {
        'newborn': 20,
        'kitten': randint(0, 2),
        'adolescent': randint(3, 5),
        'senior': randint(12, 14),
        'sick_young': 19,
        'sick_adult': 18
    }
    cat.reverse = choice([True, False])
    # skin chances
    if cat.parent1 is None:
        cat.skin = choice(random.choices(skin_categories, weights=(298, 2), k=1) [0])
    elif cat.parent2 is None:
        par1 = cat.all_cats[cat.parent1]
        if par1.skin in albino_sprites + melanistic_sprites + sphynx:
            par1.skin = choice(skin_sprites)
        cat.skin = choice([par1.skin, choice(random.choices(skin_categories, weights=(198, 2), k=1)[0])])
    else:
        par1 = cat.all_cats[cat.parent1]
        if par1.skin in albino_sprites + melanistic_sprites + sphynx:
            par1.skin = choice(skin_sprites)
        par2 = cat.all_cats[cat.parent2]
        if par2.skin in albino_sprites + melanistic_sprites + sphynx:
            par2.skin = choice(skin_sprites)
        cat.skin = choice([par1.skin, par2.skin, choice(random.choices(skin_categories, weights=(197, 3), k=1)[0])])
            
    if cat.pelt is not None:
        if cat.pelt.length != 'long':
            cat.cat_sprites['adult'] = randint(6, 8)
            cat.cat_sprites['para_adult'] = 16
        else:
            cat.cat_sprites['adult'] = randint(9, 11)
            cat.cat_sprites['para_adult'] = 15
        cat.cat_sprites['young adult'] = cat.cat_sprites['adult']
        cat.cat_sprites['senior adult'] = cat.cat_sprites['adult']


def init_scars(cat):
    if not cat.scars:
        if cat.age == "newborn":
            return
        scar_choice = randint(0, 15)
        if cat.age in ['kitten', 'adolescent']:
            scar_choice = randint(0, 50)
        elif cat.age in ['young adult', 'adult']:
            scar_choice = randint(0, 20)
        if scar_choice == 1:
            cat.scars.append(choice([
                choice(scars1),
                choice(scars3)
            ]))

    if 'NOTAIL' in cat.scars and 'HALFTAIL' in cat.scars:
        cat.scars.remove('HALFTAIL')


def init_accessories(cat):
    acc_display_choice = randint(0, 35)
    if cat.age in ['kitten', 'adolescent']:
        acc_display_choice = randint(0, 15)
    elif cat.age in ['young adult', 'adult']:    
        acc_display_choice = randint(0, 50)
    if acc_display_choice == 1:
        cat.acc_display = choice([
            choice(plant_accessories),
            choice(wild_accessories)
        ])
    else:
        cat.acc_display = None


def init_pattern(cat):
    if cat.pelt is None:
        init_pelt(cat)
    if cat.pelt.name in torties:
        if not cat.tortiebase:
            cat.tortiebase = choice(tortiebases)
        if not cat.pattern:
            cat.pattern = choice(tortiepatterns)

        wildcard_chance = game.config["cat_generation"]["wildcard_tortie"]
        if cat.pelt.colour:
            # The "not wildcard_chance" allows users to set wildcard_tortie to 0
            # and always get wildcard torties.
            if not wildcard_chance or random.getrandbits(wildcard_chance) == 1:
                # This is the "wildcard" chance, where you can get funky combinations.

                # Allow any pattern:
                cat.tortiepattern = choice(tortiebases)

                # Allow any colors that aren't the base color.
                possible_colors = pelt_colours.copy()
                possible_colors.remove(cat.pelt.colour)
                possible_colors.extend(pride_colours * 3)
                cat.tortiecolour = choice(possible_colors)

            else:
                # Normal generation
                if cat.tortiebase in ["backed", "smoke", "single", "ghost", "falsesolid"]:
                    cat.tortiepattern = choice(['backed', 'smoke', 'single', 'ghost', 'rat', 
                                    'snowflake', 'wolf', 'spirit', 'falsesolid'])
                elif cat.tortiebase in ["speckled", "banded"]:
                    cat.tortiepattern = choice(['speckled', 'banded'])
                elif cat.tortiebase in ["charcoal", "hooded"]:
                    cat.tortiepattern = choice(['charcoal', 'hooded', 'spirit'])    
                elif cat.tortiebase == "ponit":
                    cat.tortiepattern = 'ponit' 
                elif cat.tortiebase == "spirit":
                    cat.tortiepattern = random.choices([cat.tortiebase, 'wolf', 'single', 'skele', 'ponit'], weights=[75, 15, 10, 4, 1], k=1)[0]
                else:
                    cat.tortiepattern = random.choices([cat.tortiebase, 'ghost', 'rat', 'skele', 'spirit'], weights=[93, 3, 3, 1, 1], k=1)[0]

                # Ginger is often duplicated to increase its chances
                if cat.pelt.colour in ["WHITE", "SILVER", "BRONZE", "CADET", "PALEBOW", "TURQUOISE", "TIFFANY", 
                                            "SHINYMEW", "SKY", "POWDERBLUE", "PUDDLE"]:
                    cat.tortiecolour = choice([ 'PALECREAM', 'CREAM', 'SAND', 'WOOD', 'PANTONE', 'SAMON', 'THISTLE', 'PETAL', 
                                                'MEW', 'CORAL', 'FLORAL', 'LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 
                                                'EMERALD', 'OLIVE'] + (pride_colours * 2))
                elif cat.pelt.colour in ["GREY", "MARENGO", "BATTLESHIP", "BLUEGREY", "STEEL", "SLATE", "SAPPHIRE", "OCEAN", 
                                            "DENIUM", "TEAL", "COBALT", "INDIGOBLUE", "INDIGOLIGHT"]:
                    cat.tortiecolour = choice(['ROSE', 'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'APRICOT', 'GARFIELD', 
                                                'APPLE', 'DARKSAMON', 'AMYTHYST', 'MAGENTA', 'HEATHER', 'ORCHID', 'PURPLE', 
                                                'CHERRY', 'TART', 'DARKOLIVE', 'GREEN', 'SPINNACH', 'SEAWEED', 'SACRAMENTO', 
                                                'SEAGRASS'] + (pride_colours * 2))
                elif cat.pelt.colour in ["SOOT", "DARKGREY", "ANCHOR", "CHARCOAL", "COAL", "BLACK", "PITCH", "DUSKBOW", "SONIC", 
                                            "JEANS", "NAVY", "JACKET", "DEEPOCEAN", "NIGHTTIME"]:
                    cat.tortiecolour = choice(['SCARLET', 'RED', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 
                                                'RASIN', 'STRAKIT', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 'BARN', 'GARNET',
                                                'FOREST', 'JADE', 'DEEPFOREST', 'SEAFOAM', 'MALACHITE'] + (pride_colours * 2))
                
                elif cat.pelt.colour in ["PALECREAM", "CREAM", "SAND", "WOOD", "PANTONE", "SAMON", "THISTLE", "PETAL", "MEW", 
                                            "CORAL", "FLORAL"]:
                    cat.tortiecolour = choice(['WHITE', 'SILVER', 'BRONZE', 'CADET', 'PALEBOW',  'TURQUOISE', 'TIFFANY', 
                                                'SHINYMEW', 'SKY', 'POWDERBLUE', 'PUDDLE', 'LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 
                                                'MINT', 'EMERALD', 'OLIVE'] + (pride_colours * 2))
                elif cat.pelt.colour in ["ROSE", "GINGER", "SUNSET", "RUFOUS", "FIRE", "BRICK", "APRICOT", "GARFIELD", "APPLE", 
                                            "DARKSAMON", "AMYTHYST", "MAGENTA", "HEATHER", "ORCHID", "PURPLE", "CHERRY", "TART"]:
                    cat.tortiecolour = choice(['GREY', 'MARENGO', 'BATTLESHIP', 'BLUEGREY', 'STEEL', 'SLATE', 'SAPPHIRE', 'OCEAN', 
                                                'DENIUM', 'TEAL', 'COBALT', 'INDIGOBLUE', 'INDIGOLIGHT', 'DARKOLIVE', 'GREEN', 
                                                'SPINNACH', 'SEAWEED', 'SACRAMENTO', 'SEAGRASS'] + (pride_colours * 2))
                elif cat.pelt.colour in ["SCARLET", "RED", "CRIMSON", "BURNT", "CARMINE", "COSMOS", "ROSEWOOD", "BLOOD", 
                                            "RASIN", "STRAKIT", "WINE", "BRIGHTCRIMSON", "ROYALPURPLE", "BARN", "GARNET"]:                   
                    cat.tortiecolour = choice(['SOOT', 'DARKGREY', 'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'PITCH', 'DUSKBOW', 
                                                'SONIC', 'JEANS', 'NAVY', 'JACKET', 'DEEPOCEAN', 'NIGHTTIME', 'FOREST', 'JADE', 
                                                'DEEPFOREST', 'SEAFOAM', 'MALACHITE'] + (pride_colours * 2))

                elif cat.pelt.colour in ["BEIGE", "MEERKAT", "KHAKI", "BANNANA", "FARROW", "HAY", "GOLD", "HONEY", "IVORY", "LEMON", 
                                            "LAGUNA", "FAWN"]:
                    cat.tortiecolour = choice(['WHITE', 'SILVER', 'BRONZE', 'CADET', 'PALEBOW',  'TURQUOISE', 'TIFFANY', 'SHINYMEW', 'SKY', 
                                                'POWDERBLUE', 'PUDDLE', 'PALECREAM', 'CREAM', 'SAND', 'WOOD', 'PANTONE', 'SAMON', 'THISTLE', 
                                                'PETAL', 'MEW', 'CORAL', 'FLORAL', 'LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 
                                                'EMERALD', 'OLIVE'] + (pride_colours * 2))
                elif cat.pelt.colour in ["CAPPUCCINO", "ECRU", "ASHBROWN", "DUSTBROWN", "SANDALWOOD", "PINECONE", "WRENGE", "BROWN", 
                                            "MINK", "CHESTNUT", "TAN", "HAZELNUT", "MEDALLION", "YELLOW", "CORN", "BEE", 
                                            "SUNSHINE", "PYRITE"]:
                    cat.tortiecolour = choice(['GREY', 'MARENGO', 'BATTLESHIP', 'BLUEGREY', 'STEEL', 'SLATE', 'SAPPHIRE', 'OCEAN', 
                                                'DENIUM', 'TEAL', 'COBALT', 'INDIGOBLUE', 'INDIGOLIGHT','ROSE', 'GINGER', 'SUNSET', 
                                                'RUFOUS', 'FIRE', 'BRICK', 'APRICOT', 'GARFIELD', 'APPLE', 'DARKSAMON', 'AMYTHYST', 
                                                'MAGENTA', 'HEATHER', 'ORCHID', 'PURPLE', 'CHERRY', 'TART', 'DARKOLIVE', 'GREEN', 
                                                'SPINNACH', 'SEAWEED', 'SACRAMENTO', 'SEAGRASS'] + (pride_colours * 2))
                elif cat.pelt.colour in ["DARKBROWN", "BEAVER", "CHOCOLATE", "MOCHA", "COFFEE", "TAUPE", "UMBER", "SADDLE", "CEDAR", 
                                            "ONYX", "PINEAPPLE", "TROMBONE", "BRASS", "GRANOLA", "RUST"]:
                    cat.tortiecolour = choice(['SOOT', 'DARKGREY', 'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'PITCH', 'DUSKBOW', 'SONIC', 
                                                'JEANS', 'NAVY', 'JACKET', 'DEEPOCEAN', 'NIGHTTIME', 'SCARLET', 'RED', 'CRIMSON', 'BURNT', 
                                                'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 'RASIN', 'STRAKIT', 'WINE', 'BRIGHTCRIMSON', 
                                                'ROYALPURPLE', 'BARN', 'GARNET', 'FOREST', 'JADE', 'DEEPFOREST', 
                                                'SEAFOAM', 'MALACHITE'] + (pride_colours * 2))

                elif cat.pelt.colour in ["LIME", "CHARTRUSE", "LETTUCE", "GRASS", "MINT", "EMERALD", "OLIVE"]:
                    cat.tortiecolour = choice (['WHITE', 'SILVER', 'BRONZE', 'CADET', 'PALEBOW',  'TURQUOISE', 'TIFFANY', 'SHINYMEW', 'SKY', 
                                                'POWDERBLUE', 'PUDDLE','PALECREAM', 'CREAM', 'SAND', 'WOOD', 'PANTONE', 'SAMON', 'THISTLE', 
                                                'PETAL', 'MEW', 'CORAL', 'FLORAL'] + (pride_colours * 2))
                elif cat.pelt.colour in ["DARKOLIVE", "GREEN", "SPINNACH", "SEAWEED", "SACRAMENTO", "SEAGRASS"]:
                    cat.tortiecolour = choice (['GREY', 'MARENGO', 'BATTLESHIP', 'BLUEGREY', 'STEEL', 'SLATE', 'SAPPHIRE', 'OCEAN', 'DENIUM', 
                                                'TEAL', 'COBALT', 'INDIGOBLUE', 'INDIGOLIGHT', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS', 
                                                'FIRE', 'BRICK', 'APRICOT', 'GARFIELD', 'APPLE', 'DARKSAMON', 'AMYTHYST', 'MAGENTA', 'HEATHER', 
                                                'ORCHID', 'PURPLE', 'CHERRY', 'TART'] + (pride_colours * 2))
                elif cat.pelt.colour in ["FOREST", "JADE", "DEEPFOREST", "SEAFOAM", "MALACHITE"]:
                    cat.tortiecolour = choice (['SOOT', 'DARKGREY', 'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'PITCH', 'DUSKBOW', 'SONIC', 'JEANS', 
                                                'NAVY', 'JACKET', 'DEEPOCEAN', 'NIGHTTIME', 'SCARLET', 'RED', 'CRIMSON', 'BURNT', 'CARMINE', 
                                                'COSMOS', 'ROSEWOOD', 'BLOOD', 'RASIN', 'STRAKIT', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 'BARN', 
                                                'GARNET'] + (pride_colours * 2))  
                            
                elif cat.pelt.colour == "GLASS":
                    possible_colors = pelt_colours.copy()
                    possible_colors.remove(cat.pelt.colour)
                    cat.tortiecolour = choice(possible_colors)
                
                elif cat.pelt.colour in pride_colours:
                    possible_colors = pride_colours.copy()
                    possible_colors.remove(cat.pelt.colour)
                    possible_colors.extend(['STRAKIT', 'PITCH', 'PALEBOW', 'DUSKBOW'])
                    cat.tortiecolour = choice(possible_colors)

        else:
            cat.tortiecolour = choice(pride_colours)
    else:
        cat.tortiebase = None
        cat.tortiepattern = None
        cat.tortiecolour = None
        cat.pattern = None


def white_patches_inheritance(cat, parents: tuple):

    par_whitepatches = set()
    par_points = []
    for p in parents:
        if p:
            if p.white_patches:
                par_whitepatches.add(p.white_patches)
            if p.points:
                par_points.append(p.points)

    if not parents:
        print("Error - no parents. Randomizing white patches.")
        randomize_white_patches(cat)
        return

    # Direct inheritance. Will only work if at least one parent has white patches, otherwise continue on.
    if par_whitepatches and not randint(0, game.config["cat_generation"]["direct_inheritance"]):
        # This ensures Torties and Calicos won't get direct inheritance of incorrect white patch types
        _temp = par_whitepatches.copy()
        if cat.pelt.name == "Tortie":
            for p in _temp.copy():
                if p in high_white + mostly_white + ["FULLWHITE"]:
                    _temp.remove(p)
        elif cat.pelt.name == "Calico":
            for p in _temp.copy():
                if p in little_white + mid_white:
                    _temp.remove(p)

        # Only proceed with the direct inheritance if there are white patches that match the pelt.
        if _temp:
            cat.white_patches = choice(list(_temp))

            # Direct inheritance also effect the point marking.
            if par_points and cat.pelt.name != "Tortie":
                cat.points = choice(par_points)
            else:
                cat.points = None

            return

    # dealing with points
    if par_points:
        chance = 10 - len(par_points)
    else:
        chance = 40

    if cat.pelt != "Tortie" and not (random.random() * chance):
        cat.points = choice(point_markings)
    else:
        cat.points = None


    white_list = [little_white, mid_white, high_white, mostly_white, ['FULLWHITE']]

    weights = [0, 0, 0, 0, 0]  # Same order as white_list
    for p_ in par_whitepatches:
        if p_ in little_white:
            add_weights = (40, 20, 15, 5, 0)
        elif p_ in mid_white:
            add_weights = (10, 40, 15, 10, 0)
        elif p_ in high_white:
            add_weights = (15, 20, 40, 10, 1)
        elif p_ in mostly_white:
            add_weights = (5, 15, 20, 40, 5)
        elif p_ == "FULLWHITE":
            add_weights = (0, 5, 15, 40, 10)
        else:
            add_weights = (0, 0, 0, 0, 0)

        for x in range(0, len(weights)):
            weights[x] += add_weights[x]


    # If all the weights are still 0, that means none of the parents have white patches.
    if not any(weights):
        if not all(parents):  # If any of the parents are None (unknown), use the following distribution:
            weights = [20, 10, 10, 5, 0]
        else:
            # Otherwise, all parents are known and don't have any white patches. Focus distribution on little_white.
            weights = [50, 5, 0, 0, 0]

    # Adjust weights for torties, since they can't have anything greater than mid_white:
    if cat.pelt.name == "Tortie":
        weights = weights[:2] + [0, 0, 0]
        # Another check to make sure not all the values are zero. This should never happen, but better
        # safe then sorry.
        if not any(weights):
            weights = [2, 1, 0, 0, 0]
    elif cat.pelt.name == "Calico":
        weights = [0, 0, 0] + weights[3:]
        # Another check to make sure not all the values are zero. This should never happen, but better
        # safe then sorry.
        if not any(weights):
            weights = [2, 1, 0, 0, 0]
    elif cat.pelt.name == "Ponit" or cat.tortiebase == "Ponit":
        weights = [2, 1, 1, 0, 0]
        if not any(weights):
            weights = [2, 1, 1, 0, 0]
    elif cat.tortiebase == "Spirit" or cat.tortiebase == "Starpelt":
        weights = [2, 1, 0, 0, 0]
        if not any(weights):
            weights = [2, 1, 0, 0, 0]

    chosen_white_patches = choice(
        random.choices(white_list, weights=weights, k=1)[0]
    )

    cat.white_patches = chosen_white_patches
    if cat.points and cat.white_patches in [high_white, mostly_white, 'FULLWHITE']:
        cat.points = None


def randomize_white_patches(cat):

    # Points determination. Tortie can't be pointed
    if cat.pelt.name != "Tortie" and not random.getrandbits(game.config["cat_generation"]["random_point_chance"]):
        # Cat has colorpoint!
        cat.points = choice(point_markings)
    else:
        cat.points = None

    # Adjust weights for torties, since they can't have anything greater than mid_white:
    if cat.pelt.name == "Tortie":
        weights = (2, 1, 0, 0, 0)
    elif cat.pelt.name == "Ponit" or cat.tortiebase == "Ponit":
        weights = (2, 1, 1, 0, 0)
    elif cat.tortiebase == "Spirit":
        weights = (2, 1, 0, 0, 0)
    elif cat.pelt.name == "Calico":
        weights = (0, 0, 20, 15, 1)
    else:
        weights = (10, 10, 10, 10, 1)

    white_list = [little_white, mid_white, high_white, mostly_white, ['FULLWHITE']]
    chosen_white_patches = choice(
        random.choices(white_list, weights=weights, k=1)[0]
    )

    cat.white_patches = chosen_white_patches
    if cat.points and cat.white_patches in [high_white, mostly_white, 'FULLWHITE']:
        cat.points = None

def init_white_patches(cat):

    if cat.pelt is None:
        init_pelt(cat)

    #Gather parents
    par1 = None
    par2 = None
    if cat.parent1 in cat.all_cats:
        par1 = cat.all_cats[cat.parent1]
    if cat.parent2 in cat.all_cats:
        par2 = cat.all_cats[cat.parent2]

    # Vit can rool for anyone, not just cats who rolled to have white in their pelt. 
    par_vit = []
    for p in (par1, par2):
        if p:
            if p.vitiligo:
                par_vit.append(p.vitiligo)
    
    vit_chance = max(game.config["cat_generation"]["vit_chance"] - len(par_vit), 0)
    if not random.getrandbits(vit_chance):
        cat.vitiligo = choice(vit)

    if cat.white_patches or cat.points:
        return

    # If the cat was rolled previously to have white patches, then determine the patch they will have
    # these functions also handle points. 
    if cat.pelt.white:
        if par1 or par2:
            white_patches_inheritance(cat, (par1, par2))
        else:
            randomize_white_patches(cat)
            

def init_tint(cat):
    """Sets tint for pelt and white patches"""

    # PELT TINT
    hit = randint(0, 45)
    if hit <= 5:
        if cat.pelt.colour in [black_colours, grey_colours, white_colours, blue_colours]:
            possible_tints = Sprites.cat_tints["possible_tints"]["greyscale"].copy()
            cat.tint = choice(possible_tints)
        elif cat.pelt.colour in [ginger_colours, cream_colours, purple_colours]:
            possible_tints = Sprites.cat_tints["possible_tints"]["gingerscale"].copy()
            cat.tint = choice(possible_tints)
        elif cat.pelt.colour in [brown_colours, yellow_colours]:
            possible_tints = Sprites.cat_tints["possible_tints"]["brownscale"].copy()
            cat.tint = choice(possible_tints)
        elif cat.pelt.colour in green_colours:
            possible_tints = Sprites.cat_tints["possible_tints"]["greenscale"].copy()
            cat.tint = choice(possible_tints)
        elif cat.pelt.colour in pride_colours:
            cat.tint = "none"
    elif hit <= 8:
        possible_tints = Sprites.cat_tints["possible_tints"]["any"].copy()
        cat.tint = choice(possible_tints)        
    else:
        cat.tint = "none"

    # WHITE PATCHES TINT
    if cat.white_patches or cat.points:
        #Now for white patches
        possible_tints = Sprites.white_patches_tints["possible_tints"]["basic"].copy()
        cat.white_patches_tint = choice(possible_tints)
    else:
        cat.white_patches_tint = "none"
        
    # EYE TINT:
    cat.eye_tint = "none"

