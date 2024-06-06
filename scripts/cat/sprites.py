import os

import pygame

import ujson

from scripts.game_structure.game_essentials import game


class Sprites():
    cat_tints = {}
    white_patches_tints = {}
    clan_symbols = []

    def __init__(self):
        """Class that handles and hold all spritesheets. 
        Size is normally automatically determined by the size
        of the lineart. If a size is passed, it will override 
        this value. """
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
            with open("sprites/dicts/tint.json", 'r') as read_file:
                self.cat_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading Tints")

        try:
            with open("sprites/dicts/white_patches_tint.json", 'r') as read_file:
                self.white_patches_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading White Patches Tints")

        try:
            with open("sprites/dicts/vitiligo_tint.json", 'r') as read_file:
                self.vitiligo_tint = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading Vitiligo Tints")
            
    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def make_group(self,
                   spritesheet,
                   pos,
                   name,
                   sprites_x=9,
                   sprites_y=18,
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
                        self.size, self.size
                    )

                except ValueError:
                    # Fallback for non-existent sprites
                    print(f"WARNING: nonexistent sprite - {full_name}")
                    if not self.blank_sprite:
                        self.blank_sprite = pygame.Surface(
                            (self.size, self.size),
                            pygame.HWSURFACE | pygame.SRCALPHA
                        )
                    new_sprite = self.blank_sprite

                self.sprites[full_name] = new_sprite
                i += 1

    def load_all(self):
        # get the width and height of the spritesheet
        lineart = pygame.image.load('sprites/lineart.png')
        width, height = lineart.get_size()
        del lineart  # unneeded

        # if anyone changes lineart for whatever reason update this
        if isinstance(self.size, int):
            pass
        elif width / 9 == height / 18:
            self.size = width / 9
        else:
            self.size = 50  # default, what base clangen uses
            print(f"lineart.png is not 3x7, falling back to {self.size}")
            print(
                f"if you are a modder, please update scripts/cat/sprites.py and do a search for 'if width / 3 == height / 7:'")

        del width, height  # unneeded

        for x in [
            'lineart', 'lineartdf', 'lineartdead',
            'eyes', 'eyes2', 'eyes3', 'eyes4', 'eyes5', 
            'hybrideyes', 'hybrideyes2', 'hybrideyes3', 'hybrideyes4', 'hybrideyes5',             
            'skin', 'skingills', 'blep', 
            'scars', 'missingscars',
            'medcatherbs',
            'collars', 'bellcollars', 'bowcollars', 'nyloncollars',
            
            'singlecolours', 'speckledcolours', 'tabbycolours', 'bengalcolours', 'marbledcolours',
            'rosettecolours', 'smokecolours', 'tickedcolours', 'mackerelcolours', 'classiccolours', 
            'sokokecolours', 'agouticolours', 'singlestripecolours', 'maskedcolours', 
            
            'singlenaturals', 'singlepride', 'singleunnaturals', 'backednaturals', 'backedpride', 'backedunnaturals',
            'shadersnewwhite', 'lightingnew',
            'fademask', 'fadestarclan', 'fadedarkforest',
            'symbols'
        ]:
            if 'lineart' in x and game.config['fun']['april_fools']:
                self.spritesheet(f"sprites/aprilfools{x}.png", x)
            else:
                self.spritesheet(f"sprites/{x}.png", x)

        for x in [
            'whitepatches', 'tortiepatchesmasks', 'vitiligo', 
            'colourpointpatches', 'albinism', 'melanism'
        ]:
            sprites.spritesheet(f"sprites/patches/{x}.png", x) 

        # Line art
        self.make_group('lineart', (0, 0), 'lines')
        self.make_group('shadersnewwhite', (0, 0), 'shaders')
        self.make_group('lightingnew', (0, 0), 'lighting')

        self.make_group('lineartdead', (0, 0), 'lineartdead')
        self.make_group('lineartdf', (0, 0), 'lineartdf')

        # Fading Fog
        for i in range(0, 3):
            self.make_group('fademask', (i, 0), f'fademask{i}')
            self.make_group('fadestarclan', (i, 0), f'fadestarclan{i}')
            self.make_group('fadedarkforest', (i, 0), f'fadedf{i}')

        # Define eye colors
        eye_colors = [
            ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 
            'HEATHERBLUE', 'SUNLITICE'],
            ['COPPER', 'SAGE', 'COBALT', 'PALEBLUE', 'BRONZE', 'SILVER', 'PALEYELLOW', 'GOLD', 'GREENYELLOW', 
            'SUNSET', 'GHOST', 'VOID']
        ]

        for row, colors in enumerate(eye_colors):
            for col, color in enumerate(colors):
                self.make_group('eyes', (col, row), f'eyes{color}')
                self.make_group('eyes2', (col, row), f'eyes2{color}')
                self.make_group('eyes3', (col, row), f'eyes3{color}')
                self.make_group('eyes4', (col, row), f'eyes4{color}')
                self.make_group('eyes5', (col, row), f'eyes5{color}')

        hybrid_eyes = [
            ['POPPY', 'CRIMSON', 'RUBY', 'PINKPOPPY', 'BROWN', 'BROWNTWO', 'PEANUT', 'CHOCMINT', 'MINTCHOC',
            'MINT', 'JADE', 'GRASS'],
            ['STRAWBERRY', 'VIOLET', 'LILAC', 'GRAPE', 'INDIGO', 'COBOLT', 'AZURE', 'OCEAN', 'DEPTHS', 'SKY',
            'BEACH', 'SUNGRASS'],
            ['WHITE', 'MONOCHROME', 'MONOCHROMETWO', 'MONOCHROMETHREE', 'LILACGREY', 'GREYTWO', 'GREYCOAL', 
            'FAUXVOID', 'ASPEN', 'GREENGREY', 'ECTOPLASM', 'YELLOWOLIVE'],
            ['AMBERTWO', 'SUNSHINE', 'PYRITE', 'PRIMARY', 'PRIMARYB', 'PRIMARYC', 'CHROME', 'CHROMEB', 
            'CHROMEC', 'RGB', 'RGBTWO', 'RGBTHREE']
    ]

        for row, colors in enumerate(hybrid_eyes):
            for col, color in enumerate(colors):
                self.make_group('hybrideyes', (col, row), f'eyes{color}')
                self.make_group('hybrideyes2', (col, row), f'eyes2{color}')
                self.make_group('hybrideyes3', (col, row), f'eyes3{color}')
                self.make_group('hybrideyes4', (col, row), f'eyes4{color}')
                self.make_group('hybrideyes5', (col, row), f'eyes5{color}')

        # Define white patches
        white_patches = [
            ['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANYTWO', 'MOON', 'PHANTOM', 'POWDER',
             'BLEACHED', 'SAVANNAH', 'FADESPOTS', 'PEBBLESHINE'],
            ['EXTRA', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'BLACKSTAR',
             'PIEBALD', 'CURVED', 'PETAL', 'SHIBAINU', 'OWL'],
            ['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO', 'GOATEE', 'VITILIGOTWO', 'PAWS', 'MITAINE',
             'BROKENBLAZE', 'SCOURGE', 'DIVA', 'BEARD'],
            ['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'HONEY', 'FAROFA', 'DAMIEN', 'MISTER', 'BELLY',
             'TAILTIP', 'TOES', 'TOPCOVER'],
            ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW', 'PANTS', 'REVERSEPANTS',
             'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'DAPPLEPAW'],
            ['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT', 'MAO', 'LUNA', 'CHESTSPECK',
             'WINGS', 'PAINTED', 'HEARTTWO', 'WOODPECKER'],
            ['BOOTS', 'MISS', 'COW', 'COWTWO', 'BUB', 'BOWTIE', 'MUSTACHE', 'REVERSEHEART', 'SPARROW', 'VEST',
             'LOVEBUG', 'TRIXIE', 'SAMMY', 'SPARKLE'],
            ['RIGHTEAR', 'LEFTEAR', 'ESTRELLA', 'SHOOTINGSTAR', 'EYESPOT', 'REVERSEEYE', 'FADEBELLY', 'FRONT',
             'BLOSSOMSTEP', 'PEBBLE', 'TAILTWO', 'BUDDY', 'BACKSPOT', 'EYEBAGS'],
            ['BULLSEYE', 'FINN', 'DIGIT', 'KROPKA', 'FCTWO', 'FCONE', 'MIA', 'SCAR', 'BUSTER', 'SMOKEY', 'HAWKBLAZE',
             'CAKE', 'ROSINA', 'PRINCESS'],
            ['LOCKET', 'BLAZEMASK', 'TEARS', 'DOUGIE']
        ]

        for row, patches in enumerate(white_patches):
            for col, patch in enumerate(patches):
                self.make_group('whitepatches', (col, row), f'white{patch}')

        vitiligo = [
            ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'POWDER', 'BLEACHED', 'SMOKEY'], 
            ['SHADOWSIGHT']
        ]
        
        for row, vitiligo in enumerate(vitiligo):
            for col, vit in enumerate(vitiligo):
                self.make_group('vitiligo', (col, row), f'white{vit}')

        colourpoint = [
            ['COLOURPOINT', 'RAGDOLL', 'KARPATI', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT'], 
            ['REVERSEPOINT', 'PONIT', 'LIGHTPOINT', 'SNOWSHOE', 'SNOWBOOT', 'WHITEPOINT']
        ]
        
        for row, colourpoint in enumerate(colourpoint):
            for col, colorpoint in enumerate(colourpoint):
                self.make_group('colourpointpatches', (col, row), f'white{colorpoint}')

        ##Albinism + Melanism Sheets
        for a, i in enumerate(
                ['FLATALBINO', 'REDALBINO', 'PINKALBINO', 'VIOLETALBINO', 'BLUEALBINO', 'GREENALBINO',
                    'YELLOWALBINO']):
            self.make_group('albinism', (a, 0), f'albinism{i}')     
        for a, i in enumerate(
                ['PINK', 'VIOLETPINK', 'YELLOWPINK', 'CYANPINK', 'BLUEPINK', 'MINTPINK', 'NACRE', 
                    'GHOSTPINK', 'LIGHTPOPPY', 'LIGHTBROWN']):
            self.make_group('albinism', (a, 1), f'eyes' + i)
            self.make_group('albinism', (a, 2), f'eyes2{i}')
            self.make_group('albinism', (a, 3), f'eyes3{i}')
            self.make_group('albinism', (a, 4), f'eyes4{i}')
            self.make_group('albinism', (a, 5), f'eyes5{i}')	
        for a, i in enumerate(
                ['FLATMELANISTIC', 'REDMELANISTIC', 'PINKMELANISTIC', 'VIOLETMELANISTIC', 'BLUEMELANISTIC',
                    'GREENMELANISTIC', 'YELLOWMELANISTIC']):
            self.make_group('melanism', (a, 0), f'melanism{i}')    
        for a, i in enumerate(
                ['RUBEN', 'DUSK', 'SUNSHADOW', 'DARKCYAN', 'DEEPBLUE', 'FERN', 'NIGHT',  'BLACKHOLE', 
                    'DARKPOPPY', 'DARKBROWN']):
            self.make_group('melanism', (a, 1), f'eyes' + i)
            self.make_group('melanism', (a, 2), f'eyes2{i}')
            self.make_group('melanism', (a, 3), f'eyes3{i}')
            self.make_group('melanism', (a, 4), f'eyes4{i}')
            self.make_group('melanism', (a, 5), f'eyes5{i}')	

        # Define colors and categories
        color_categories = [
            ['WHITE', 'PALEGREY', 'SILVER', 'BANNANA', 'PALECREAM', 'SAND', 'CREAM', 'LIGHTBROWN', 'FARROW', 'BEIGE', 'HAY', 'MEERKAT'],
            ['PANTONE', 'PALEGINGER', 'WOOD', 'GOLDEN', 'APRICOT', 'GINGER', 'LILAC', 'KHAKI', 'HAZELNUT', 'CADET', 'BRONZE', 'MARENGO'],
            ['SAMON', 'THISTLE', 'GOLD', 'FIRE', 'GARFIELD', 'DARKGINGER', 'GOLDEN-BROWN', 'CAPPUCCINO', 'ECRU', 'GREY', 'BLUEGREY', 'BATTLESHIP'],
            ['HONEY', 'MEDALLION', 'BRICK', 'ROSE', 'SIENNA', 'DUSTBROWN', 'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'PINECONE', 'STEEL', 'SLATE'],
            ['GRANOLA', 'SADDLE', 'SUNSET', 'APPLE', 'RED', 'RUFOUS', 'TAN', 'CHESTNUT', 'MINK', 'BROWN', 'XANADU', 'SOOT'],
            ['CEDAR', 'DARKSAMON', 'CRIMSON', 'CARMINE', 'SCARLET', 'COSMOS', 'BEAVER', 'DARKBROWN', 'CHOCOLATE', 'DARKGREY', 'CHARCOAL', 'ANCHOR'],
            ['ROSEWOOD', 'BURNT', 'BLOOD', 'COFFEE', 'MOCHA', 'TAUPE', 'UMBER', 'COAL', 'GHOST', 'BLACK', 'PITCH']
        ]

        color_types = [
            'singlenaturals', 'backednaturals'
        ]

        for row, colors in enumerate(color_categories):
            for col, color in enumerate(colors):
                for color_type in color_types:
                    self.make_group(color_type, (col, row), f'{color_type[:-8]}{color}')

        pride_categories = [
            ['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 'PAN'],
            ['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 'BISEX', 'GLASS'],
            ['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']
        ]

        pride_types = [
            'singlepride', 'backedpride'
        ]

        for row, colors in enumerate(pride_categories):
            for col, color in enumerate(colors):
                for color_type in pride_types:
                    self.make_group(color_type, (col, row), f'{color_type[:-5]}{color}')

        f_color_categories = [
            ['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'MINTY', 'EMERALD', 'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA'],
            ['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST'],
            ['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 'WAVES', 'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY'],
            ['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'BUBBLEGUM', 'TART'],
            ['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'FLUORITE', 'DARKTEAL', 'SONIC', 'NAVY', 'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE'],
            ['TROMBONE', 'BRASS', 'YELLOW-GREEN', 'FOREST', 'SEAFOAM', 'FERN', 'JEANS', 'JACKET', 'DEEPOCEAN', 'DARKSTRAKIT', 'BARN', 'GARNET'],
            ['DIJON', 'RUST', 'COPPER', 'DEEPOLIVE', 'DEEPFOREST', 'MALACHITE', 'OCEANIC', 'NIGHTTIME', 'ONYX', 'RASIN', 'DUSKBOW']
        ]

        f_color_types = [
            'singleunnaturals', 'backedunnaturals'
        ]

        for row, colors in enumerate(f_color_categories):
            for col, color in enumerate(colors):
                for color_type in f_color_types:
                    self.make_group(color_type, (col, row), f'{color_type[:-10]}{color}')
            
        # tortiepatchesmasks
        tortiepatchesmasks = [
            ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'HALF', 'STREAK', 'MASK', 'SMOKE'],
            ['MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'OREO', 'SWOOP', 'CHIMERA', 'CHEST', 'ARMTAIL',
             'GRUMPYFACE'],
            ['MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'SMUDGED', 'DAUB', 'EMBER', 'BRIE'],
            ['ORIOLE', 'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'DAPPLENIGHT', 'BLANKET', 'BELOVED', 'BODY'],
            ['SHILOH', 'FRECKLED', 'HEARTBEAT']
        ]

        for row, masks in enumerate(tortiepatchesmasks):
            for col, mask in enumerate(masks):
                self.make_group('tortiepatchesmasks', (col, row), f"tortiemask{mask}")

        # Define skin colors 
        skin_colors = [
            ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'ALBINO'],
            ['DARK', 'DARKGREY', 'GREY', 'DARKSALMON', 'SALMON', 'PEACH', 'MELANISTIC'],
            ['DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE', 'WHITEMARBLE']
        ]

        for row, colors in enumerate(skin_colors):
            for col, color in enumerate(colors):
                self.make_group('skin', (col, row), f"skin{color}")
                self.make_group('blep', (col, row), f"blep{color}")

        gill_colors = [
            ['BLACKGILL', 'REDGILL', 'PINKGILL', 'DARKBROWNGILL', 'BROWNGILL', 'LIGHTBROWNGILL', 'ALBINOGILL'],
            ['DARKGILL', 'DARKGREYGILL', 'GREYGILL', 'DARKSALMONGILL', 'SALMONGILL', 'PEACHGILL', 'MELANISTICGILL'],
            ['DARKMARBLEDGILL', 'MARBLEDGILL', 'LIGHTMARBLEDGILL', 'DARKBLUEGILL', 'BLUEGILL', 'LIGHTBLUEGILL', 'WHITEMARBLEGILL']
        ]
        
        for row, colors in enumerate(gill_colors):
            for col, color in enumerate(colors):
                self.make_group('skingills', (col, row), f"skin{color}")
                self.make_group('blep', (col, row), f"blep{color}")            

        self.load_scars()
        self.load_symbols()

    def load_scars(self):
        """
        Loads scar sprites and puts them into groups.
        """

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

        # scars 
        for row, scars in enumerate(scars_data):
            for col, scar in enumerate(scars):
                self.make_group('scars', (col, row), f'scars{scar}')

        # missing parts
        for row, missing_parts in enumerate(missing_parts_data):
            for col, missing_part in enumerate(missing_parts):
                self.make_group('missingscars', (col, row), f'scars{missing_part}')

        # accessories
        medcatherbs_data = [
            ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL"],
            ["BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS"],
            [],  # Empty row because this is the wild data, except dry herbs.
            ["OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"]
        ]

        wild_data = [
            ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"]
        ]

        collars_data = [
            ["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"],
            ["GREEN", "RAINBOW", "BLACK", "SPIKES", "WHITE"],
            ["PINK", "PURPLE", "MULTI", "INDIGO"]
        ]

        bellcollars_data = [
            ["CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL"],
            ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL"],
            ["PINKBELL", "PURPLEBELL", "MULTIBELL", "INDIGOBELL"]
        ]

        bowcollars_data = [
            ["CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW", "LIMEBOW"],
            ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW"],
            ["PINKBOW", "PURPLEBOW", "MULTIBOW", "INDIGOBOW"]
        ]

        nyloncollars_data = [
            ["CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", "REDNYLON", "LIMENYLON"],
            ["GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON"],
            ["PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON"]
        ]

        # medcatherbs
        for row, herbs in enumerate(medcatherbs_data):
            for col, herb in enumerate(herbs):
                self.make_group('medcatherbs', (col, row), f'acc_herbs{herb}')
        self.make_group('medcatherbs', (5, 2), 'acc_herbsDRY HERBS')

        # wild
        for row, wilds in enumerate(wild_data):
            for col, wild in enumerate(wilds):
                self.make_group('medcatherbs', (col, 2), f'acc_wild{wild}')

        # collars
        for row, collars in enumerate(collars_data):
            for col, collar in enumerate(collars):
                self.make_group('collars', (col, row), f'collars{collar}')

        # bellcollars
        for row, bellcollars in enumerate(bellcollars_data):
            for col, bellcollar in enumerate(bellcollars):
                self.make_group('bellcollars', (col, row), f'collars{bellcollar}')

        # bowcollars
        for row, bowcollars in enumerate(bowcollars_data):
            for col, bowcollar in enumerate(bowcollars):
                self.make_group('bowcollars', (col, row), f'collars{bowcollar}')

        # nyloncollars
        for row, nyloncollars in enumerate(nyloncollars_data):
            for col, nyloncollar in enumerate(nyloncollars):
                self.make_group('nyloncollars', (col, row), f'collars{nyloncollar}')

    def load_symbols(self):
        """
        loads clan symbols
        """

        if os.path.exists('resources/dicts/clan_symbols.json'):
            with open('resources/dicts/clan_symbols.json') as read_file:
                self.symbol_dict = ujson.loads(read_file.read())

        # U and X omitted from letter list due to having no prefixes
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "V", "W", "Y", "Z"]

        # sprite names will format as "symbol{PREFIX}{INDEX}", ex. "symbolSPRING0"
        y_pos = 1
        for letter in letters:
            for i, symbol in enumerate([symbol for symbol in self.symbol_dict if
                                        letter in symbol and self.symbol_dict[symbol]["variants"]]):
                x_mod = 0
                for variant_index in range(self.symbol_dict[symbol]["variants"]):
                    x_mod += variant_index
                    self.clan_symbols.append(f"symbol{symbol.upper()}{variant_index}")
                    self.make_group('symbols',
                                    (i + x_mod, y_pos),
                                    f"symbol{symbol.upper()}{variant_index}",
                                    sprites_x=1, sprites_y=1, no_index=True)

            y_pos += 1


# CREATE INSTANCE
sprites = Sprites()
