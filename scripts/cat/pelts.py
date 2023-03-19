from random import choice

class SingleColour():
    name = "SingleColour"
    sprites = {1: 'single'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length
class TwoColour():
    name = "TwoColour"
    sprites = {1: 'single', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"
class FalseSolid():
    name = "FalseSolid"
    sprites = {1: 'falsesolid'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length
class FalseTwoColour():
    name = "FalseTwoColour"
    sprites = {1: 'falsesolid', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"


class Tabby():
    name = "Tabby"
    sprites = {1: 'tabby', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} tabby"
        else:
            return self.colour + self.length + " tabby"


class Marbled():
    name = "Marbled"
    sprites = {1: 'marbled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} marbled"
        else:
            return self.colour + self.length + " marbled"


class Rosette():
    name = "Rosette"
    sprites = {1: 'rosette', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} rosette"
        else:
            return self.colour + self.length + " rosette"


class Smoke():
    name = "Smoke"
    sprites = {1: 'smoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} smoke"
        else:
            return self.colour + self.length + " smoke"


class Ticked():
    name = "Ticked"
    sprites = {1: 'ticked', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ticked"
        else:
            return self.colour + self.length + " ticked"


class Speckled():
    name = "Speckled"
    sprites = {1: 'speckled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} speckled{self.length}"
        else:
            return f"{self.colour} speckled{self.length}"


class Bengal():
    name = "Bengal"
    sprites = {1: 'bengal', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bengal{self.length}"
        else:
            return f"{self.colour} bengal{self.length}"


class Mackerel():
    name = "Mackerel"
    sprites = {1: 'mackerel', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} mackerel tabby{self.length}"
        else:
            return f"{self.colour} mackerel tabby{self.length}"


class Classic():
    name = "Classic"
    sprites = {1: 'classic', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} classic tabby{self.length}"
        else:
            return f"{self.colour} classic tabby{self.length}"


class Sokoke():
    name = "Sokoke"
    sprites = {1: 'sokoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} sokoke tabby{self.length}"
        else:
            return f"{self.colour} sokoke tabby{self.length}"


class Agouti():
    name = "Agouti"
    sprites = {1: 'agouti', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} agouti{self.length}"
        else:
            return f"{self.colour} agouti{self.length}"


class Backed():
    name = "Backed"
    sprites = {1: 'backed', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} backed{self.length}"
        else:
            return f"{self.colour} backed{self.length}"


class Tortie():
    name = "Tortie"
    sprites = {1: 'tortie', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and tortoiseshell{self.length}"
        else:
            return f"tortoiseshell{self.length}"


class Calico():
    name = "Calico"
    sprites = {1: 'calico', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"calico{self.length}"


# ATTRIBUTES, including non-pelt related
pelt_colours = ['PALECREAM', 'CREAM', 'BEIGE', 'MEERKAT', 'KHAKI', 'SAND', 'WOOD', 'ROSE', 
    'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'RED', 'SCARLET', 'APRICOT', 'GARFIELD', 
    'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 'SOOT', 'DARKGREY', 
    'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'PITCH', 'GREY', 'MARENGO', 'BATTLESHIP', 'CADET', 
    'BLUEGREY', 'STEEL', 'SLATE', 'CAPPUCCINO', 'ECRU', 'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 
    'PINECONE', 'WRENGE', 'BROWN', 'MINK', 'CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 
    'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER', 'WHITE', 'SILVER', 'BRONZE', 'PALEBOW', 
    'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM', 'SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC',
    'POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW', 'PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 
    'DARKSALMON', 'MAGENTA', 'PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT', 'PURPLE', 'WINE', 'RASIN',
    'GENDER', 'REDNEG', 'IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT', 'LEMON', 'LAGUNA', 
    'YELLOW', 'CORN', 'GOLD', 'HONEY', 'BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA', 
    'SADDLE', 'CEDAR', 'ONYX', 'LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD', 'OLIVE',
    'DARKOLIVE', 'GREEN', 'FOREST', 'JADE', 'SPINNACH', 'SEAWEED', 'SACRAMENTO', 'XANADU', 'DEEPFOREST',
    'AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']

pelt_falsesolid = ['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS',
    'SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET', 'APRICOT', 
    'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 
    'ROSEWOOD', 'BLOOD', 'PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 
    'DARKSALMON', 'MAGENTA', 'PURPLE', 'WINE', 'RASIN', 'GENDER', 'REDNEG',
    'AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']

pelt_c_no_white = ['PALECREAM', 'CREAM', 'BEIGE', 'MEERKAT', 'KHAKI', 'SAND', 'WOOD', 'ROSE', 
    'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'RED', 'SCARLET', 'APRICOT', 'GARFIELD', 
    'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 'SOOT', 'DARKGREY', 
    'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'GREY', 'MARENGO', 'BATTLESHIP', 'CADET', 
    'BLUEGREY', 'STEEL', 'SLATE', 'CAPPUCCINO', 'ECRU', 'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 
    'PINECONE', 'WRENGE', 'BROWN', 'MINK', 'CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 
    'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER','TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM', 
    'SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC', 'POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW', 
    'PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA', 'MEW', 
    'HEATHER', 'ORCHID', 'STRAKIT', 'PURPLE', 'WINE', 'RASIN','GENDER', 'REDNEG', 'BANNANA', 'FARROW', 
    'HAY', 'FAWN', 'HAZELNUT', 'LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY', 'BEE', 
    'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA', 'SADDLE', 'CEDAR', 'ONYX', 'LIME', 'CHARTRUSE', 
    'LETTUCE', 'GRASS', 'MINT', 'EMERALD', 'OLIVE','DARKOLIVE', 'GREEN', 'FOREST', 'JADE', 'SPINNACH', 
    'SEAWEED', 'SACRAMENTO', 'XANADU', 'DEEPFOREST', 'GAYBOW']
pelt_c_no_bw = ['PALECREAM', 'CREAM', 'BEIGE', 'MEERKAT', 'KHAKI', 'SAND', 'WOOD', 'ROSE', 
    'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'RED', 'SCARLET', 'APRICOT', 'GARFIELD', 
    'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 'GREY', 'MARENGO', 
    'BATTLESHIP', 'CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'CAPPUCCINO', 'ECRU', 
    'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK', 
    'CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER',
    'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM', 'SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC',
    'POWDERBLUE', 'JEANS', 'NAVY', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM', 'SHINYMEW', 
    'SKY', 'TEAL', 'COBALT', 'SONIC', 'POWDERBLUE', 'JEANS', 'NAVY', 'PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 
    'DARKSALMON', 'MAGENTA', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT', 'PURPLE', 'WINE',
    'GENDER', 'REDNEG', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT', 'LEMON', 'LAGUNA', 
    'YELLOW', 'CORN', 'GOLD', 'HONEY', 'BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA', 
    'SADDLE', 'CEDAR', 'LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD', 'OLIVE',
    'DARKOLIVE', 'GREEN', 'FOREST', 'JADE', 'SPINNACH', 'SEAWEED', 'SACRAMENTO', 'XANADU', 'DEEPFOREST',
    'GAYBOW']  

tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMAL1', 'MINIMAL2', 'MINIMAL3', 'MINIMAL4',
                  'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE',
                  'ROBIN', 'BRINDLE', 'PAIGE']
tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
               'classic', 'sokoke', 'agouti', 'singlestripe']

pelt_length = ["short", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 
    'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 'GREENYELLOW', 
    'BRONZE', 'SILVER', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 
    'GREENYELLOW', 'POPPY', 'CRIMSON', 'RUBY', 'BROWN', 'JADE', 'SKY', 'LILAC', 'BROWNTWO', 'PEANUT', 'GREYTWO', 
    'YELLOWOLIVE', 'SUNSHINE', 'AZURE', 'COBOLT', 'GRASS', 'MINT', 'LILACGREY', 'WHITE', 'VIOLET', 'GRAPE', 'INDIGO', 
    'PRIMARY', 'PRIMARYB', 'PRIMARYC', 'CHROME', 'CHROMEB', 'CHROMEC', 'RBG', 'RBGTWO', 'RBGTHREE', 'MONOCHROME', 
    'MONOCHROMETWO', 'MONOCHROMETHREE', 'POPPYPINK', 'STRAWBERRY', 'MINTCHOC', 'CHOCMINT', 'AMBERTWO', 'BEACH', 
    'NACRE', 'NIGHT', 'OCEAN']
yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'BRONZE', 'GOLD', 'COPPER', 'GREENYELLOW', 'BROWN', 'BROWNtWO', 
                'PEANUT', 'YELLOWOLIVE', 'SUNSHINE', 'AMBERTWO', 'BEACH']
blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'COBALT', 'SUNLITICE', 'AZURE', 
                'COBOLT', 'OCEAN']
green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL', 'JADE', 'GRASS', 'MINT',
    'MINTCHOC', 'CHOCMINT']
mono_eyes = ['GREY', 'SILVER', 'VOID', 'GHOST', 'GREYTWO', 'LILACGREY', 'WHITE', 'MONOCHROME', 
    'MONOCHROMETWO', 'MONOCHROMETHREE', 'NACRE', 'NIGHT']
purple_eyes = ['POPPY', 'CRIMSON', 'RUBY', 'LILAC', 'VIOLET', 'GRAPE', 'INDIGO', 
    'POPPY2', 'STRAWBERRY']
chromatic_eyes = ['PRIMARY', 'PRIMARYB', 'PRIMARYC', 'CHROME', 'CHROMEB', 'CHROMEC', 'RBG', 
    'RBGTWO', 'RBGTHREE',]
# scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
# bite scars by @wood pank on discord
scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
          "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
          "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH"]
scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
          "FROSTSOCK", ]

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

tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti"]
spotted = ["Speckled", "Rosette"]
plain = ["SingleColour", "TwoColour", "FalseSolid", "FalseTwoColour", "Smoke", 
        "Backed"]
exotic = ["Bengal", "Marbled"]
torties = ["Tortie", "Calico"]
pelt_categories = [tabbies, spotted, plain, exotic, torties]

# SPRITE NAMES
pride_colours = ['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']
single_colours = ['PALECREAM', 'CREAM', 'BEIGE', 'MEERKAT', 'KHAKI', 'SAND', 'WOOD', 'ROSE', 
    'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'RED', 'SCARLET', 'APRICOT', 'GARFIELD', 
    'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 'SOOT', 'DARKGREY', 
    'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'PITCH', 'GREY', 'MARENGO', 'BATTLESHIP', 'CADET', 
    'BLUEGREY', 'STEEL', 'SLATE', 'CAPPUCCINO', 'ECRU', 'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 
    'PINECONE', 'WRENGE', 'BROWN', 'MINK', 'CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 
    'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER', 'WHITE', 'SILVER', 'BRONZE', 'PALEBOW', 
    'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM', 'SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC',
    'POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW', 'PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 
    'DARKSALMON', 'MAGENTA', 'PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT', 'PURPLE', 'WINE', 'RASIN',
    'GENDER', 'REDNEG', 'IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT', 'LEMON', 'LAGUNA', 
    'YELLOW', 'CORN', 'GOLD', 'HONEY', 'BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA', 
    'SADDLE', 'CEDAR', 'ONYX', 'LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD', 'OLIVE',
    'DARKOLIVE', 'GREEN', 'FOREST', 'JADE', 'SPINNACH', 'SEAWEED', 'SACRAMENTO', 'XANADU', 'DEEPFOREST']
cream_colours = ['PALECREAM', 'CREAM', 'BEIGE', 'MEERKAT', 'KHAKI', 'SAND', 'WOOD', 'PANTONE', 'SALMON',
    'THISTLE', 'BANNANA', 'FARROW', 'HAY']
ginger_colours = ['ROSE', 'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'RED', 
    'SCARLET', 'APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 
    'ROSEWOOD', 'BLOOD']
black_colours = ['SOOT', 'DARKGREY', 'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'PITCH', 'ONYX', 'RASIN', 'DUSKBOW']
grey_colours = ['GREY', 'MARENGO', 'BATTLESHIP', 'CADET', 'BLUEGREY', 'STEEL', 'SLATE']
white_colours = ['WHITE', 'SILVER', 'BRONZE', 'PALEBOW', 'PETAL', 'IVORY']
brown_colours = ['CAPPUCCINO', 'ECRU', 'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 
    'PINECONE', 'WRENGE', 'BROWN', 'MINK', 'CHESTNUT', 'TAN', 'TROMBONE', 'MEDALLION', 'GRANOLA', 
    'SADDLE', 'CEDAR', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER']
blue_colours = ['TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'SHINYMEW', 'SKY', 'OCEAN', 'DENIUM', 'COBALT', 'SONIC', 'POWDERBLUE', 'JEANS', 'NAVY']
yellow_colours = ['FAWN', 'HAZELNUT', 'LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY', 'BEE', 'PINEAPPLE']
purple_colours = ['AMYTHYST', 'DARKSALMON', 'MAGENTA', 'MEW', 'HEATHER', 
    'ORCHID', 'STRAKIT', 'PURPLE', 'WINE', 'GENDER', 'REDNEG']
green_colours = ['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD', 'OLIVE', 'DARKOLIVE', 'GREEN', 
    'FOREST', 'JADE', 'SPINNACH', 'SEAWEED', 'SACRAMENTO', 'XANADU', 'DEEPFOREST']

colour_categories = [cream_colours, ginger_colours, black_colours, grey_colours, white_colours, brown_colours, blue_colours, 
    yellow_colours, purple_colours, green_colours, pride_colours]

eye_sprites = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
    'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT',
    'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER', 'POPPY', 'CRIMSON', 'RUBY', 'BROWN', 'JADE', 'SKY', 
    'LILAC', 'BROWNTWO', 'PEANUT', 'GREYTWO', 'YELLOWOLIVE', 'SUNSHINE', 'AZURE', 'COBOLT', 'GRASS', 'MINT', 
    'LILACGREY', 'WHITE', 'VIOLET', 'GRAPE', 'INDIGO', 'VOID', 'GHOST', 'PRIMARY', 'PRIMARYB', 'PRIMARYC', 
    'CHROME', 'CHROMEB', 'CHROMEC','RBG', 'RBGTWO', 'RBGTHREE', 'MONOCHROME', 'MONOCHROMETWO', 'MONOCHROMETHREE', 
    'POPPY2', 'STRAWBERRY', 'MINTCHOC', 'CHOCMINT', 'AMBERTWO', 'BEACH', 'NACRE', 'NIGHT', 'OCEAN']

little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'LUNA',
                'EXTRA']
mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR',
             'WINGS']
high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
              'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
              'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED']
mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO']
point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER']
white_sprites = [little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

tint_colors = ['none', 'off white', 'gray', 'dark cream', 'cream', 'pink', 'blue-white', 'mint', 'black',
    'midnight', 'scarlet', 'starkit', 'sunshine']

skin_sprites = ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']
skin_sphynx = ['S_BLACK', 'S_RED', 'S_PINK', 'S_DARKBROWN', 'S_BROWN', 'S_LIGHTBROWN', 'S_DARK', 'S_DARKGREY', 'S_GREY', 'S_DARKSALMON',
                'S_SALMON', 'S_PEACH', 'S_DARKMARBLED', 'S_MARBLED', 'S_LIGHTMARBLED', 'S_DARKBLUE', 'S_BLUE', 'S_LIGHTBLUE']
albino_sprites = ['ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET', 'ALBINOYELLOW', 'ALBINOGREEN', 'S_ALBINOPINK',  
                'S_ALBINOBLUE', 'S_ALBINORED', 'S_ALBINOVIOLET', 'S_ALBINOYELLOW', 'S_ALBINOGREEN']
melanistic_sprites = ['MELANISTIC', 'MELANISTIC2', 'MELANISTIC3', 'S_MELANISTIC', 'S_MELANISTIC2', 'S_MELANISTIC3'] 
skin_categories = [skin_sprites, skin_sphynx, albino_sprites, melanistic_sprites]

# CHOOSING PELT
def choose_pelt(colour=None, white=None, pelt=None, length=None, category=None, determined=False):
    colour = colour
    white = white
    pelt = pelt
    length = length
    category = category
    if pelt is None:
        if category != None:
            pelt = choice(category)
    else:
        pelt = pelt
    if length is None:
        length = choice(pelt_length)
    if pelt == 'SingleColour':
        if colour is None and not white:
            return SingleColour(choice(pelt_colours), length)
        elif colour is None:
            return SingleColour("WHITE", length)
        else:
            return SingleColour(colour, length)
    elif pelt == 'TwoColour':
        if colour is None:
            return TwoColour(choice(pelt_c_no_white), length)
        else:
            return TwoColour(colour, length)
    elif pelt == 'FalseSolid':
        if colour is None and not white:
            return FalseSolid(choice(pelt_falsesolid), length)
        elif colour is None:
            return FalseSolid("WHITE", length)
        else:
            return FalseSolid(colour, length)
    elif pelt == 'FalseTwoColour':
        if colour is None:
            return FalseTwoColour(choice(pelt_falsesolid), length)
        else:
            return FalseTwoColour(colour, length)
    elif pelt == 'Tabby':
        if colour is None and white is None:
            return Tabby(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Tabby(choice(pelt_colours), white, length)
        else:
            return Tabby(colour, white, length)
    elif pelt == 'Marbled':
        if colour is None and white is None:
            return Marbled(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Marbled(choice(pelt_colours), white, length)
        else:
            return Marbled(colour, white, length)
    elif pelt == 'Rosette':
        if colour is None and white is None:
            return Rosette(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Rosette(choice(pelt_colours), white, length)
        else:
            return Rosette(colour, white, length)
    elif pelt == 'Smoke':
        if colour is None and white is None:
            return Smoke(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Smoke(choice(pelt_colours), white, length)
        else:
            return Smoke(colour, white, length)
    elif pelt == 'Ticked':
        if colour is None and white is None:
            return Ticked(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ticked(choice(pelt_colours), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == 'Speckled':
        if colour is None and white is None:
            return Speckled(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Speckled(choice(pelt_colours), white, length)
        else:
            return Speckled(colour, white, length)
    elif pelt == 'Bengal':
        if colour is None and white is None:
            return Bengal(choice(pelt_colours), choice([False, True]),
                          length)
        elif colour is None:
            return Bengal(choice(pelt_colours), white, length)
        else:
            return Bengal(colour, white, length)
    elif pelt == 'Mackerel':
        if colour is None and white is None:
            return Mackerel(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Mackerel(choice(pelt_colours), white, length)
        else:
            return Mackerel(colour, white, length)
    elif pelt == 'Classic':
        if colour is None and white is None:
            return Classic(choice(pelt_colours), choice([False, True]),
                           length)
        elif colour is None:
            return Classic(choice(pelt_colours), white, length)
        else:
            return Classic(colour, white, length)
    elif pelt == 'Sokoke':
        if colour is None and white is None:
            return Sokoke(choice(pelt_colours), choice([False, True]),
                          length)
        elif colour is None:
            return Sokoke(choice(pelt_colours), white, length)
        else:
            return Sokoke(colour, white, length)
    elif pelt == 'Agouti':
        if colour is None and white is None:
            return Agouti(choice(pelt_colours), choice([False, True]),
                          length)
        elif colour is None:
            return Agouti(choice(pelt_colours), white, length)
        else:
            return Agouti(colour, white, length)
    elif pelt == 'Backed':
        if colour is None and white is None:
            return Backed(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Backed(choice(pelt_colours), white, length)
        else:
            return Backed(colour, white, length)
    elif pelt == 'Tortie':
        if white is None:
            return Tortie(colour, choice([False, True]), length)
        else:
            return Tortie(colour, white, length)
    else:
        return Calico(colour, length)
    
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
            "darksalmon": "salmon",
            "strakit": "purple",
            "gender": "blurple",
            "redneg": "blurple"
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
            "darksalmon": "dark salmon",
            "strakit": "starkit purple",
            "gender": "genderfluid blurple",
            "redneg": "genderfluid blurple"
        }

    pattern_des = {
        "Marbled": "c_n marbled tabby",
        "Ticked": "c_n ticked tabby",
        "Mackerel": "c_n mackerel tabby",
        "Classic": "c_n classic tabby",
        "Agouti": "c_n ticked tabby",
        "Backed": "stripe backed c_n",
        "Sokoke": "c_n sokoke tabby"
    }

    # Start with determining the base color name. 
    color_name = str(cat.pelt.colour).lower()
    if color_name in renamed_colors:
        color_name = renamed_colors[color_name]

    if cat.skin in albino_sprites:
        color_name = "albino"      
    elif cat.skin in melanistic_sprites:
        color_name = "melanistic"  

    if cat.pelt.name not in ["SingleColour", "TwoColour", "FalseSolid", "FalseTwoColour", 
        "Tortie", "Calico"] and color_name == "white" or color_name == "petal" or color_name == "ivory":
        color_name = "pale"

    # Time to descibe the pattern and any additional colors. 
    if cat.pelt.name in pattern_des:
        color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
    elif cat.pelt.name in torties:
        # Calicos and Torties need their own desciptions. 
        if short:
        # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
            if cat.pelt.colour in black_colours + grey_colours + white_colours + blue_colours and \
            cat.tortiecolour in black_colours + brown_colours + white_colours + blue_colours:
                color_name = "mottled"
            elif cat.pelt.colour in brown_colours + yellow_colours and \
            cat.tortiecolour in brown_colours + yellow_colours:
                colour_name = "splattered"
            else:
                color_name = cat.pelt.name.lower()
        else:
            base = cat.tortiebase.lower()
            if base in tabbies + ['bengal', 'rosette', 'speckled']:
                base = 'tabby'
            else:
                base = ''

            patches_color = cat.tortiecolour.lower()
            if patches_color in renamed_colors:
                patches_color = renamed_colors[patches_color]
            color_name = f"{color_name}/{patches_color}"
            
            if cat.pelt.colour in black_colours + grey_colours + white_colours + blue_colours and \
                cat.tortiecolour in black_colours + brown_colours + white_colours + blue_colours:
                color_name = "mottled"
            elif cat.pelt.colour in brown_colours + yellow_colours and \
                cat.tortiecolour in brown_colours + yellow_colours:
                colour_name = "splattered"
            else:
                color_name = f"{color_name} {cat.pelt.name.lower()}"

    elif cat.pelt.name not in ["SingleColour", "TwoColour", "FalseSolid", "FalseTwoColour"]:
        color_name = f"{color_name} {cat.pelt.name.lower()}"

    if cat.skin in skin_sphynx:
        color_name = color_name + ' sphynx'

    if cat.white_patches:
        if cat.white_patches == "FULLWHITE":
            # If the cat is fullwhite, discard all other information. They are just white. 
            color_name = "stained"
        if cat.white_patches in [high_white, mostly_white] and cat.pelt.name != "Calico":
            color_name = f"{color_name} with patches"
        elif cat.pelt.name != "Calico":
            color_name = f"{color_name} with small patches"

    if cat.white_patches_tint != "None":
        colour_name = f"{color_name} + ' of ' + {cat.white_patches_tint}"
    
    if cat.points:
        color_name = f"{color_name} point"
        if "ginger point" in color_name:
            color_name.replace("ginger point", "flame point")

    # Now it's time for gender
    if cat.genderalign in ["female", "trans female"]:
        color_name = f"{color_name} molly"
    elif cat.genderalign in ["male", "trans male"]:
        color_name = f"{color_name} tom"
    else:
        color_name = f"{color_name} eli"

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
        if cat.vitiligo:
            additional_details.append("vitiligo")
        for scar in cat.scars:
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
    