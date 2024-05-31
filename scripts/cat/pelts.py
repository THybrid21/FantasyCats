from random import choice
from scripts.cat.sprites import sprites
import random
from re import sub
from scripts.game_structure.game_essentials import game


    

class Pelt():
    
    sprites_names = {
        "SingleColour": 'single',
        'TwoColour': 'single',
        'Tabby': 'tabby',
        'Marbled': 'marbled',
        'Rosette': 'rosette',
        'Smoke': 'smoke',
        'Ticked': 'ticked',
        'Speckled': 'speckled',
        'Bengal': 'bengal',
        'Mackerel': 'mackerel',
        'Classic': 'classic',
        'Sokoke': 'sokoke',
        'Agouti': 'agouti',
        'Backed': 'backed',
        'Masked': 'masked',
        'Tortie': None,
        'Calico': None,
    }
    
    # ATTRIBUTES, including non-pelt related
    pelt_colours = [
        'WHITE', 'PALEGREY', 'SILVER', 'BANNANA', 'PALECREAM', 'SAND', 'CREAM', 'LIGHTBROWN', 
        'FARROW', 'BEIGE', 'HAY', 'MEERKAT', 'PANTONE', 'PALEGINGER', 'WOOD', 'GOLDEN', 'APRICOT', 
        'GINGER', 'LILAC', 'KHAKI', 'HAZELNUT', 'CADET', 'BRONZE', 'MARENGO', 'SAMON', 'THISTLE', 'GOLD', 
        'FIRE', 'GARFIELD', 'DARKGINGER', 'GOLDEN-BROWN', 'CAPPUCCINO', 'ECRU', 'GREY', 'BLUEGREY', 
        'BATTLESHIP', 'HONEY', 'MEDALLION', 'BRICK', 'ROSE', 'SIENNA', 'DUSTBROWN', 'ASHBROWN', 
        'SANDALWOOD', 'WRENGE', 'PINECONE', 'STEEL', 'SLATE', 'GRANOLA', 'SADDLE', 'SUNSET', 'APPLE', 
        'RED', 'RUFOUS', 'TAN', 'CHESTNUT', 'MINK', 'BROWN', 'XANADU', 'SOOT', 'CEDAR', 'DARKSAMON', 
        'CRIMSON', 'CARMINE', 'SCARLET', 'COSMOS', 'BEAVER', 'DARKBROWN', 'CHOCOLATE', 'DARKGREY', 'CHARCOAL', 
        'ANCHOR', 'ROSEWOOD', 'BURNT', 'BLOOD', 'COFFEE', 'MOCHA', 'TAUPE', 'UMBER', 'COAL', 'GHOST', 
        'BLACK', 'PITCH', 'DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 'PAN', 'DEMIGIRL', 
        'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 'BISEX', 'GLASS', 'POLY', 'ENBY', 'INTERSEX', 'MLM', 
        'WLW', 'GAYBOW', 'PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'MINTY', 'EMERALD', 'TURQUOISE', 
        'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA', 'PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 
        'SHINYMEW', 'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST', 'LEMON', 'LAGUNA', 'FAWN', 'CORN', 
        'DARKOLIVE', 'SPINNACH', 'WAVES', 'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY', 'SUNSHINE', 'BEE', 
        'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'BUBBLEGUM', 'TART',
        'YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'FLUORITE', 'DARKTEAL', 'SONIC', 'NAVY', 'PURPLE', 'WINE', 
        'BRIGHTCRIMSON', 'ROYALPURPLE', 'TROMBONE', 'BRASS', 'YELLOW-GREEN', 'FOREST', 'SEAFOAM', 'FERN', 
        'JEANS', 'JACKET', 'DEEPOCEAN', 'DARKSTRAKIT', 'BARN', 'GARNET', 'DIJON', 'RUST', 'COPPER', 'DEEPOLIVE', 
        'DEEPFOREST', 'MALACHITE', 'OCEANIC', 'NIGHTTIME', 'ONYX', 'RASIN', 'DUSKBOW'
    ]
    pelt_c_no_white = [
        'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]
    pelt_c_no_bw = [
        'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]

    tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'HALF',
                    'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE', 'CHIMERA', 'DAUB', 'EMBER', 'BLANKET',
                    'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'SMUDGED', 'DAPPLENIGHT', 'STREAK', 'MASK', 'CHEST', 'ARMTAIL', 'SMOKE', 'GRUMPYFACE',
                    'BRIE', 'BELOVED', 'BODY', 'SHILOH', 'FRECKLED', 'HEARTBEAT']
    tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel', 'classic', 
                    'sokoke', 'agouti', 'Backed', 'masked']

    pelt_length = ["short", "medium", "long", "snat", "wolf", "skele", "bare", "catfish", "scug", "saint"]
    eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 
    'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 'GREENYELLOW', 
    'BRONZE', 'SILVER', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 
    'GREENYELLOW', 'POPPY', 'CRIMSON', 'RUBY', 'BROWN', 'JADE', 'SKY', 'LILAC', 'BROWNTWO', 'PEANUT', 'GREYTWO', 
    'YELLOWOLIVE', 'SUNSHINE', 'AZURE', 'COBOLT', 'GRASS', 'MINT', 'LILACGREY', 'WHITE', 'VIOLET', 'GRAPE', 'INDIGO', 
    'PRIMARY', 'PRIMARYB', 'PRIMARYC', 'CHROME', 'CHROMEB', 'CHROMEC', 'RGB', 'RGBTWO', 'RGBTHREE', 'MONOCHROME', 
    'MONOCHROMETWO', 'MONOCHROMETHREE', 'PINKPOPPY', 'STRAWBERRY', 'MINTCHOC', 'CHOCMINT', 'AMBERTWO', 'BEACH', 'OCEAN', 
    'SUNSET', 'GREENGREY', 'ASPEN', 'GREYCOAL', 'FAUXVOID', 'ECTOPLASM', 'DEPTHS', 'PYRITE']
    yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'BRONZE', 'GOLD', 'COPPER', 'GREENYELLOW', 'BROWN', 'BROWNTWO', 
                    'PEANUT', 'YELLOWOLIVE', 'SUNSHINE', 'AMBERTWO', 'BEACH', 'ASPEN', 'PYRITE']
    blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'COBALT', 'SUNLITICE', 'AZURE', 
                    'COBOLT', 'OCEAN', 'SKY', 'DEPTHS']
    green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL', 'JADE', 'GRASS', 'MINT',
        'MINTCHOC', 'CHOCMINT', 'GREENGREY', 'ECTOPLASM']
    mono_eyes = ['GREY', 'SILVER', 'VOID', 'GHOST', 'GREYTWO', 'LILACGREY', 'WHITE', 'MONOCHROME', 
        'MONOCHROMETWO', 'MONOCHROMETHREE', 'GREYCOAL', 'FAUXVOID']
    purple_eyes = ['POPPY', 'CRIMSON', 'RUBY', 'LILAC', 'VIOLET', 'GRAPE', 'INDIGO', 
        'PINKPOPPY', 'STRAWBERRY', 'SUNSET']
    chromatic_eyes = ['PRIMARY', 'PRIMARYB', 'PRIMARYC', 'CHROME', 'CHROMEB', 'CHROMEC', 'RGB', 
        'RGBTWO', 'RGBTHREE']

    # scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
    # bite scars by @wood pank on discord
    scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
            "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH", "HINDLEG",
            "BACK", "QUILLSIDE", "SCRATCHSIDE", "BEAKSIDE", "CATBITETWO", "FOUR"]
    scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
    scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
            "FROSTSOCK", "TOE", "SNAKETWO"]

    # make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
    plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                        "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                        "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
                        ]
    wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
                        ]
    tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS"]
    collars = [
        "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
        "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "CRIMSONBELL", "BLUEBELL",
        "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
        "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL", "PINKBELL", "PURPLEBELL",
        "MULTIBELL", "INDIGOBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
        "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW", "PINKBOW",
        "PURPLEBOW", "MULTIBOW", "INDIGOBOW", "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON",
        "REDNYLON", "LIMENYLON", "GREENNYLON", "RAINBOWNYLON",
        "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", "PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON",
    ]

    tabbies = ["SingleColour", "TwoColour", "Backed"]##"Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti"
    spotted = ["SingleColour", "TwoColour", "Backed"]##"Speckled", "Rosette"
    plain = ["SingleColour", "TwoColour", "Backed"]##"Smoke", 
    exotic = ["SingleColour", "TwoColour", "Backed"]##"Bengal", "Marbled", "Masked"
    torties = ["Tortie", "Calico"]
    pelt_categories = [tabbies, spotted, plain, exotic, torties]

    # SPRITE NAMES
    pride_colours = ['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
        'PAN', 'DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 'BISEX', 
        'POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']
    single_colours = [
        'WHITE', 'PALEGREY', 'SILVER', 'BANNANA', 'PALECREAM', 'SAND', 'CREAM', 'LIGHTBROWN', 
        'FARROW', 'BEIGE', 'HAY', 'MEERKAT', 'PANTONE', 'PALEGINGER', 'WOOD', 'GOLDEN', 'APRICOT', 
        'GINGER', 'LILAC', 'KHAKI', 'HAZELNUT', 'CADET', 'BRONZE', 'MARENGO', 'SAMON', 'THISTLE', 'GOLD', 
        'FIRE', 'GARFIELD', 'DARKGINGER', 'GOLDEN-BROWN', 'CAPPUCCINO', 'ECRU', 'GREY', 'BLUEGREY', 
        'BATTLESHIP', 'HONEY', 'MEDALLION', 'BRICK', 'ROSE', 'SIENNA', 'DUSTBROWN', 'ASHBROWN', 
        'SANDALWOOD', 'WRENGE', 'PINECONE', 'STEEL', 'SLATE', 'GRANOLA', 'SADDLE', 'SUNSET', 'APPLE', 
        'RED', 'RUFOUS', 'TAN', 'CHESTNUT', 'MINK', 'BROWN', 'XANADU', 'SOOT', 'CEDAR', 'DARKSAMON', 
        'CRIMSON', 'CARMINE', 'SCARLET', 'COSMOS', 'BEAVER', 'DARKBROWN', 'CHOCOLATE', 'DARKGREY', 'CHARCOAL', 
        'ANCHOR', 'ROSEWOOD', 'BURNT', 'BLOOD', 'COFFEE', 'MOCHA', 'TAUPE', 'UMBER', 'COAL', 'GHOST', 
        'BLACK', 'PITCH', 'DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 'PAN', 'DEMIGIRL', 
        'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 'BISEX', 'GLASS', 'POLY', 'ENBY', 'INTERSEX', 'MLM', 
        'WLW', 'GAYBOW', 'PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'MINTY', 'EMERALD', 'TURQUOISE', 
        'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA', 'PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 
        'SHINYMEW', 'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST', 'LEMON', 'LAGUNA', 'FAWN', 'CORN', 
        'DARKOLIVE', 'SPINNACH', 'WAVES', 'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY', 'SUNSHINE', 'BEE', 
        'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'BUBBLEGUM', 'TART',
        'YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'FLUORITE', 'DARKTEAL', 'SONIC', 'NAVY', 'PURPLE', 'WINE', 
        'BRIGHTCRIMSON', 'ROYALPURPLE', 'TROMBONE', 'BRASS', 'YELLOW-GREEN', 'FOREST', 'SEAFOAM', 'FERN', 
        'JEANS', 'JACKET', 'DEEPOCEAN', 'DARKSTRAKIT', 'BARN', 'GARNET', 'DIJON', 'RUST', 'COPPER', 'DEEPOLIVE', 
        'DEEPFOREST', 'MALACHITE', 'OCEANIC', 'NIGHTTIME', 'ONYX', 'RASIN', 'DUSKBOW'
    ]
    cream_colours = ['BANNANA', 'PALECREAM', 'SAND', 'CREAM', 'CORAL', 'MEW']
    ginger_colours = ['PALEGINGER', 'WOOD', 'GOLDEN', 'APRICOT', 'GINGER', 'GOLD', 'FIRE', 'GARFIELD', 
        'DARKGINGER', 'HONEY', 'BRICK', 'ROSE', 'SIENNA', 'SUNSET', 'APPLE', 'RED', 'RUFOUS', 'CRIMSON', 'CARMINE', 
        'SCARLET', 'COSMOS', 'ROSEWOOD', 'BURNT', 'BLOOD']
    black_colours = ['COAL', 'GHOST', 'BLACK', 'PITCH', 'DUSKBOW', 'ONYX', 'RASIN']
    grey_colours = ['CADET', 'BRONZE', 'MARENGO', 'GREY', 'BLUEGREY', 'BATTLESHIP', 'STEEL', 'SLATE', 'XANADU', 'SOOT', 
        'DARKGREY', 'CHARCOAL', 'ANCHOR']
    white_colours = ['WHITE', 'PALEGREY', 'SILVER', 'GLASS', 'PALEBOW', 'IVORY', 'PETAL']
    brown_colours = ['LIGHTBROWN', 'FARROW', 'BEIGE', 'HAY', 'MEERKAT', 'PANTONE', 'LILAC', 'KHAKI', 'HAZELNUT', 'SAMON', 
        'THISTLE', 'GOLDEN-BROWN', 'CAPPUCCINO', 'ECRU', 'MEDALLION', 'DUSTBROWN', 'ASHBROWN', 'SANDALWOOD', 'WRENGE', 
        'PINECONE', 'GRANOLA', 'SADDLE', 'TAN', 'CHESTNUT', 'MINK', 'BROWN', 'CEDAR', 'DARKSAMON', 'BEAVER', 'DARKBROWN', 
        'CHOCOLATE', 'COFFEE', 'MOCHA', 'TAUPE', 'UMBER', 'BRASS', 'YELLOW-GREEN', 'DIJON', 'RUST', 'COPPER']
    blue_colours = ['TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'SHINYMEW', 'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 
        'WAVES', 'SAPPHIRE', 'OCEAN', 'TEAL', 'DENIUM', 'COBALT', 'DARKTEAL', 'SONIC', 'NAVY', 'JEANS', 
        'JACKET', 'DEEPOCEAN', 'OCEANIC', 'NIGHTTIME']
    yellow_colours = ['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'SUNSHINE', 'BEE', 'PYRITE', 'YELLOW', 'PINEAPPLE', 'TROMBONE']
    purple_colours = ['MAGENTA', 'PETAL', 'MEW', 'HEATHER', 'AMYTHYST', 'ORCHID', 'FLORAL', 'CHERRY', 'STRAKIT', 'BUBBLEGUM', 
        'TART', 'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 'DARKSTRAKIT', 'BARN', 'GARNET']
    green_colours = ['CHARTRUSE', 'MINT', 'MINTY', 'EMERALD', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'DARKOLIVE', 'SPINNACH', 'GREEN', 
        'SEAWEED', 'SACRAMENTO', 'SEAGRASS', 'JADE', 'FLUORITE', 'FOREST', 'SEAFOAM', 'FERN', 'DEEPOLIVE', 'DEEPFOREST', 
        'MALACHITE']
    colour_categories = [cream_colours, ginger_colours, black_colours, grey_colours, white_colours, brown_colours, blue_colours, 
    yellow_colours, purple_colours, green_colours, pride_colours]
    
    little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'LUNA',
                    'EXTRA', 'MUSTACHE', 'REVERSEHEART', 'SPARKLE', 'RIGHTEAR', 'LEFTEAR', 'ESTRELLA', 'REVERSEEYE', 'BACKSPOT',
                    'EYEBAGS', 'LOCKET', 'BLAZEMASK', 'TEARS']
    mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR', 'WINGS',
                'DIVA', 'SAVANNAH', 'FADESPOTS', 'BEARD', 'DAPPLEPAW', 'TOPCOVER', 'WOODPECKER', 'MISS', 'BOWTIE', 'VEST',
                'FADEBELLY', 'DIGIT', 'FCTWO', 'FCONE', 'MIA', 'ROSINA', 'PRINCESS', 'DOUGIE']
    high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
                'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
                'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED', 'SHIBAINU', 'OWL', 'BUB', 'SPARROW', 'TRIXIE',
                'SAMMY', 'FRONT', 'BLOSSOMSTEP', 'BULLSEYE', 'FINN', 'SCAR', 'BUSTER', 'HAWKBLAZE', 'CAKE']
    mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                    'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO','PEBBLESHINE', 'BOOTS', 'COW', 'COWTWO', 'LOVEBUG', 'SHOOTINGSTAR',
                    'EYESPOT', 'PEBBLE', 'TAILTWO', 'BUDDY', 'KROPKA']
    point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT', 'KARPATI']
    vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'POWDER', 'BLEACHED', 'SMOKEY']
    white_sprites = [
        little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

    skin_sprites = ['BLACK',  'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                    'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE', 'RED', 
                    'WHITEMARBLE', 'BLACKGILL', 'REDGILL', 'PINKGILL', 'DARKBROWNGILL', 'BROWNGILL', 
                    'LIGHTBROWNGILL',  'DARKGILL', 'DARKGREYGILL', 'GREYGILL', 'DARKSALMONGILL', 'SALMONGILL', 
                    'PEACHGILL', 'DARKMARBLEDGILL', 'MARBLEDGILL', 'LIGHTMARBLEDGILL', 'DARKBLUEGILL', 
                    'BLUEGILL', 'LIGHTBLUEGILL', 'WHITEMARBLEGILL']

    albinism = ['FLATALBINO', 'REDALBINO', 'PINKALBINO', 'VIOLETALBINO', 'BLUEALBINO', 'GREENALBINO',
                    'YELLOWALBINO']
    melanism = ['FLATMELANISTIC', 'REDMELANISTIC', 'PINKMELANISTIC', 'VIOLETMELANISTIC', 'BLUEMELANISTIC',
                    'GREENMELANISTIC', 'YELLOWMELANISTIC']
    albino_eyes = ['PINK', 'VIOLETPINK', 'YELLOWPINK', 'CYANPINK', 'BLUEPINK', 'MINTPINK', 'GHOSTPINK', 
        'NACRE', 'LIGHTPOPPY', 'LIGHTBROWN']
    melanistic_eyes = ['RUBEN', 'DUSK', 'SUNSHADOW', 'DARKCYAN', 'DEEPBLUE', 'FERN', 'BLACKHOLE', 'NIGHT',
        'DARKPOPPY', 'DARKBROWN']

    """Holds all appearence information for a cat. """
    def __init__(self,
                 name:str="SingleColour",
                 length:str="short",
                 colour:str="WHITE",
                 white_patches:str=None,
                 eye_color:str="BLUE",
                 eye_colour2:str=None,
                 eye_colour3:str=None,
                 eye_lazy:str=None,
                 eye_lazy2:str=None,
                 tortiebase:str=None,
                 tortiecolour:str=None,
                 pattern:str=None,
                 tortiepattern:str=None,
                 vitiligo:str=None,
                 points:str=None,
                 albino:str=None,
                 melanistic:str=None,
                 accessory:str=None,
                 magic:str=None,
                 paralyzed:bool=False,
                 opacity:int=100,
                 scars:list=None,
                 tint:str="none",
                 skin:str="BLACK",
                 blep:bool=False,
                 white_patches_tint:str="none",
                 newborn_sprite:int=None,
                 kitten_sprite:int=None,
                 adol_sprite:int=None,
                 adult_sprite:int=None,
                 senior_sprite:int=None,
                 para_young_sprite:int=None,
                 para_adult_sprite:int=None,
                 reverse:bool=False,
                 ) -> None:
        self.name = name
        self.colour = colour
        self.white_patches = white_patches
        self.eye_colour = eye_color
        self.eye_colour2 = eye_colour2
        self.eye_colour3 = eye_colour3
        self.eye_lazy = eye_lazy
        self.eye_lazy2 = eye_lazy2
        self.tortiebase = tortiebase
        self.pattern = pattern
        self.tortiepattern = tortiepattern
        self.tortiecolour = tortiecolour
        self.vitiligo = vitiligo
        self.length=length
        self.points = points
        self.albino = albino
        self.melanistic = melanistic
        self.accessory = accessory
        self.magic = magic
        self.paralyzed = paralyzed
        self.opacity = opacity
        self.scars = scars if isinstance(scars, list) else []
        self.tint = tint
        self.white_patches_tint = white_patches_tint
        self.cat_sprites =  {
            "newborn": newborn_sprite if newborn_sprite is not None else 0,
            "kitten": kitten_sprite if kitten_sprite is not None else 0,
            "adolescent": adol_sprite if adol_sprite is not None else 0,
            "young adult": adult_sprite if adult_sprite is not None else 0,
            "adult": adult_sprite if adult_sprite is not None else 0,
            "senior adult": adult_sprite if adult_sprite is not None else 0,
            "senior": senior_sprite if senior_sprite is not None else 0,
            "para_young": para_young_sprite if para_young_sprite is not None else 0,
            "para_adult": para_adult_sprite if para_adult_sprite is not None else 0,
        }        
        self.cat_sprites["sick_adult"] = 18
        self.cat_sprites["sick_young"] = 19
        
        self.reverse = reverse
        self.skin = skin
        self.blep = blep

    @staticmethod
    def generate_new_pelt(gender:str, parents:tuple=(), age:str="adult"):
        new_pelt = Pelt()
        
        pelt_white = new_pelt.init_pattern_color(parents, gender)
        new_pelt.init_white_patches(pelt_white, parents)
        new_pelt.init_sprite()
        new_pelt.init_skin(parents)
        new_pelt.init_scars(age)
        new_pelt.init_accessories(age)
        new_pelt.init_eyes(parents)
        new_pelt.init_pattern()
        new_pelt.init_tint()
        
        return new_pelt
    
    def check_and_convert(self, convert_dict):
        """Checks for old-type properties for the apperence-related properties
        that are stored in Pelt, and converts them. To be run when loading a cat in. """
        
        #First, convert from some old names that may be in white_patches. 
        if self.white_patches == 'POINTMARK':
            self.white_patches = "SEALPOINT"
        elif self.white_patches == 'PANTS2':
            self.white_patches = 'PANTSTWO'
        elif self.white_patches == 'ANY2':
            self.white_patches = 'ANYTWO'
        elif self.white_patches == "VITILIGO2":
            self.white_patches = "VITILIGOTWO"
            
        if self.vitiligo == "VITILIGO2":
            self.vitiligo = "VITILIGOTWO"
        
        # Move white_patches that should be in vit or points. 
        if self.white_patches in Pelt.vit:
            self.vitiligo = self.white_patches
            self.white_patches = None
        elif self.white_patches in Pelt.point_markings:
            self.points = self.white_patches
            self.white_patches = None

        
        if self.tortiepattern and "tortie" in self.tortiepattern:
            self.tortiepattern = sub("tortie", "", self.tortiepattern.lower())
            if self.tortiepattern == "solid":
                self.tortiepattern = "single"
                
        if self.white_patches in convert_dict["old_creamy_patches"]:
            self.white_patches = convert_dict["old_creamy_patches"][self.white_patches]
            self.white_patches_tint = "darkcream"
        elif self.white_patches in ['SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']:
            self.white_patches_tint = "none"
        
        # Eye Color Convert Stuff
        if self.eye_colour == "BLUE2":
            self.eye_colour = "COBALT"
        if self.eye_colour2 == "BLUE2":
            self.eye_colour2 = "COBALT"
            
        if self.eye_colour in ["BLUEYELLOW", "BLUEGREEN"]:
            if self.eye_colour == "BLUEYELLOW":
                self.eye_colour2 = "YELLOW"
            elif self.eye_colour == "BLUEGREEN":
                self.eye_colour2 = "GREEN"
            self.eye_colour = "BLUE"
        
        if self.pattern in convert_dict["old_tortie_patches"]:
            old_pattern = self.pattern
            self.pattern = convert_dict["old_tortie_patches"][old_pattern][1]
            
            # If the pattern is old, there is also a change the base color is stored in
            # tortiecolour, and that may be different from the pelt color (main for torties
            # generated before the "ginger-on-ginger" update. If it was generated after that update,
            # tortiecolour and pelt_colour will be the same. Therefore, lets also re-set the pelt color
            self.colour = self.tortiecolour
            self.tortiecolour = convert_dict["old_tortie_patches"][old_pattern][0]
            
        if self.pattern == "MINIMAL1":
            self.pattern = "MINIMALONE"
        elif self.pattern == "MINIMAL2":
            self.pattern = "MINIMALTWO"
        elif self.pattern == "MINIMAL3":
            self.pattern = "MINIMALTHREE"
        elif self.pattern == "MINIMAL4":
            self.pattern = "MINIMALFOUR"
        
    def init_eyes(self, parents):
        if not parents:
            self.eye_colour = choice(Pelt.eye_colours)
        else:
            for _par in parents:
                if _par.pelt.eye_colour in Pelt.albino_eyes + Pelt.melanistic_eyes: 
                    if _par.pelt.eye_colour in ['CYANPINK', 'BLUEPINK', 'DARKCYAN', 'DEEPBLUE']:
                        _par.pelt.eye_colour = choice(Pelt.blue_eyes)                      
                    elif _par.pelt.eye_colour in ['YELLOWPINK', 'SUNSHADOW', 'LIGHTBROWN', 'DARKBROWN']:
                        _par.pelt.eye_colour = choice(Pelt.yellow_eyes)    
                    elif _par.pelt.eye_colour in ['MINTPINK','FERN']:
                        _par.pelt.eye_colour = choice(Pelt.green_eyes)     
                    elif _par.pelt.eye_colour in ['PINK','VIOLETPINK', 'RUBEN', 'DUSK', 'LIGHTPOPPY', 'DARKPOPPY']:
                        _par.pelt.eye_colour = choice(Pelt.purple_eyes)     
                    elif _par.pelt.eye_colour in ['GHOSTPINK', 'BLACKHOLE']:
                        _par.pelt.eye_colour = choice(Pelt.mono_eyes)   
                    elif _par.pelt.eye_colour in ['NACRE', 'NIGHT']:
                        _par.pelt.eye_colour = choice(Pelt.chromatic_eyes)   
                self.eye_colour = choice([i.pelt.eye_colour for i in parents] + [choice(Pelt.eye_colours)])
   
        #White patches must be initalized before eye color. 
        num = game.config["cat_generation"]["base_heterochromia"]
        if self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE'] or self.colour == 'WHITE':
            num = num - 90
        for _par in parents:
            if _par.pelt.eye_colour2 or _par.pelt.eye_colour3:
                num -= 10
        
        if num < 0:
            num = 4
            
        hit = random.randint(0, num)
        if hit == 0:
            if self.eye_colour in Pelt.yellow_eyes:
                eye_choice = choice([Pelt.blue_eyes, Pelt.green_eyes, Pelt.purple_eyes, Pelt.mono_eyes, Pelt.chromatic_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.blue_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.green_eyes, Pelt.purple_eyes, Pelt.mono_eyes, Pelt.chromatic_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.green_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.purple_eyes, Pelt.mono_eyes, Pelt.chromatic_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.purple_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.mono_eyes, Pelt.chromatic_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.mono_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.purple_eyes, Pelt.chromatic_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.chromatic_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.purple_eyes, Pelt.mono_eyes])
                self.eye_colour2 = choice(eye_choice)
        if hit == 1:
            if self.eye_colour in Pelt.yellow_eyes:
                eye_choice = choice([Pelt.blue_eyes, Pelt.green_eyes, Pelt.purple_eyes, Pelt.mono_eyes, Pelt.chromatic_eyes])
                self.eye_colour3 = choice(eye_choice)
            elif self.eye_colour in Pelt.blue_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.green_eyes, Pelt.purple_eyes, Pelt.mono_eyes, Pelt.chromatic_eyes])
                self.eye_colour3 = choice(eye_choice)
            elif self.eye_colour in Pelt.green_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.purple_eyes, Pelt.mono_eyes, Pelt.chromatic_eyes])
                self.eye_colour3 = choice(eye_choice)
            elif self.eye_colour in Pelt.purple_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.mono_eyes, Pelt.chromatic_eyes])
                self.eye_colour3 = choice(eye_choice)
            elif self.eye_colour in Pelt.mono_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.purple_eyes, Pelt.chromatic_eyes])
                self.eye_colour3 = choice(eye_choice)
            elif self.eye_colour in Pelt.chromatic_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.purple_eyes, Pelt.mono_eyes])
                self.eye_colour3 = choice(eye_choice)
        if hit == 2:
            possible_eyes = Pelt.eye_colours.copy()
            possible_eyes.remove(self.eye_colour)
            self.eye_colour2 = choice(possible_eyes)
        if hit == 3:
            possible_eyes = Pelt.eye_colours.copy()
            possible_eyes.remove(self.eye_colour)
            self.eye_colour3 = choice(possible_eyes)
            
                
        lazy = random.randint(0, 50)
        if lazy == 0:
            self.eye_lazy = self.eye_colour
            if self.eye_colour2 != None:
                self.eye_lazy = self.eye_colour2
            if self.eye_colour3 != None:
                self.eye_lazy2 = self.eye_colour3
                
    def pattern_color_inheritance(self, parents: tuple=(), gender="female"):
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
                if p.pelt.name in Pelt.torties:
                    par_peltnames.add(p.pelt.tortiebase.capitalize())
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
            print("Warning - no parents: pelt randomized")
            return self.randomize_pattern_color(gender)

        # There is a 1/10 chance for kits to have the exact same pelt as one of their parents
        if not random.randint(0, game.config["cat_generation"]["direct_inheritance"]):  # 1/10 chance
            selected = choice(par_pelts)
            self.name = selected.name
            self.length = selected.length
            self.colour = selected.colour
            self.tortiebase = selected.tortiebase
            return selected.white

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT
        # ------------------------------------------------------------------------------------------------------------#

        # Determine pelt.
        weights = [0, 0, 0, 0]  #Weights for each pelt group. It goes: (tabbies, spotted, plain, exotic)
        for p_ in par_peltnames:
            if p_ in Pelt.tabbies:
                add_weight = (50, 10, 5, 7)
            elif p_ in Pelt.spotted:
                add_weight = (10, 50, 5, 5)
            elif p_ in Pelt.plain:
                add_weight = (0, 0, 50, 0)
            elif p_ in Pelt.exotic:
                add_weight = (15, 15, 1, 45)
            elif p_ is None:  # If there is at least one unknown parent, a None will be added to the set.
                add_weight = (0, 0, 30, 0)
            else:
                add_weight = (0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

        #A quick check to make sure all the weights aren't 0
        if all([x == 0 for x in weights]):
            weights = [1, 1, 1, 1]

        # Now, choose the pelt category and pelt. The extra 0 is for the tortie pelts,
        chosen_pelt = choice(
            random.choices(Pelt.pelt_categories, weights=weights + [0], k = 1)[0]
        )

        # Tortie chance
        tortie_chance_f = game.config["cat_generation"]["base_female_tortie"]  # There is a default chance for female tortie
        tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
        tortie_chance_i = game.config["cat_generation"]["base_intersex_tortie"]
        for p_ in par_pelts:
            if p_.name in Pelt.torties:
                tortie_chance_f = int(tortie_chance_f / 2)
                tortie_chance_i = int(tortie_chance_i - 1)
                tortie_chance_m = tortie_chance_m - 1
                break

        # Determine tortie:
        if gender == "female":
            torbie = random.getrandbits(tortie_chance_f) == 1
        elif gender == "intersex":
            torbie = random.getrandbits(tortie_chance_i) == 1        
        else:
            torbie = random.getrandbits(tortie_chance_m) == 1

        chosen_tortie_base = None
        if torbie:
            # If it is tortie, the chosen pelt above becomes the base pelt.
            chosen_tortie_base = chosen_pelt
            if chosen_tortie_base in ["TwoColour", "SingleColour"]:
                chosen_tortie_base = "Single"
            chosen_tortie_base = chosen_tortie_base.lower()
            chosen_pelt = random.choice(Pelt.torties)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT COLOUR
        # ------------------------------------------------------------------------------------------------------------#
        # Weights for each colour group. It goes: (ginger_colours, black_colours, white_colours, brown_colours)
        weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for p_ in par_peltcolours:
            if p_ in Pelt.cream_colours:
                add_weight = (40, 20, 0, 0, 0, 10, 0, 5, 5, 2, 1)
            if p_ in Pelt.ginger_colours:
                add_weight = (20, 40, 0, 0, 0, 10, 0, 0, 5, 0, 5)
            elif p_ in Pelt.black_colours:
                add_weight = (0, 0, 40, 20, 2, 5, 5, 0, 0, 0, 1)
            elif p_ in Pelt.grey_colours:
                add_weight = (0, 0, 10, 40, 10, 2, 5, 0, 0, 1, 1)            
            elif p_ in Pelt.white_colours:
                add_weight = (2, 0, 5, 20, 40, 0, 5, 2, 0, 1, 1)
            elif p_ in Pelt.brown_colours:
                add_weight = (5, 10, 5, 2, 0, 35, 0, 5, 0, 1, 1)
            elif p_ in Pelt.blue_colours:
                add_weight = (0, 0, 20, 20, 20, 0, 25, 0, 2, 0, 5)
            elif p_ in Pelt.yellow_colours:
                add_weight = (10, 0, 0, 0, 10, 20, 0, 25, 0, 5, 5)
            elif p_ in Pelt.purple_colours:
                add_weight = (20, 20, 0, 0, 0, 0, 0, 5, 25, 0, 5)
            elif p_ in Pelt.green_colours:
                add_weight = (2, 0, 0, 1, 1, 1, 0, 5, 0, 35, 5)
            elif p_ in Pelt.pride_colours:
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

        chosen_pelt_color = choice(
            random.choices(Pelt.colour_categories, weights=weights, k=1)[0]
        )

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT LENGTH
        # ------------------------------------------------------------------------------------------------------------#

        weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Weights for each length. It goes (short, medium, long, snat, wolf, skele, bare, catfish, scug, saint)
        for p_ in par_peltlength:
            if p_ == "short":
                add_weight = (50, 25, 10, 5, 5, 10, 2, 5, 5, 5)
            elif p_ == "medium":
                add_weight = (25, 50, 25, 5, 25, 10, 1, 1, 1, 5)
            elif p_ == "long":
                add_weight = (10, 25, 50, 1, 10, 1, 0, 1, 1, 5)
            elif p_ == "snat":
                add_weight = (5, 5, 5, 50, 0, 5, 1, 1, 10, 10)
            elif p_ == "wolf":
                add_weight = (15, 15, 15, 0, 50, 5, 1, 0, 1, 1)
            elif p_ == "skele":
                add_weight = (25, 5, 5, 1, 1, 50, 25, 1, 5, 5)
            elif p_ == "bare":
                add_weight = (25, 10, 5, 1, 1, 25, 50, 25, 5, 5)
            elif p_ == "catfish":
                add_weight = (5, 5, 0, 5, 10, 10, 25, 50, 10, 5)
            elif p_ == "scug":
                add_weight = (5, 5, 1, 25, 5, 10, 10, 5, 50, 25)
            elif p_ == "saint":
                add_weight = (5, 5, 5, 25, 10, 5, 0, 5, 25, 50)
            elif p_ is None:
                add_weight = (10, 10, 10, 5, 5, 5, 2, 5, 5, 5)
            else:
                add_weight = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

        # A quick check to make sure all the weights aren't 0
        if all([x == 0 for x in weights]):
            weights = [1, 1, 1, 1, 1, 1, 1]

        chosen_pelt_length = random.choices(Pelt.pelt_length, weights=weights, k=1)[0]

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
        elif chosen_pelt == "Calico":
            if not chosen_white:
                chosen_pelt = "Tortie"

        # SET THE PELT
        self.name = chosen_pelt
        self.colour = chosen_pelt_color
        self.length = chosen_pelt_length
        self.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.
        return chosen_white

    def randomize_pattern_color(self, gender):
        # ------------------------------------------------------------------------------------------------------------#
        #   PELT
        # ------------------------------------------------------------------------------------------------------------#

        # Determine pelt.
        chosen_pelt = choice(
            random.choices(Pelt.pelt_categories, weights=(0, 0, 30, 0, 0), k=1)[0]
        )

        # Tortie chance
        # There is a default chance for female tortie, slightly increased for completely random generation.
        tortie_chance_f = game.config["cat_generation"]["base_female_tortie"] - 1
        tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
        if gender == "female":
            torbie = random.getrandbits(tortie_chance_f) == 1
        else:
            torbie = random.getrandbits(tortie_chance_m) == 1

        chosen_tortie_base = None
        if torbie:
            # If it is tortie, the chosen pelt above becomes the base pelt.
            chosen_tortie_base = chosen_pelt
            if chosen_tortie_base in ["TwoColour", "SingleColour"]:
                chosen_tortie_base = "Single"
            chosen_tortie_base = chosen_tortie_base.lower()
            chosen_pelt = random.choice(Pelt.torties)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT COLOUR
        # ------------------------------------------------------------------------------------------------------------#

        chosen_pelt_color = choice(
            random.choices(Pelt.colour_categories, weights=(30, 45, 40, 30, 25, 45, 15, 15, 10, 25, 2), k=1)[0]
        )

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT LENGTH
        # ------------------------------------------------------------------------------------------------------------#


        chosen_pelt_length = random.choices(Pelt.pelt_length, weights=(10, 10, 10, 5, 5, 5, 1, 5, 5, 5), k=1)[0]

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT WHITE
        # ------------------------------------------------------------------------------------------------------------#


        chosen_white = random.randint(1, 100) <= 40

        # Adjustments to pelt chosen based on if the pelt has white in it or not.
        if chosen_pelt in ["TwoColour", "SingleColour"]:
            if chosen_white:
                chosen_pelt = "TwoColour"
            else:
                chosen_pelt = "SingleColour"
        elif chosen_pelt == "Calico":
            if not chosen_white:
                chosen_pelt = "Tortie"

        self.name = chosen_pelt
        self.colour = chosen_pelt_color
        self.length = chosen_pelt_length
        self.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.
        return chosen_white

    def init_pattern_color(self, parents, gender) -> bool:
        """Inits self.name, self.colour, self.length, 
            self.tortiebase and determines if the cat 
            will have white patche or not. 
            Return TRUE is the cat should have white patches, 
            false is not. """
        
        if parents:
            #If the cat has parents, use inheritance to decide pelt.
            chosen_white = self.pattern_color_inheritance(parents, gender)
        else:
            chosen_white = self.randomize_pattern_color(gender)
        
        return chosen_white

    def init_sprite(self):
        self.cat_sprites = {
            'newborn': random.randint(49, 50),
            'sick_young': 48,
            'sick_adult': 47
        }
        self.reverse = choice([True, False])
                
        if self.length == 'long':
            self.cat_sprites['kitten'] = random.randint(3, 5)
            self.cat_sprites['adolescent'] = random.randint(12, 14)
            self.cat_sprites['adult'] = random.randint(21, 23)
            self.cat_sprites['senior'] = random.randint(30, 32)
            self.cat_sprites['para_young'] = random.randint(37, 38)
            self.cat_sprites['para_adult'] = random.randint(45, 46)
        elif self.length == 'snat':
            self.cat_sprites['newborn'] = 6
            self.cat_sprites['kitten'] = random.randint(7, 8)
            self.cat_sprites['adolescent'] = random.randint(15, 16)
            self.cat_sprites['adult'] = choice([17, 24, 25])
            self.cat_sprites['senior'] = random.choice([26, 33, 34])
            self.cat_sprites['para_young'] = 42
            self.cat_sprites['para_adult'] = 43
            self.cat_sprites['sick_young'] = 51
            self.cat_sprites['sick_adult'] = 44
        elif self.length == 'bare':
            self.cat_sprites['newborn'] = 54
            self.cat_sprites['kitten'] = random.randint(55, 56)
            self.cat_sprites['adolescent'] = random.randint(63, 65)
            self.cat_sprites['adult'] = random.randint(72, 74)
            self.cat_sprites['senior'] = random.randint(81, 83)
            self.cat_sprites['para_young'] = random.randint(90, 91)
            self.cat_sprites['para_adult'] = random.choice([92, 99])
            self.cat_sprites['sick_young'] = 101
            self.cat_sprites['sick_adult'] = 100
        elif self.length == 'skele':
            self.cat_sprites['newborn'] = 57
            self.cat_sprites['kitten'] = random.randint(58, 59)
            self.cat_sprites['adolescent'] = random.randint(66, 68)
            self.cat_sprites['adult'] = random.randint(75, 77)
            self.cat_sprites['senior'] = random.randint(84, 86)
            self.cat_sprites['para_young'] = 94
            self.cat_sprites['para_adult'] = random.choice([95, 102])
            self.cat_sprites['sick_young'] = 104
            self.cat_sprites['sick_adult'] = 103
        elif self.length == 'wolf':
            self.cat_sprites['newborn'] = 107
            self.cat_sprites['kitten'] = random.randint(60, 62)
            self.cat_sprites['adolescent'] = random.randint(69, 71)
            self.cat_sprites['adult'] = random.randint(78, 80)
            self.cat_sprites['senior'] = random.randint(87, 89)
            self.cat_sprites['para_young'] = 98
            self.cat_sprites['para_adult'] = random.randint(96, 97)
            self.cat_sprites['sick_young'] = 106
            self.cat_sprites['sick_adult'] = 105
        elif self.length == 'catfish':
            self.cat_sprites['newborn'] = 155
            self.cat_sprites['kitten'] = random.randint(108, 110)
            self.cat_sprites['adolescent'] = random.randint(117, 119)
            self.cat_sprites['adult'] = random.randint(126, 128)
            self.cat_sprites['senior'] = random.randint(135, 137)
            self.cat_sprites['para_young'] = 146
            self.cat_sprites['para_adult'] = random.randint(144, 145)
            self.cat_sprites['sick_young'] = 154
            self.cat_sprites['sick_adult'] = 153
        elif self.length == 'scug':
            self.cat_sprites['newborn'] = random.randint(160, 161)
            self.cat_sprites['kitten'] = random.randint(111, 113)
            self.cat_sprites['adolescent'] = random.randint(120, 122)
            self.cat_sprites['adult'] = random.randint(129, 131)
            self.cat_sprites['senior'] = random.randint(138, 140)
            self.cat_sprites['para_young'] = random.randint(147, 148)
            self.cat_sprites['para_adult'] = random.randint(151, 152)
            self.cat_sprites['sick_young'] = 159
            self.cat_sprites['sick_adult'] = 158
        elif self.length == 'saint':
            self.cat_sprites['newborn'] = random.randint(160, 161)
            self.cat_sprites['kitten'] = random.randint(114, 116)
            self.cat_sprites['adolescent'] = random.randint(123, 125)
            self.cat_sprites['adult'] = random.randint(132, 134)
            self.cat_sprites['senior'] = random.randint(141, 143)
            self.cat_sprites['para_young'] = random.randint(149, 150)
            self.cat_sprites['para_adult'] = random.randint(156, 157)
            self.cat_sprites['sick_young'] = 159
            self.cat_sprites['sick_adult'] = 158
        else:
            self.cat_sprites['kitten'] = random.randint(0, 2)
            self.cat_sprites['adolescent'] = random.randint(9, 11)
            self.cat_sprites['adult'] = random.randint(18, 20)
            self.cat_sprites['senior'] = random.randint(27, 29)
            self.cat_sprites['para_young'] = random.randint(36, 37)
            self.cat_sprites['para_adult'] = random.randint(40, 41)

        self.cat_sprites['young adult'] = self.cat_sprites['adult']
        self.cat_sprites['senior adult'] = self.cat_sprites['adult']

    def init_skin(self, parents):
        # skin chances
        if not parents:
            self.skin = choice(Pelt.skin_sprites)
        else:
            for _par in parents:
                if _par.pelt.skin in ["ALBINO", "ALBINOGILL", "MELANISTIC", "MELANISTICGILL"]:
                    _par.pelt.skin = choice(Pelt.skin_sprites)
                self.skin = choice([i.pelt.skin for i in parents] + Pelt.skin_sprites)
        
        num = game.config["cat_generation"]["base_blep"]
        for _par in parents:
            if _par.pelt.blep == True:
                num -= 90        
        if num < 0:
            num = 1

        hit = random.randint(0, num)
        if hit == 0:
            self.blep = True

    def init_scars(self, age):
        if age == "newborn":
            return
        
        if age in ['kitten', 'adolescent']:
            scar_choice = random.randint(0, 50)
        elif age in ['young adult', 'adult']:
            scar_choice = random.randint(0, 20)
        else:
            scar_choice = random.randint(0, 15)
            
        if scar_choice == 1:
            self.scars.append(choice([
                choice(Pelt.scars1),
                choice(Pelt.scars3)
            ]))

        if 'NOTAIL' in self.scars and 'HALFTAIL' in self.scars:
            self.scars.remove('HALFTAIL')

    def init_accessories(self, age):
        if age == "newborn": 
            self.accessory = None
            return
        
        acc_display_choice = random.randint(0, 80)
        if age in ['kitten', 'adolescent']:
            acc_display_choice = random.randint(0, 180)
        elif age in ['young adult', 'adult']:    
            acc_display_choice = random.randint(0, 100)
        
        if acc_display_choice == 1:
            self.accessory = choice([
                choice(Pelt.plant_accessories),
                choice(Pelt.wild_accessories)
            ])
        else:
            self.accessory = None

    def init_pattern(self):
        if self.name in Pelt.torties:
            if not self.tortiebase:
                self.tortiebase = choice(Pelt.tortiebases)
            if not self.pattern:
                self.pattern = choice(Pelt.tortiepatterns)

            wildcard_chance = game.config["cat_generation"]["wildcard_tortie"]
            if self.colour:
                # The "not wildcard_chance" allows users to set wildcard_tortie to 0
                # and always get wildcard torties.
                if not wildcard_chance or random.getrandbits(wildcard_chance) == 1:
                    # This is the "wildcard" chance, where you can get funky combinations.
                    # people are fans of the print message so I'm putting it back
                    print("Wildcard tortie!")

                    # Allow any pattern:
                    self.tortiepattern = choice(Pelt.tortiebases)

                    # Allow any colors that aren't the base color.
                    possible_colors = Pelt.pelt_colours.copy()
                    possible_colors.remove(self.colour)
                    self.tortiecolour = choice(possible_colors)

                else:
                    # Normal generation
                    self.tortiepattern = self.tortiebase

                    # Ginger is often dupliselfed to increase its chances
                    if self.colour in ["WHITE", "PALEGREY", "SILVER", "CADET", "BRONZE", "TURQUOISE", "SKY", 
                                        "SHINYMEW", "PUDDLE", "TIFFANY", "PALEBOW"]:
                        self.tortiecolour = choice(['PALECREAM', 'SAND', 'CREAM', 'PALEGINGER', 'WOOD', 'GOLDEN', 'APRICOT', 'CORAL', 
                                                'PETAL', 'MEW', 'MAGENTA', 'HEATHER', 'AMYTHYST', 'CHARTRUSE', 'MINT', 'MINTY', 'LIME', 
                                                'LETTUCE', 'GRASS', 'OLIVE'] + (Pelt.pride_colours * 2))
                    elif self.colour in ["MARENGO", "GREY", "BLUEGREY", "BATTLESHIP", "STEEL", "SLATE", "POWDERBLUE", 
                                        "INDIGOBLUE", "INDIGOLIGHT", "WAVES", "SAPPHIRE", "OCEAN", "TEAL", 
                                        "DENIUM", "COBALT"]:
                        self.tortiecolour = choice(['GINGER', 'GOLD', 'FIRE', 'GARFIELD', 'DARKGINGER', 'HONEY', 'BRICK', 'ROSE', 'ORCHID', 
                                                'FLORAL', 'CHERRY', 'STRAKIT', 'BUBBLEGUM', 'TART', 'PURPLE', 'EMERALD', 'DARKOLIVE', 'SPINNACH', 
                                                'GREEN', 'SEAWEED', 'SACRAMENTO', 'SEAGRASS', 'JADE'] + (Pelt.pride_colours * 2))
                    elif self.colour in ["XANADU", "SOOT", "DARKGREY", "CHARCOAL", "ANCHOR", "COAL", "GHOST", 
                                        "BLACK", "PITCH", "DUSKBOW", "DARKTEAL", "SONIC", "NAVY", "JEANS", 
                                        "JACKET", "DEEPOCEAN", "OCEANIC", "NIGHTTIME"]:
                        self.tortiecolour = choice(['SIENNA', 'SUNSET', 'APPLE', 'RED', 'RUFOUS', 'CRIMSON', 'CARMINE', 'SCARLET', 'COSMOS', 'ROSEWOOD',
                                                'BURNT', 'BLOOD', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 'DARKSTRAKIT', 'BARN', 'GARNET', 'RASIN', 'FLUORITE', 
                                                'FOREST', 'SEAFOAM', 'FERN', 'DEEPOLIVE', 'DEEPFOREST', 'MALACHITE'] + (Pelt.pride_colours * 2))
                    
                    elif self.colour in ["PALECREAM", "SAND", "CREAM", "PALEGINGER", "WOOD", "GOLDEN", "APRICOT", "CORAL", 
                                        "PETAL", "MEW", "MAGENTA", "HEATHER", "AMYTHYST"]:
                        self.tortiecolour = choice(['WHITE', 'PALEGREY', 'SILVER', 'CADET', 'BRONZE', 'TURQUOISE', 'SKY', 
                                                'SHINYMEW', 'PUDDLE', 'TIFFANY', 'PALEBOW', 'CHARTRUSE', 'MINT', 'MINTY', 'LIME', 
                                                'LETTUCE', 'GRASS', 'OLIVE'] + (Pelt.pride_colours * 2))
                    elif self.colour in ["GINGER", "GOLD", "FIRE", "GARFIELD", "DARKGINGER", "HONEY", "BRICK", "ROSE", "ORCHID", 
                                        "FLORAL", "CHERRY", "STRAKIT", "BUBBLEGUM", "TART", "PURPLE"]:
                        self.tortiecolour = choice(['MARENGO', 'GREY', 'BLUEGREY', 'BATTLESHIP', 'STEEL', 'SLATE', 'POWDERBLUE', 
                                                'INDIGOBLUE', 'INDIGOLIGHT', 'WAVES', 'SAPPHIRE', 'OCEAN', 'TEAL', 
                                                'DENIUM', 'COBALT', 'EMERALD', 'DARKOLIVE', 'SPINNACH', 
                                                'GREEN', 'SEAWEED', 'SACRAMENTO', 'SEAGRASS', 'JADE'] + (Pelt.pride_colours * 2))
                    elif self.colour in ["SIENNA", "SUNSET", "APPLE", "RED", "RUFOUS", "CRIMSON", "CARMINE", "SCARLET", "COSMOS", "ROSEWOOD",
                                        "BURNT", "BLOOD", "WINE", "BRIGHTCRIMSON", "ROYALPURPLE", "DARKSTRAKIT", "BARN", "GARNET", "RASIN"]:                   
                        self.tortiecolour = choice(['XANADU', 'SOOT', 'DARKGREY', 'CHARCOAL', 'ANCHOR', 'COAL', 'GHOST', 
                                                'BLACK', 'PITCH', 'DUSKBOW', 'DARKTEAL', 'SONIC', 'NAVY', 'JEANS', 
                                                'JACKET', 'DEEPOCEAN', 'OCEANIC', 'NIGHTTIME', 'FLUORITE', 
                                                'FOREST', 'SEAFOAM', 'FERN', 'DEEPOLIVE', 'DEEPFOREST', 'MALACHITE'] + (Pelt.pride_colours * 2))

                    elif self.colour in ["BANNANA", "LIGHTBROWN", "FARROW", "BEIGE", "HAY", "MEERKAT", "PANTONE", "LILAC", "KHAKI", 
                                        "HAZELNUT", "SAMON", "IVORY", "LEMON", "LAGUNA", "FAWN", "CORN"]:
                        self.tortiecolour = choice(['WHITE', 'PALEGREY', 'SILVER', 'CADET', 'BRONZE', 'TURQUOISE', 'SKY', 
                                                'SHINYMEW', 'PUDDLE', 'TIFFANY', 'PALEBOW', 'PALECREAM', 'SAND', 'CREAM', 'PALEGINGER', 
                                                'WOOD', 'GOLDEN', 'APRICOT', 'CORAL', 'PETAL', 'MEW', 'MAGENTA', 'HEATHER', 'AMYTHYST', 
                                                'CHARTRUSE', 'MINT', 'MINTY', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE'] + (Pelt.pride_colours * 2))
                    elif self.colour in ["THISTLE", "GOLDEN-BROWN", "CAPPUCCINO", "ECRU", "MEDALLION", "DUSTBROWN", "ASHBROWN", 
                                        "SANDALWOOD", "WRENGE", "PINECONE", "GRANOLA", "SADDLE", "TAN", "CHESTNUT", "MINK", "BROWN", 
                                        "BEE", "PYRITE", "YELLOW", "PINEAPPLE"]:
                        self.tortiecolour = choice(['MARENGO', 'GREY', 'BLUEGREY', 'BATTLESHIP', 'STEEL', 'SLATE', 'GINGER', 'GOLD', 
                                                'FIRE', 'GARFIELD', 'DARKGINGER', 'HONEY', 'BRICK', 'ROSE', 'ORCHID', 'FLORAL', 'CHERRY', 
                                                'STRAKIT', 'BUBBLEGUM', 'TART', 'PURPLE', 'POWDERBLUE', 'INDIGOBLUE', 'INDIGOLIGHT', 
                                                'WAVES', 'SAPPHIRE', 'OCEAN', 'TEAL', 'DENIUM', 'COBALT', 'EMERALD', 'DARKOLIVE', 'SPINNACH', 
                                                'GREEN', 'SEAWEED', 'SACRAMENTO', 'SEAGRASS', 'JADE'] + (Pelt.pride_colours * 2))
                    elif self.colour in ["CEDAR", "DARKSAMON", "BEAVER", "DARKBROWN", "CHOCOLATE", "COFFEE", "MOCHA", "TAUPE", "UMBER", "TROMBONE", 
                                        "BRASS", "YELLOW-GREEN", "DIJON", "RUST", "COPPER", "ONYX"]:
                        self.tortiecolour = choice(['XANADU', 'SOOT', 'DARKGREY', 'CHARCOAL', 'ANCHOR', 'COAL', 'GHOST', 'BLACK', 
                                                'PITCH', 'DUSKBOW', 'SIENNA', 'SUNSET', 'APPLE', 'RED', 'RUFOUS', 'CRIMSON', 'CARMINE', 'SCARLET', 
                                                'COSMOS', 'ROSEWOOD', 'BURNT', 'BLOOD', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 'DARKSTRAKIT', 'BARN', 
                                                'GARNET', 'RASIN', 'DARKTEAL', 'SONIC', 'NAVY', 'JEANS', 'JACKET', 'DEEPOCEAN', 'OCEANIC', 'NIGHTTIME', 
                                                'FLUORITE', 'FOREST', 'SEAFOAM', 'FERN', 'DEEPOLIVE', 'DEEPFOREST', 'MALACHITE'] + (Pelt.pride_colours * 2))

                    elif self.colour in ["CHARTRUSE", "MINT", "MINTY", "LIME", "LETTUCE", "GRASS", "OLIVE"]:
                        self.tortiecolour = choice (['WHITE', 'PALEGREY', 'SILVER', 'CADET', 'BRONZE', 'TURQUOISE', 'SKY', 
                                                'SHINYMEW', 'PUDDLE', 'TIFFANY', 'PALEBOW', 'PALECREAM', 'SAND', 'CREAM', 'PALEGINGER', 
                                                'WOOD', 'GOLDEN', 'APRICOT', 'CORAL', 'PETAL', 'MEW', 'MAGENTA', 'HEATHER', 'AMYTHYST'] + (Pelt.pride_colours * 2))
                    elif self.colour in ["EMERALD", "DARKOLIVE", "SPINNACH", "GREEN", "SEAWEED", "SACRAMENTO", "SEAGRASS", "JADE"]:
                        self.tortiecolour = choice (['MARENGO', 'GREY', 'BLUEGREY', 'BATTLESHIP', 'STEEL', 'SLATE', 'GINGER', 'GOLD', 
                                                'FIRE', 'GARFIELD', 'DARKGINGER', 'HONEY', 'BRICK', 'ROSE', 'ORCHID', 'FLORAL', 'CHERRY', 
                                                'STRAKIT', 'BUBBLEGUM', 'TART', 'PURPLE', 'POWDERBLUE', 'INDIGOBLUE', 'INDIGOLIGHT', 
                                                'WAVES', 'SAPPHIRE', 'OCEAN', 'TEAL', 'DENIUM', 'COBALT'] + (Pelt.pride_colours * 2))
                    elif self.colour in ["FLUORITE", "FOREST", "SEAFOAM", "FERN", "DEEPOLIVE", "DEEPFOREST", "MALACHITE"]:
                        self.tortiecolour = choice (['XANADU', 'SOOT', 'DARKGREY', 'CHARCOAL', 'ANCHOR', 'COAL', 'GHOST', 'BLACK', 
                                                'PITCH', 'DUSKBOW', 'SIENNA', 'SUNSET', 'APPLE', 'RED', 'RUFOUS', 'CRIMSON', 'CARMINE', 'SCARLET', 
                                                'COSMOS', 'ROSEWOOD', 'BURNT', 'BLOOD', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 'DARKSTRAKIT', 'BARN', 
                                                'GARNET', 'RASIN', 'DARKTEAL', 'SONIC', 'NAVY', 'JEANS', 'JACKET', 'DEEPOCEAN', 'OCEANIC', 'NIGHTTIME'] + (Pelt.pride_colours * 2))
                                
                    elif self.colour == "GLASS":
                        possible_colors = Pelt.pelt_colours.copy()
                        possible_colors.remove(self.pelt.colour)
                        self.tortiecolour = choice(possible_colors)
                    
                    elif self.colour in Pelt.pride_colours:
                        possible_colors = Pelt.pride_colours.copy()
                        possible_colors.remove(self.colour)
                        possible_colors.extend(['STRAKIT', 'DARKSTRAKIT', 'PITCH', 'PALEBOW', 'DUSKBOW'])
                        self.tortiecolour = choice(possible_colors)

            else:
                self.tortiecolour = choice(Pelt.pride_colours)
                
        else:
            self.tortiebase = None
            self.tortiepattern = None
            self.tortiecolour = None
            self.pattern = None

    def white_patches_inheritance(self, parents: tuple):

        par_whitepatches = set()
        for p in parents:
            if p.pelt.white_patches:
                par_whitepatches.add(p.pelt.white_patches)

        if not parents:
            print("Error - no parents. Randomizing white patches.")
            self.randomize_white_patches()
            return

        # Direct inheritance. Will only work if at least one parent has white patches, otherwise continue on.
        if par_whitepatches and not random.randint(0, game.config["cat_generation"]["direct_inheritance"]):
            # This ensures Torties and Calicos won't get direct inheritance of incorrect white patch types
            _temp = par_whitepatches.copy()
            if self.name == "Tortie":
                for p in _temp.copy():
                    if p in Pelt.high_white + Pelt.mostly_white + ["FULLWHITE"]:
                        _temp.remove(p)
            elif self.name == "Calico":
                for p in _temp.copy():
                    if p in Pelt.little_white + Pelt.mid_white:
                        _temp.remove(p)

            # Only proceed with the direct inheritance if there are white patches that match the pelt.
            if _temp:
                self.white_patches = choice(list(_temp))

                return

        white_list = [Pelt.little_white, Pelt.mid_white, Pelt.high_white, Pelt.mostly_white, ['FULLWHITE']]

        weights = [0, 0, 0, 0, 0]  # Same order as white_list
        for p_ in par_whitepatches:
            if p_ in Pelt.little_white:
                add_weights = (40, 20, 15, 5, 0)
            elif p_ in Pelt.mid_white:
                add_weights = (10, 40, 15, 10, 0)
            elif p_ in Pelt.high_white:
                add_weights = (15, 20, 40, 10, 1)
            elif p_ in Pelt.mostly_white:
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
        if self.name == "Tortie":
            weights = weights[:2] + [0, 0, 0]
            # Another check to make sure not all the values are zero. This should never happen, but better
            # safe then sorry.
            if not any(weights):
                weights = [2, 1, 0, 0, 0]
        elif self.name == "Calico":
            weights = [0, 0, 0] + weights[3:]
            # Another check to make sure not all the values are zero. This should never happen, but better
            # safe then sorry.
            if not any(weights):
                weights = [2, 1, 0, 0, 0]

        chosen_white_patches = choice(
            random.choices(white_list, weights=weights, k=1)[0]
        )

        self.white_patches = chosen_white_patches
        if self.points and self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE']:
            self.points = None

    def randomize_white_patches(self):

        # Adjust weights for torties, since they can't have anything greater than mid_white:
        if self.name == "Tortie":
            weights = (2, 1, 0, 0, 0)
        elif self.name == "Calico":
            weights = (0, 0, 20, 15, 1)
        else:
            weights = (10, 10, 10, 10, 1)

        white_list = [Pelt.little_white, Pelt.mid_white, Pelt.high_white, Pelt.mostly_white, ['FULLWHITE']]
        chosen_white_patches = choice(
            random.choices(white_list, weights=weights, k=1)[0]
        )

        self.white_patches = chosen_white_patches
        if self.points and self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE']:
            self.points = None

    def init_white_patches(self, pelt_white, parents:tuple):
        # Vit can roll for anyone, not just cats who rolled to have white in their pelt. 
        par_vit = []
        for p in parents:
            if p:
                if p.pelt.vitiligo:
                    par_vit.append(p.pelt.vitiligo)
        
        vit_chance = max(game.config["cat_generation"]["vit_chance"] - len(par_vit), 0)
        if not random.getrandbits(vit_chance):
            self.vitiligo = choice(Pelt.vit)

        #Moved the Points for my mod. Because no to your restrictions
        par_points = []
        for p in parents:
            if p.pelt.points:
                par_points.append(p.pelt.points)

        if par_points and not random.randint(0, game.config["cat_generation"]["direct_inheritance"]):
            # Direct inheritance WHOO!
            if par_points and self.name != "Tortie":
                self.points = choice(par_points)
            else:
                self.points = None

        if par_points:
            chance = 10 - len(par_points)
        else:
            chance = game.config["cat_generation"]["random_point_chance"]

        if self.name != "Tortie" and not (random.random() * chance):
            self.points = choice(Pelt.point_markings)
        else:
            self.points = None

        # Points determination. Tortie can't be pointed
        if self.name != "Tortie" and not random.getrandbits:
            # Cat has colorpoint!
            self.points = choice(Pelt.point_markings)
        else:
            self.points = None

        # If the cat was rolled previously to have white patches, then determine the patch they will have
        # these functions also handle points. 
        if pelt_white:
            if parents:
                self.white_patches_inheritance(parents)
            else:
                self.randomize_white_patches()
        else:
            self.white_patches = None
            self.points = None

    def init_tint(self):
        """Sets tint for pelt and white patches"""

        # PELT TINT
        # Basic tints as possible for all colors.
        hit = random.randint(0, 20)
        if hit <= 5:
            possible_tints = sprites.cat_tints["possible_tints"]["any"].copy()
            self.tint = choice(possible_tints)  
        elif hit <= 10:      
            if self.colour in [Pelt.black_colours, Pelt.grey_colours, Pelt.white_colours, Pelt.blue_colours]:
                possible_tints = sprites.cat_tints["possible_tints"]["greyscale"].copy()
                self.tint = choice(possible_tints)
            elif self.colour in [Pelt.ginger_colours, Pelt.cream_colours, Pelt.purple_colours]:
                possible_tints = sprites.cat_tints["possible_tints"]["gingerscale"].copy()
                self.tint = choice(possible_tints)
            elif self.colour in [Pelt.brown_colours, Pelt.yellow_colours]:
                possible_tints = sprites.cat_tints["possible_tints"]["brownscale"].copy()
                self.tint = choice(possible_tints)
            elif self.colour in Pelt.green_colours:
                possible_tints = sprites.cat_tints["possible_tints"]["greenscale"].copy()
                self.tint = choice(possible_tints)
            elif self.colour in Pelt.pride_colours:
                self.tint = "none"
        else:
            self.tint = "none"

    # WHITE PATCHES TINT
        if self.white_patches or self.points:
            #Now for white patches
            possible_tints = sprites.white_patches_tints["possible_tints"]["basic"].copy()
            self.white_patches_tint = choice(possible_tints)
        else:
            self.white_patches_tint = "none"

    @property
    def white(self):
        return self.white_patches or self.points
    
    @white.setter
    def white(self, val):
        print("Can't set pelt.white")
        return    

    @staticmethod
    def describe_appearance(cat, short=False):
        
        # Define look-up dictionaries
        if short:
            renamed_colors = {
                "ashbrown": "brown",
                "dustbrown": "brown",
                "darkbrown": "brown",
                "palecream": "cream",
                "bluegrey": "grey",
                "darkgrey": "grey",
                "shinymew": "sky",
                "sonic": "blue",
                "samon": "salmon",
                "darksamon": "salmon",
                "strakit": "purple",
                "darkstrakit": "purple",
                "indigoblue": "indigo",
                "indigolight": "indigo",
                "seagrass": "olive",
                "brightcrimson": "crimson",
                "royalpurple": "purple",
                "seafoam": "green",
                "deepocean": "blue",
                "nighttime": "midnight"
            }
        else:
            renamed_colors = {
                "ashbrown": "ash brown",
                "dustbrown": "dust brown",
                "darkbrown": "dark brown",
                "palecream": "pale cream",
                "bluegrey": "blue-grey",
                "darkgrey": "dark grey",
                "shinymew": "shiny mew",
                "sonic": "sonic blue",
                "samon": "salmon",
                "darksamon": "dark salmon",
                "strakit": "starkit purple",
                "darkstrakit": "dark starkit purple",
                "indigoblue": "indigo blue",
                "indigolight": "light indigo",
                "seagrass": "sea grass green",
                "brightcrimson": "crimson",
                "royalpurple": "royal purple",
                "seafoam": "seafoam green",
                "deepocean": "deep ocean",
                "nighttime": "midnight"
            }

        pattern_des = {
            "Tabby": "c_n tabby",
            "Speckled": "speckled c_n",
            "Bengal": "unusually dappled c_n",
            "Marbled": "c_n tabby",
            "Ticked": "c_n ticked",
            "Smoke": "c_n smoke",
            "Mackerel": "c_n tabby",
            "Classic": "c_n tabby",
            "Agouti": "c_n tabby",
            "Backed": "backed c_n",
            "Rosette": "unusually spotted c_n",
            "Sokoke": "c_n tabby",
            "Masked": "masked c_n tabby"
        }

        # Start with determining the base color name
        color_name = str(cat.pelt.colour).lower()
        if color_name in renamed_colors:
            color_name = renamed_colors[color_name]

        if cat.pelt.albino:
            color_name = "albino"      
        elif cat.pelt.melanistic:
            color_name = "melanistic"  
        
        # Replace "white" with "pale" if the cat is white
        if cat.pelt.name not in ["SingleColour", "TwoColour", "Tortie", "Calico"] and color_name == "white":
            color_name = "pale"

        # Time to descibe the pattern and any additional colors
        if cat.pelt.name in pattern_des:
            color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
        elif cat.pelt.name in Pelt.torties:
            # Calicos and Torties need their own desciptions
            if short:
                # If using short, don't add describe the colors of calicos and torties. Just call them calico, tortie, or mottled
                # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled
                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                    color_name = "mottled"
                else:
                    color_name = cat.pelt.name.lower()
            else:
                base = cat.pelt.tortiebase.lower()
                if base in Pelt.tabbies + ['bengal', 'rosette', 'speckled']:
                    base = 'tabby'
                else:
                    base = ''

                patches_color = cat.pelt.tortiecolour.lower()
                if patches_color in renamed_colors:
                    patches_color = renamed_colors[patches_color]
                color_name = f"{color_name}/{patches_color}"
                
                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                        color_name = f"{color_name} mottled"
                else:
                    color_name = f"{color_name} {cat.pelt.name.lower()}"

        if cat.pelt.white_patches and not cat.pelt.albino and not cat.pelt.melanistic:
            if cat.pelt.white_patches == "FULLWHITE":
                # If the cat is fullwhite, discard all other information. They are just white. 
                if cat.pelt.white_patches_tint != "none":
                    color_name = f"{cat.pelt.white_patches_tint}"
                else:
                    color_name = f"white"
        
        if cat.pelt.points:
            color_name = f"{color_name} point"
            if "ginger point" in color_name:
                color_name.replace("ginger point", "flame point")
                    
        # Here is the place where we can add some additional details about the cat, for the full non-short one. 
        # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars. 
        if not short:

            scar_details = {
                "NOTAIL": "no tail", 
                "HALFTAIL": "half a tail", 
                "NOPAW": "three legs", 
                "NOLEFTEAR": "a missing ear", 
                "NORIGHTEAR": "a missing ear",
                "NOEAR": "no ears"
            }

            additional_details = []
            if cat.pelt.vitiligo:
                additional_details.append("vitiligo")
            for scar in cat.pelt.scars:
                if scar in scar_details and scar_details[scar] not in additional_details:
                    additional_details.append(scar_details[scar])
            
            if len(additional_details) > 1:
                color_name = f"{color_name} with {', '.join(additional_details[:-1])} and {additional_details[-1]}"
            elif additional_details:
                color_name = f"{color_name} with {additional_details[0]}"
        
        
            if len(cat.pelt.scars) >= 3:
                color_name = f"scarred {color_name}"
            if cat.pelt.length == "long":
                color_name = f"long-furred {color_name}"
            if cat.pelt.length == "bare":
                color_name = f"furless {color_name}"
            if cat.pelt.length == "snat":
                color_name = f"slime {color_name}"
            if cat.pelt.length == "wolf":
                color_name = f"canid-furred {color_name}"
            if cat.pelt.length == "skele":
                color_name = f"skeletonized {color_name}"
            if cat.pelt.length == "catfish":
                color_name = f"fishy {color_name}"
            if cat.pelt.length in ["scug", "saint"]:
                color_name = f"{color_name} slugcat"

        # Now it's time for gender
        if cat.genderalign in ["female", "trans female"]:
            color_name = f"{color_name} molly"
        elif cat.genderalign in ["male", "trans male"]:
            color_name = f"{color_name} tom"
        elif cat.pelt.length != ["scug", "saint"] and not short: 
            color_name = f"{color_name} cat"
        else:
            color_name = f"{color_name} cat"        

        if cat.pelt.white_patches and not cat.pelt.albino and not cat.pelt.melanistic:
            if short:
                color_name = f"{color_name} with patches" 
            elif cat.pelt.white_patches in Pelt.high_white + Pelt.mostly_white and cat.pelt.name != "Calico":
                if cat.pelt.white_patches_tint != "none":            
                    color_name = f"{color_name} with patches of {cat.pelt.white_patches_tint}"
                else: 
                    color_name = f"{color_name} with patches of white" 
            elif cat.pelt.white_patches in Pelt.little_white + Pelt.mid_white and cat.pelt.name != "Calico":
                if cat.pelt.white_patches_tint != "none":            
                    color_name = f"{color_name} with small patches of {cat.pelt.white_patches_tint}"
                else: 
                    color_name = f"{color_name} with small patches of white"
               
        return color_name
    
    def get_sprites_name(self):
        return Pelt.sprites_names[self.name]
