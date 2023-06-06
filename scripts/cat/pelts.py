from random import choice
from scripts.cat.sprites import Sprites
import random
from re import sub
from scripts.game_structure.game_essentials import game


class Pelt():
    
    sprites_names = {
        "SingleColour": 'single',
        'TwoColour': 'single',
        'FalseSolid': 'falsesolid',
        'FalseTwo': 'falsesolid',
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
        'Charcoal': 'charcoal',
        'Ghost': 'ghost',
        'Merle': 'merle',
        'Doberman': 'doberman',
        'Snowflake': 'snowflake',
        'Skele': 'skele',
        'Stain': 'stain', 
        'Banded': 'banded',
        'Rat': 'rat',
        'Skitty': 'skitty',
        'Hooded': 'hooded',
        'Ponit': 'ponit',
        'Spirit': 'spirit',
        'Starpelt': 'starpelt',
        'Dalmation': 'dalmation',
        'Leonid': 'leonid',
        'Lynx': 'lynx',
        'SparkleTabby': 'sparkletabby',
        'SparkleSpeckled': 'sparklespeckled',
        'SparkleDalmation': 'sparkledalmation',
        'SparkleLynx': 'sparklelynx',
        'Wolf': 'wolf',
        'WolfBicolour': 'wolf',
        'Tortie': None,
        'Calico': None,
    }
    
    # ATTRIBUTES, including non-pelt related
    pelt_colours = [
        'WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET',
        'PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 
        'MARENGO', 'GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 
        'BATTLESHIP', 'HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 'ASHBROWN', 'SANDALWOOD', 'WRENGE', 
        'STEEL', 'SLATE', 'GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT',
        'CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 'DARKGREY', 'CHARCOAL', 'ANCHOR', 'BURNT', 'BLOOD', 
        'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 'PITCH', 'DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
        'PAN', 'DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 'BISEX', 'GLASS', 'POLY', 'ENBY', 'INTERSEX', 'MLM', 
        'WLW', 'GAYBOW', 'PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 
        'MAGENTA', 'PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 
        'HEATHER', 'AMYTHYST', 'LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 
        'CHERRY', 'SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART',
        'YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 
        'TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 'DEEPOCEAN', 'BARN', 'GARNET', 'DIJON', 'RUST', 'DEEPFOREST', 
        'MALACHITE', 'NIGHTTIME', 'ONYX', 'RASIN', 'DUSKBOW'
    ]
    pelt_c_no_white = [
        'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET',
        'PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 
        'MARENGO', 'GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 
        'BATTLESHIP', 'HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 'ASHBROWN', 'SANDALWOOD', 'WRENGE', 
        'STEEL', 'SLATE', 'GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT',
        'CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 'DARKGREY', 'CHARCOAL', 'ANCHOR', 'BURNT', 'BLOOD', 
        'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 'PITCH', 'DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
        'PAN', 'DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 'BISEX', 'POLY', 'ENBY', 'INTERSEX', 'MLM', 
        'WLW', 'GAYBOW', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 
        'MAGENTA', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 
        'HEATHER', 'AMYTHYST', 'LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 
        'CHERRY', 'SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART',
        'YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 
        'TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 'DEEPOCEAN', 'BARN', 'GARNET', 'DIJON', 'RUST', 'DEEPFOREST', 
        'MALACHITE', 'NIGHTTIME', 'ONYX', 'RASIN', 'DUSKBOW'
    ]
    pelt_c_no_bw = [
        'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET',
        'PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 
        'MARENGO', 'GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 
        'BATTLESHIP', 'HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 'ASHBROWN', 'SANDALWOOD', 'WRENGE', 
        'STEEL', 'SLATE', 'GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT',
        'CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 'DARKGREY', 'CHARCOAL', 'ANCHOR', 'BURNT', 'BLOOD', 
        'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
        'PAN', 'DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 'BISEX', 'POLY', 'ENBY', 'INTERSEX', 'MLM', 
        'WLW', 'GAYBOW', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 
        'MAGENTA', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 
        'HEATHER', 'AMYTHYST', 'LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 
        'CHERRY', 'SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART',
        'YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 
        'TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 'DEEPOCEAN', 'BARN', 'GARNET', 'DIJON', 'RUST', 'DEEPFOREST', 
        'MALACHITE', 'NIGHTTIME'
    ]

    tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'HALF',
                    'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE', 'CHIMERA',
                    'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'SMUDGED', 'DAPPLENIGHT', 'STREAK', 'MASK', 'CHEST', 'ARMTAIL',
                    'COMBO', 'BLENDED', 'SCATTER', 'LIGHT', 'BROKENONE', 'BROKENTWO', 'BROKENTHREE', 'BROKENFOUR', 'GLITCH', 'WAVE', 
                    'STRIPESMASK', 'KOI', 'SKULL', 'LITTLE', 'O', 'TOADSTOOL', 'SPOTSCHAOS', 'FOG', 'SUNSET', 'TAIL', 'MOOSTONE', 
                    'PONITMASK', 'REVPONITMASK', 'ERAPONITMASK', 'FALSESOLID', 'LYNXMASK']
    tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
                'classic', 'sokoke', 'agouti', 'backed', 'charcoal', 'ghost', 'merle', 'doberman', 'skele', 'stain', 
               'banded', 'snowflake', 'rat', 'hooded', 'skitty', 'ponit', 'spirit', 'wolf', 'dalmation', 'leonid',
               'lynx', 'starpelt', 'sparkledalmation', 'sparkletabby', 'sparklespeckled', 'sparklelynx', 'falsesolid']

    pelt_length = ["short", "medium", "long"]

    eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 
    'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 'GREENYELLOW', 
    'BRONZE', 'SILVER', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 
    'GREENYELLOW', 'POPPY', 'CRIMSON', 'RUBY', 'BROWN', 'JADE', 'SKY', 'LILAC', 'BROWNTWO', 'PEANUT', 'GREYTWO', 
    'YELLOWOLIVE', 'SUNSHINE', 'AZURE', 'COBOLT', 'GRASS', 'MINT', 'LILACGREY', 'WHITE', 'VIOLET', 'GRAPE', 'INDIGO', 
    'PRIMARY', 'PRIMARYB', 'PRIMARYC', 'CHROME', 'CHROMEB', 'CHROMEC', 'RGB', 'RGBTWO', 'RGBTHREE', 'MONOCHROME', 
    'MONOCHROMETWO', 'MONOCHROMETHREE', 'POPPYPINK', 'STRAWBERRY', 'MINTCHOC', 'CHOCMINT', 'AMBERTWO', 'BEACH', 
    'NACRE', 'NIGHT', 'OCEAN']
    yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'BRONZE', 'GOLD', 'COPPER', 'GREENYELLOW', 'BROWN', 'BROWNTWO', 
                    'PEANUT', 'YELLOWOLIVE', 'SUNSHINE', 'AMBERTWO', 'BEACH']
    blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'COBALT', 'SUNLITICE', 'AZURE', 
                    'COBOLT', 'OCEAN']
    green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL', 'JADE', 'GRASS', 'MINT',
        'MINTCHOC', 'CHOCMINT']
    mono_eyes = ['GREY', 'SILVER', 'VOID', 'GHOST', 'GREYTWO', 'LILACGREY', 'WHITE', 'MONOCHROME', 
        'MONOCHROMETWO', 'MONOCHROMETHREE', 'NACRE', 'NIGHT']
    purple_eyes = ['POPPY', 'CRIMSON', 'RUBY', 'LILAC', 'VIOLET', 'GRAPE', 'INDIGO', 
        'POPPYPINK', 'STRAWBERRY']
    chromatic_eyes = ['PRIMARY', 'PRIMARYB', 'PRIMARYC', 'CHROME', 'CHROMEB', 'CHROMEC', 'RGB', 
        'RGBTWO', 'RGBTHREE',]
    sus_yellow = ['SUSYELLOW', 'SUSAMBER', 'SUSGOLDGREEN', 'SUSBRIGHT', 'SUSGOLD', 'SUSYELLOWGREEN', 'SUSRUSSET', 
        'SUSPEANUT', 'SUSBROWN', 'SUSBROWNTWO']
    sus_blue = ['SUSINDIGO', 'SUSBLUE', 'SUSBLUETWO', 'SUSCOBOLT', 'SUSTURQUOISE', 'SUSSKY', 'SUSOCEAN',
        'SUSBEACH']
    sus_green = ['SUSMINTCHOC', 'SUSCHOCMINT', 'SUSGREEN', 'SUSEMERALD', 'SUSJADE', 'SUSOLIVE', 
        'SUSGREENYELLOW']
    sus_mono = ['SUSVISOR', 'SUSGREY', 'SUSGREENGREY', 'SUSOLIVEGREY', 'SUSBROWNGREY', 'SUSBLUEGREY', 
        'SUSPURPLEGREY', 'SUSWHITE', 'SUSBLACK']
    sus_purple = ['SUSPOPPY', 'SUSCRIMSON', 'SUSSCARLET', 'SUSGRAPE', 'SUSVIOLET', 'SUSSTRAWBERRY', 'SUSPINK',
        'SUSMELON', 'SUSRUBEN']
    sus_chrome = ['SUSDARKCHROME',  'SUSNACRE', 'SUSNIGHT', 'SUSCHROME', 'SUSRGB']
    sus_eyes = ['SUSVISOR', 'SUSGREY', 'SUSGREENGREY', 'SUSOLIVEGREY', 'SUSBROWNGREY', 'SUSBLUEGREY', 
        'SUSPURPLEGREY', 'SUSDARKCHROME', 'SUSNACRE', 'SUSNIGHT', 'SUSCHROME', 'SUSRGB', 'SUSYELLOW', 'SUSAMBER', 'SUSGOLDGREEN', 
        'SUSBRIGHT', 'SUSMINTCHOC', 'SUSCHOCMINT', 'SUSGREEN', 'SUSEMERALD', 'SUSJADE', 'SUSOLIVE', 'SUSGOLD', 'SUSRUSSET', 
        'SUSPOPPY', 'SUSCRIMSON', 'SUSSCARLET', 'SUSGRAPE', 'SUSVIOLET', 'SUSSTRAWBERRY', 'SUSPINK',
        'SUSINDIGO', 'SUSBLUE', 'SUSBLUETWO', 'SUSCOBOLT', 'SUSTURQUOISE', 'SUSSKY', 'SUSOCEAN', 'SUSYELLOWGREEN', 
        'SUSWHITE', 'SUSBLACK', 'SUSMELON', 'SUSBEACH', 'SUSGREENYELLOW', 'SUSPEANUT', 'SUSBROWN', 'SUSBROWNTWO', 'SUSRUBEN']
    # scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
    # bite scars by @wood pank on discord
    scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
            "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH"]
    scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
    scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
            "FROSTSOCK", "RASH", "DECLAWED"]

    # make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
    plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                         "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                         "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
                         ]
    wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS",
                        "RAT BLACK", "RAT BROWN", "RAT CREAM", "RAT WHITE", "RAT GREY", "RAT HOODED"]
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
        "CRIMSONHAT", "BLUEHAT", "YELLOWHAT", "CYANHAT", "REDHAT", "LIMEHAT", "GREENHAT", "RAINBOWHAT", 
        "BLACKHAT", "WHITEHAT", "PINKHAT", "PURPLEHAT", "MULTIHAT", "INDIGOHAT", "CRIMSONBOOT", "BLUEBOOT", 
        "YELLOWBOOT", "CYANBOOT", "REDBOOT", "LIMEBOOT", "GREENBOOT", "RAINBOWBOOT", "BLACKBOOT", "SPIKESBOOT", 
        "WHITEBOOT", "PINKBOOT", "PURPLEBOOT", "MULTIBOOT", "INDIGOBOOT"
    ]

    tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti"]
    spotted = ["Speckled", "Rosette", "Snowflake", "Banded", "Dalmation"]
    plain = ["SingleColour", "TwoColour", "Smoke",  "Backed", "Ghost", "Doberman", 
            "Skitty", "Rat", "Wolf", "WolfBicolour", "FalseSolid", "FalseTwo"]
    exotic = ["Bengal", "Marbled", "Skele", "Stain", "Charcoal", "Hooded", "Ponit", "Lynx", "Leonid"]
    sparkle_cats = ["Spirit", "Starpelt", "SparkleTabby", "SparkleSpeckled", "SparkleDalmation",
            "SparkleLynx"]
    torties = ["Tortie", "Calico"]
    pelt_categories = [tabbies, spotted, plain, exotic, sparkle_cats, torties]

    # SPRITE NAMES
    pride_colours = ['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
        'PAN', 'DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 'BISEX', 
        'POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']
    single_colours = [
        'WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET',
        'PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 
        'MARENGO', 'GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 
        'BATTLESHIP', 'HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 'ASHBROWN', 'SANDALWOOD', 'WRENGE', 
        'STEEL', 'SLATE', 'GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT',
        'CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 'DARKGREY', 'CHARCOAL', 'ANCHOR', 'BURNT', 'BLOOD', 
        'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 'PITCH', 'DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
        'PAN', 'DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 'BISEX', 'GLASS', 'POLY', 'ENBY', 'INTERSEX', 'MLM', 
        'WLW', 'GAYBOW', 'PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 
        'MAGENTA', 'PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 
        'HEATHER', 'AMYTHYST', 'LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 
        'CHERRY', 'SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART',
        'YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 
        'TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 'DEEPOCEAN', 'BARN', 'GARNET', 'DIJON', 'RUST', 'DEEPFOREST', 
        'MALACHITE', 'NIGHTTIME', 'ONYX', 'RASIN', 'DUSKBOW'
    ]
    cream_colours = ['BANNANA', 'PALECREAM', 'SAND', 'FARROW', 'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 
        'PANTONE', 'SAMON', 'THISTLE', 'WOOD']
    ginger_colours = ['APRICOT', 'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 
        'ROSE', 'DARKSAMON',  'APPLE', 'RED', 'CRIMSON', 'CARMINE', 'SCARLET', 'COSMOS', 'ROSEWOOD',
        'BURNT', 'BLOOD', 'FLORAL', 'CHERRY', 'TART', 'WINE', 'BRIGHTCRIMSON', 'BARN', 'GARNET']
    black_colours = ['SOOT', 'CHARCOAL', 'ANCHOR', 'COAL', 'BLACK', 'PITCH', 'ONYX', 'RASIN', 'DUSKBOW']
    grey_colours = ['MARENGO', 'GREY', 'STEEL', 'SLATE', 'BLUEGREY', 'BATTLESHIP','XANADU', 'DARKGREY']
    white_colours = ['WHITE', 'SILVER', 'CADET', 'BRONZE', 'PALEBOW', 'PETAL', 'IVORY', 'GLASS']
    brown_colours = ['HAZELNUT', 'CAPPUCCINO', 'ECRU', 'PINECONE', 'TAN', 'MEDALLION', 'DUSTBROWN', 
        'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'GRANOLA', 'SADDLE', 'MINK', 'BROWN', 'CHESTNUT', 'BEAVER', 
        'CEDAR', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER', 'BRASS', 'DIJON', 'RUST']
    blue_colours = ['TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'SHINYMEW', 'PUDDLE', 'TIFFANY', 
        'INDIGOLIGHT', 'SAPPHIRE', 'OCEAN', 'ORCHID', 'TEAL', 'DENIUM', 'COBALT', 'SONIC', 'NAVY',
        'JEANS', 'JACKET', 'DEEPOCEAN', 'NIGHTTIME']
    yellow_colours = ['GOLD', 'HONEY', 'LEMON', 'LAGUNA', 'FAWN', 'CORN', 'SUNSHINE', 'BEE', 'PYRITE',
        'YELLOW', 'PINEAPPLE','TROMBONE']
    purple_colours = ['CORAL', 'MEW', 'HEATHER', 'AMYTHYST', 'STRAKIT', 'PURPLE', 'ROYALPURPLE']
    green_colours = ['CHARTRUSE', 'MINT', 'EMERALD', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'DARKOLIVE', 
        'SPINNACH', 'GREEN', 'SEAWEED', 'SACRAMENTO', 'SEAGRASS', 'JADE', 'FOREST', 'SEAFOAM',
        'DEEPFOREST', 'MALACHITE']
    colour_categories = [cream_colours, ginger_colours, black_colours, grey_colours, white_colours, brown_colours, blue_colours, 
    yellow_colours, purple_colours, green_colours, pride_colours]    

    eye_sprites = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
        'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT',
        'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER', 'POPPY', 'CRIMSON', 'RUBY', 'BROWN', 'JADE', 'SKY', 
        'LILAC', 'BROWNTWO', 'PEANUT', 'GREYTWO', 'YELLOWOLIVE', 'SUNSHINE', 'AZURE', 'COBOLT', 'GRASS', 'MINT', 
        'LILACGREY', 'WHITE', 'VIOLET', 'GRAPE', 'INDIGO', 'VOID', 'GHOST', 'PRIMARY', 'PRIMARYB', 'PRIMARYC', 
        'CHROME', 'CHROMEB', 'CHROMEC','RBG', 'RBGTWO', 'RBGTHREE', 'MONOCHROME', 'MONOCHROMETWO', 'MONOCHROMETHREE', 
        'POPPYPINK', 'STRAWBERRY', 'MINTCHOC', 'CHOCMINT', 'AMBERTWO', 'BEACH', 'NACRE', 'NIGHT', 'OCEAN']
    little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'LUNA',
                    'EXTRA']
    mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR',
                'WINGS', 'DIVA', 'SAVANNAH', 'FADESPOTS', 'BEARD', 'DAPPLEPAW', 'TOPCOVER']
    high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
                'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
                'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED', 'SHIBAINU']
    mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                    'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO']
    point_markings = ['COLOURPOINT', 'RAGDOLL', 'KARPATI', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT', 'REVERSEPOINT', 'PONIT', 
    'LIGHTPOINT', 'SNOWSHOE', 'SNOWBOOT']
    vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'POWDER', 'BLEACHED', 'SHADOWSIGHT', 'BLACKVIT', 'BLACKVITTWO', 
    'BLACKMOON', 'BLACKPHANTOM', 'BLACKPOWDER', 'BLACKENED', 'BLACKSIGHT']
    white_sprites = [
        little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

    skin_sprites = ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE', 'BLACKMANE', 'REDMANE', 
                'PINKMANE', 'DARKBROWNMANE', 'BROWNMANE', 'LIGHTBROWNMANE', 'DARKMANE', 'DARKGREYMANE', 'GREYMANE', 'DARKSALMONMANE', 
                'SALMONMANE', 'PEACHMANE', 'DARKMARBLEDMANE', 'MARBLEDMANE', 'LIGHTMARBLEDMANE', 'DARKBLUEMANE', 'BLUEMANE', 'LIGHTBLUEMANE']
    albino_sprites = ['ALBINO', 'ALBINOWING', 'ALBINOMANE']
    melanistic_sprites = ['MELANISTIC', 'MELANISTICWING', 'MELANISTICMANE'] 
    wing_sprites = ['WHITEWING', 'BLUEGREENWING', 'REDWING', 'PURPLEFADEWING', 'RAINBOWWING', 'SILVERWING',
                    'STRAKITWING', 'SONICWING', 'MEWWING', 'OLIVEWING', 'GREENWING', 'GREYWING', 'GREYFADEWING',
                    'BROWNFADEWING', 'PARROTWING', 'GOLDWING', 'LIGHTBROWNWING', 'BLACKWING']
    skin_categories = [skin_sprites, wing_sprites]
    sphynx = ['S_BLACK', 'S_RED', 'S_PINK', 'S_DARKBROWN', 'S_BROWN', 'S_LIGHTBROWN', 'S_DARK', 'S_DARKGREY', 'S_GREY', 'S_DARKSALMON',
                'S_SALMON', 'S_PEACH', 'S_DARKMARBLED', 'S_MARBLED', 'S_LIGHTMARBLED', 'S_DARKBLUE', 'S_BLUE', 'S_LIGHTBLUE', 
                'ALBINOSPHYNX', 'MELANISTICSPHYNX']
    wings = ['WHITEWING', 'BLUEGREENWING', 'REDWING', 'PURPLEFADEWING', 'RAINBOWWING', 'SILVERWING',
                'STRAKITWING', 'SONICWING', 'MEWWING', 'OLIVEWING', 'GREENWING', 'GREYWING', 'GREYFADEWING',
                'BROWNFADEWING', 'PARROTWING', 'GOLDWING', 'LIGHTBROWNWING', 'BLACKWING', 'ALBINOWING', 'MELANISTICWING']
    """Holds all apperence information for a cat. """
        
    def __init__(self,
                 name:str="SingleColour",
                 length:str="short",
                 colour:str="WHITE",
                 white_patches:str=None,
                 eye_color:str="BLUE",
                 eye_colour2:str=None,
                 tortiebase:str=None,
                 tortiecolour:str=None,
                 pattern:str=None,
                 tortiepattern:str=None,
                 vitiligo:str=None,
                 points:str=None,
                 accessory:str=None,
                 paralyzed:bool=False,
                 opacity:int=100,
                 scars:list=None,
                 tint:str="none",
                 skin:str="BLACK",
                 white_patches_tint:str="none",
                 kitten_sprite:int=None,
                 adol_sprite:int=None,
                 adult_sprite:int=None,
                 senior_sprite:int=None,
                 para_adult_sprite:int=None,
                 reverse:bool=False,
                 ) -> None:
        self.name = name
        self.colour = colour
        self.white_patches = white_patches
        self.eye_colour = eye_color
        self.eye_colour2 = eye_colour2
        self.tortiebase = tortiebase
        self.pattern = pattern
        self.tortiepattern = tortiepattern
        self.tortiecolour = tortiecolour
        self.vitiligo = vitiligo
        self.length=length
        self.points = points
        self.accessory = accessory
        self.paralyzed = paralyzed
        self.opacity = opacity
        self.scars = scars if isinstance(scars, list) else []
        self.tint = tint
        self.white_patches_tint = white_patches_tint
        self.cat_sprites =  {
            "kitten": kitten_sprite if kitten_sprite is not None else 0,
            "adolescent": adol_sprite if adol_sprite is not None else 0,
            "young adult": adult_sprite if adult_sprite is not None else 0,
            "adult": adult_sprite if adult_sprite is not None else 0,
            "senior adult": adult_sprite if adult_sprite is not None else 0,
            "senior": senior_sprite if senior_sprite is not None else 0,
            "para_adult": para_adult_sprite if para_adult_sprite is not None else 0,
        }        
        self.cat_sprites['newborn'] = 20
        self.cat_sprites['para_young'] = 17
        self.cat_sprites["sick_adult"] = 18
        self.cat_sprites["sick_young"] = 19
        
        self.reverse = reverse
        self.skin = skin

    @staticmethod
    def generate_new_pelt(gender:str, parents:tuple=(), age:str="adult"):
        new_pelt = Pelt()
        
        pelt_white = new_pelt.init_pattern_color(parents, gender)
        new_pelt.init_white_patches(pelt_white, parents)
        new_pelt.init_sprite()
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
        
        if self.length == 'long':
            if self.cat_sprites['adult'] not in [9, 10, 11]:
                if self.cat_sprites['adult'] == 0:
                    self.cat_sprites['adult'] = 9
                elif self.cat_sprites['adult'] == 1:
                    self.cat_sprites['adult'] = 10
                elif self.cat_sprites['adult'] == 2:
                    self.cat_sprites['adult'] = 11
                self.cat_sprites['young adult'] = self.cat_sprites['adult']
                self.cat_sprites['senior adult'] = self.cat_sprites['adult']
                self.cat_sprites['para_adult'] = 16
        else:
            self.cat_sprites['para_adult'] = 15
        if self.cat_sprites['senior'] not in [12, 13, 14]:
            if self.cat_sprites['senior'] == 3:
                self.cat_sprites['senior'] = 12
            elif self.cat_sprites['senior'] == 4:
                self.cat_sprites['senior'] = 13
            elif self.cat_sprites['senior'] == 5:
                self.cat_sprites['senior'] = 14
        
        if self.pattern in convert_dict["old_tortie_patches"]:
            self.pattern = convert_dict["old_tortie_patches"][self.pattern][1]
            # If the pattern is old, there is also a change the base color is stored in
            # tortiecolour, and that may be different from the pelt color (main for torties
            # generated before the "ginger-on-ginger" update. If it was generated after that update,
            # tortiecolour and pelt_colour will be the same. Therefore, lets also re-set the pelt color
            self.colour = self.tortiecolour
            self.tortiecolour = convert_dict["old_tortie_patches"][self.pattern][0]
            
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
            self.eye_colours = choice([i.pelt.eye_colour for i in parents] + [choice(Pelt.eye_colours)])
        
        #White patches must be initalized before eye color. 
        num = game.config["cat_generation"]["base_heterochromia"]
        if self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE'] or self.colour == 'WHITE':
            num = num - 90
        if self.white_patches == 'FULLWHITE' or self.colour == 'WHITE':
            num -= 10
        for _par in parents:
            if _par.pelt.eye_colour2:
                num -= 10
        
        if num < 0:
            num = 1
            
        if not random.randint(0, num):
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
            elif self.eye_colour in Pelt.sus_yellow:
                eye_choice = choice([Pelt.sus_blue, Pelt.sus_green, Pelt.sus_purple, Pelt.sus_mono, Pelt.sus_chrome])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.sus_blue:
                eye_choice = choice([Pelt.sus_yellow, Pelt.sus_green, Pelt.sus_purple, Pelt.sus_mono, Pelt.sus_chrome])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.sus_green:
                eye_choice = choice([Pelt.sus_yellow, Pelt.sus_blue, Pelt.sus_purple, Pelt.sus_mono, Pelt.sus_chrome])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.sus_purple:
                eye_choice = choice([Pelt.sus_yellow, Pelt.sus_blue, Pelt.sus_green, Pelt.sus_mono, Pelt.sus_chrome])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.sus_mono:
                eye_choice = choice([Pelt.sus_yellow, Pelt.sus_blue, Pelt.sus_green, Pelt.sus_purple, Pelt.sus_chrome])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.sus_chrome:
                eye_choice = choice([Pelt.sus_yellow, Pelt.sus_blue, Pelt.sus_green, Pelt.sus_purple, Pelt.sus_mono])
                self.eye_colour2 = choice(eye_choice)

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
                add_weight = (50, 10, 5, 7, 1)
            elif p_ in Pelt.spotted:
                add_weight = (10, 50, 5, 5, 1)
            elif p_ in Pelt.plain:
                add_weight = (5, 5, 50, 2, 0)
            elif p_ in Pelt.exotic:
                add_weight = (15, 15, 1, 45, 1)
            elif p_ in Pelt.sparkle_cats:
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
            random.choices(Pelt.pelt_categories, weights=weights + [0], k = 1)[0]
        )

        # Tortie chance
        tortie_chance_f = game.config["cat_generation"]["base_female_tortie"]  # There is a default chance for female tortie
        tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
        for p_ in par_pelts:
            if p_.name in Pelt.torties:
                tortie_chance_f = int(tortie_chance_f / 2)
                tortie_chance_m = tortie_chance_m - 1
                break

        # Determine tortie:
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
            if chosen_tortie_base in ["FalseSolid", "FalseTwo"]:
                chosen_tortie_base = "FalseSolid"
            if chosen_tortie_base in ["Wolf", "WolfBicolour"]:
                chosen_tortie_base = "Wolf" 
            chosen_tortie_base = chosen_tortie_base.lower()
            chosen_pelt = random.choice(Pelt.torties)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT COLOUR
        # ------------------------------------------------------------------------------------------------------------#
        # Weights for each colour group. It goes: (ginger_colours, black_colours, white_colours, brown_colours)
        weights = [0, 0, 0, 0]
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
        elif chosen_pelt in ["FalseTwo", "FalseSolid"]:
            if chosen_white:
                chosen_pelt = "FalseTwo"
            else:
                chosen_pelt = "FalseSolid"   
        elif chosen_pelt in ["Wolf", "WolfBicolour"]:
            if chosen_white:
                chosen_pelt = "WolfBicolour"
            else:
                chosen_pelt = "Wolf" 
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
            random.choices(Pelt.pelt_categories, weights=(35, 20, 30, 15, 1, 0), k=1)[0]
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
            if chosen_tortie_base in ["FalseSolid", "FalseTwo"]:
                chosen_tortie_base = "FalseSolid"
            if chosen_tortie_base in ["Wolf", "WolfBicolour"]:
                chosen_tortie_base = "Wolf" 
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


        chosen_pelt_length = random.choice(Pelt.pelt_length)

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
        elif chosen_pelt in ["Wolf", "WolfBicolour"]:
            if chosen_white:
                chosen_pelt = "WolfBicolour"
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
            'newborn': 20,
            'kitten': random.randint(0, 2),
            'adolescent': random.randint(3, 5),
            'senior': random.randint(12, 14),
            'sick_young': 19,
            'sick_adult': 18
        }
        self.reverse = choice([True, False])
                
        if self.length != 'long':
            self.cat_sprites['adult'] = random.randint(6, 8)
            self.cat_sprites['para_adult'] = 16
        else:
            self.cat_sprites['adult'] = random.randint(9, 11)
            self.cat_sprites['para_adult'] = 15
        self.cat_sprites['young adult'] = self.cat_sprites['adult']
        self.cat_sprites['senior adult'] = self.cat_sprites['adult']

    def init_skin(self, parents):

        # skin chances
        if not parents:
            self.skin = choice(random.choices(Pelt.skin_categories, weights=(298, 2), k=1) [0])
        else:
            for _par in parents:
                if _par.pelt.skin in Pelt.albino_sprites + Pelt.melanistic_sprites + Pelt.sphynx:
                    _par.pelt.skin = choice(Pelt.skin_sprites)
            self.skin = choice([i.pelt.skin for i in parents] + [choice(random.choices(Pelt.skin_categories, weights=(197, 3), k=1)[0])])

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
                    if self.tortiebase in ["backed", "smoke", "single", "ghost", "falsesolid"]:
                        self.tortiepattern = choice(['backed', 'smoke', 'single', 'ghost', 'rat', 
                                        'snowflake', 'wolf', 'spirit', 'falsesolid'])
                    elif self.tortiebase in ["speckled", "banded"]:
                        self.tortiepattern = choice(['speckled', 'banded'])
                    elif self.tortiebase in ["charcoal", "hooded"]:
                        self.tortiepattern = choice(['charcoal', 'hooded', 'spirit'])    
                    elif self.tortiebase == "ponit":
                        self.tortiepattern = 'ponit' 
                    elif self.tortiebase == "spirit":
                        self.tortiepattern = random.choices([self.tortiebase, 'wolf', 'single', 'skele', 'ponit'], weights=[75, 15, 10, 4, 1], k=1)[0]
                    else:
                        self.tortiepattern = random.choices([self.tortiebase, 'ghost', 'rat', 'skele', 'spirit'], weights=[93, 3, 3, 1, 1], k=1)[0]

                    # Ginger is often dupliselfed to increase its chances
                    if self.pelt.colour in ["WHITE", "SILVER", "BRONZE", "CADET", "PALEBOW", "TURQUOISE", "TIFFANY", 
                                                "SHINYMEW", "SKY", "POWDERBLUE", "PUDDLE"]:
                        self.tortiecolour = choice([ 'PALECREAM', 'CREAM', 'SAND', 'WOOD', 'PANTONE', 'SAMON', 'THISTLE', 'PETAL', 
                                                    'MEW', 'CORAL', 'FLORAL', 'LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 
                                                    'EMERALD', 'OLIVE'] + (Pelt.pride_colours * 2))
                    elif self.pelt.colour in ["GREY", "MARENGO", "BATTLESHIP", "BLUEGREY", "STEEL", "SLATE", "SAPPHIRE", "OCEAN", 
                                                "DENIUM", "TEAL", "COBALT", "INDIGOBLUE", "INDIGOLIGHT"]:
                        self.tortiecolour = choice(['ROSE', 'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'APRICOT', 'GARFIELD', 
                                                    'APPLE', 'DARKSAMON', 'AMYTHYST', 'MAGENTA', 'HEATHER', 'ORCHID', 'PURPLE', 
                                                    'CHERRY', 'TART', 'DARKOLIVE', 'GREEN', 'SPINNACH', 'SEAWEED', 'SACRAMENTO', 
                                                    'SEAGRASS'] + (Pelt.pride_colours * 2))
                    elif self.pelt.colour in ["SOOT", "DARKGREY", "ANCHOR", "CHARCOAL", "COAL", "BLACK", "PITCH", "DUSKBOW", "SONIC", 
                                                "JEANS", "NAVY", "JACKET", "DEEPOCEAN", "NIGHTTIME"]:
                        self.tortiecolour = choice(['SCARLET', 'RED', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 
                                                    'RASIN', 'STRAKIT', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 'BARN', 'GARNET',
                                                    'FOREST', 'JADE', 'DEEPFOREST', 'SEAFOAM', 'MALACHITE'] + (Pelt.pride_colours * 2))
                    
                    elif self.pelt.colour in ["PALECREAM", "CREAM", "SAND", "WOOD", "PANTONE", "SAMON", "THISTLE", "PETAL", "MEW", 
                                                "CORAL", "FLORAL"]:
                        self.tortiecolour = choice(['WHITE', 'SILVER', 'BRONZE', 'CADET', 'PALEBOW',  'TURQUOISE', 'TIFFANY', 
                                                    'SHINYMEW', 'SKY', 'POWDERBLUE', 'PUDDLE', 'LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 
                                                    'MINT', 'EMERALD', 'OLIVE'] + (Pelt.pride_colours * 2))
                    elif self.pelt.colour in ["ROSE", "GINGER", "SUNSET", "RUFOUS", "FIRE", "BRICK", "APRICOT", "GARFIELD", "APPLE", 
                                                "DARKSAMON", "AMYTHYST", "MAGENTA", "HEATHER", "ORCHID", "PURPLE", "CHERRY", "TART"]:
                        self.tortiecolour = choice(['GREY', 'MARENGO', 'BATTLESHIP', 'BLUEGREY', 'STEEL', 'SLATE', 'SAPPHIRE', 'OCEAN', 
                                                    'DENIUM', 'TEAL', 'COBALT', 'INDIGOBLUE', 'INDIGOLIGHT', 'DARKOLIVE', 'GREEN', 
                                                    'SPINNACH', 'SEAWEED', 'SACRAMENTO', 'SEAGRASS'] + (Pelt.pride_colours * 2))
                    elif self.pelt.colour in ["SCARLET", "RED", "CRIMSON", "BURNT", "CARMINE", "COSMOS", "ROSEWOOD", "BLOOD", 
                                                "RASIN", "STRAKIT", "WINE", "BRIGHTCRIMSON", "ROYALPURPLE", "BARN", "GARNET"]:                   
                        self.tortiecolour = choice(['SOOT', 'DARKGREY', 'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'PITCH', 'DUSKBOW', 
                                                    'SONIC', 'JEANS', 'NAVY', 'JACKET', 'DEEPOCEAN', 'NIGHTTIME', 'FOREST', 'JADE', 
                                                    'DEEPFOREST', 'SEAFOAM', 'MALACHITE'] + (Pelt.pride_colours * 2))

                    elif self.pelt.colour in ["BEIGE", "MEERKAT", "KHAKI", "BANNANA", "FARROW", "HAY", "GOLD", "HONEY", "IVORY", "LEMON", 
                                                "LAGUNA", "FAWN"]:
                        self.tortiecolour = choice(['WHITE', 'SILVER', 'BRONZE', 'CADET', 'PALEBOW',  'TURQUOISE', 'TIFFANY', 'SHINYMEW', 'SKY', 
                                                    'POWDERBLUE', 'PUDDLE', 'PALECREAM', 'CREAM', 'SAND', 'WOOD', 'PANTONE', 'SAMON', 'THISTLE', 
                                                    'PETAL', 'MEW', 'CORAL', 'FLORAL', 'LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 
                                                    'EMERALD', 'OLIVE'] + (Pelt.pride_colours * 2))
                    elif self.pelt.colour in ["CAPPUCCINO", "ECRU", "ASHBROWN", "DUSTBROWN", "SANDALWOOD", "PINECONE", "WRENGE", "BROWN", 
                                                "MINK", "CHESTNUT", "TAN", "HAZELNUT", "MEDALLION", "SUNSHINE", "YELLOW", "CORN", "BEE", "PYRITE"]:
                        self.tortiecolour = choice(['GREY', 'MARENGO', 'BATTLESHIP', 'BLUEGREY', 'STEEL', 'SLATE', 'SAPPHIRE', 'OCEAN', 
                                                    'DENIUM', 'TEAL', 'COBALT', 'INDIGOBLUE', 'INDIGOLIGHT','ROSE', 'GINGER', 'SUNSET', 
                                                    'RUFOUS', 'FIRE', 'BRICK', 'APRICOT', 'GARFIELD', 'APPLE', 'DARKSAMON', 'AMYTHYST', 
                                                    'MAGENTA', 'HEATHER', 'ORCHID', 'PURPLE', 'CHERRY', 'TART', 'DARKOLIVE', 'GREEN', 
                                                    'SPINNACH', 'SEAWEED', 'SACRAMENTO', 'SEAGRASS'] + (Pelt.pride_colours * 2))
                    elif self.pelt.colour in ["DARKBROWN", "BEAVER", "CHOCOLATE", "MOCHA", "COFFEE", "TAUPE", "UMBER", "SADDLE", "CEDAR", 
                                                "ONYX", "PINEAPPLE", "TROMBONE", "BRASS", "GRANOLA", "DIJON", "RUST"]:
                        self.tortiecolour = choice(['SOOT', 'DARKGREY', 'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'PITCH', 'DUSKBOW', 'SONIC', 
                                                    'JEANS', 'NAVY', 'JACKET', 'DEEPOCEAN', 'NIGHTTIME', 'SCARLET', 'RED', 'CRIMSON', 'BURNT', 
                                                    'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 'RASIN', 'STRAKIT', 'WINE', 'BRIGHTCRIMSON', 
                                                    'ROYALPURPLE', 'BARN', 'GARNET', 'FOREST', 'JADE', 'DEEPFOREST', 
                                                    'SEAFOAM', 'MALACHITE'] + (Pelt.pride_colours * 2))

                    elif self.pelt.colour in ["LIME", "CHARTRUSE", "LETTUCE", "GRASS", "MINT", "EMERALD", "OLIVE"]:
                        self.tortiecolour = choice (['WHITE', 'SILVER', 'BRONZE', 'CADET', 'PALEBOW',  'TURQUOISE', 'TIFFANY', 'SHINYMEW', 'SKY', 
                                                    'POWDERBLUE', 'PUDDLE','PALECREAM', 'CREAM', 'SAND', 'WOOD', 'PANTONE', 'SAMON', 'THISTLE', 
                                                    'PETAL', 'MEW', 'CORAL', 'FLORAL'] + (Pelt.pride_colours * 2))
                    elif self.pelt.colour in ["DARKOLIVE", "GREEN", "SPINNACH", "SEAWEED", "SACRAMENTO", "SEAGRASS"]:
                        self.tortiecolour = choice (['GREY', 'MARENGO', 'BATTLESHIP', 'BLUEGREY', 'STEEL', 'SLATE', 'SAPPHIRE', 'OCEAN', 'DENIUM', 
                                                    'TEAL', 'COBALT', 'INDIGOBLUE', 'INDIGOLIGHT', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS', 
                                                    'FIRE', 'BRICK', 'APRICOT', 'GARFIELD', 'APPLE', 'DARKSAMON', 'AMYTHYST', 'MAGENTA', 'HEATHER', 
                                                    'ORCHID', 'PURPLE', 'CHERRY', 'TART'] + (Pelt.pride_colours * 2))
                    elif self.pelt.colour in ["FOREST", "JADE", "DEEPFOREST", "SEAFOAM", "MALACHITE"]:
                        self.tortiecolour = choice (['SOOT', 'DARKGREY', 'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'PITCH', 'DUSKBOW', 'SONIC', 'JEANS', 
                                                    'NAVY', 'JACKET', 'DEEPOCEAN', 'NIGHTTIME', 'SCARLET', 'RED', 'CRIMSON', 'BURNT', 'CARMINE', 
                                                    'COSMOS', 'ROSEWOOD', 'BLOOD', 'RASIN', 'STRAKIT', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE', 'BARN', 
                                                    'GARNET'] + (Pelt.pride_colours * 2))
                                
                    elif self.pelt.colour == "GLASS":
                        possible_colors = Pelt.pelt_colours.copy()
                        possible_colors.remove(self.pelt.colour)
                        self.tortiecolour = choice(possible_colors)
                    
                    elif self.pelt.colour in Pelt.pride_colours:
                        possible_colors = Pelt.pride_colours.copy()
                        possible_colors.remove(self.pelt.colour)
                        possible_colors.extend(['STRAKIT', 'PITCH', 'PALEBOW', 'DUSKBOW'])
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
        par_points = []
        for p in parents:
            if p:
                if p.pelt.white_patches:
                    par_whitepatches.add(p.pelt.white_patches)
                if p.pelt.points:
                    par_points.append(p.pelt.points)

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

                # Direct inheritance also effect the point marking.
                if par_points and self.name != "Tortie":
                    self.points = choice(par_points)
                else:
                    self.points = None

                return

        # dealing with points
        if par_points:
            chance = 10 - len(par_points)
        else:
            chance = 40

        if self.name != "Tortie" and not (random.random() * chance):
            self.points = choice(Pelt.point_markings)
        else:
            self.points = None


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
        elif self.name in ["Ponit", "Spirit", "Starpelt"] or self.tortiebase in ["Ponit", "Spirit", "Starpelt"]:
            weights = [2, 1, 0, 0, 0]
            if not any(weights):
                weights = [2, 1, 0, 0, 0]

        chosen_white_patches = choice(
            random.choices(white_list, weights=weights, k=1)[0]
        )

        self.white_patches = chosen_white_patches
        if self.points and self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE']:
            self.points = None

    def randomize_white_patches(self):

        # Points determination. Tortie can't be pointed
        if self.name != "Tortie" and not random.getrandbits(game.config["cat_generation"]["random_point_chance"]):
            # Cat has colorpoint!
            self.points = choice(Pelt.point_markings)
        else:
            self.points = None

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
        self.tint = "none"

    # WHITE PATCHES TINT
        if self.white_patches or self.points:
            #Now for white patches
            possible_tints = Sprites.white_patches_tints["possible_tints"]["basic"].copy()
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
            "Marbled": "c_n marbled tabby",
            "Ticked": "c_n ticked tabby",
            "Mackerel": "c_n mackerel tabby",
            "Classic": "c_n classic tabby",
            "Agouti": "c_n ticked tabby",
            "Backed": "stripe backed c_n",
            "Sokoke": "c_n sokoke tabby",
            "Charcoal": "charcoal c_n tabby",
            "Ghost": "c_n ghost tabby",
            "Doberman": "c_n doberman point",
            "Skele": "c_n skeleton",
            "Hooded": "hooded charcoal c_n tabby",
            "Ponit": "bleach point c_n",
            "Spirit": "c_n ghostly spirit",
            "WolfBicolour": "c_n painted wolf",
            "SparkleTabby": "c_n sparkling tabby",
            "SparkleSpeckled": "c_n sparkling speckled",
            "SparkleDalmation": "c_n sparkling dalmation",
            "SparkleLynx": "c_n sparkling lynx"
            
        }

        # Start with determining the base color name. 
        color_name = str(cat.pelt.colour).lower()
        if color_name in renamed_colors:
            color_name = renamed_colors[color_name]

        if cat.pelt.skin in Pelt.albino_sprites or cat.pelt.skin == "ALBINOSPHYNX":
            color_name = "albino"      
        elif cat.pelt.skin in Pelt.melanistic_sprites or cat.pelt.skin == "MELANISTICSPHYNX":
            color_name = "melanistic"  

        if cat.pelt.name not in ["SingleColour", "TwoColour", "Wolf", "WolfBicolour", 
            "Tortie", "Calico", "FalseSolid", "FalseTwo"] and color_name == "white" or color_name == "petal" \
        or color_name == "ivory":
            color_name = "pale"

        # Time to descibe the pattern and any additional colors. 
        if cat.pelt.name in pattern_des:
            color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
        elif cat.pelt.name in Pelt.torties:
            # Calicos and Torties need their own desciptions. 
            if short:
            # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
                if cat.pelt.colour in Pelt.black_colours + Pelt.grey_colours + Pelt.white_colours + Pelt.blue_colours and \
                cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours + Pelt.blue_colours:
                    color_name = "mottled"
                elif cat.pelt.colour in Pelt.brown_colours + Pelt.yellow_colours and \
                cat.pelt.tortiecolour in Pelt.brown_colours + Pelt.yellow_colours:
                    colour_name = "splattered"
                else:
                    color_name = cat.pelt.name.lower()
            else:
                base = cat.pelt.tortiebase.lower()
                if base in Pelt.tabbies + ['marbled', 'charcoal', 'hooded', 'spirit']:
                    base = 'tabby'
                elif base in Pelt.spotted + ['bengal']:
                    base = 'spotted'
                else:
                    base = ''

                patches_color = cat.pelt.tortiecolour.lower()
                if patches_color in renamed_colors:
                    patches_color = renamed_colors[patches_color]
                color_name = f"{color_name}-{patches_color}"
                
                if cat.pelt.colour in Pelt.black_colours + Pelt.grey_colours + Pelt.white_colours + Pelt.blue_colours and \
                    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.grey_colours + Pelt.white_colours + Pelt.blue_colours:
                    color_name = "mottled"
                elif cat.pelt.colour in Pelt.brown_colours + Pelt.yellow_colours and \
                    cat.pelt.tortiecolour in Pelt.brown_colours + Pelt.yellow_colours:
                    colour_name = "splattered"
                else:
                    color_name = f"{color_name} {cat.pelt.name.lower()}"

        elif cat.pelt.name not in ["SingleColour", "TwoColour", "FalseSolid", "FalseTwo"]:
            color_name = f"{color_name} {cat.pelt.name.lower()}"

        if cat.pelt.skin in Pelt.sphynx:
            color_name = color_name + ' sphynx'
        elif cat.pelt.skin in Pelt.wings:
            color_name = 'winged ' + color_name 

        if cat.pelt.points and cat.pelt.name not in ["Doberman", "Ponit"]:
            color_name = f"{color_name} point"
            if "ginger point" in color_name:
                color_name.replace("ginger point", "flame point")

        if "white and white" in color_name:
            color_name = color_name.replace("white and white", "white")

        if cat.pelt.white_patches and cat.pelt.skin not in Pelt.albino_sprites + Pelt.melanistic_sprites:
            if cat.white_patches == "FULLWHITE":
                # If the cat is fullwhite, discard all other information. They are just white. 
                if cat.white_patches_tint != "none":
                    color_name = f"stained {cat.pelt.white_patches_tint}"
                else:
                    color_name = f"stained white"
        # Now it's time for gender
        if cat.genderalign in ["female", "trans female", "demifemale"]:
            color_name = f"{color_name} molly"
        elif cat.genderalign in ["male", "trans male", "demimale"]:
            color_name = f"{color_name} tom"
        else:
            color_name = f"{color_name} eli"

        if cat.white_patches and cat.skin not in Pelt.albino_sprites + Pelt.melanistic_sprites + ["ALBINOSPHYNX", "MELANISTICSPHYNX"]:
            if cat.white_patches in Pelt.high_white + Pelt.mostly_white and cat.pelt.name != "Calico":
                if cat.white_patches_tint != "none":            
                    color_name = f"{color_name} with patches of {cat.white_patches_tint}"
                else: 
                    color_name = f"{color_name} with patches of white" 
            elif cat.white_patches in Pelt.little_white + Pelt.mid_white and cat.pelt.name != "Calico":
                if cat.pelt.white_patches_tint != "none":            
                    color_name = f"{color_name} with small patches of {cat.pelt.white_patches_tint}"
                else: 
                    color_name = f"{color_name} with small patches of white" 

        if not short and cat.pelt.eye_colour in Pelt.sus_eyes:
            color_name = f"{color_name} looking sus"

        # Here is the place where we can add some additional details about the cat, for the full non-short one. 
        # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars. 
        if not short:
            
            scar_details = {
                "NOTAIL": "no tail", 
                "HALFTAIL": "half a tail", 
                "NOPAW": "three legs", 
                "NOLEFTEAR": "a missing ear", 
                "NORIGHTEAR": "a missing ear",
                "NOEAR": "no ears",
                "DECLAWED": "missing claws"
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
        
        
            if len(cat.scars) >= 3:
                color_name = f"scarred {color_name}"
            if cat.pelt.length == "long":
                color_name = f"long-furred {color_name}"

        return color_name

    def get_sprites_name(self):
        return Pelt.sprites_names[self.name]
