import logging
import os
from copy import copy

import pygame
import ujson

from scripts.cat.enums import CatGroup
from scripts.game_structure import constants, image_cache
from scripts.game_structure.game.settings import game_setting_get
from scripts.special_dates import SpecialDate, is_today
from scripts.game_structure.game_essentials import game

logger = logging.getLogger(__name__)


class Sprites:
    cat_tints = {}
    white_patches_tints = {}
    clan_symbols = []

    def __init__(self):
        """Class that handles and hold all spritesheets.
        Size is normally automatically determined by the size
        of the lineart. If a size is passed, it will override
        this value."""
        self.symbol_dict = None
        self.size = None
        self.spritesheets = {}
        self.images = {}
        self.sprites = {}

        # Shared empty sprite for placeholders
        self.blank_sprite = None

        self.load_tints()

    def load_tints(self):
        try:
            with open("sprites/dicts/tint.json", "r", encoding="utf-8") as read_file:
                self.cat_tints = ujson.loads(read_file.read())
        except IOError:
            print("ERROR: Reading Tints")

        try:
            with open(
                "sprites/dicts/white_patches_tint.json", "r", encoding="utf-8"
            ) as read_file:
                self.white_patches_tints = ujson.loads(read_file.read())
        except IOError:
            print("ERROR: Reading White Patches Tints")

        try:
            with open("sprites/dicts/vitiligo_tint.json", 'r') as read_file:
                self.vitiligo_tint = ujson.loads(read_file.read())
        except IOError:
            print("ERROR: Reading Vitiligo Tints")

    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def make_group(
        self, 
        spritesheet, 
        pos, 
        name, 
        sprites_x=9, 
        sprites_y=7, 
        no_index=False):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a spritesheet into groups of sprites that are easily accessible
        :param spritesheet: Name of spritesheet file
        :param pos: (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites
        :param name: Name of group being made
        :param sprites_x: default 3, number of sprites horizontally
        :param sprites_y: default 3, number of sprites vertically
        :param no_index: default False, set True if sprite name does not require cat pose index
        """

        group_x_ofs = pos[0] * sprites_x * self.size
        group_y_ofs = pos[1] * sprites_y * self.size
        i = 0

        # splitting group into singular sprites and storing into self.sprites section
        for y in range(sprites_y):
            for x in range(sprites_x):
                if no_index:
                    full_name = f"{name}"
                else:
                    full_name = f"{name}{i}"

                try:
                    new_sprite = pygame.Surface.subsurface(
                        self.spritesheets[spritesheet],
                        group_x_ofs + x * self.size,
                        group_y_ofs + y * self.size,
                        self.size,
                        self.size,
                    )

                except ValueError:
                    # Fallback for non-existent sprites
                    print(f"WARNING: nonexistent sprite - {full_name}")
                    if not self.blank_sprite:
                        self.blank_sprite = pygame.Surface(
                            (self.size, self.size), pygame.HWSURFACE | pygame.SRCALPHA
                        )
                    new_sprite = self.blank_sprite

                self.sprites[full_name] = new_sprite
                i += 1

    def load_all(self):
        if not game.sprite_folders:
            raise Exception("[SPS] Cannot find sprite folders or none exist")

        lineart = pygame.image.load('sprites/1/lineart.png')

        # get the width and height of the spritesheet
        width, height = lineart.get_size()
        del lineart  # unneeded

        # if anyone changes lineart for whatever reason update this
        if isinstance(self.size, int):
            pass
        elif width / 9 == height / 7:
            self.size = width / 9
        else:
            self.size = 50  # default, what base clangen uses
            print(f"lineart.png is not 9x7, falling back to {self.size}")
            print(
                f"if you are a modder, please update scripts/cat/sprites.py and "
                f"do a search for 'if width / 9 == height / 7:'"
            )

        del width, height  # unneeded

        # load sprite sheets for all folders
        for f in game.sprite_folders:
            for x in [
                "lineart", "lineartdf", "lineartdead", "lineartur",
                "line_sc_overlay", "line_ur_overlay", "line_ur_underlay", "gradient_ur",
                "eyes", "eyes2", "eyes3", "eyes4", "eyes5", 
                "hybrideyes", "hybrideyes2", "hybrideyes3", "hybrideyes4", "hybrideyes5",  
                "skin", "skingills", "blep", 
                "scars", "missingscars", "hybridscars",
                
                "singlecolours",
                
                "shadersnewwhite", "lightingnew",
                "fademask", "fadestarclan", "fadedarkforest", "fadeunknownresidence",
                "symbols",
            ]:
                if "lineart" in x and (
                    constants.CONFIG["fun"]["april_fools"]
                    or is_today(SpecialDate.APRIL_FOOLS)
                ):
                    self.spritesheet(f"sprites/{f}/aprilfools{x}.png", x)
                elif 'symbols' in x:
                    self.spritesheet(f"sprites/{x}.png", x)
                else:
                    self.spritesheet(f"sprites/{f}/{x}.png", x)

            for x in [
                "whitepatches", "tortiepatchesmasks", "vitiligo", 
                "colourpointpatches", "albinism", "melanism"
            ]:
                sprites.spritesheet(f"sprites/{f}/patches/{x}.png", x) 

            for x in [
                "medcatherbs", "wild", "collars", "bellcollars", "bowcollars", "nyloncollars",
            ]:
                sprites.spritesheet(f"sprites/{f}/accessories/{x}.png", x)

            # Line art
            self.make_group("lineart", (0, 0), f"lines{f}_")
            self.make_group("shadersnewwhite", (0, 0), f"shaders{f}_")
            self.make_group("lightingnew", (0, 0), f"lighting{f}_")

            self.make_group("lineartdead", (0, 0), "lineartdead{f}_")
            self.make_group("lineartdf", (0, 0), "lineartdf{f}_")
            self.make_group("lineartur", (0, 0), "lineartur{f}_")
            self.make_group("line_sc_overlay", (0, 0), "sc_overlay{f}_")
            self.make_group("line_ur_underlay", (0, 0), "ur_underlay{f}_")
            self.make_group("line_ur_overlay", (0, 0), "ur_overlay{f}_")
            self.make_group("gradient_ur", (0, 0), "gradient_ur{f}_")

            # Fading Fog
            for i in range(0, 3):
                self.make_group("fademask", (i, 0), f"fademask{f}_{i}")
                self.make_group("fadestarclan", (i, 0), f"fadestarclan{f}_{i}")
                self.make_group("fadedarkforest", (i, 0), f"fadedf{f}_{i}")
                self.make_group("fadeunknownresidence", (i, 0), f"fadeur{f}_{i}")

            # Define eye colors
            eye_colors = [
                ["YELLOW", "AMBER", "HAZEL", "PALEGREEN", "GREEN", "BLUE", "DARKBLUE", "GREY", "CYAN", "EMERALD", 
                "HEATHERBLUE", "SUNLITICE"],
                ["COPPER", "SAGE", "COBALT", "PALEBLUE", "BRONZE", "SILVER", "PALEYELLOW", "GOLD", "GREENYELLOW", 
                "SUNSET", "GHOST", "VOID"]
            ]

            for row, colors in enumerate(eye_colors):
                for col, color in enumerate(colors):
                    self.make_group("eyes", (col, row), f"eyes{f}_{color}")
                    self.make_group("eyes2", (col, row), f"eyes2{f}_{color}")
                    self.make_group('eyes3', (col, row), f'eyes3{f}_{color}')
                    self.make_group('eyes4', (col, row), f'eyes4{f}_{color}')
                    self.make_group('eyes5', (col, row), f'eyes5{f}_{color}')

            hybrid_eyes = [
                ["POPPY", "CRIMSON", "RUBY", "PINKPOPPY", "BROWN", "BROWNTWO", "PEANUT", "CHOCMINT", "MINTCHOC",
                "MINT", "JADE", "GRASS"],
                ["STRAWBERRY", "VIOLET", "LILAC", "GRAPE", "INDIGO", "COBOLT", "AZURE", "OCEAN", "DEPTHS", "SKY",
                "BEACH", "SUNGRASS"],
                ["WHITE", "MONOCHROME", "MONOCHROMETWO", "MONOCHROMETHREE", "LILACGREY", "GREYTWO", "GREYCOAL", 
                "FAUXVOID", "ASPEN", "GREENGREY", "ECTOPLASM", "YELLOWOLIVE"],
                ["AMBERTWO", "SUNSHINE", "PYRITE", "PRIMARY", "PRIMARYB", "PRIMARYC", "CHROME", "CHROMEB", 
                "CHROMEC", "RGB", "RGBTWO", "RGBTHREE"]
        ]

            for row, colors in enumerate(hybrid_eyes):
                for col, color in enumerate(colors):
                    self.make_group('hybrideyes', (col, row), f'eyes{f}_{color}')
                    self.make_group('hybrideyes2', (col, row), f'eyes2{f}_{color}')
                    self.make_group('hybrideyes3', (col, row), f'eyes3{f}_{color}')
                    self.make_group('hybrideyes4', (col, row), f'eyes4{f}_{color}')
                    self.make_group('hybrideyes5', (col, row), f'eyes5{f}_{color}')

            # Define white patches
            white_patches = [
                [
                    "FULLWHITE", "ANY", "TUXEDO", "LITTLE", "COLOURPOINT", "VAN", "ANYTWO",
                    "MOON", "PHANTOM", "POWDER", "BLEACHED", "SAVANNAH", "FADESPOTS",
                    "PEBBLESHINE",
                ],
                [
                    "EXTRA", "ONEEAR", "BROKEN", "LIGHTTUXEDO", "BUZZARDFANG", "RAGDOLL",
                    "LIGHTSONG", "VITILIGO", "BLACKSTAR", "PIEBALD", "CURVED", "PETAL", "SHIBAINU",
                    "OWL",
                ],
                [
                    "TIP", "FANCY", "FRECKLES", "RINGTAIL", "HALFFACE", "PANTSTWO", "GOATEE", "VITILIGOTWO",
                    "PAWS", "MITAINE", "BROKENBLAZE", "SCOURGE", "DIVA", "BEARD",
                ],
                [
                    "TAIL", "BLAZE", "PRINCE", "BIB", "VEE", "UNDERS", "HONEY", "FAROFA", "DAMIEN", "MISTER",
                    "BELLY", "TAILTIP", "TOES", "TOPCOVER",
                ],
                [
                    "APRON", "CAPSADDLE", "MASKMANTLE", "SQUEAKS", "STAR", "TOESTAIL", "RAVENPAW", "PANTS",
                    "REVERSEPANTS", "SKUNK", "KARPATI", "HALFWHITE",  "APPALOOSA", "DAPPLEPAW",
                ],
                [
                    "HEART", "LILTWO", "GLASS", "MOORISH", "SEPIAPOINT", "MINKPOINT", "SEALPOINT",
                    "MAO", "LUNA", "CHESTSPECK", "WINGS", "PAINTED", "HEARTTWO", "WOODPECKER",
                ],
                [
                    "BOOTS", "MISS", "COW", "COWTWO", "BUB", "BOWTIE", "MUSTACHE", "REVERSEHEART",
                    "SPARROW", "VEST", "LOVEBUG", "TRIXIE", "SAMMY", "SPARKLE",
                ],
                [
                    "RIGHTEAR", "LEFTEAR", "ESTRELLA", "SHOOTINGSTAR", "EYESPOT", "REVERSEEYE",
                    "FADEBELLY", "FRONT", "BLOSSOMSTEP", "PEBBLE", "TAILTWO", "BUDDY", "BACKSPOT", "EYEBAGS",
                ],
                [
                    "BULLSEYE", "FINN", "DIGIT", "KROPKA", "FCTWO", "FCONE", "MIA", "SCAR", "BUSTER", "SMOKEY",
                    "HAWKBLAZE", "CAKE", "ROSINA", "PRINCESS",
                ],
                [
                    "LOCKET", "BLAZEMASK", "TEARS", "DOUGIE"
                ],
            ]

            for row, patches in enumerate(white_patches):
                for col, patch in enumerate(patches):
                    self.make_group("whitepatches", (col, row), f"white{f}_{patch}")

            vitiligo = [
                ["VITILIGO", "VITILIGOTWO", "MOON", "PHANTOM", "POWDER", "BLEACHED", "SMOKEY"], 
                ["SHADOWSIGHT", "HALFSPLASH"]
            ]
            
            for row, vitiligo in enumerate(vitiligo):
                for col, vit in enumerate(vitiligo):
                    self.make_group("vitiligo", (col, row), f"white{f}_{vit}")

            colourpoint = [
                ["COLOURPOINT", "RAGDOLL", "KARPATI", "SEPIAPOINT", "MINKPOINT", "SEALPOINT"], 
                ["REVERSEPOINT", "PONIT", "LIGHTPOINT", "SNOWSHOE", "SNOWBOOT", "WHITEPOINT"]
            ]
            
            for row, colourpoint in enumerate(colourpoint):
                for col, colorpoint in enumerate(colourpoint):
                    self.make_group("colourpointpatches", (col, row), f"white{f}_{colorpoint}")

            ##Albinism + Melanism Sheets
            for a, i in enumerate(
                    ["FLATALBINO", "REDALBINO", "PINKALBINO", "VIOLETALBINO", "BLUEALBINO", "GREENALBINO",
                        "YELLOWALBINO"]):
                self.make_group("albinism", (a, 0), f"albinism{f}_{i}")     
            for a, i in enumerate(
                    ["PINK", "VIOLETPINK", "YELLOWPINK", "CYANPINK", "BLUEPINK", "MINTPINK", "NACRE", 
                        "GHOSTPINK", "LIGHTPOPPY", "LIGHTBROWN"]):
                self.make_group("albinism", (a, 1), f"eyes{f}_" + i)
                self.make_group("albinism", (a, 2), f"eyes2{f}_{i}")
                self.make_group("albinism", (a, 3), f"eyes3{f}_{i}")
                self.make_group("albinism", (a, 4), f"eyes4{f}_{i}")
                self.make_group("albinism", (a, 5), f"eyes5{f}_{i}")	
            for a, i in enumerate(
                    ["FLATMELANISTIC", "REDMELANISTIC", "PINKMELANISTIC", "VIOLETMELANISTIC", "BLUEMELANISTIC",
                        "GREENMELANISTIC", "YELLOWMELANISTIC"]):
                self.make_group("melanism", (a, 0), f"melanism{f}_{i}")    
            for a, i in enumerate(
                    ["RUBEN", "DUSK", "SUNSHADOW", "DARKCYAN", "DEEPBLUE", "FERN", "NIGHT",  "BLACKHOLE", 
                        "DARKPOPPY", "DARKBROWN"]):
                self.make_group("melanism", (a, 1), f"eyes{f}_" + i)
                self.make_group("melanism", (a, 2), f"eyes2{f}_{i}")
                self.make_group("melanism", (a, 3), f"eyes3{f}_{i}")
                self.make_group("melanism", (a, 4), f"eyes4{f}_{i}")
                self.make_group("melanism", (a, 5), f"eyes5{f}_{i}")	

            # Define colors and categories
            color_categories = [
                ["WHITE", "PALEGREY", "SILVER", "BRONZE", "GREY", "BLUEGREY", "XANADU", "DARKGREY", "COAL", "GHOST", "BLACK", "PITCH"],
                ["BEIGE", "PANTONE", "LIGHTBROWN", "LILAC", "BROWN", "GOLDEN-BROWN", "TAN", "CHESTNUT", "DARKBROWN", "CHOCOLATE", "COFFEE", "UMBER"],
                ["BANNANA", "PALECREAM", "CREAM", "PALEGINGER", "HONEY", "GOLDEN", "APRICOT", "GINGER", "ROSE", "DARKGINGER", "SIENNA", "BLOOD"],
                ["CHARTRUSE", "MINT", "LETTUCE", "LIGHTGREEN", "OLIVE", "EMERALD", "DARKMINT", "GREEN", "DARKGREEN", "DARKOLIVE", "FERN", "FOREST"],
                ["PALEBOW", "SKY", "POWDERBLUE", "SHINYMEW", "SAPPHIRE", "OCEAN", "COBALT", "DARKCOBALT", "INDIGO", "NIGHT", "DUSKBOW"],
                ["PETAL", "PALESTRAKIT", "FLORAL", "AMYTHYST", "ORCHID", "STRAKIT", "PURPLE", "WINE", "DARKSTRAKIT"],
                ["CORAL", "MEW", "PALERED", "APPLE", "BLUSH", "RED", "SCARLET", "DARKRED", "GARNET"],
                ["IVORY", "LEMON", "LAGUNA", "YELLOW", "BEE", "PYRITE", "PINEAPPLE", "YELLOW-GREEN", "DIJON"]
            ]

            color_types = [
                "singlecolours"
            ]

            for row, colors in enumerate(color_categories):
                for col, color in enumerate(colors):
                    for color_type in color_types:
                        self.make_group(color_type, (col, row), f"{color_type[:-7]}{f}_{color}")

            '''pride_categories = [
                ["DEMIENBY", "DEMIBOY", "TRANS", "ARO", "DEMIROM", "AGENDER", "PAN"],
                ["DEMIGIRL", "GENDERQUEER", "DEMISEX", "ASEXUAL", "GENDER", "BISEX", "GLASS"],
                ["POLY", "ENBY", "INTERSEX", "MLM", "WLW", "GAYBOW"]
            ]

            pride_types = [
                "singlepride"
            ] #, "backedpride", "smokepride", "ratpride", "dunnartpride", "lanternpride", "armoredpride"

            for row, colors in enumerate(pride_categories):
                for col, color in enumerate(colors):
                    for color_type in pride_types:
                        self.make_group(color_type, (col, row), f'{color_type[:-5]}{f}_{color}')'''

            # tortiepatchesmasks
            tortiepatchesmasks = [
                [
                    "ONE", "TWO", "THREE", "FOUR", "REDTAIL", "DELILAH", "HALF", "STREAK", "MASK", "SMOKE",
                ],
                [
                    "MINIMALONE", "MINIMALTWO", "MINIMALTHREE", "MINIMALFOUR", "OREO", "SWOOP", "CHIMERA",
                    "CHEST", "ARMTAIL", "GRUMPYFACE",
                ],
                [
                    "MOTTLED", "SIDEMASK", "EYEDOT", "BANDANA", "PACMAN", "STREAMSTRIKE", "SMUDGED", "DAUB",
                    "EMBER", "BRIE",
                ],
                [
                    "ORIOLE", "ROBIN", "BRINDLE", "PAIGE", "ROSETAIL", "SAFI", "DAPPLENIGHT", "BLANKET",
                    "BELOVED", "BODY",
                ],
                [
                    "SHILOH", "FRECKLED", "HEARTBEAT"
                ],
            ]

            for row, masks in enumerate(tortiepatchesmasks):
                for col, mask in enumerate(masks):
                    self.make_group("tortiepatchesmasks", (col, row), f"tortiemask{f}_{mask}")

            # Define skin colors
            skin_colors = [
                ["BLACK", "RED", "PINK", "DARKBROWN", "BROWN", "LIGHTBROWN", "ALBINO"],
                ["DARK", "DARKGREY", "GREY", "DARKSALMON", "SALMON", "PEACH", "MELANISTIC"],
                ["DARKMARBLED", "MARBLED", "LIGHTMARBLED", "DARKBLUE", "BLUE", "LIGHTBLUE", "WHITEMARBLE"],
            ]

            for row, colors in enumerate(skin_colors):
                for col, color in enumerate(colors):
                    self.make_group("skin", (col, row), f"skin{f}_{color}")
                    self.make_group("blep", (col, row), f"blep{f}_{color}")

            gill_colors = [
                ["BLACKGILL", "REDGILL", "PINKGILL", "DARKBROWNGILL", "BROWNGILL", "LIGHTBROWNGILL", "ALBINOGILL"],
                ["DARKGILL", "DARKGREYGILL", "GREYGILL", "DARKSALMONGILL", "SALMONGILL", "PEACHGILL", "MELANISTICGILL"],
                ["DARKMARBLEDGILL", "MARBLEDGILL", "LIGHTMARBLEDGILL", "DARKBLUEGILL", "BLUEGILL", "LIGHTBLUEGILL", "WHITEMARBLEGILL"]
            ]
            
            for row, colors in enumerate(gill_colors):
                for col, color in enumerate(colors):
                    self.make_group("skingills", (col, row), f"skin{f}_{color}")
                    self.make_group("blep", (col, row), f"blep{f}_{color}") 

            self.load_scars(f)
        self.load_symbols()

    def load_scars(self, f):
        """
        Loads scar sprites and puts them into groups.
        """

        # Define scars
        # Define scars
        scars_data = [
            ["ONE", "TWO", "THREE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
             "BOTHBLIND", "BURNPAWS", "BURNTAIL"],
            ["BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE", "FROSTFACE", "FROSTTAIL",
             "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"],
            ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY", "TOETRAP", "SNAKE", "LEGBITE",
             "NECKBITE", "FACE"],
            ["HINDLEG", "BACK", "QUILLSIDE", "SCRATCHSIDE", "TOE", "BEAKSIDE", "CATBITETWO", "SNAKETWO", "FOUR"]
        ]

        # define missing parts
        missing_parts_data = [
            ["LEFTEAR", "RIGHTEAR", "NOTAIL", "NOLEFTEAR", "NORIGHTEAR", "NOEAR", "HALFTAIL", "NOPAW"]
        ]

        hybrid_scars = [
            ["RASH", "DECLAWED", "RIGHTTAG", "LEFTTAG", "SNAKETHREE"]
        ]

        # scars
        for row, scars in enumerate(scars_data):
            for col, scar in enumerate(scars):
                self.make_group('scars', (col, row), f'scars{f}_{scar}')

        # missing parts
        for row, missing_parts in enumerate(missing_parts_data):
            for col, missing_part in enumerate(missing_parts):
                self.make_group('missingscars', (col, row), f'scars{f}_{missing_part}')

        # hybrid scars 
        for row, scars in enumerate(hybrid_scars):
            for col, scar in enumerate(scars):
                self.make_group('hybridscars', (col, row), f'scars{f}_{scar}')

        # accessories
        # to my beloved modders, im very sorry for reordering everything <333 -clay
        medcatherbs_data = [
            [
                "MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "CATTAIL",
                "POPPY", "ORANGE POPPY", "CYAN POPPY", "WHITE POPPY", "PINK POPPY",
            ],
            [
                "BLUEBELLS", "LILY OF THE VALLEY", "SNAPDRAGON", "HERBS", "PETALS", "NETTLE",
                "HEATHER", "GORSE", "JUNIPER", "RASPBERRY", "LAVENDER",
            ],
            [
                "OAK LEAVES", "CATMINT", "MAPLE SEED", "LAUREL", "BULB WHITE", "BULB YELLOW",
                "BULB ORANGE", "BULB PINK", "BULB BLUE", "CLOVER", "DAISY",
            ],
            [
                "WISTERIA", "ROSE MALLOW", "PICKLEWEED", "GOLDEN CREEPING JENNY", "DESERT WILLOW",
                "CACTUS FLOWER", "PRAIRIE FIRE", "VERBENA EAR", "VERBENA PELT",
            ],
        ]
        dryherbs_data = [["DRY HERBS", "DRY CATMINT", "DRY NETTLES", "DRY LAURELS"]]
        wild_data = [
            [
                "RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "GULL FEATHERS", "SPARROW FEATHERS", 
                "MOTH WINGS", "ROSY MOTH WINGS", "MORPHO BUTTERFLY", "MONARCH BUTTERFLY", "CICADA WINGS",
                "BLACK CICADA",
            ],
            [
                "ROAD RUNNER FEATHER",
            ],
        ]

        collars_data = [
            ["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"],
            ["GREEN", "RAINBOW", "BLACK", "SPIKES", "WHITE"],
            ["PINK", "PURPLE", "MULTI", "INDIGO"],
        ]

        bellcollars_data = [
            ["CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL"],
            ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL"],
            ["PINKBELL", "PURPLEBELL", "MULTIBELL", "INDIGOBELL"],
        ]

        bowcollars_data = [
            ["CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW", "LIMEBOW"],
            ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW"],
            ["PINKBOW", "PURPLEBOW", "MULTIBOW", "INDIGOBOW"],
        ]

        nyloncollars_data = [
            ["CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", "REDNYLON", "LIMENYLON"],
            ["GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON"],
            ["PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON"],
        ]

        # medcatherbs
        for row, herbs in enumerate(medcatherbs_data):
            for col, herb in enumerate(herbs):
                self.make_group("medcatherbs", (col, row), f"acc_herbs{f}_{herb}")
        # dryherbs
        for row, dry in enumerate(dryherbs_data):
            for col, dryherbs in enumerate(dry):
                self.make_group("medcatherbs", (col, 4), f"acc_herbs{f}_{dryherbs}")
        # wild
        for row, wilds in enumerate(wild_data):
            for col, wild in enumerate(wilds):
                self.make_group("wild", (col, row), f"acc_wild{f}_{wild}")

        # collars
        for row, collars in enumerate(collars_data):
            for col, collar in enumerate(collars):
                self.make_group('collars', (col, row), f'collars{f}_{collar}')

        # bellcollars
        for row, bellcollars in enumerate(bellcollars_data):
            for col, bellcollar in enumerate(bellcollars):
                self.make_group('bellcollars', (col, row), f'collars{f}_{bellcollar}')

        # bowcollars
        for row, bowcollars in enumerate(bowcollars_data):
            for col, bowcollar in enumerate(bowcollars):
                self.make_group('bowcollars', (col, row), f'collars{f}_{bowcollar}')

        # nyloncollars
        for row, nyloncollars in enumerate(nyloncollars_data):
            for col, nyloncollar in enumerate(nyloncollars):
                self.make_group('nyloncollars', (col, row), f'collars{f}_{nyloncollar}')

    def load_symbols(self):
        """
        loads clan symbols
        """

        if os.path.exists("resources/dicts/clan_symbols.json"):
            with open(
                "resources/dicts/clan_symbols.json", encoding="utf-8"
            ) as read_file:
                self.symbol_dict = ujson.loads(read_file.read())

        # U and X omitted from letter list due to having no prefixes
        letters = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "V",
            "W",
            "Y",
            "Z",
        ]

        # sprite names will format as "symbol{PREFIX}{INDEX}", ex. "symbolSPRING0"
        y_pos = 1
        for letter in letters:
            x_mod = 0
            for i, symbol in enumerate(
                [
                    symbol
                    for symbol in self.symbol_dict
                    if letter in symbol and self.symbol_dict[symbol]["variants"]
                ]
            ):
                if self.symbol_dict[symbol]["variants"] > 1 and x_mod > 0:
                    x_mod += -1
                for variant_index in range(self.symbol_dict[symbol]["variants"]):
                    x_pos = i + x_mod

                    if self.symbol_dict[symbol]["variants"] > 1:
                        x_mod += 1
                    elif x_mod > 0:
                        x_pos += -1

                    self.clan_symbols.append(f"symbol{symbol.upper()}{variant_index}")
                    self.make_group(
                        "symbols",
                        (x_pos, y_pos),
                        f"symbol{symbol.upper()}{variant_index}",
                        sprites_x=1,
                        sprites_y=1,
                        no_index=True,
                    )

            y_pos += 1

    def get_symbol(self, symbol: str, force_light=False):
        """Change the color of the symbol to match the requested theme, then return it
        :param Surface symbol: The clan symbol to convert
        :param force_light: Use to ignore dark mode and always display the light mode color
        """
        symbol = self.sprites.get(symbol)
        if symbol is None:
            logger.warning("%s is not a known Clan symbol! Using default.")
            symbol = self.sprites[self.clan_symbols[0]]

        recolored_symbol = copy(symbol)
        var = pygame.PixelArray(recolored_symbol)
        var.replace(
            (87, 76, 45),
            (
                pygame.Color(constants.CONFIG["theme"]["dark_mode_clan_symbols"])
                if not force_light and game_setting_get("dark mode")
                else pygame.Color(constants.CONFIG["theme"]["light_mode_clan_symbols"])
            ),
            distance=0,
        )
        del var

        return recolored_symbol

    @staticmethod
    def get_platform(biome, season, show_nest, group: CatGroup) -> pygame.Surface:
        """
        Returns the relevant platform
        :param biome: The current game biome
        :param season: The current game season
        :param show_nest: If true, displays the nest
        :param group: Used to determine appropriate afterlife platform
        :return: pygame.Surface containing the desired platform
        """
        offset = 0 if game_setting_get("dark mode") else 80
        """Used to choose the dark mode version of platforms"""

        available_biome = ["Forest", "Mountainous", "Plains", "Beach"]

        if biome not in available_biome:
            biome = available_biome[0]
        if show_nest:
            biome = "nest"

        biome = biome.lower()

        platformsheet = image_cache.load_image(
            "resources/images/platforms.png"
        ).convert_alpha()

        order = ["beach", "forest", "mountainous", "nest", "plains", "dead"]

        if group and group.is_afterlife():
            biome_platforms = platformsheet.subsurface(
                pygame.Rect(0, order.index("dead") * 70, 640, 70)
            )

            if group == CatGroup.DARK_FOREST:
                return biome_platforms.subsurface(pygame.Rect(0 + offset, 0, 80, 70))
            elif group == CatGroup.STARCLAN:
                return biome_platforms.subsurface(pygame.Rect(160 + offset, 0, 80, 70))
            elif group == CatGroup.UNKNOWN_RESIDENCE:
                return biome_platforms.subsurface(pygame.Rect(320 + offset, 0, 80, 70))

        biome_platforms = platformsheet.subsurface(
            pygame.Rect(0, order.index(biome) * 70, 640, 70)
        ).convert_alpha()
        season_x = {
            "greenleaf": 0 + offset,
            "leaf-bare": 160 + offset,
            "leaf-fall": 320 + offset,
            "newleaf": 480 + offset,
        }

        return biome_platforms.subsurface(
            pygame.Rect(
                season_x[season.lower()],
                0,
                80,
                70,
            )
        )


# CREATE INSTANCE
sprites = Sprites()
