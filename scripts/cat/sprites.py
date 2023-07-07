import pygame

import ujson

from scripts.game_structure.game_essentials import game

class Sprites():
    cat_tints = {}
    white_patches_tints = {}

    def __init__(self, original_size, new_size=None):
        self.size = original_size  # size of a single sprite in a spritesheet
        self.new_size = self.size * 2 if new_size is None else new_size
        self.spritesheets = {}
        self.images = {}
        self.groups = {}
        self.sprites = {}

        self.load_tints()

    def load_tints(self):
        try:
            with open("sprites/dicts/tint.json", 'r') as read_file:
                Sprites.cat_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading Tints")

        try:
            with open("sprites/dicts/white_patches_tint.json", 'r') as read_file:
                Sprites.white_patches_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading White Patches Tints")
            
    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def find_sprite(self, group_name, x, y):
        """
        Find singular sprite from a group.

        Parameters:
        group_name -- Name of Pygame group to find sprite from.
        x -- X-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        y -- Y-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        """
        # pixels will be calculated automatically, so for x and y, just use 0, 1, 2, 3 etc.
        new_sprite = pygame.Surface((self.size, self.size),
                                    pygame.HWSURFACE | pygame.SRCALPHA)
        new_sprite.blit(self.groups[group_name], (0, 0),
                        (x * self.size, y * self.size, (x + 1) * self.size,
                         (y + 1) * self.size))
        return new_sprite

    def make_group(self,
                   spritesheet,
                   pos,
                   name,
                   sprites_x=3,
                   sprites_y=7):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a sprite-sheet into groups of sprites that are easily accessible.

        Parameters:
        spritesheet -- Name of spritesheet.
        pos -- (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites.
        name -- Name of group to make.
        
        Keyword Arguments
        sprites_x -- Number of sprites horizontally (default: 3)
        sprites_y -- Number of sprites vertically (default: 3)
        """

        # making the group
        new_group = pygame.Surface(
            (self.size * sprites_x, self.size * sprites_y),
            pygame.HWSURFACE | pygame.SRCALPHA)
        new_group.blit(
            self.spritesheets[spritesheet], (0, 0),
            (pos[0] * sprites_x * self.size, pos[1] * sprites_y * self.size,
             (pos[0] + sprites_x) * self.size,
             (pos[1] + sprites_y) * self.size))

        self.groups[name] = new_group

        # splitting group into singular sprites and storing into self.sprites section
        x_spr = 0
        y_spr = 0
        for x in range(sprites_x * sprites_y):
            new_sprite = pygame.Surface((self.size, self.size),
                                        pygame.HWSURFACE | pygame.SRCALPHA)
            new_sprite.blit(new_group, (0, 0),
                            (x_spr * self.size, y_spr * self.size,
                             (x_spr + 1) * self.size, (y_spr + 1) * self.size))
            self.sprites[name + str(x)] = new_sprite
            x_spr += 1
            if x_spr == sprites_x:
                x_spr = 0
                y_spr += 1

    def load_scars(self):
        """
        Loads scar sprites and puts them into groups.
        """
        for a, i in enumerate(
                ["ONE", "TWO", "THREE", "MANLEG", "BRIGHTHEART", "MANTAIL", 
                 "BRIDGE", "RIGHTBLIND", "LEFTBLIND", "BOTHBLIND", "BURNPAWS", "BURNTAIL"]):
            sprites.make_group('scars', (a, 0), f'scars{i}')
        for a, i in enumerate(
                ["BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE",
                 "FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"]):
            sprites.make_group('scars', (a, 1), f'scars{i}')
        for a, i in enumerate(
                ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY", "TOETRAP", "SNAKE",
                 "LEGBITE", "NECKBITE", "FACE"]):
            sprites.make_group('scars', (a, 2), f'scars{i}')
        for a, i in enumerate(
                ["RASH", "DECLAWED"]):
            sprites.make_group('scars', (a, 3), f'scars{i}')
        # missing parts
        for a, i in enumerate(
                ["LEFTEAR", "RIGHTEAR", "NOTAIL", "NOLEFTEAR", "NORIGHTEAR", "NOEAR", "HALFTAIL", "NOPAW"]):
            sprites.make_group('missingscars', (a, 0), f'scars{i}')

            # Accessories
        for a, i in enumerate([
            "MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL"]):
            sprites.make_group('medcatherbs', (a, 0), f'acc_herbs{i}')
        for a, i in enumerate([
            "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS"]):
            sprites.make_group('medcatherbs', (a, 1), f'acc_herbs{i}')
        for a, i in enumerate([
            "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"]):
            sprites.make_group('medcatherbs', (a, 3), f'acc_herbs{i}')
        sprites.make_group('medcatherbs', (5, 2), 'acc_herbsDRY HERBS')

        for a, i in enumerate([
            "RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"]):
            sprites.make_group('medcatherbs', (a, 2), f'acc_wild{i}')
            
        for a, i in enumerate(["RAT BLACK", "RAT BROWN", "RAT CREAM"]):
            sprites.make_group('ratcessories', (a, 0), f'acc_wild{i}')
        for a, i in enumerate(["RAT WHITE", "RAT GREY", "RAT HOODED"]):
            sprites.make_group('ratcessories', (a, 1), f'acc_wild{i}')        
            
        for a, i in enumerate(["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"]):
            sprites.make_group('collars', (a, 0), f'collars{i}')
        for a, i in enumerate(["GREEN", "RAINBOW", "BLACK", "SPIKES", "WHITE"]):
            sprites.make_group('collars', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINK", "PURPLE", "MULTI", "INDIGO"]):
            sprites.make_group('collars', (a, 2), f'collars{i}')
        for a, i in enumerate([
            "CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL",
            "LIMEBELL"
        ]):
            sprites.make_group('bellcollars', (a, 0), f'collars{i}')
        for a, i in enumerate(
                ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL"]):
            sprites.make_group('bellcollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINKBELL", "PURPLEBELL", "MULTIBELL", "INDIGOBELL"]):
            sprites.make_group('bellcollars', (a, 2), f'collars{i}')
        for a, i in enumerate([
            "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
            "LIMEBOW"
        ]):
            sprites.make_group('bowcollars', (a, 0), f'collars{i}')
        for a, i in enumerate(
                ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW"]):
            sprites.make_group('bowcollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINKBOW", "PURPLEBOW", "MULTIBOW", "INDIGOBOW"]):
            sprites.make_group('bowcollars', (a, 2), f'collars{i}')
        for a, i in enumerate([
            "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", "REDNYLON",
            "LIMENYLON"
        ]):
            sprites.make_group('nyloncollars', (a, 0), f'collars{i}')
        for a, i in enumerate(
                ["GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON"]):
            sprites.make_group('nyloncollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON"]):
            sprites.make_group('nyloncollars', (a, 2), f'collars{i}')
        for a, i in enumerate(["CRIMSONHAT", "BLUEHAT", "YELLOWHAT", "CYANHAT", "REDHAT", 
                                "LIMEHAT"]):
            sprites.make_group('pibhat', (a, 0), f'collars{i}')
        for a, i in enumerate(["GREENHAT", "RAINBOWHAT", "BLACKHAT", "WHITEHAT"]):
            sprites.make_group('pibhat', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINKHAT", "PURPLEHAT", "MULTIHAT", "INDIGOHAT"]):
            sprites.make_group('pibhat', (a, 2), f'collars{i}')
        for a, i in enumerate(["CRIMSONBOOT", "BLUEBOOT", "YELLOWBOOT", "CYANBOOT", 
                                "REDBOOT", "LIMEBOOT"]):
            sprites.make_group('booties', (a, 0), f'collars{i}')
        for a, i in enumerate(["GREENBOOT", "RAINBOWBOOT", "BLACKBOOT", "SPIKESBOOT", 
                                "WHITEBOOT"]):
            sprites.make_group('booties', (a, 1), f'collars{i}')
        for a, i in enumerate(["PINKBOOT", "PURPLEBOOT", "MULTIBOOT", "INDIGOBOOT"]):
            sprites.make_group('booties', (a, 2), f'collars{i}')

# get the width and height of the spritesheet
lineart = pygame.image.load('sprites/lineart.png')
width, height = lineart.get_size()
del lineart # unneeded

# if anyone changes lineart for whatever reason update this
if width / 3 == height / 7:
    spriteSize = width / 3
else:
    spriteSize = 50 # default, what base clangen uses
    print(f"lineart.png is not 3x7, falling back to {spriteSize}")
    print(f"if you are a modder, please update scripts/cat/sprites.py and do a search for 'if width / 3 == height / 7:'")

del width, height # unneeded


# i am sorry for merge conflicts, modders :fadeaway:
sprites = Sprites(spriteSize)
#tiles = Sprites(64)

for x in [
    'lineart', 'lineartdead', 'lineartdf', 'shadersnewwhite', 'lightingnew',
    'eyes', 'eyes2', 'eyeshybrid', 'eyes2hybrid', 'sus', 'sus2',    
    'skin', 'skin2', 'skinsphynx', 'wings', 'manes', 
    'scars', 'missingscars', 'fademask', 'fadestarclan', 'fadedarkforest',
    'solidnaturals', 'solidprides', 'solidunnaturals'
]:
    if 'lineart' in x and game.config['fun']['april_fools']:
        sprites.spritesheet(f"sprites/aprilfools{x}.png", x)
    else:
        sprites.spritesheet(f"sprites/{x}.png", x)

for x in [
    'bellcollars', 'bowcollars', 'collars', 'medcatherbs', 'nyloncollars',
    'ratcessories', 'booties', 'pibhat'
]:
    sprites.spritesheet(f"sprites/accessories/{x}.png", x)    

for x in [
    'whitepatches', 'tortiepatchesmasks', 'vitilligopatches', 
    'colourpointpatches'
]:
    sprites.spritesheet(f"sprites/patches/{x}.png", x)    

for x in [
    'backednaturals', 'dobermannaturals', 'falsesolidnaturals', 'ponitnaturals', 'ratnaturals',
    'skelenaturals', 'skittynaturals', 'smokenaturals', 'stainnaturals', 'wolfnaturals',
    'backedprides', 'dobermanprides', 'falsesolidprides', 'ponitprides', 'ratprides',
    'skeleprides', 'skittyprides', 'smokeprides', 'stainprides', 'wolfprides', 'backedunnaturals', 
    'dobermanunnaturals', 'falsesolidunnaturals', 'ponitunnaturals', 'ratunnaturals',
    'skeleunnaturals', 'skittyunnaturals', 'smokeunnaturals', 'stainunnaturals', 'wolfunnaturals'
]:
    sprites.spritesheet(f"sprites/solid/{x}.png", x)    

for x in [
    'bandednaturals', 'bengalnaturals', 'dalmationnaturals', 'leonidnaturals', 'lynxnaturals',
    'rosettenaturals', 'snowflakenaturals', 'specklednaturals', 'bandedprides', 'bengalprides', 
    'dalmationprides', 'leonidprides', 'lynxprides', 'rosetteprides', 'snowflakeprides', 'speckledprides', 
    'bandedunnaturals', 'bengalunnaturals', 'dalmationunnaturals', 'leonidunnaturals', 'lynxunnaturals',
    'rosetteunnaturals', 'snowflakeunnaturals', 'speckledunnaturals'
]:
    sprites.spritesheet(f"sprites/spotted/{x}.png", x)  

for x in [
    'agoutinaturals', 'charcoalnaturals', 'classicnaturals', 'ghostnaturals', 'hoodednaturals', 'mackerelnaturals',
    'marblednaturals', 'merlenaturals', 'sokokenaturals', 'tabbynaturals', 'tickednaturals', 'agoutiprides', 
    'charcoalprides', 'classicprides', 'ghostprides', 'hoodedprides', 'mackerelprides', 'marbledprides', 
    'merleprides', 'sokokeprides', 'tabbyprides', 'tickedprides', 'agoutiunnaturals', 'charcoalunnaturals', 
    'classicunnaturals', 'ghostunnaturals', 'hoodedunnaturals', 'mackerelunnaturals','marbledunnaturals', 
    'merleunnaturals', 'sokokeunnaturals', 'tabbyunnaturals', 'tickedunnaturals'
]:
    sprites.spritesheet(f"sprites/tabby/{x}.png", x)  

for x in [
    'sparkledalmationnaturals', 'sparklelynxnaturals', 'sparklespecklednaturals', 'sparkletabbynaturals', 'spiritnaturals',
    'starpeltnaturals', 'sparkledalmationprides', 'sparklelynxprides', 'sparklespeckledprides', 'sparkletabbyprides', 'spiritprides',
    'starpeltprides', 'sparkledalmationunnaturals', 'sparklelynxunnaturals', 'sparklespeckledunnaturals', 'sparkletabbyunnaturals', 'spiritunnaturals',
    'starpeltunnaturals'
]:
    sprites.spritesheet(f"sprites/sparkle/{x}.png", x)  

# Line art
sprites.make_group('lineart', (0, 0), 'lines')
sprites.make_group('shadersnewwhite', (0, 0), 'shaders')
sprites.make_group('lightingnew', (0, 0), 'lighting')

sprites.make_group('lineartdead', (0, 0), 'lineartdead')
sprites.make_group('lineartdf', (0, 0), 'lineartdf')

# Fading Fog
for i in range(0, 3):
    sprites.make_group('fademask', (i, 0), f'fademask{i}')
    sprites.make_group('fadestarclan', (i, 0), f'fadestarclan{i}')
    sprites.make_group('fadedarkforest', (i, 0), f'fadedf{i}')

#Regular Eyes
for a, i in enumerate(['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 
        'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHERBLUE', 'SUNLITICE']):
    sprites.make_group('eyes', (a, 0), f'eyes{i}')
    sprites.make_group('eyes2', (a, 0), f'eyes2{i}')
for a, i in enumerate(['COPPER', 'SAGE', 'COBALT', 'PALEBLUE', 'BRONZE', 'SILVER',
        'PALEYELLOW', 'GOLD', 'GREENYELLOW']):
    sprites.make_group('eyes', (a, 1), f'eyes{i}')
    sprites.make_group('eyes2', (a, 1), f'eyes2{i}')
for a, i in enumerate(['POPPY', 'CRIMSON', 'RUBY', 'BROWN', 'JADE', 'SKY', 
        'LILAC', 'BROWNTWO', 'PEANUT', 'GREYTWO', 'YELLOWOLIVE', 'SUNSHINE']):
    sprites.make_group('eyeshybrid', (a, 0), f'eyes{i}')
    sprites.make_group('eyes2hybrid', (a, 0), f'eyes2{i}')
for a, i in enumerate(['AZURE', 'COBOLT', 'GRASS', 'MINT', 'LILACGREY', 'WHITE',
        'VIOLET', 'GRAPE', 'INDIGO', 'VOID', 'GHOST']):
    sprites.make_group('eyeshybrid', (a, 1), f'eyes{i}')
    sprites.make_group('eyes2hybrid', (a, 1), f'eyes2{i}')
for a, i in enumerate(['PRIMARY', 'PRIMARYB', 'PRIMARYC', 'CHROME', 'CHROMEB', 
        'CHROMEC', 'RGB', 'RGBTWO', 'RGBTHREE', 'MONOCHROME', 'MONOCHROMETWO', 'MONOCHROMETHREE']):
    sprites.make_group('eyeshybrid', (a, 2), f'eyes{i}')
    sprites.make_group('eyes2hybrid', (a, 2), f'eyes2{i}')
for a, i in enumerate(['POPPYPINK', 'STRAWBERRY', 'MINTCHOC', 'CHOCMINT', 'AMBERTWO', 'BEACH',
        'NACRE', 'NIGHT', 'OCEAN']):
    sprites.make_group('eyeshybrid', (a, 3), f'eyes{i}')
    sprites.make_group('eyes2hybrid', (a, 3), f'eyes2{i}')
#AmongUs SUS
for a, i in enumerate(['SUSVISOR', 'SUSGREY', 'SUSGREENGREY', 'SUSOLIVEGREY', 'SUSBROWNGREY', 'SUSBLUEGREY', 
    'SUSPURPLEGREY', 'SUSDARKCHROME', 'SUSNACRE', 'SUSNIGHT', 'SUSCHROME', 'SUSRGB']):
    sprites.make_group('sus', (a, 0), f'eyes{i}')
    sprites.make_group('sus2', (a, 0), f'eyes2{i}')
for a, i in enumerate(['SUSYELLOW', 'SUSAMBER', 'SUSGOLDGREEN', 'SUSBRIGHT', 'SUSMINTCHOC', 'SUSCHOCMINT',
    'SUSGREEN', 'SUSEMERALD', 'SUSJADE', 'SUSOLIVE', 'SUSGOLD', 'SUSRUSSET']):
    sprites.make_group('sus', (a, 1), f'eyes{i}')
    sprites.make_group('sus2', (a, 1), f'eyes2{i}')
for a, i in enumerate(['SUSPOPPY', 'SUSCRIMSON', 'SUSSCARLET', 'SUSGRAPE', 'SUSVIOLET', 'SUSSTRAWBERRY', 'SUSPINK',
    'SUSINDIGO', 'SUSBLUE', 'SUSBLUETWO', 'SUSCOBOLT', 'SUSTURQUOISE']):
    sprites.make_group('sus', (a, 2), f'eyes{i}')
    sprites.make_group('sus2', (a, 2), f'eyes2{i}')
for a, i in enumerate(['SUSSKY', 'SUSOCEAN', 'SUSYELLOWGREEN', 'SUSWHITE', 'SUSBLACK', 'SUSMELON', 'SUSBEACH',
    'SUSGREENYELLOW', 'SUSPEANUT', 'SUSBROWN', 'SUSBROWNTWO', 'SUSRUBEN']):
    sprites.make_group('sus', (a, 3), f'eyes{i}')
    sprites.make_group('sus2', (a, 3), f'eyes2{i}')    

# white patches
for a, i in enumerate(['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'VAN', 'ANYTWO', 'SAVANNAH', 
    'FADESPOTS', 'SKELEPATCH', 'HOODED', 'TOPCOVER', 'DAPPLEPAW', 'PEBBLESHINE', 'BUB']):
    sprites.make_group('whitepatches', (a, 0), f'white{i}')
for a, i in enumerate(['EXTRA', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'LIGHTSONG', 
    'BLACKSTAR', 'PIEBALD', 'CURVED', 'PETAL', 'SHIBAINU', 'BEARD', 'OWL', 'BOWTIE']):
    sprites.make_group('whitepatches', (a, 1), f'white{i}')
for a, i in enumerate(['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO', 'GOATEE', 
    'PAWS', 'MITAINE', 'BROKENBLAZE', 'SCOURGE', 'DIVA', 'WOODPECKER', 'BOOTS']):
    sprites.make_group('whitepatches', (a, 2), f'white{i}')
for a, i in enumerate(['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'HONEY',
    'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TAILTIP', 'TOES', 'MISS', 'COW', 'COWTWO']):
    sprites.make_group('whitepatches', (a, 3), f'white{i}')
for a, i in enumerate(
        ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW',
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'HALFWHITE', 'APPALOOSA', 'MOUSTACHE', 'REVERSEHEART']):
    sprites.make_group('whitepatches', (a, 4), f'white{i}')
for a, i in enumerate(['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'MAO', 'LUNA', 'CHESTSPECK', 
    'WINGS', 'PAINTED', 'HEARTTWO', 'FRINGEKIT', 'SPARROW', 'VEST']):
    sprites.make_group('whitepatches', (a, 5), 'white' + i)
for a, i in enumerate(['VENUS', 'CHANCE', 'MOSSCLAW', 'DAPPLED', 'NIGHTMIST', 'HAWK',
    'TWIST', 'RETSUKO', 'OKAPI', 'FRECKLEMASK', 'MOTH']):
    sprites.make_group('whitepatches', (a, 6), 'white' + i)

#Colourpoints
for a, i in enumerate(['COLOURPOINT', 'RAGDOLL', 'KARPATI', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']):
    sprites.make_group('colourpointpatches', (a, 0), f'white{i}')
for a, i in enumerate(['REVERSEPOINT', 'PONIT', 'LIGHTPOINT', 'SNOWSHOE', 'SNOWBOOT']):
    sprites.make_group('colourpointpatches', (a, 1), f'white{i}')

#Vitiligo
for a, i in enumerate(['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'POWDER', 'BLEACHED', 'SHADOWSIGHT']):
    sprites.make_group('vitilligopatches', (a, 0), f'white{i}')
for a, i in enumerate(['BLACKVIT', 'BLACKVITTWO', 'BLACKMOON', 'BLACKPHANTOM', 'BLACKPOWDER', 'BLACKENED',
    'BLACKSIGHT']):
    sprites.make_group('vitilligopatches', (a, 1), f'white{i}')

# single (solid)
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('solidnaturals', (a, 0), f'single{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('solidnaturals', (a, 1), f'single{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('solidnaturals', (a, 2), f'single{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('solidnaturals', (a, 3), f'single{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('solidnaturals', (a, 4), f'single{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('solidnaturals', (a, 5), f'single{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('solidnaturals', (a, 6), f'single{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('solidprides', (a, 0), f'single{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('solidprides', (a, 1), f'single{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('solidprides', (a, 2), f'single{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('solidunnaturals', (a, 0), f'single{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('solidunnaturals', (a, 1), f'single{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('solidunnaturals', (a, 2), f'single{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('solidunnaturals', (a, 3), f'single{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('solidunnaturals', (a, 4), f'single{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('solidunnaturals', (a, 5), f'single{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('solidunnaturals', (a, 6), f'single{i}')   

#false solid
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('falsesolidnaturals', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('falsesolidnaturals', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('falsesolidnaturals', (a, 2), f'falsesolid{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('falsesolidnaturals', (a, 3), f'falsesolid{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('falsesolidnaturals', (a, 4), f'falsesolid{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('falsesolidnaturals', (a, 5), f'falsesolid{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('falsesolidnaturals', (a, 6), f'falsesolid{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('falsesolidprides', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('falsesolidprides', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('falsesolidprides', (a, 2), f'falsesolid{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('falsesolidunnaturals', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('falsesolidunnaturals', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('falsesolidunnaturals', (a, 2), f'falsesolid{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('falsesolidunnaturals', (a, 3), f'falsesolid{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('falsesolidunnaturals', (a, 4), f'falsesolid{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('falsesolidunnaturals', (a, 5), f'falsesolid{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('falsesolidunnaturals', (a, 6), f'falsesolid{i}')  
    
# tabby
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('tabbynaturals', (a, 0), f'tabby{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('tabbynaturals', (a, 1), f'tabby{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('tabbynaturals', (a, 2), f'tabby{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('tabbynaturals', (a, 3), f'tabby{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('tabbynaturals', (a, 4), f'tabby{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('tabbynaturals', (a, 5), f'tabby{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('tabbynaturals', (a, 6), f'tabby{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('tabbyprides', (a, 0), f'tabby{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('tabbyprides', (a, 1), f'tabby{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('tabbyprides', (a, 2), f'tabby{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('tabbyunnaturals', (a, 0), f'tabby{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('tabbyunnaturals', (a, 1), f'tabby{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('tabbyunnaturals', (a, 2), f'tabby{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('tabbyunnaturals', (a, 3), f'tabby{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('tabbyunnaturals', (a, 4), f'tabby{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('tabbyunnaturals', (a, 5), f'tabby{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('tabbyunnaturals', (a, 6), f'tabby{i}')  
    
# marbled
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('marblednaturals', (a, 0), f'marbled{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('marblednaturals', (a, 1), f'marbled{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('marblednaturals', (a, 2), f'marbled{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('marblednaturals', (a, 3), f'marbled{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('marblednaturals', (a, 4), f'marbled{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('marblednaturals', (a, 5), f'marbled{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('marblednaturals', (a, 6), f'marbled{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('marbledprides', (a, 0), f'marbled{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('marbledprides', (a, 1), f'marbled{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('marbledprides', (a, 2), f'marbled{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('marbledunnaturals', (a, 0), f'marbled{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('marbledunnaturals', (a, 1), f'marbled{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('marbledunnaturals', (a, 2), f'marbled{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('marbledunnaturals', (a, 3), f'marbled{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('marbledunnaturals', (a, 4), f'marbled{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('marbledunnaturals', (a, 5), f'marbled{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('marbledunnaturals', (a, 6), f'marbled{i}')  
    
# rosette
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('rosettenaturals', (a, 0), f'rosette{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('rosettenaturals', (a, 1), f'rosette{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('rosettenaturals', (a, 2), f'rosette{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('rosettenaturals', (a, 3), f'rosette{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('rosettenaturals', (a, 4), f'rosette{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('rosettenaturals', (a, 5), f'rosette{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('rosettenaturals', (a, 6), f'rosette{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('rosetteprides', (a, 0), f'rosette{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('rosetteprides', (a, 1), f'rosette{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('rosetteprides', (a, 2), f'rosette{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('rosetteunnaturals', (a, 0), f'rosette{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('rosetteunnaturals', (a, 1), f'rosette{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('rosetteunnaturals', (a, 2), f'rosette{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('rosetteunnaturals', (a, 3), f'rosette{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('rosetteunnaturals', (a, 4), f'rosette{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('rosetteunnaturals', (a, 5), f'rosette{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('rosetteunnaturals', (a, 6), f'rosette{i}')    
    
# smoke
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('smokenaturals', (a, 0), f'smoke{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('smokenaturals', (a, 1), f'smoke{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('smokenaturals', (a, 2), f'smoke{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('smokenaturals', (a, 3), f'smoke{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('smokenaturals', (a, 4), f'smoke{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('smokenaturals', (a, 5), f'smoke{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('smokenaturals', (a, 6), f'smoke{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('smokeprides', (a, 0), f'smoke{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('smokeprides', (a, 1), f'smoke{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('smokeprides', (a, 2), f'smoke{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('smokeunnaturals', (a, 0), f'smoke{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('smokeunnaturals', (a, 1), f'smoke{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('smokeunnaturals', (a, 2), f'smoke{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('smokeunnaturals', (a, 3), f'smoke{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('smokeunnaturals', (a, 4), f'smoke{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('smokeunnaturals', (a, 5), f'smoke{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('smokeunnaturals', (a, 6), f'smoke{i}')  
    
# ticked
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('tickednaturals', (a, 0), f'ticked{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('tickednaturals', (a, 1), f'ticked{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('tickednaturals', (a, 2), f'ticked{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('tickednaturals', (a, 3), f'ticked{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('tickednaturals', (a, 4), f'ticked{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('tickednaturals', (a, 5), f'ticked{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('tickednaturals', (a, 6), f'ticked{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('tickedprides', (a, 0), f'ticked{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('tickedprides', (a, 1), f'ticked{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('tickedprides', (a, 2), f'ticked{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('tickedunnaturals', (a, 0), f'ticked{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('tickedunnaturals', (a, 1), f'ticked{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('tickedunnaturals', (a, 2), f'ticked{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('tickedunnaturals', (a, 3), f'ticked{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('tickedunnaturals', (a, 4), f'ticked{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('tickedunnaturals', (a, 5), f'ticked{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('tickedunnaturals', (a, 6), f'ticked{i}')  
    
# speckled
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('specklednaturals', (a, 0), f'speckled{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('specklednaturals', (a, 1), f'speckled{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('specklednaturals', (a, 2), f'speckled{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('specklednaturals', (a, 3), f'speckled{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('specklednaturals', (a, 4), f'speckled{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('specklednaturals', (a, 5), f'speckled{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('specklednaturals', (a, 6), f'speckled{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('speckledprides', (a, 0), f'speckled{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('speckledprides', (a, 1), f'speckled{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('speckledprides', (a, 2), f'speckled{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('speckledunnaturals', (a, 0), f'speckled{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('speckledunnaturals', (a, 1), f'speckled{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('speckledunnaturals', (a, 2), f'speckled{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('speckledunnaturals', (a, 3), f'speckled{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('speckledunnaturals', (a, 4), f'speckled{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('speckledunnaturals', (a, 5), f'speckled{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('speckledunnaturals', (a, 6), f'speckled{i}')  
    
# bengal
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('bengalnaturals', (a, 0), f'bengal{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('bengalnaturals', (a, 1), f'bengal{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('bengalnaturals', (a, 2), f'bengal{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('bengalnaturals', (a, 3), f'bengal{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('bengalnaturals', (a, 4), f'bengal{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('bengalnaturals', (a, 5), f'bengal{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('bengalnaturals', (a, 6), f'bengal{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('bengalprides', (a, 0), f'bengal{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('bengalprides', (a, 1), f'bengal{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('bengalprides', (a, 2), f'bengal{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('bengalunnaturals', (a, 0), f'bengal{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('bengalunnaturals', (a, 1), f'bengal{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('bengalunnaturals', (a, 2), f'bengal{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('bengalunnaturals', (a, 3), f'bengal{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('bengalunnaturals', (a, 4), f'bengal{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('bengalunnaturals', (a, 5), f'bengal{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('bengalunnaturals', (a, 6), f'bengal{i}')   
    
# mackerel
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('mackerelnaturals', (a, 0), f'mackerel{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('mackerelnaturals', (a, 1), f'mackerel{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('mackerelnaturals', (a, 2), f'mackerel{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('mackerelnaturals', (a, 3), f'mackerel{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('mackerelnaturals', (a, 4), f'mackerel{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('mackerelnaturals', (a, 5), f'mackerel{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('mackerelnaturals', (a, 6), f'mackerel{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('mackerelprides', (a, 0), f'mackerel{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('mackerelprides', (a, 1), f'mackerel{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('mackerelprides', (a, 2), f'mackerel{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('mackerelunnaturals', (a, 0), f'mackerel{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('mackerelunnaturals', (a, 1), f'mackerel{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('mackerelunnaturals', (a, 2), f'mackerel{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('mackerelunnaturals', (a, 3), f'mackerel{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('mackerelunnaturals', (a, 4), f'mackerel{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('mackerelunnaturals', (a, 5), f'mackerel{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('mackerelunnaturals', (a, 6), f'mackerel{i}')  
    
# classic
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('classicnaturals', (a, 0), f'classic{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('classicnaturals', (a, 1), f'classic{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('classicnaturals', (a, 2), f'classic{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('classicnaturals', (a, 3), f'classic{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('classicnaturals', (a, 4), f'classic{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('classicnaturals', (a, 5), f'classic{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('classicnaturals', (a, 6), f'classic{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('classicprides', (a, 0), f'classic{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('classicprides', (a, 1), f'classic{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('classicprides', (a, 2), f'classic{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('classicunnaturals', (a, 0), f'classic{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('classicunnaturals', (a, 1), f'classic{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('classicunnaturals', (a, 2), f'classic{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('classicunnaturals', (a, 3), f'classic{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('classicunnaturals', (a, 4), f'classic{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('classicunnaturals', (a, 5), f'classic{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('classicunnaturals', (a, 6), f'classic{i}')   
    
# sokoke
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('sokokenaturals', (a, 0), f'sokoke{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('sokokenaturals', (a, 1), f'sokoke{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('sokokenaturals', (a, 2), f'sokoke{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('sokokenaturals', (a, 3), f'sokoke{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('sokokenaturals', (a, 4), f'sokoke{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('sokokenaturals', (a, 5), f'sokoke{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('sokokenaturals', (a, 6), f'sokoke{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('sokokeprides', (a, 0), f'sokoke{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('sokokeprides', (a, 1), f'sokoke{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('sokokeprides', (a, 2), f'sokoke{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('sokokeunnaturals', (a, 0), f'sokoke{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('sokokeunnaturals', (a, 1), f'sokoke{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('sokokeunnaturals', (a, 2), f'sokoke{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('sokokeunnaturals', (a, 3), f'sokoke{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('sokokeunnaturals', (a, 4), f'sokoke{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('sokokeunnaturals', (a, 5), f'sokoke{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('sokokeunnaturals', (a, 6), f'sokoke{i}')  
    
# agouti
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('agoutinaturals', (a, 0), f'agouti{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('agoutinaturals', (a, 1), f'agouti{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('agoutinaturals', (a, 2), f'agouti{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('agoutinaturals', (a, 3), f'agouti{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('agoutinaturals', (a, 4), f'agouti{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('agoutinaturals', (a, 5), f'agouti{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('agoutinaturals', (a, 6), f'agouti{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('agoutiprides', (a, 0), f'agouti{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('agoutiprides', (a, 1), f'agouti{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('agoutiprides', (a, 2), f'agouti{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('agoutiunnaturals', (a, 0), f'agouti{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('agoutiunnaturals', (a, 1), f'agouti{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('agoutiunnaturals', (a, 2), f'agouti{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('agoutiunnaturals', (a, 3), f'agouti{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('agoutiunnaturals', (a, 4), f'agouti{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('agoutiunnaturals', (a, 5), f'agouti{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('agoutiunnaturals', (a, 6), f'agouti{i}')  
    
# backed
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('backednaturals', (a, 0), f'backed{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('backednaturals', (a, 1), f'backed{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('backednaturals', (a, 2), f'backed{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('backednaturals', (a, 3), f'backed{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('backednaturals', (a, 4), f'backed{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('backednaturals', (a, 5), f'backed{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('backednaturals', (a, 6), f'backed{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('backedprides', (a, 0), f'backed{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('backedprides', (a, 1), f'backed{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('backedprides', (a, 2), f'backed{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('backedunnaturals', (a, 0), f'backed{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('backedunnaturals', (a, 1), f'backed{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('backedunnaturals', (a, 2), f'backed{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('backedunnaturals', (a, 3), f'backed{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('backedunnaturals', (a, 4), f'backed{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('backedunnaturals', (a, 5), f'backed{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('backedunnaturals', (a, 6), f'backed{i}')  
    
# doberman
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('dobermannaturals', (a, 0), f'doberman{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('dobermannaturals', (a, 1), f'doberman{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('dobermannaturals', (a, 2), f'doberman{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('dobermannaturals', (a, 3), f'doberman{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('dobermannaturals', (a, 4), f'doberman{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('dobermannaturals', (a, 5), f'doberman{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('dobermannaturals', (a, 6), f'doberman{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('dobermanprides', (a, 0), f'doberman{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('dobermanprides', (a, 1), f'doberman{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('dobermanprides', (a, 2), f'doberman{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('dobermanunnaturals', (a, 0), f'doberman{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('dobermanunnaturals', (a, 1), f'doberman{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('dobermanunnaturals', (a, 2), f'doberman{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('dobermanunnaturals', (a, 3), f'doberman{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('dobermanunnaturals', (a, 4), f'doberman{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('dobermanunnaturals', (a, 5), f'doberman{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('dobermanunnaturals', (a, 6), f'doberman{i}')  
    
# ponit
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('ponitnaturals', (a, 0), f'ponit{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('ponitnaturals', (a, 1), f'ponit{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('ponitnaturals', (a, 2), f'ponit{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('ponitnaturals', (a, 3), f'ponit{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('ponitnaturals', (a, 4), f'ponit{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('ponitnaturals', (a, 5), f'ponit{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('ponitnaturals', (a, 6), f'ponit{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('ponitprides', (a, 0), f'ponit{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('ponitprides', (a, 1), f'ponit{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('ponitprides', (a, 2), f'ponit{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('ponitunnaturals', (a, 0), f'ponit{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('ponitunnaturals', (a, 1), f'ponit{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('ponitunnaturals', (a, 2), f'ponit{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('ponitunnaturals', (a, 3), f'ponit{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('ponitunnaturals', (a, 4), f'ponit{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('ponitunnaturals', (a, 5), f'ponit{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('ponitunnaturals', (a, 6), f'ponit{i}')  
    
# rat
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('ratnaturals', (a, 0), f'rat{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('ratnaturals', (a, 1), f'rat{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('ratnaturals', (a, 2), f'rat{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('ratnaturals', (a, 3), f'rat{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('ratnaturals', (a, 4), f'rat{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('ratnaturals', (a, 5), f'rat{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('ratnaturals', (a, 6), f'rat{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('ratprides', (a, 0), f'rat{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('ratprides', (a, 1), f'rat{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('ratprides', (a, 2), f'rat{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('ratunnaturals', (a, 0), f'rat{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('ratunnaturals', (a, 1), f'rat{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('ratunnaturals', (a, 2), f'rat{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('ratunnaturals', (a, 3), f'rat{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('ratunnaturals', (a, 4), f'rat{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('ratunnaturals', (a, 5), f'rat{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('ratunnaturals', (a, 6), f'rat{i}')  
    
# skele
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('skelenaturals', (a, 0), f'skele{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('skelenaturals', (a, 1), f'skele{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('skelenaturals', (a, 2), f'skele{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('skelenaturals', (a, 3), f'skele{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('skelenaturals', (a, 4), f'skele{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('skelenaturals', (a, 5), f'skele{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('skelenaturals', (a, 6), f'skele{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('skeleprides', (a, 0), f'skele{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('skeleprides', (a, 1), f'skele{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('skeleprides', (a, 2), f'skele{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('skeleunnaturals', (a, 0), f'skele{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('skeleunnaturals', (a, 1), f'skele{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('skeleunnaturals', (a, 2), f'skele{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('skeleunnaturals', (a, 3), f'skele{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('skeleunnaturals', (a, 4), f'skele{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('skeleunnaturals', (a, 5), f'skele{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('skeleunnaturals', (a, 6), f'skele{i}')  
    
# skitty
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('skittynaturals', (a, 0), f'skitty{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('skittynaturals', (a, 1), f'skitty{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('skittynaturals', (a, 2), f'skitty{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('skittynaturals', (a, 3), f'skitty{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('skittynaturals', (a, 4), f'skitty{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('skittynaturals', (a, 5), f'skitty{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('skittynaturals', (a, 6), f'skitty{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('skittyprides', (a, 0), f'skitty{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('skittyprides', (a, 1), f'skitty{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('skittyprides', (a, 2), f'skitty{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('skittyunnaturals', (a, 0), f'skitty{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('skittyunnaturals', (a, 1), f'skitty{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('skittyunnaturals', (a, 2), f'skitty{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('skittyunnaturals', (a, 3), f'skitty{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('skittyunnaturals', (a, 4), f'skitty{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('skittyunnaturals', (a, 5), f'skitty{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('skittyunnaturals', (a, 6), f'skitty{i}')  
    
# stain
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('stainnaturals', (a, 0), f'stain{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('stainnaturals', (a, 1), f'stain{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('stainnaturals', (a, 2), f'stain{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('stainnaturals', (a, 3), f'stain{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('stainnaturals', (a, 4), f'stain{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('stainnaturals', (a, 5), f'stain{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('stainnaturals', (a, 6), f'stain{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('stainprides', (a, 0), f'stain{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('stainprides', (a, 1), f'stain{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('stainprides', (a, 2), f'stain{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('stainunnaturals', (a, 0), f'stain{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('stainunnaturals', (a, 1), f'stain{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('stainunnaturals', (a, 2), f'stain{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('stainunnaturals', (a, 3), f'stain{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('stainunnaturals', (a, 4), f'stain{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('stainunnaturals', (a, 5), f'stain{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('stainunnaturals', (a, 6), f'stain{i}')   
    
# wolf
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('wolfnaturals', (a, 0), f'wolf{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('wolfnaturals', (a, 1), f'wolf{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('wolfnaturals', (a, 2), f'wolf{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('wolfnaturals', (a, 3), f'wolf{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('wolfnaturals', (a, 4), f'wolf{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('wolfnaturals', (a, 5), f'wolf{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('wolfnaturals', (a, 6), f'wolf{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('wolfprides', (a, 0), f'wolf{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('wolfprides', (a, 1), f'wolf{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('wolfprides', (a, 2), f'wolf{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('wolfunnaturals', (a, 0), f'wolf{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('wolfunnaturals', (a, 1), f'wolf{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('wolfunnaturals', (a, 2), f'wolf{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('wolfunnaturals', (a, 3), f'wolf{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('wolfunnaturals', (a, 4), f'wolf{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('wolfunnaturals', (a, 5), f'wolf{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('wolfunnaturals', (a, 6), f'wolf{i}')  
    
# banded
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('bandednaturals', (a, 0), f'banded{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('bandednaturals', (a, 1), f'banded{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('bandednaturals', (a, 2), f'banded{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('bandednaturals', (a, 3), f'banded{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('bandednaturals', (a, 4), f'banded{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('bandednaturals', (a, 5), f'banded{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('bandednaturals', (a, 6), f'banded{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('bandedprides', (a, 0), f'banded{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('bandedprides', (a, 1), f'banded{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('bandedprides', (a, 2), f'banded{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('bandedunnaturals', (a, 0), f'banded{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('bandedunnaturals', (a, 1), f'banded{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('bandedunnaturals', (a, 2), f'banded{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('bandedunnaturals', (a, 3), f'banded{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('bandedunnaturals', (a, 4), f'banded{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('bandedunnaturals', (a, 5), f'banded{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('bandedunnaturals', (a, 6), f'banded{i}')  
    
# snowflake
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('snowflakenaturals', (a, 0), f'snowflake{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('snowflakenaturals', (a, 1), f'snowflake{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('snowflakenaturals', (a, 2), f'snowflake{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('snowflakenaturals', (a, 3), f'snowflake{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('snowflakenaturals', (a, 4), f'snowflake{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('snowflakenaturals', (a, 5), f'snowflake{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('snowflakenaturals', (a, 6), f'snowflake{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('snowflakeprides', (a, 0), f'snowflake{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('snowflakeprides', (a, 1), f'snowflake{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('snowflakeprides', (a, 2), f'snowflake{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('snowflakeunnaturals', (a, 0), f'snowflake{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('snowflakeunnaturals', (a, 1), f'snowflake{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('snowflakeunnaturals', (a, 2), f'snowflake{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('snowflakeunnaturals', (a, 3), f'snowflake{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('snowflakeunnaturals', (a, 4), f'snowflake{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('snowflakeunnaturals', (a, 5), f'snowflake{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('snowflakeunnaturals', (a, 6), f'snowflake{i}')  
    
# charcoal
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('charcoalnaturals', (a, 0), f'charcoal{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('charcoalnaturals', (a, 1), f'charcoal{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('charcoalnaturals', (a, 2), f'charcoal{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('charcoalnaturals', (a, 3), f'charcoal{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('charcoalnaturals', (a, 4), f'charcoal{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('charcoalnaturals', (a, 5), f'charcoal{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('charcoalnaturals', (a, 6), f'charcoal{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('charcoalprides', (a, 0), f'charcoal{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('charcoalprides', (a, 1), f'charcoal{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('charcoalprides', (a, 2), f'charcoal{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('charcoalunnaturals', (a, 0), f'charcoal{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('charcoalunnaturals', (a, 1), f'charcoal{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('charcoalunnaturals', (a, 2), f'charcoal{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('charcoalunnaturals', (a, 3), f'charcoal{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('charcoalunnaturals', (a, 4), f'charcoal{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('charcoalunnaturals', (a, 5), f'charcoal{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('charcoalunnaturals', (a, 6), f'charcoal{i}')  
    
# ghost
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('ghostnaturals', (a, 0), f'ghost{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('ghostnaturals', (a, 1), f'ghost{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('ghostnaturals', (a, 2), f'ghost{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('ghostnaturals', (a, 3), f'ghost{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('ghostnaturals', (a, 4), f'ghost{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('ghostnaturals', (a, 5), f'ghost{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('ghostnaturals', (a, 6), f'ghost{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('ghostprides', (a, 0), f'ghost{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('ghostprides', (a, 1), f'ghost{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('ghostprides', (a, 2), f'ghost{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('ghostunnaturals', (a, 0), f'ghost{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('ghostunnaturals', (a, 1), f'ghost{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('ghostunnaturals', (a, 2), f'ghost{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('ghostunnaturals', (a, 3), f'ghost{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('ghostunnaturals', (a, 4), f'ghost{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('ghostunnaturals', (a, 5), f'ghost{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('ghostunnaturals', (a, 6), f'ghost{i}')  
    
# hooded
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('hoodednaturals', (a, 0), f'hooded{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('hoodednaturals', (a, 1), f'hooded{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('hoodednaturals', (a, 2), f'hooded{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('hoodednaturals', (a, 3), f'hooded{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('hoodednaturals', (a, 4), f'hooded{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('hoodednaturals', (a, 5), f'hooded{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('hoodednaturals', (a, 6), f'hooded{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('hoodedprides', (a, 0), f'hooded{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('hoodedprides', (a, 1), f'hooded{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('hoodedprides', (a, 2), f'hooded{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('hoodedunnaturals', (a, 0), f'hooded{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('hoodedunnaturals', (a, 1), f'hooded{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('hoodedunnaturals', (a, 2), f'hooded{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('hoodedunnaturals', (a, 3), f'hooded{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('hoodedunnaturals', (a, 4), f'hooded{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('hoodedunnaturals', (a, 5), f'hooded{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('hoodedunnaturals', (a, 6), f'hooded{i}')  
    
# merle
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('merlenaturals', (a, 0), f'merle{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('merlenaturals', (a, 1), f'merle{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('merlenaturals', (a, 2), f'merle{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('merlenaturals', (a, 3), f'merle{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('merlenaturals', (a, 4), f'merle{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('merlenaturals', (a, 5), f'merle{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('merlenaturals', (a, 6), f'merle{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('merleprides', (a, 0), f'merle{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('merleprides', (a, 1), f'merle{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('merleprides', (a, 2), f'merle{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('merleunnaturals', (a, 0), f'merle{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('merleunnaturals', (a, 1), f'merle{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('merleunnaturals', (a, 2), f'merle{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('merleunnaturals', (a, 3), f'merle{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('merleunnaturals', (a, 4), f'merle{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('merleunnaturals', (a, 5), f'merle{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('merleunnaturals', (a, 6), f'merle{i}')   
    
# spirit
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('spiritnaturals', (a, 0), f'spirit{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('spiritnaturals', (a, 1), f'spirit{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('spiritnaturals', (a, 2), f'spirit{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('spiritnaturals', (a, 3), f'spirit{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('spiritnaturals', (a, 4), f'spirit{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('spiritnaturals', (a, 5), f'spirit{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('spiritnaturals', (a, 6), f'spirit{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('spiritprides', (a, 0), f'spirit{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('spiritprides', (a, 1), f'spirit{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('spiritprides', (a, 2), f'spirit{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('spiritunnaturals', (a, 0), f'spirit{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('spiritunnaturals', (a, 1), f'spirit{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('spiritunnaturals', (a, 2), f'spirit{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('spiritunnaturals', (a, 3), f'spirit{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('spiritunnaturals', (a, 4), f'spirit{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('spiritunnaturals', (a, 5), f'spirit{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('spiritunnaturals', (a, 6), f'spirit{i}')  
    
# dalmation
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('dalmationnaturals', (a, 0), f'dalmation{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('dalmationnaturals', (a, 1), f'dalmation{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('dalmationnaturals', (a, 2), f'dalmation{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('dalmationnaturals', (a, 3), f'dalmation{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('dalmationnaturals', (a, 4), f'dalmation{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('dalmationnaturals', (a, 5), f'dalmation{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('dalmationnaturals', (a, 6), f'dalmation{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('dalmationprides', (a, 0), f'dalmation{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('dalmationprides', (a, 1), f'dalmation{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('dalmationprides', (a, 2), f'dalmation{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('dalmationunnaturals', (a, 0), f'dalmation{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('dalmationunnaturals', (a, 1), f'dalmation{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('dalmationunnaturals', (a, 2), f'dalmation{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('dalmationunnaturals', (a, 3), f'dalmation{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('dalmationunnaturals', (a, 4), f'dalmation{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('dalmationunnaturals', (a, 5), f'dalmation{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('dalmationunnaturals', (a, 6), f'dalmation{i}')  
    
# leonid
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('leonidnaturals', (a, 0), f'leonid{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('leonidnaturals', (a, 1), f'leonid{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('leonidnaturals', (a, 2), f'leonid{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('leonidnaturals', (a, 3), f'leonid{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('leonidnaturals', (a, 4), f'leonid{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('leonidnaturals', (a, 5), f'leonid{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('leonidnaturals', (a, 6), f'leonid{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('leonidprides', (a, 0), f'leonid{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('leonidprides', (a, 1), f'leonid{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('leonidprides', (a, 2), f'leonid{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('leonidunnaturals', (a, 0), f'leonid{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('leonidunnaturals', (a, 1), f'leonid{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('leonidunnaturals', (a, 2), f'leonid{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('leonidunnaturals', (a, 3), f'leonid{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('leonidunnaturals', (a, 4), f'leonid{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('leonidunnaturals', (a, 5), f'leonid{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('leonidunnaturals', (a, 6), f'leonid{i}')  
    
# lynx
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('lynxnaturals', (a, 0), f'lynx{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('lynxnaturals', (a, 1), f'lynx{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('lynxnaturals', (a, 2), f'lynx{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('lynxnaturals', (a, 3), f'lynx{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('lynxnaturals', (a, 4), f'lynx{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('lynxnaturals', (a, 5), f'lynx{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('lynxnaturals', (a, 6), f'lynx{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('lynxprides', (a, 0), f'lynx{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('lynxprides', (a, 1), f'lynx{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('lynxprides', (a, 2), f'lynx{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('lynxunnaturals', (a, 0), f'lynx{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('lynxunnaturals', (a, 1), f'lynx{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('lynxunnaturals', (a, 2), f'lynx{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('lynxunnaturals', (a, 3), f'lynx{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('lynxunnaturals', (a, 4), f'lynx{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('lynxunnaturals', (a, 5), f'lynx{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('lynxunnaturals', (a, 6), f'lynx{i}')  
    
# starpelt
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('starpeltnaturals', (a, 0), f'starpelt{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('starpeltnaturals', (a, 1), f'starpelt{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('starpeltnaturals', (a, 2), f'starpelt{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('starpeltnaturals', (a, 3), f'starpelt{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('starpeltnaturals', (a, 4), f'starpelt{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('starpeltnaturals', (a, 5), f'starpelt{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('starpeltnaturals', (a, 6), f'starpelt{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('starpeltprides', (a, 0), f'starpelt{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('starpeltprides', (a, 1), f'starpelt{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('starpeltprides', (a, 2), f'starpelt{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('starpeltunnaturals', (a, 0), f'starpelt{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('starpeltunnaturals', (a, 1), f'starpelt{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('starpeltunnaturals', (a, 2), f'starpelt{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('starpeltunnaturals', (a, 3), f'starpelt{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('starpeltunnaturals', (a, 4), f'starpelt{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('starpeltunnaturals', (a, 5), f'starpelt{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('starpeltunnaturals', (a, 6), f'starpelt{i}')  
    
# sparkletabby
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('sparkletabbynaturals', (a, 0), f'sparkletabby{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('sparkletabbynaturals', (a, 1), f'sparkletabby{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('sparkletabbynaturals', (a, 2), f'sparkletabby{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('sparkletabbynaturals', (a, 3), f'sparkletabby{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('sparkletabbynaturals', (a, 4), f'sparkletabby{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('sparkletabbynaturals', (a, 5), f'sparkletabby{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('sparkletabbynaturals', (a, 6), f'sparkletabby{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('sparkletabbyprides', (a, 0), f'sparkletabby{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('sparkletabbyprides', (a, 1), f'sparkletabby{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('sparkletabbyprides', (a, 2), f'sparkletabby{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('sparkletabbyunnaturals', (a, 0), f'sparkletabby{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('sparkletabbyunnaturals', (a, 1), f'sparkletabby{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('sparkletabbyunnaturals', (a, 2), f'sparkletabby{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('sparkletabbyunnaturals', (a, 3), f'sparkletabby{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('sparkletabbyunnaturals', (a, 4), f'sparkletabby{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('sparkletabbyunnaturals', (a, 5), f'sparkletabby{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('sparkletabbyunnaturals', (a, 6), f'sparkletabby{i}')  
    
# sparklespeckled
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('sparklespecklednaturals', (a, 0), f'sparklespeckled{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('sparklespecklednaturals', (a, 1), f'sparklespeckled{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('sparklespecklednaturals', (a, 2), f'sparklespeckled{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('sparklespecklednaturals', (a, 3), f'sparklespeckled{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('sparklespecklednaturals', (a, 4), f'sparklespeckled{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('sparklespecklednaturals', (a, 5), f'sparklespeckled{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('sparklespecklednaturals', (a, 6), f'sparklespeckled{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('sparklespeckledprides', (a, 0), f'sparklespeckled{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('sparklespeckledprides', (a, 1), f'sparklespeckled{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('sparklespeckledprides', (a, 2), f'sparklespeckled{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('sparklespeckledunnaturals', (a, 0), f'sparklespeckled{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('sparklespeckledunnaturals', (a, 1), f'sparklespeckled{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('sparklespeckledunnaturals', (a, 2), f'sparklespeckled{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('sparklespeckledunnaturals', (a, 3), f'sparklespeckled{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('sparklespeckledunnaturals', (a, 4), f'sparklespeckled{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('sparklespeckledunnaturals', (a, 5), f'sparklespeckled{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('sparklespeckledunnaturals', (a, 6), f'sparklespeckled{i}')  
    
# sparkledalmation
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('sparkledalmationnaturals', (a, 0), f'sparkledalmation{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('sparkledalmationnaturals', (a, 1), f'sparkledalmation{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('sparkledalmationnaturals', (a, 2), f'sparkledalmation{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('sparkledalmationnaturals', (a, 3), f'sparkledalmation{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('sparkledalmationnaturals', (a, 4), f'sparkledalmation{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('sparkledalmationnaturals', (a, 5), f'sparkledalmation{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('sparkledalmationnaturals', (a, 6), f'sparkledalmation{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('sparkledalmationprides', (a, 0), f'sparkledalmation{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('sparkledalmationprides', (a, 1), f'sparkledalmation{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('sparkledalmationprides', (a, 2), f'sparkledalmation{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('sparkledalmationunnaturals', (a, 0), f'sparkledalmation{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('sparkledalmationunnaturals', (a, 1), f'sparkledalmation{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('sparkledalmationunnaturals', (a, 2), f'sparkledalmation{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('sparkledalmationunnaturals', (a, 3), f'sparkledalmation{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('sparkledalmationunnaturals', (a, 4), f'sparkledalmation{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('sparkledalmationunnaturals', (a, 5), f'sparkledalmation{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('sparkledalmationunnaturals', (a, 6), f'sparkledalmation{i}')   
    
# sparklelynx
for a, i in enumerate(['WHITE', 'BANNANA', 'PALECREAM', 'SAND', 'FARROW', 
    'CREAM', 'BEIGE', 'HAY', 'MEERKAT', 'KHAKI', 'SILVER', 'CADET']):
    sprites.make_group('sparklelynxnaturals', (a, 0), f'sparklelynx{i}')
for a, i in enumerate(['PANTONE', 'SAMON', 'THISTLE', 'WOOD', 'APRICOT', 
    'GINGER', 'GARFIELD', 'SUNSET', 'RUFOUS','HAZELNUT', 'BRONZE', 'MARENGO']):
    sprites.make_group('sparklelynxnaturals', (a, 1), f'sparklelynx{i}')
for a, i in enumerate(['GOLD', 'FIRE', 'BRICK', 'ROSE', 'DARKSAMON', 'CAPPUCCINO', 
    'ECRU', 'PINECONE', 'TAN', 'GREY', 'BLUEGREY', 'BATTLESHIP']):
    sprites.make_group('sparklelynxnaturals', (a, 2), f'sparklelynx{i}')
for a, i in enumerate(['HONEY', 'MEDALLION', 'APPLE', 'RED', 'CRIMSON', 'DUSTBROWN', 
    'ASHBROWN', 'SANDALWOOD', 'WRENGE', 'STEEL', 'SLATE']):
    sprites.make_group('sparklelynxnaturals', (a, 3), f'sparklelynx{i}')
for a, i in enumerate(['GRANOLA', 'SADDLE', 'CARMINE', 'SCARLET', 'MINK', 'BROWN', 
    'CHESTNUT', 'BEAVER', 'XANADU', 'SOOT']):
    sprites.make_group('sparklelynxnaturals', (a, 4), f'sparklelynx{i}')
for a, i in enumerate(['CEDAR', 'COSMOS', 'ROSEWOOD', 'DARKBROWN', 'CHOCOLATE', 'MOCHA', 
    'DARKGREY', 'CHARCOAL', 'ANCHOR']):
    sprites.make_group('sparklelynxnaturals', (a, 5), f'sparklelynx{i}')
for a, i in enumerate(['BURNT', 'BLOOD', 'COFFEE', 'TAUPE', 'UMBER', 'COAL', 'BLACK', 
    'PITCH']):
    sprites.make_group('sparklelynxnaturals', (a, 6), f'sparklelynx{i}')   
for a, i in enumerate(['DEMIENBY', 'DEMIBOY', 'TRANS', 'ARO', 'DEMIROM', 'AGENDER', 
    'PAN']):
    sprites.make_group('sparklelynxprides', (a, 0), f'sparklelynx{i}')
for a, i in enumerate(['DEMIGIRL', 'GENDERQUEER', 'DEMISEX', 'ASEXUAL', 'GENDER', 
    'BISEX', 'GLASS']):
    sprites.make_group('sparklelynxprides', (a, 1), f'sparklelynx{i}')
for a, i in enumerate(['POLY', 'ENBY', 'INTERSEX', 'MLM', 'WLW', 'GAYBOW']):
    sprites.make_group('sparklelynxprides', (a, 2), f'sparklelynx{i}')
for a, i in enumerate(['PALEBOW', 'IVORY', 'CORAL', 'CHARTRUSE', 'MINT', 'EMERALD', 
    'TURQUOISE', 'SKY', 'POWDERBLUE', 'INDIGOBLUE', 'MAGENTA']):
    sprites.make_group('sparklelynxunnaturals', (a, 0), f'sparklelynx{i}')
for a, i in enumerate(['PETAL', 'MEW', 'LIME', 'LETTUCE', 'GRASS', 'OLIVE', 'SHINYMEW', 
    'PUDDLE', 'TIFFANY', 'INDIGOLIGHT', 'HEATHER', 'AMYTHYST']):
    sprites.make_group('sparklelynxunnaturals', (a, 1), f'sparklelynx{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'FAWN', 'CORN', 'DARKOLIVE', 'SPINNACH', 
    'SAPPHIRE', 'OCEAN', 'ORCHID', 'FLORAL', 'CHERRY']):
    sprites.make_group('sparklelynxunnaturals', (a, 2), f'sparklelynx{i}')
for a, i in enumerate(['SUNSHINE', 'BEE', 'PYRITE', 'GREEN', 'SEAWEED', 'SACRAMENTO', 
    'TEAL', 'DENIUM', 'COBALT', 'STRAKIT', 'TART']):
    sprites.make_group('sparklelynxunnaturals', (a, 3), f'sparklelynx{i}')
for a, i in enumerate(['YELLOW', 'PINEAPPLE', 'SEAGRASS', 'JADE', 'SONIC', 'NAVY', 
    'PURPLE', 'WINE', 'BRIGHTCRIMSON', 'ROYALPURPLE']):
    sprites.make_group('sparklelynxunnaturals', (a, 4), f'sparklelynx{i}')
for a, i in enumerate(['TROMBONE', 'BRASS', 'FOREST', 'SEAFOAM', 'JEANS', 'JACKET', 
    'DEEPOCEAN', 'BARN', 'GARNET']):
    sprites.make_group('sparklelynxunnaturals', (a, 5), f'sparklelynx{i}')
for a, i in enumerate(['DIJON', 'RUST', 'DEEPFOREST', 'MALACHITE', 'NIGHTTIME', 'ONYX', 
    'RASIN', 'DUSKBOW']):
    sprites.make_group('sparklelynxunnaturals', (a, 6), f'sparklelynx{i}')  
 
# new new torties
for a, i in enumerate(['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 
    'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'OREO', 'SWOOP',
    'HALF']):
    sprites.make_group('tortiepatchesmasks', (a, 0), f"tortiemask{i}")
for a, i in enumerate(['MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 
    'STREAMSTRIKE', 'ORIOLE', 'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI',
    'CHIMERA']):
    sprites.make_group('tortiepatchesmasks', (a, 1), f"tortiemask{i}")
for a, i in enumerate(['SMUDGED', 'STREAK', 'MASK', 'CHEST', 'ARMTAIL','DAUB',
    'DAPPLENIGHT', 'BLANKET', 'EMBER', 'COMBO', 'BLENDED', 'SCATTER', 'LIGHT']):
    sprites.make_group('tortiepatchesmasks', (a, 2), f"tortiemask{i}")
for a, i in enumerate(['BROKENONE', 'BROKENTWO', 'BROKENTHREE', 'BROKENFOUR', 'GLITCH', 
    'WAVE', 'STRIPESMASK', 'KOI', 'SKULL', 'LITTLE', 'O', 'TOADSTOOL']):
    sprites.make_group('tortiepatchesmasks', (a, 3), f"tortiemask{i}")
for a, i in enumerate(['SPOTSCHAOS', 'FOG', 'SUNSET', 'TAIL', 'MOOSTONE', 'PONITMASK', 
    'REVPONITMASK', 'ERAPONITMASK', 'FALSESOLID', 'LYNXMASK']):
    sprites.make_group('tortiepatchesmasks', (a, 4), f"tortiemask{i}")
    
# SKINS
for a, i in enumerate(['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN']):
    sprites.make_group('skin', (a, 0), f"skin{i}")
for a, i in enumerate(['DARK', 'DARKGREY', 'GREY', 'DARKSALMON', 'SALMON', 'PEACH']):
    sprites.make_group('skin', (a, 1), f"skin{i}")
for a, i in enumerate(['DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']):
    sprites.make_group('skin', (a, 2), f"skin{i}")
for a, i in enumerate(['S_BLACK', 'S_RED', 'S_PINK', 'S_DARKBROWN', 'S_BROWN', 'S_LIGHTBROWN']):
    sprites.make_group('skinsphynx', (a, 0), f"skin{i}")
for a, i in enumerate(['S_DARK', 'S_DARKGREY', 'S_GREY', 'S_DARKSALMON', 'S_SALMON', 'S_PEACH']):
    sprites.make_group('skinsphynx', (a, 1), f"skin{i}")
for a, i in enumerate(['S_DARKMARBLED', 'S_MARBLED', 'S_LIGHTMARBLED', 'S_DARKBLUE', 'S_BLUE', 
        'S_LIGHTBLUE']):
    sprites.make_group('skinsphynx', (a, 2), f"skin{i}")
for a, i in enumerate(['BLACKMANE', 'REDMANE', 'PINKMANE', 'DARKBROWNMANE', 
    'BROWNMANE', 'LIGHTBROWNMANE']):
    sprites.make_group('manes', (a, 0), f"skin{i}")
for a, i in enumerate(['DARKMANE', 'DARKGREYMANE', 'GREYMANE', 'DARKSALMONMANE', 
    'SALMONMANE', 'PEACHMANE']):
    sprites.make_group('manes', (a, 1), f"skin{i}")
for a, i in enumerate(['DARKMARBLEDMANE', 'MARBLEDMANE', 'LIGHTMARBLEDMANE', 'DARKBLUEMANE', 
    'BLUEMANE', 'LIGHTBLUEMANE']):
    sprites.make_group('manes', (a, 2), f"skin{i}")    
for a, i in enumerate(['ALBINO', 'ALBINOSPHYNX', 'MELANISTIC', 'MELANISTICSPHYNX', 'SUSALBINO', 
    'SUSALBINOSPHYNX', 'SUSMELANISTIC', 'SUSMELANISTICSPHYNX']):
    sprites.make_group('skin2', (a, 0), f"skin{i}")
for a, i in enumerate(['ALBINOWING', 'MELANISTICWING', 'ALBINOMANE', 'MELANISTICMANE', 'SUSALBINOWING', 
    'SUSMELANISTICWING', 'SUSALBINOMANE', 'SUSMELANISTICMANE']):
    sprites.make_group('skin2', (a, 1), f"skin{i}")
for a, i in enumerate(['WHITEWING', 'BLUEGREENWING', 'REDWING', 'PURPLEFADEWING', 
    'RAINBOWWING', 'SILVERWING']):
    sprites.make_group('wings', (a, 0), f"skin{i}")
for a, i in enumerate(['STRAKITWING', 'SONICWING', 'MEWWING', 'OLIVEWING', 'GREENWING', 
    'GREYWING']):
    sprites.make_group('wings', (a, 1), f"skin{i}")
for a, i in enumerate(['GREYFADEWING', 'BROWNFADEWING', 'PARROTWING', 'GOLDWING', 'LIGHTBROWNWING', 
    'BLACKWING']):
    sprites.make_group('wings', (a, 2), f"skin{i}")


sprites.load_scars()
