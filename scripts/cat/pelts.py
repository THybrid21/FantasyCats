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

class Charcoal():
    name = "Charcoal"
    sprites = {1: 'charcoal', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} charcoal"
        else:
            return self.colour + self.length + " charcoal"

class Ghost():
    name = "Ghost"
    sprites = {1: 'tabby', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ghost"
        else:
            return self.colour + self.length + " ghost"

class Merle():
    name = "Merle"
    sprites = {1: 'merle', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} merle"
        else:
            return self.colour + self.length + " merle"

class Doberman():
    name = "Doberman"
    sprites = {1: 'doberman', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} doberman"
        else:
            return self.colour + self.length + " doberman"

class Snowflake():
    name = "Snowflake"
    sprites = {1: 'snowflake', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} snowflake"
        else:
            return self.colour + self.length + " snowflake"            

class Skele():
    name = "Skele"
    sprites = {1: 'skele', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} skele"
        else:
            return self.colour + self.length + " skele"

class Stain():
    name = "Stain"
    sprites = {1: 'stain', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} stain"
        else:
            return self.colour + self.length + " stain"     

class Mottled():
    name = "Mottled"
    sprites = {1: 'mottled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} mottled"
        else:
            return self.colour + self.length + " mottled"     

class Rat():
    name = "Rat"
    sprites = {1: 'rat', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} rat"
        else:
            return self.colour + self.length + " rat"  

class Skitty():
    name = "Skitty"
    sprites = {1: 'skitty', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} skitty"
        else:
            return self.colour + self.length + " skitty"  

class Hooded():
    name = "Hooded"
    sprites = {1: 'hooded', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} hooded"
        else:
            return self.colour + self.length + " hooded"  

class Ponit():
    name = "Ponit"
    sprites = {1: 'ponit', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ponit"
        else:
            return self.colour + self.length + " ponit"  

class Spirit():
    name = "Spirit"
    sprites = {1: 'spirit'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length + " spirit"  

class Wolf():
    name = "Wolf"
    sprites = {1: 'wolf'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length + " wolf"  
class WolfBicolour():
    name = "WolfBicolour"
    sprites = {1: 'wolf', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length} wolf"

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
    'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'GREY', 'MARENGO', 'BATTLESHIP', 'CADET', 
    'BLUEGREY', 'STEEL', 'SLATE', 'CAPPUCCINO', 'ECRU', 'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 
    'PINECONE', 'WRENGE', 'BROWN', 'MINK', 'CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 
    'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER', 'WHITE', 'SILVER', 'BRONZE']
pelt_c_no_white = ['PALECREAM', 'CREAM', 'BEIGE', 'MEERKAT', 'KHAKI', 'SAND', 'WOOD', 'ROSE', 
    'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'RED', 'SCARLET', 'APRICOT', 'GARFIELD', 
    'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 'SOOT', 'DARKGREY', 
    'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'GREY', 'MARENGO', 'BATTLESHIP', 'CADET', 
    'BLUEGREY', 'STEEL', 'SLATE', 'CAPPUCCINO', 'ECRU', 'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 
    'PINECONE', 'WRENGE', 'BROWN', 'MINK', 'CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 
    'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER']
pelt_c_no_bw = ['PALECREAM', 'CREAM', 'BEIGE', 'MEERKAT', 'KHAKI', 'SAND', 'WOOD', 'ROSE', 
    'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'RED', 'SCARLET', 'APRICOT', 'GARFIELD', 
    'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 'GREY', 'MARENGO', 
    'BATTLESHIP', 'CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'CAPPUCCINO', 'ECRU', 
    'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK', 
    'CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER']    

tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMAL1', 'MINIMAL2', 'MINIMAL3', 'MINIMAL4',
                  'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE',
                  'ROBIN', 'BRINDLE', 'PAIGE', 'COMBO', 'BLENDED', 'SCATTER', 'LIGHT']
tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
               'classic', 'sokoke', 'agouti', 'backed', 'charcoal', 'ghost', 'merle', 'doberman', 'skele', 'stain', 
               'mottled', 'snowflake', 'rat', 'hooded', 'skitty']

pelt_length = ["short", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD',
   'PALEBLUE', 'VOID', 'GHOST', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'BLUE2', 'SUNLITICE', 
   'GREENYELLOW', 'POPPY', 'CRIMSON', 'RUBY', 'BROWN', 'EMERALD2', 'SKY', 'LILAC', 'BROWN2', 'PEANUT', 
   'GREY2', 'YELLOWOLIVE', 'SUNSHINE', 'AZURE', 'COBOLT', 'GRASS', 'MINT', 'LILACGREY', 'WHITE',
   'VIOLET', 'GRAPE', 'INDIGO', 'PRIMARY', 'PRIMARY2', 'PRIMARY3', 'CHROME', 'CHROME2', 'CHROME3',
   'RBG', 'RBG2', 'RBG3', 'MONOCHROME', 'MONOCHROME2', 'MONOCHROME3', 'POPPY2', 'STRAWBERRY', 'MINTCHOC', 
   'CHOCMINT', 'AMBER2', 'BEACH', 'NACRE', 'NIGHT', 'OCEAN']
yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'GOLD', 'COPPER', 'GREENYELLOW', 'BROWN', 'BROWN2', 
                'PEANUT', 'YELLOWOLIVE', 'SUNSHINE', 'AMBER2', 'BEACH']
blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'BLUE2', 'SUNLITICE', 'AZURE', 
                'COBOLT', 'OCEAN']
green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL', 'EMERALD2', 'GRASS', 'MINT',
    'MINTCHOC', 'CHOCMINT']
mono_eyes = ['GREY', 'VOID', 'GHOST', 'GREY2', 'LILACGREY', 'WHITE', 'MONOCHROME', 
    'MONOCHROME2', 'MONOCHROME3', 'NACRE', 'NIGHT']
purple_eyes = ['POPPY', 'CRIMSON', 'RUBY', 'LILAC', 'VIOLET', 'GRAPE', 'INDIGO', 
    'POPPY2', 'STRAWBERRY']
chromatic_eyes = ['PRIMARY', 'PRIMARY2', 'PRIMARY3', 'CHROME', 'CHROME2', 'CHROME3', 'RBG', 
    'RBG2', 'RBG3']
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
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS",
    "RAT BLACK", "RAT BROWN", "RAT CREAM", "RAT WHITE", "RAT GREY", "RAT HOODED", "CRIMSONSTAR", "BLUESTAR", 
    "YELLOWSTAR", "CYANSTAR", "REDSTAR", "LIMESTAR", "DARKSEAWEED", "LIGHTSEAWEED", "DRYSEAWEED", "MAGICSEAWEED",
    "DARKPEARLS", "LIGHTPEARL"]
tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS"]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "INDIGOBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW", "INDIGOBOW", "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON",
    "REDNYLON", "LIMENYLON", "GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", 
    "PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON", "CRIMSONBC", "BLUEBC", "YELLOWBC", "CYANBC", 
    "REDBC", "LIMEBC", "GREENBC", "RAINBOWBC", "BLACKBC", "SPIKESBC", "PINKBC", "PURPLEBC", "MULTIBC",
    "CRIMSONCAPE", "BLUECAPE", "YELLOWCAPE", "CYANCAPE", "REDCAPE", "LIMECAPE", "GREENCAPE", "RAINBOWCAPE", 
    "BLACKCAPE", "ORANGECAPE", "PINKCAPE", "PURPLECAPE", "WHITECAPE"
]

tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti", "Merle"]
spotted = ["Speckled", "Rosette", "Snowflake", "Mottled"]
plain = ["SingleColour", "TwoColour", "Smoke", "Backed", "Doberman", 
    "Skitty", "Rat", "Wolf", "WolfBicolour", "Ghost"]
exotic = ["Bengal", "Marbled", "Skele", "Stain", "Charcoal", "Hooded", 
    "Ponit", "Spirit"]
torties = ["Tortie", "Calico"]
pelt_categories = [tabbies, spotted, plain, exotic, torties]

# SPRITE NAMES
single_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK'
]
single_colours = ['PALECREAM', 'CREAM', 'BEIGE', 'MEERKAT', 'KHAKI', 'SAND', 'WOOD', 'ROSE', 
    'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'RED', 'SCARLET', 'APRICOT', 'GARFIELD', 
    'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD', 'SOOT', 'DARKGREY', 
    'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK', 'GREY', 'MARENGO', 'BATTLESHIP', 'CADET', 
    'BLUEGREY', 'STEEL', 'SLATE', 'CAPPUCCINO', 'ECRU', 'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 
    'PINECONE', 'WRENGE', 'BROWN', 'MINK', 'CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 
    'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER', 'WHITE', 'SILVER', 'BRONZE']
cream_colours = ['PALECREAM', 'CREAM', 'BEIGE', 'MEERKAT', 'KHAKI', 'SAND', 'WOOD']
ginger_colours = ['ROSE', 'GINGER', 'SUNSET', 'RUFOUS', 'FIRE', 'BRICK', 'RED', 
    'SCARLET', 'APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT', 'CARMINE', 'COSMOS', 
    'ROSEWOOD', 'BLOOD']
black_colours = ['SOOT', 'DARKGREY', 'ANCHOR', 'CHARCOAL', 'COAL', 'BLACK']
grey_colours = ['GREY', 'MARENGO', 'BATTLESHIP', 'CADET', 'BLUEGREY', 'STEEL', 'SLATE']
white_colours = ['WHITE', 'SILVER', 'BRONZE']
brown_colours = ['CAPPUCCINO', 'ECRU', 'ASHBROWN', 'DUSTBROWN', 'SANDALWOOD', 
    'PINECONE', 'WRENGE', 'BROWN', 'MINK', 'CHESTNUT', 'TAN']
chocolate_colours = ['DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA', 'COFFEE', 'TAUPE', 'UMBER']
colour_categories = [cream_colours, ginger_colours, black_colours, grey_colours, white_colours, brown_colours, chocolate_colours]

little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS', 
    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'VENUS', 
    'SHADOWSIGHT', 'TWIST', 'OKAPI', 'LUNA', 'EXTRA']
mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR', 'MOSSCLAW',
             'NIGHTMIST', 'SKELEWHITE', 'WINGS']           
high_white = ['ANY', 'ANY2', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 
    'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
    'CURVED', 'GLASS', 'MASKMANTLE', 'CHANCE', 'RETSUKO', 'MAO', 'PAINTED'] 
mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE', 'DAPPLED', 
    'HAWK', 'FRECKLEMASK', 'MOTH', 'CHESTSPECK', 'HEART2', 'BLACKSTAR']
point_markings = ['COLOURPOINT', 'RAGDOLL', 'KARPATI', 'SNOWSHOE', 'SNOWBOOT', 'LIGHTPOINT', 
    'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
vit = ['VITILIGO', 'VITILIGO2', 'DARKVITILIGO', 'DARKVITILIGO2']
white_sprites = [little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

tint_colors = ['none', 'off white', 'gray', 'dark cream', 'cream', 'pink', 'blue-white', 'black',
    'scarlet', 'sunshine']

skin_sprites = ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']
skin_sphynx = ['S_BLACK', 'S_RED', 'S_PINK', 'S_DARKBROWN', 'S_BROWN', 'S_LIGHTBROWN', 'S_DARK', 'S_DARKGREY', 'S_GREY', 'S_DARKSALMON',
                'S_SALMON', 'S_PEACH', 'S_DARKMARBLED', 'S_MARBLED', 'S_LIGHTMARBLED', 'S_DARKBLUE', 'S_BLUE', 'S_LIGHTBLUE']
albino_sprites = ["ALBINOPINK", "ALBINOBLUE", "ALBINORED", "ALBINOVIOLET", "S_ALBINOPINK", "S_ALBINOBLUE", "S_ALBINORED", "S_ALBINOVIOLET"]
melanistic_sprites = ["MELANISTICLIGHT", "MELANISTIC", "MELANISTICDARK", "S_MELANISTICLIGHT", "S_MELANISTIC", "S_MELANISTICDARK"] 
skin_categories = [skin_sprites, skin_sphynx, albino_sprites, melanistic_sprites] 
sphynx = ['S_BLACK', 'S_RED', 'S_PINK', 'S_DARKBROWN', 'S_BROWN', 'S_LIGHTBROWN', 'S_DARK', 'S_DARKGREY', 'S_GREY', 'S_DARKSALMON',
            'S_SALMON', 'S_PEACH', 'S_DARKMARBLED', 'S_MARBLED', 'S_LIGHTMARBLED', 'S_DARKBLUE', 'S_BLUE', 'S_LIGHTBLUE',  
            "S_ALBINOPINK", "S_ALBINOBLUE", "S_ALBINORED", "S_ALBINOVIOLET", "S_MELANISTICLIGHT", 
            "S_MELANISTIC", "S_MELANISTICDARK"]

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
    elif pelt == "Charcoal":
        if colour is None and white is None:
            return Charcoal(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Charcoal(choice(pelt_colours), white, length)
        else:
            return Charcoal(colour, white, length) 
    elif pelt == "Doberman":
        if colour is None and white is None:
            return Doberman(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Doberman(choice(pelt_colours), white, length)
        else:
            return Doberman(colour, white, length)   
    elif pelt == "Ghost":
        if colour is None and white is None:
            return Ghost(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ghost(choice(pelt_colours), white, length)
        else:
            return Ghost(colour, white, length)            
    elif pelt == "Merle":
        if colour is None and white is None:
            return Merle(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Merle(choice(pelt_colours), white, length)
        else:
            return Merle(colour, white, length)     
    elif pelt == "Snowflake":
        if colour is None and white is None:
            return Snowflake(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Snowflake(choice(pelt_colours), white, length)
        else:
            return Snowflake(colour, white, length)            
    elif pelt == "Skele":
        if colour is None and white is None:
            return Skele(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Skele(choice(pelt_colours), white, length)
        else:
            return Skele(colour, white, length)      
    elif pelt == "Stain":
        if colour is None and white is None:
            return Stain(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Stain(choice(pelt_colours), white, length)
        else:
            return Stain(colour, white, length) 
    elif pelt == "Mottled":
        if colour is None and white is None:
            return Mottled(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Mottled(choice(pelt_colours), white, length)
        else:
            return Mottled(colour, white, length)  
    elif pelt == "Rat":
        if colour is None and white is None:
            return Rat(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Rat(choice(pelt_colours), white, length)
        else:
            return Rat(colour, white, length) 
    elif pelt == "Skitty":
        if colour is None and white is None:
            return Skitty(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Skitty(choice(pelt_colours), white, length)
        else:
            return Skitty(colour, white, length) 
    elif pelt == "Hooded":
        if colour is None and white is None:
            return Hooded(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Hooded(choice(pelt_colours), white, length)
        else:
            return Hooded(colour, white, length) 
    elif pelt == "Ponit":
        if colour is None and white is None:
            return Ponit(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ponit(choice(pelt_colours), white, length)
        else:
            return Ponit(colour, white, length) 
    elif pelt == "Spirit":
        if colour is None and not white:
            return Spirit(choice(pelt_colours), length)
        elif colour is None:
            return Spirit("WHITE", length)
        else:
            return Spirit(colour, length) 
    if pelt == 'Wolf':
        if colour is None and not white:
            return Wolf(choice(pelt_colours), length)
        elif colour is None:
            return Wolf("WHITE", length)
        else:
            return Wolf(colour, length)
    elif pelt == 'WolfBicolour':
        if colour is None:
            return WolfBicolour(choice(pelt_c_no_white), length)
        else:
            return WolfBicolour(colour, length)
    elif pelt == 'Tortie':
        if white is None:
            return Tortie(colour, choice([False, True]), length)
        else:
            return Tortie(colour, white, length)
    else:
        return Calico(colour, length)

def describe_color(pelt, tortiebase, tortiecolour, white_patches, skin, short=False):
    """ short=True makes everything just slightly shorter, mainly for kit purposes. """
    
    if short:
        renamed_colors = {
            "ashbrown": "brown",
            "dustbrown": "brown",
            "darkbrown": "brown",
            "palecream": "cream",
            "bluegrey": "grey",
            "darkgrey": "grey"
        }
    else:
        renamed_colors = {
            "ashbrown": "ash brown",
            "dustbrown": "dust brown",
            "darkbrown": "dark brown",
            "palecream": "pale cream",
            "bluegrey": "blue-grey",
            "darkgrey": "dark grey",
        }

    pattern_des = {
        "Marbled": "marbled tabby",
        "Ticked": "ticked tabby",
        "Mackerel": "mackerel tabby",
        "Classic": "classic tabby",
        "Agouti": "ticked tabby",
        "Backed": "stripe backed",
        "Sokoke": "sokoke tabby",
        "Charcoal": "charcoal tabby",
        "Ghost": "ghost tabby",
        "Doberman": "doberman point",
        "Skele": "skeleton",
        "Hooded": "hooded charcoal tabby",
        "Ponit": "bleach point",
        "Spirit": "ghostly spirit",
        "WolfBicolour": "painted wolf"
    }
    
    color_name = str(pelt.colour).lower()
    if color_name in renamed_colors:
        color_name = renamed_colors[color_name]

    if skin in albino_sprites:
        color_name = "albino"      
    elif skin in melanistic_sprites:
        color_name = "melanistic"  

    if pelt.name not in ["SingleColour", "TwoColour", "Tortie", "Calico", "Wolf", "WolfBicolour"] and color_name == "white":
        color_name = "pale"

    if pelt.name in pattern_des:
        color_name += f" {pattern_des[pelt.name]}"
    elif pelt.name in ["Tortie", "Calico"]:
        if short:
            color_name = f"mottled"
        else:
            base = tortiebase.lower()
            if base in tabbies:
                base = 'tabby'
            elif base in spotted:
                base = 'spotted tabby'
            else:
                base = ''

            patches = tortiecolour.lower()
            if patches in renamed_colors:
                patches = renamed_colors[patches]
            color_name = f"{color_name} {patches} {pelt.name.lower()}"
    elif pelt.name not in ["SingleColour", "TwoColour"]:
        color_name = f"{color_name} {pelt.name.lower()}"

    if skin in sphynx:
        color_name = color_name + ' sphynx'

    if white_patches:
        if white_patches == "FULLWHITE":
            color_name = "stained"
        if white_patches in [high_white, mostly_white]:
            if pelt.name != "Calico":
                color_name = color_name + ' with patches'
        elif white_patches in vit and not short:
            # If short, don't include vit information. 
            color_name = color_name + " with vitilago"
        elif white_patches in point_markings and pelt.name not in ["Doberman", "Ponit"]:
            color_name = color_name + " point"
            if color_name == 'dark ginger point' or color_name == 'ginger point':
                color_name = "flame point"
        else:
            if pelt.name != "Calico":
                color_name = color_name + ' with patches'

    return color_name
