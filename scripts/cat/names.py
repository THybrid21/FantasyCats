import random
import os
import ujson
from .pelts import (
    black_colours,
    brown_colours,
    ginger_colours,
    white_colours,
    cream_colours,
    grey_colours,
    blue_colours,
    yellow_colours,
    green_colours,
    purple_colours,
    pride_colours,
    tabbies,
    spotted,
    exotic,
    sparkle_cats,
    torties,
    )

from scripts.housekeeping.datadir import get_save_dir

from scripts.game_structure.game_essentials import game


class Name():
    if os.path.exists('resources/dicts/names/names.json'):
        with open('resources/dicts/names/names.json') as read_file:
            names_dict = ujson.loads(read_file.read())

        if os.path.exists(get_save_dir() + '/prefixlist.txt'):
            with open(get_save_dir() + '/prefixlist.txt', 'r') as read_file:
                name_list = read_file.read()
                if_names = len(name_list)
            if if_names > 0:
                new_names = name_list.split('\n')
                for new_name in new_names:
                    if new_name != '':
                        if new_name.startswith('-'):
                            while new_name[1:] in names_dict["normal_prefixes"]:
                                names_dict["normal_prefixes"].remove(new_name[1:])
                        else:
                            names_dict["normal_prefixes"].append(new_name)

        if os.path.exists(get_save_dir() + '/suffixlist.txt'):
            with open(get_save_dir() + '/suffixlist.txt', 'r') as read_file:
                name_list = read_file.read()
                if_names = len(name_list)
            if if_names > 0:
                new_names = name_list.split('\n')
                for new_name in new_names:
                    if new_name != '':
                        if new_name.startswith('-'):
                            while new_name[1:] in names_dict["normal_suffixes"]:
                                names_dict["normal_suffixes"].remove(new_name[1:])
                        else:
                            names_dict["normal_suffixes"].append(new_name)

        if os.path.exists(get_save_dir() + '/specialsuffixes.txt'):
            with open(get_save_dir() + '/specialsuffixes.txt', 'r') as read_file:
                name_list = read_file.read()
                if_names = len(name_list)
            if if_names > 0:
                new_names = name_list.split('\n')
                for new_name in new_names:
                    if new_name != '':
                        if new_name.startswith('-'):
                            del names_dict["special_suffixes"][new_name[1:]]
                        elif ':' in new_name:
                            _tmp = new_name.split(':')
                            names_dict["special_suffixes"][_tmp[0]] = _tmp[1]


    def __init__(self, 
                 status="warrior",
                 prefix=None,
                 suffix=None,
                 colour=None,
                 pelt=None,
                 tortiebase=None,
                 biome=None,
                 specsuffix_hidden=False,
                 load_existing_name = False):
        self.status = status
        self.prefix = prefix
        self.suffix = suffix
        self.specsuffix_hidden = specsuffix_hidden
        name_fixpref = False

        # Set prefix
        if prefix is None:
            self.give_prefix(colour, biome)
            # needed for random dice when we're changing the Prefix
            name_fixpref = True
                    
        # Set suffix
        if self.suffix is None and not str(self.suffix) == '':
            self.give_suffix(pelt, biome, tortiebase)
            if name_fixpref and self.prefix is None:
                # needed for random dice when we're changing the Prefix
                name_fixpref = False

        if self.suffix and not load_existing_name:
            # Prevent triple letter names from joining prefix and suffix from occuring (ex. Beeeye)
            triple_letter = False
            possible_three_letter = (self.prefix[-2:] + self.suffix[0], self.prefix[-1] + self.suffix[:2])
            if all(i == possible_three_letter[0][0] for i in possible_three_letter[0]) or \
                    all(i == possible_three_letter[1][0] for i in possible_three_letter[1]):
                triple_letter = True
            # Prevent double animal names (ex. Spiderfalcon)
            double_animal = False
            if self.prefix in self.names_dict["animal_prefixes"] and self.suffix in self.names_dict["animal_suffixes"]:
                double_animal = True
            # Prevent the inappropriate names
            nono_name = self.prefix + self.suffix
            # Prevent double names (ex. Iceice)
            # Prevent suffixes containing the prefix (ex. Butterflyfly)

            i = 0
            while nono_name in self.names_dict["inappropriate_names"] or triple_letter or double_animal or self.suffix == self.prefix.casefold() or str(self.suffix) in \
                self.prefix.casefold() and not str(self.suffix) == '':

                # check if random die was for prefix
                if name_fixpref:
                    self.give_prefix(colour, biome)
                else:
                    self.give_suffix(pelt, biome, tortiebase)
                
                nono_name = self.prefix + self.suffix
                possible_three_letter = (self.prefix[-2:] + self.suffix[0], self.prefix[-1] + self.suffix[:2])    
                if not(all(i == possible_three_letter[0][0] for i in possible_three_letter[0]) or \
                        all(i == possible_three_letter[1][0] for i in possible_three_letter[1])):
                    triple_letter = False
                if not(self.prefix in self.names_dict["animal_prefixes"] and self.suffix in self.names_dict["animal_suffixes"]):
                    double_animal = False
                i += 1
    
    # Generate possible prefix
    def give_prefix(self, colour, biome):
        named_after_biome = not random.getrandbits(3) # chance for True is 1/8
        # Add possible prefix categories to list.
        possible_prefix_categories = []
        if colour is not None:
            if colour in black_colours:
                possible_prefix_categories.append(self.names_dict["black_prefixes"])
            elif colour in grey_colours:
                possible_prefix_categories.append(self.names_dict["grey_prefixes"])
            elif colour in white_colours:
                possible_prefix_categories.append(self.names_dict["white_prefixes"])
            elif colour in ginger_colours:
                possible_prefix_categories.append(self.names_dict["ginger_prefixes"])
            elif colour in brown_colours:
                possible_prefix_categories.append(self.names_dict["brown_prefixes"])                   
            elif colour in cream_colours:
                possible_prefix_categories.append(self.names_dict["cream_prefixes"])
            elif colour in yellow_colours:
                possible_prefix_categories.append(self.names_dict["yellow_prefixes"])
            elif colour in green_colours:
                possible_prefix_categories.append(self.names_dict["green_prefixes"])                    
            elif colour in blue_colours:
                possible_prefix_categories.append(self.names_dict["blue_prefixes"])
            elif colour in purple_colours:
                possible_prefix_categories.append(self.names_dict["purple_prefixes"])
            elif colour in pride_colours:
                possible_prefix_categories.append(self.names_dict["pride_prefixes"][colour]) 
        if possible_prefix_categories and not named_after_biome:
            prefix_category = random.choice(possible_prefix_categories)
            self.prefix = random.choice(prefix_category)
        elif named_after_biome and possible_prefix_categories:
            if biome is not None and biome in self.names_dict["biome_prefixes"]:
                possible_prefix_categories.clear()
                possible_prefix_categories.append(self.names_dict["biome_prefixes"][biome])
                prefix_category = random.choice(possible_prefix_categories)
                self.prefix = random.choice(prefix_category)
            else:
                self.prefix = random.choice(self.names_dict["normal_prefixes"])
        else:
            self.prefix = random.choice(self.names_dict["normal_prefixes"])

    
    # Generate possible suffix
    def give_suffix(self, pelt, biome, tortiebase):
        named_after_pelt = not random.getrandbits(2) # Pelt name only gets used if there's an associated suffix.
        possible_suffix_categories = []
        if named_after_pelt:
            possible_suffix_categories.append(self.names_dict["normal_suffixes"])
            if pelt in tabbies or tortiebase in tabbies:
                possible_suffix_categories.append(self.names_dict["tabby_suffixes"])
            elif pelt in spotted or tortiebase in spotted:
                possible_suffix_categories.append(self.names_dict["spotted_suffixes"])
            elif pelt in exotic or tortiebase in exotic:
                possible_suffix_categories.append(self.names_dict["exotic_suffixes"])
            elif pelt in exotic or tortiebase in sparkle_cats:
                possible_suffix_categories.append(self.names_dict["sparkle_suffixes"])
            elif pelt in torties:
                possible_suffix_categories.append(self.names_dict["tortie_suffixes"])   
        if possible_suffix_categories:    
            suffix_category = random.choice(possible_suffix_categories)
            self.suffix = random.choice(suffix_category)
        else:
            self.suffix = random.choice(self.names_dict["normal_suffixes"])
    
    def __repr__(self):
        if self.status in self.names_dict["special_suffixes"] and not self.specsuffix_hidden:
            return self.prefix + self.names_dict["special_suffixes"][self.status]
        else:
            if game.config['fun']['april_fools']:
                return self.prefix + 'egg'
            return self.prefix + self.suffix



names = Name()
