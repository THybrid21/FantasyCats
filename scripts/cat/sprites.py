import pygame

try:
    import ujson
except ImportError:
    import json as ujson


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


sprites = Sprites(50)
#tiles = Sprites(64)

for x in [
    'lineart', 'lineartdead', 'lineartdf', 'eyes', 'eyes2', 'eyeshybrid', 
    'eyes2hybrid', 'skin', 'skin2', 'skinsphynx', 'scars', 'missingscars', 
    'shadersnewwhite', 'lightingnew', 'fademask', 'fadestarclan', 'fadedarkforest',
    'solidbrowns', 'solidgingers', 'solidgreys', 'solidblues', 'solidgreens',
    'solidpurples', 'solidyellows', 'solidpride'
]:
    sprites.spritesheet(f"sprites/{x}.png", x)

for x in [
    'bellcollars', 'bowcollars', 'collars', 'medcatherbs', 'nyloncollars'
]:
    sprites.spritesheet(f"sprites/accessories/{x}.png", x)    

for x in [
    'whitepatches', 'tortiepatchesmasks'
]:
    sprites.spritesheet(f"sprites/patches/{x}.png", x)    

for x in [
    'backedbrowns', 'backedgingers', 'backedgreys', 'backedblues', 'backedgreens',
    'backedpurples', 'backedyellows', 'backedpride', 'falsesolidgingers', 'falsesolidpurples',
    'falsesolidpride', 'smokebrowns', 'smokegingers', 'smokegreys', 'smokeblues', 'smokegreens',
    'smokepurples', 'smokeyellows', 'smokepride'
]:
    sprites.spritesheet(f"sprites/solid/{x}.png", x)    

for x in [
    'bengalbrowns', 'bengalgingers', 'bengalgreys', 'bengalblues', 'bengalgreens',
    'bengalpurples', 'bengalyellows', 'bengalpride', 'rosettebrowns', 'rosettegingers', 
    'rosettegreys', 'rosetteblues', 'rosettegreens', 'rosettepurples', 'rosetteyellows',
    'rosettepride', 'speckledbrowns', 'speckledgingers', 'speckledgreys', 'speckledblues', 
    'speckledgreens', 'speckledpurples', 'speckledyellows', 'speckledpride'
]:
    sprites.spritesheet(f"sprites/spotted/{x}.png", x)  

for x in [
    'agoutibrowns', 'agoutigingers', 'agoutigreys', 'agoutiblues', 'agoutigreens',
    'agoutipurples', 'agoutiyellows', 'agoutipride', 'classicbrowns', 'classicgingers', 
    'classicgreys', 'classicblues', 'classicblues', 'classicgreens', 'classicpurples', 'classicpride',
    'classicyellows', 'mackerelbrowns', 'mackerelgingers', 'mackerelgreys', 'mackerelblues',
    'mackerelgreens', 'mackerelpurples', 'mackerelyellows', 'mackerelpride', 'marbledbrowns',
    'marbledgingers', 'marbledgreys', 'marbledblues', 'marbledgreens', 'marbledpurples', 'marbledyellows',
    'marbledpride', 'sokokebrowns', 'sokokegingers', 'sokokegreys', 'sokokeblues', 'sokokegreens',
    'sokokepurples', 'sokokeyellows', 'sokokepride', 'tabbybrowns', 'tabbygingers', 'tabbygreys',
    'tabbyblues', 'tabbygreens', 'tabbypurples', 'tabbyyellows', 'tabbypride', 'tickedbrowns', 
    'tickedgingers', 'tickedgreys', 'tickedblues', 'tickedgreens', 'tickedpurples', 'tickedyellows',
    'tickedpride'
]:
    sprites.spritesheet(f"sprites/tabby/{x}.png", x)  

# Line art
sprites.make_group('lineart', (0, 0), 'lines')
sprites.make_group('shadersnewwhite', (0, 0), 'shaders')
sprites.make_group('lightingnew', (0, 0), 'lighting')

sprites.make_group('lineartdead', (0, 0), 'lineartdead')
sprites.make_group('lineartdf', (0, 0), 'lineartdf')

# Fading Fog
for i in range(1, 4):
    sprites.make_group('fademask', (i, 0), f'fademask{i}',)
    sprites.make_group('fadestarclan', (i, 0), f'fadestarclan{i}')
    sprites.make_group('fadedarkforest', (i, 0), f'fadedf{i}')

for a, i in enumerate(['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 
        'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHERBLUE', 'SUNLITICE']):
    sprites.make_group('eyes', (a, 0), f'eyes{i}')
    sprites.make_group('eyes2', (a, 0), f'eyes2{i}')
for a, i in enumerate(['COPPER', 'SAGE', 'COBALT', 'PALEBLUE', 'BRONZE', 'SILVER',
        'PALEYELLOW', 'GOLD', 'GREENYELLOW']):
    sprites.make_group('eyes', (a, 1), f'eyes{i}')
    sprites.make_group('eyes2', (a, 1), f'eyes2{i}')
for a, i in enumerate(['POPPY', 'CRIMSON', 'RUBY', 'BROWN', 'EMERALD2', 'SKY', 
        'LILAC', 'BROWN2', 'PEANUT', 'GREY2', 'YELLOWOLIVE', 'SUNSHINE']):
    sprites.make_group('eyeshybrid', (a, 0), f'eyes{i}')
    sprites.make_group('eyes2hybrid', (a, 0), f'eyes2{i}')
for a, i in enumerate(['AZURE', 'COBOLT', 'GRASS', 'MINT', 'LILACGREY', 'WHITE',
        'VIOLET', 'GRAPE', 'INDIGO', 'VOID', 'GHOST']):
    sprites.make_group('eyeshybrid', (a, 1), f'eyes{i}')
    sprites.make_group('eyes2hybrid', (a, 1), f'eyes2{i}')
for a, i in enumerate(['PRIMARY', 'PRIMARY2', 'PRIMARY3', 'CHROME', 'CHROME2', 
        'CHROME3', 'RBG', 'RBG2', 'RBG3', 'MONOCHROME', 'MONOCHROME2', 'MONOCHROME3']):
    sprites.make_group('eyeshybrid', (a, 2), f'eyes{i}')
    sprites.make_group('eyes2hybrid', (a, 2), f'eyes2{i}')
for a, i in enumerate(['POPPY2', 'STRAWBERRY', 'MINTCHOC', 'CHOCMINT', 'AMBER2', 'BEACH',
        'NACRE', 'NIGHT', 'OCEAN']):
    sprites.make_group('eyeshybrid', (a, 3), f'eyes{i}')
    sprites.make_group('eyes2hybrid', (a, 3), f'eyes2{i}')

# white patches
for a, i in enumerate(['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANYTWO',
    'MOON', 'PHANTOM', 'POWDER']):
    sprites.make_group('whitepatches', (a, 0), f'white{i}')
for a, i in enumerate(['EXTRA', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL', 
    'LIGHTSONG', 'VITILIGO', 'BLACKSTAR', 'PIEBALD', 'CURVED', 'PETAL']):
    sprites.make_group('whitepatches', (a, 1), f'white{i}')
# ryos white patches
for a, i in enumerate(['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO', 'GOATEE', 'VITILIGOTWO',
    'PAWS', 'MITAINE', 'BROKENBLAZE', 'SCOURGE']):
    sprites.make_group('whitepatches', (a, 2), f'white{i}')
for a, i in enumerate(['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'HONEY',
    'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TAILTIP', 'TOES']):
    sprites.make_group('whitepatches', (a, 3), f'white{i}')
for a, i in enumerate(
        ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW',
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA']):
    sprites.make_group('whitepatches', (a, 4), f'white{i}')
# beejeans white patches + perrio's point marks, painted, and heart2 + anju's new marks + key's blackstar
for a, i in enumerate(['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT',
    'MAO', 'LUNA', 'CHESTSPECK', 'WINGS', 'PAINTED', 'HEARTTWO']):
    sprites.make_group('whitepatches', (a, 5), 'white' + i)

# single (solid)
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('solidbrowns', (a, 0), f'single{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('solidbrowns', (a, 1), f'single{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('solidbrowns', (a, 2), f'single{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('solidbrowns', (a, 3), f'single{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('solidgingers', (a, 0), f'single{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('solidgingers', (a, 1), f'single{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('solidgingers', (a, 2), f'single{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('solidgingers', (a, 3), f'single{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('solidgreys', (a, 0), f'single{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('solidgreys', (a, 1), f'single{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('solidgreys', (a, 2), f'single{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('solidgreys', (a, 3), f'single{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('solidblues', (a, 0), f'single{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('solidblues', (a, 1), f'single{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('solidblues', (a, 2), f'single{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('solidgreens', (a, 0), f'single{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('solidgreens', (a, 1), f'single{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('solidgreens', (a, 2), f'single{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('solidgreens', (a, 3), f'single{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('solidpurples', (a, 0), f'single{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('solidpurples', (a, 1), f'single{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('solidpurples', (a, 2), f'single{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('solidpurples', (a, 3), f'single{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('solidyellows', (a, 0), f'single{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('solidyellows', (a, 1), f'single{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('solidyellows', (a, 2), f'single{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('solidyellows', (a, 3), f'single{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('solidpride', (a, 0), f'single{i}')
# tabby
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('tabbybrowns', (a, 0), f'tabby{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('tabbybrowns', (a, 1), f'tabby{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('tabbybrowns', (a, 2), f'tabby{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('tabbybrowns', (a, 3), f'tabby{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('tabbygingers', (a, 0), f'tabby{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('tabbygingers', (a, 1), f'tabby{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('tabbygingers', (a, 2), f'tabby{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('tabbygingers', (a, 3), f'tabby{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('tabbygreys', (a, 0), f'tabby{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('tabbygreys', (a, 1), f'tabby{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('tabbygreys', (a, 2), f'tabby{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('tabbygreys', (a, 3), f'tabby{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('tabbyblues', (a, 0), f'tabby{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('tabbyblues', (a, 1), f'tabby{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('tabbyblues', (a, 2), f'tabby{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('tabbygreens', (a, 0), f'tabby{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('tabbygreens', (a, 1), f'tabby{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('tabbygreens', (a, 2), f'tabby{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('tabbygreens', (a, 3), f'tabby{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('tabbypurples', (a, 0), f'tabby{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('tabbypurples', (a, 1), f'tabby{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('tabbypurples', (a, 2), f'tabby{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('tabbypurples', (a, 3), f'tabby{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('tabbyyellows', (a, 0), f'tabby{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('tabbyyellows', (a, 1), f'tabby{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('tabbyyellows', (a, 2), f'tabby{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('tabbyyellows', (a, 3), f'tabby{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('tabbypride', (a, 0), f'tabby{i}')
# marbled
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('marbledbrowns', (a, 0), f'marbled{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('marbledbrowns', (a, 1), f'marbled{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('marbledbrowns', (a, 2), f'marbled{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('marbledbrowns', (a, 3), f'marbled{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('marbledgingers', (a, 0), f'marbled{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('marbledgingers', (a, 1), f'marbled{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('marbledgingers', (a, 2), f'marbled{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('marbledgingers', (a, 3), f'marbled{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('marbledgreys', (a, 0), f'marbled{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('marbledgreys', (a, 1), f'marbled{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('marbledgreys', (a, 2), f'marbled{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('marbledgreys', (a, 3), f'marbled{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('marbledblues', (a, 0), f'marbled{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('marbledblues', (a, 1), f'marbled{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('marbledblues', (a, 2), f'marbled{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('marbledgreens', (a, 0), f'marbled{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('marbledgreens', (a, 1), f'marbled{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('marbledgreens', (a, 2), f'marbled{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('marbledgreens', (a, 3), f'marbled{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('marbledpurples', (a, 0), f'marbled{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('marbledpurples', (a, 1), f'marbled{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('marbledpurples', (a, 2), f'marbled{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('marbledpurples', (a, 3), f'marbled{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('marbledyellows', (a, 0), f'marbled{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('marbledyellows', (a, 1), f'marbled{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('marbledyellows', (a, 2), f'marbled{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('marbledyellows', (a, 3), f'marbled{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('marbledpride', (a, 0), f'marbled{i}')
# rosette
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('rosettebrowns', (a, 0), f'rosette{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('rosettebrowns', (a, 1), f'rosette{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('rosettebrowns', (a, 2), f'rosette{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('rosettebrowns', (a, 3), f'rosette{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('rosettegingers', (a, 0), f'rosette{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('rosettegingers', (a, 1), f'rosette{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('rosettegingers', (a, 2), f'rosette{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('rosettegingers', (a, 3), f'rosette{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('rosettegreys', (a, 0), f'rosette{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('rosettegreys', (a, 1), f'rosette{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('rosettegreys', (a, 2), f'rosette{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('rosettegreys', (a, 3), f'rosette{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('rosetteblues', (a, 0), f'rosette{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('rosetteblues', (a, 1), f'rosette{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('rosetteblues', (a, 2), f'rosette{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('rosettegreens', (a, 0), f'rosette{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('rosettegreens', (a, 1), f'rosette{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('rosettegreens', (a, 2), f'rosette{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('rosettegreens', (a, 3), f'rosette{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('rosettepurples', (a, 0), f'rosette{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('rosettepurples', (a, 1), f'rosette{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('rosettepurples', (a, 2), f'rosette{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('rosettepurples', (a, 3), f'rosette{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('rosetteyellows', (a, 0), f'rosette{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('rosetteyellows', (a, 1), f'rosette{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('rosetteyellows', (a, 2), f'rosette{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('rosetteyellows', (a, 3), f'rosette{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('rosettepride', (a, 0), f'rosette{i}')
# smoke
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('smokebrowns', (a, 0), f'smoke{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('smokebrowns', (a, 1), f'smoke{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('smokebrowns', (a, 2), f'smoke{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('smokebrowns', (a, 3), f'smoke{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('smokegingers', (a, 0), f'smoke{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('smokegingers', (a, 1), f'smoke{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('smokegingers', (a, 2), f'smoke{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('smokegingers', (a, 3), f'smoke{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('smokegreys', (a, 0), f'smoke{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('smokegreys', (a, 1), f'smoke{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('smokegreys', (a, 2), f'smoke{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('smokegreys', (a, 3), f'smoke{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('smokeblues', (a, 0), f'smoke{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('smokeblues', (a, 1), f'smoke{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('smokeblues', (a, 2), f'smoke{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('smokegreens', (a, 0), f'smoke{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('smokegreens', (a, 1), f'smoke{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('smokegreens', (a, 2), f'smoke{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('smokegreens', (a, 3), f'smoke{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('smokepurples', (a, 0), f'smoke{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('smokepurples', (a, 1), f'smoke{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('smokepurples', (a, 2), f'smoke{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('smokepurples', (a, 3), f'smoke{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('smokeyellows', (a, 0), f'smoke{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('smokeyellows', (a, 1), f'smoke{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('smokeyellows', (a, 2), f'smoke{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('smokeyellows', (a, 3), f'smoke{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('smokepride', (a, 0), f'smoke{i}')
# ticked
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('tickedbrowns', (a, 0), f'ticked{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('tickedbrowns', (a, 1), f'ticked{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('tickedbrowns', (a, 2), f'ticked{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('tickedbrowns', (a, 3), f'ticked{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('tickedgingers', (a, 0), f'ticked{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('tickedgingers', (a, 1), f'ticked{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('tickedgingers', (a, 2), f'ticked{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('tickedgingers', (a, 3), f'ticked{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('tickedgreys', (a, 0), f'ticked{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('tickedgreys', (a, 1), f'ticked{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('tickedgreys', (a, 2), f'ticked{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('tickedgreys', (a, 3), f'ticked{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('tickedblues', (a, 0), f'ticked{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('tickedblues', (a, 1), f'ticked{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('tickedblues', (a, 2), f'ticked{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('tickedgreens', (a, 0), f'ticked{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('tickedgreens', (a, 1), f'ticked{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('tickedgreens', (a, 2), f'ticked{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('tickedgreens', (a, 3), f'ticked{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('tickedpurples', (a, 0), f'ticked{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('tickedpurples', (a, 1), f'ticked{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('tickedpurples', (a, 2), f'ticked{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('tickedpurples', (a, 3), f'ticked{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('tickedyellows', (a, 0), f'ticked{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('tickedyellows', (a, 1), f'ticked{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('tickedyellows', (a, 2), f'ticked{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('tickedyellows', (a, 3), f'ticked{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('tickedpride', (a, 0), f'ticked{i}')
# speckled
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('speckledbrowns', (a, 0), f'speckled{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('speckledbrowns', (a, 1), f'speckled{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('speckledbrowns', (a, 2), f'speckled{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('speckledbrowns', (a, 3), f'speckled{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('speckledgingers', (a, 0), f'speckled{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('speckledgingers', (a, 1), f'speckled{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('speckledgingers', (a, 2), f'speckled{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('speckledgingers', (a, 3), f'speckled{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('speckledgreys', (a, 0), f'speckled{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('speckledgreys', (a, 1), f'speckled{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('speckledgreys', (a, 2), f'speckled{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('speckledgreys', (a, 3), f'speckled{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('speckledblues', (a, 0), f'speckled{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('speckledblues', (a, 1), f'speckled{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('speckledblues', (a, 2), f'speckled{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('speckledgreens', (a, 0), f'speckled{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('speckledgreens', (a, 1), f'speckled{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('speckledgreens', (a, 2), f'speckled{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('speckledgreens', (a, 3), f'speckled{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('speckledpurples', (a, 0), f'speckled{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('speckledpurples', (a, 1), f'speckled{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('speckledpurples', (a, 2), f'speckled{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('speckledpurples', (a, 3), f'speckled{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('speckledyellows', (a, 0), f'speckled{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('speckledyellows', (a, 1), f'speckled{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('speckledyellows', (a, 2), f'speckled{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('speckledyellows', (a, 3), f'speckled{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('speckledpride', (a, 0), f'speckled{i}')
# bengal
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('bengalbrowns', (a, 0), f'bengal{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('bengalbrowns', (a, 1), f'bengal{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('bengalbrowns', (a, 2), f'bengal{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('bengalbrowns', (a, 3), f'bengal{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('bengalgingers', (a, 0), f'bengal{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('bengalgingers', (a, 1), f'bengal{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('bengalgingers', (a, 2), f'bengal{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('bengalgingers', (a, 3), f'bengal{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('bengalgreys', (a, 0), f'bengal{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('bengalgreys', (a, 1), f'bengal{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('bengalgreys', (a, 2), f'bengal{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('bengalgreys', (a, 3), f'bengal{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('bengalblues', (a, 0), f'bengal{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('bengalblues', (a, 1), f'bengal{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('bengalblues', (a, 2), f'bengal{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('bengalgreens', (a, 0), f'bengal{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('bengalgreens', (a, 1), f'bengal{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('bengalgreens', (a, 2), f'bengal{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('bengalgreens', (a, 3), f'bengal{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('bengalpurples', (a, 0), f'bengal{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('bengalpurples', (a, 1), f'bengal{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('bengalpurples', (a, 2), f'bengal{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('bengalpurples', (a, 3), f'bengal{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('bengalyellows', (a, 0), f'bengal{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('bengalyellows', (a, 1), f'bengal{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('bengalyellows', (a, 2), f'bengal{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('bengalyellows', (a, 3), f'bengal{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('bengalpride', (a, 0), f'bengal{i}')
# mackerel
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('mackerelbrowns', (a, 0), f'mackerel{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('mackerelbrowns', (a, 1), f'mackerel{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('mackerelbrowns', (a, 2), f'mackerel{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('mackerelbrowns', (a, 3), f'mackerel{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('mackerelgingers', (a, 0), f'mackerel{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('mackerelgingers', (a, 1), f'mackerel{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('mackerelgingers', (a, 2), f'mackerel{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('mackerelgingers', (a, 3), f'mackerel{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('mackerelgreys', (a, 0), f'mackerel{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('mackerelgreys', (a, 1), f'mackerel{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('mackerelgreys', (a, 2), f'mackerel{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('mackerelgreys', (a, 3), f'mackerel{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('mackerelblues', (a, 0), f'mackerel{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('mackerelblues', (a, 1), f'mackerel{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('mackerelblues', (a, 2), f'mackerel{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('mackerelgreens', (a, 0), f'mackerel{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('mackerelgreens', (a, 1), f'mackerel{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('mackerelgreens', (a, 2), f'mackerel{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('mackerelgreens', (a, 3), f'mackerel{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('mackerelpurples', (a, 0), f'mackerel{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('mackerelpurples', (a, 1), f'mackerel{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('mackerelpurples', (a, 2), f'mackerel{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('mackerelpurples', (a, 3), f'mackerel{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('mackerelyellows', (a, 0), f'mackerel{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('mackerelyellows', (a, 1), f'mackerel{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('mackerelyellows', (a, 2), f'mackerel{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('mackerelyellows', (a, 3), f'mackerel{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('mackerelpride', (a, 0), f'mackerel{i}')
# classic
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('classicbrowns', (a, 0), f'classic{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('classicbrowns', (a, 1), f'classic{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('classicbrowns', (a, 2), f'classic{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('classicbrowns', (a, 3), f'classic{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('classicgingers', (a, 0), f'classic{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('classicgingers', (a, 1), f'classic{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('classicgingers', (a, 2), f'classic{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('classicgingers', (a, 3), f'classic{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('classicgreys', (a, 0), f'classic{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('classicgreys', (a, 1), f'classic{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('classicgreys', (a, 2), f'classic{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('classicgreys', (a, 3), f'classic{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('classicblues', (a, 0), f'classic{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('classicblues', (a, 1), f'classic{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('classicblues', (a, 2), f'classic{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('classicgreens', (a, 0), f'classic{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('classicgreens', (a, 1), f'classic{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('classicgreens', (a, 2), f'classic{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('classicgreens', (a, 3), f'classic{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('classicpurples', (a, 0), f'classic{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('classicpurples', (a, 1), f'classic{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('classicpurples', (a, 2), f'classic{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('classicpurples', (a, 3), f'classic{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('classicyellows', (a, 0), f'classic{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('classicyellows', (a, 1), f'classic{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('classicyellows', (a, 2), f'classic{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('classicyellows', (a, 3), f'classic{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('classicpride', (a, 0), f'classic{i}')
# sokoke
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('sokokebrowns', (a, 0), f'sokoke{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('sokokebrowns', (a, 1), f'sokoke{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('sokokebrowns', (a, 2), f'sokoke{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('sokokebrowns', (a, 3), f'sokoke{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('sokokegingers', (a, 0), f'sokoke{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('sokokegingers', (a, 1), f'sokoke{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('sokokegingers', (a, 2), f'sokoke{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('sokokegingers', (a, 3), f'sokoke{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('sokokegreys', (a, 0), f'sokoke{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('sokokegreys', (a, 1), f'sokoke{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('sokokegreys', (a, 2), f'sokoke{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('sokokegreys', (a, 3), f'sokoke{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('sokokeblues', (a, 0), f'sokoke{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('sokokeblues', (a, 1), f'sokoke{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('sokokeblues', (a, 2), f'sokoke{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('sokokegreens', (a, 0), f'sokoke{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('sokokegreens', (a, 1), f'sokoke{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('sokokegreens', (a, 2), f'sokoke{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('sokokegreens', (a, 3), f'sokoke{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('sokokepurples', (a, 0), f'sokoke{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('sokokepurples', (a, 1), f'sokoke{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('sokokepurples', (a, 2), f'sokoke{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('sokokepurples', (a, 3), f'sokoke{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('sokokeyellows', (a, 0), f'sokoke{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('sokokeyellows', (a, 1), f'sokoke{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('sokokeyellows', (a, 2), f'sokoke{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('sokokeyellows', (a, 3), f'sokoke{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('sokokepride', (a, 0), f'sokoke{i}')
# agouti
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('agoutibrowns', (a, 0), f'agouti{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('agoutibrowns', (a, 1), f'agouti{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('agoutibrowns', (a, 2), f'agouti{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('agoutibrowns', (a, 3), f'agouti{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('agoutigingers', (a, 0), f'agouti{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('agoutigingers', (a, 1), f'agouti{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('agoutigingers', (a, 2), f'agouti{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('agoutigingers', (a, 3), f'agouti{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('agoutigreys', (a, 0), f'agouti{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('agoutigreys', (a, 1), f'agouti{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('agoutigreys', (a, 2), f'agouti{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('agoutigreys', (a, 3), f'agouti{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('agoutiblues', (a, 0), f'agouti{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('agoutiblues', (a, 1), f'agouti{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('agoutiblues', (a, 2), f'agouti{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('agoutigreens', (a, 0), f'agouti{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('agoutigreens', (a, 1), f'agouti{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('agoutigreens', (a, 2), f'agouti{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('agoutigreens', (a, 3), f'agouti{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('agoutipurples', (a, 0), f'agouti{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('agoutipurples', (a, 1), f'agouti{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('agoutipurples', (a, 2), f'agouti{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('agoutipurples', (a, 3), f'agouti{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('agoutiyellows', (a, 0), f'agouti{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('agoutiyellows', (a, 1), f'agouti{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('agoutiyellows', (a, 2), f'agouti{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('agoutiyellows', (a, 3), f'agouti{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('agoutipride', (a, 0), f'agouti{i}')
# backed
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('backedbrowns', (a, 0), f'backed{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('backedbrowns', (a, 1), f'backed{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('backedbrowns', (a, 2), f'backed{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('backedbrowns', (a, 3), f'backed{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('backedgingers', (a, 0), f'backed{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('backedgingers', (a, 1), f'backed{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('backedgingers', (a, 2), f'backed{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('backedgingers', (a, 3), f'backed{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('backedgreys', (a, 0), f'backed{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('backedgreys', (a, 1), f'backed{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('backedgreys', (a, 2), f'backed{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('backedgreys', (a, 3), f'backed{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('backedblues', (a, 0), f'backed{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('backedblues', (a, 1), f'backed{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('backedblues', (a, 2), f'backed{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('backedgreens', (a, 0), f'backed{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('backedgreens', (a, 1), f'backed{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('backedgreens', (a, 2), f'backed{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('backedgreens', (a, 3), f'backed{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('backedpurples', (a, 0), f'backed{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('backedpurples', (a, 1), f'backed{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('backedpurples', (a, 2), f'backed{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('backedpurples', (a, 3), f'backed{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('backedyellows', (a, 0), f'backed{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('backedyellows', (a, 1), f'backed{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('backedyellows', (a, 2), f'backed{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('backedyellows', (a, 3), f'backed{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('backedpride', (a, 0), f'backed{i}')
#falsesolid
for a, i in enumerate(['BEIGE', 'MEERKAT', 'KHAKI', 'CAPPUCCINO', 'ECRU', 'ASHBROWN']):
    sprites.make_group('solidbrowns', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['DUSTBROWN', 'SANDALWOOD', 'PINECONE', 'WRENGE', 'BROWN', 'MINK']):
    sprites.make_group('solidbrowns', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['CHESTNUT', 'TAN', 'DARKBROWN', 'BEAVER', 'CHOCOLATE', 'MOCHA']):
    sprites.make_group('solidbrowns', (a, 2), f'falsesolid{i}')
for a, i in enumerate(['COFFEE', 'TAUPE', 'UMBER']):
    sprites.make_group('solidbrowns', (a, 3), f'falsesolid{i}')
for a, i in enumerate(['PALECREAM', 'CREAM', 'ROSE', 'GINGER', 'SUNSET', 'RUFOUS']):
    sprites.make_group('falsesolidgingers', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['SAND', 'WOOD', 'FIRE', 'BRICK', 'RED', 'SCARLET']):
    sprites.make_group('falsesolidgingers', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['APRICOT', 'GARFIELD', 'APPLE', 'CRIMSON', 'BURNT']):
    sprites.make_group('falsesolidgingers', (a, 2), f'falsesolid{i}')   
for a, i in enumerate(['CARMINE', 'COSMOS', 'ROSEWOOD', 'BLOOD']):
    sprites.make_group('falsesolidgingers', (a, 3), f'falsesolid{i}')  
for a, i in enumerate(['WHITE', 'SILVER', 'BRONZE', 'GREY', 'MARENGO', 'BATTLESHIP']):
    sprites.make_group('solidgreys', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['CADET', 'BLUEGREY', 'STEEL', 'SLATE', 'SOOT']):
    sprites.make_group('solidgreys', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['DARKGREY', 'ANCHOR', 'CHARCOAL']):
    sprites.make_group('solidgreys', (a, 2), f'falsesolid{i}')
for a, i in enumerate(['COAL', 'BLACK', 'PITCH']):
    sprites.make_group('solidgreys', (a, 3), f'falsesolid{i}')
for a, i in enumerate(['PALEBOW', 'TURQUOISE', 'TIFFANY', 'SAPPHIRE', 'OCEAN', 'DENIUM']):
    sprites.make_group('solidblues', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['SHINYMEW', 'SKY', 'TEAL', 'COBALT', 'SONIC']):
    sprites.make_group('solidblues', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['POWDERBLUE', 'JEANS', 'NAVY', 'DUSKBOW']):
    sprites.make_group('solidblues', (a, 2), f'falsesolid{i}')
for a, i in enumerate(['LIME', 'CHARTRUSE', 'LETTUCE', 'GRASS', 'MINT', 'EMERALD']):
    sprites.make_group('solidgreens', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['OLIVE', 'DARKOLIVE', 'GREEN', 'FOREST', 'JADE']):
    sprites.make_group('solidgreens', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['SPINNACH', 'SEAWEED', 'SACRAMENTO']):
    sprites.make_group('solidgreens', (a, 2), f'falsesolid{i}')
for a, i in enumerate(['XANADU', 'DEEPFOREST']):
    sprites.make_group('solidgreens', (a, 3), f'falsesolid{i}')
for a, i in enumerate(['PANTONE', 'SALMON', 'THISTLE', 'AMYTHYST', 'DARKSALMON', 'MAGENTA']):
    sprites.make_group('falsesolidpurples', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['PETAL', 'MEW', 'HEATHER', 'ORCHID', 'STRAKIT']):
    sprites.make_group('falsesolidpurples', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['PURPLE', 'WINE', 'RASIN']):
    sprites.make_group('falsesolidpurples', (a, 2), f'falsesolid{i}')
for a, i in enumerate(['GENDER', 'REDNEG']):
    sprites.make_group('falsesolidpurples', (a, 3), f'falsesolid{i}')
for a, i in enumerate(['IVORY', 'BANNANA', 'FARROW', 'HAY', 'FAWN', 'HAZELNUT']):
    sprites.make_group('solidyellows', (a, 0), f'falsesolid{i}')
for a, i in enumerate(['LEMON', 'LAGUNA', 'YELLOW', 'CORN', 'GOLD', 'HONEY']):
    sprites.make_group('solidyellows', (a, 1), f'falsesolid{i}')
for a, i in enumerate(['BEE', 'PINEAPPLE', 'TROMBONE', 'MEDALLION', 'GRANOLA']):
    sprites.make_group('solidyellows', (a, 2), f'falsesolid{i}')
for a, i in enumerate(['SADDLE', 'CEDAR', 'ONYX']):
    sprites.make_group('solidyellows', (a, 3), f'falsesolid{i}')
for a, i in enumerate(['AGENDER', 'ENBY', 'ASEXUAL', 'TRANS', 'GAYBOW']):
    sprites.make_group('falsesolidpride', (a, 0), f'falsesolid{i}')
    
# new new torties
for a, i in enumerate(['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH']):
    sprites.make_group('tortiepatchesmasks', (a, 0), f"tortiemask{i}")
for a, i in enumerate(['MINIMAL1', 'MINIMAL2', 'MINIMAL3', 'MINIMAL4', 'OREO', 'SWOOP']):
    sprites.make_group('tortiepatchesmasks', (a, 1), f"tortiemask{i}")
for a, i in enumerate(['MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE']):
    sprites.make_group('tortiepatchesmasks', (a, 2), f"tortiemask{i}")
for a, i in enumerate(['ORIOLE', 'ROBIN', 'BRINDLE', 'PAIGE']):
    sprites.make_group('tortiepatchesmasks', (a, 3), f"tortiemask{i}")

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
for a, i in enumerate(['ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET', 
        'ALBINOGREEN', 'ALBINOYELLOW']):
    sprites.make_group('skin2', (a, 0), f"skin{i}")
for a, i in enumerate(['MELANISTIC', 'MELANISTIC2', 'MELANISTIC3', 'S_MELANISTIC', 
        'S_MELANISTIC2', 'S_MELANISTIC3']):
    sprites.make_group('skin2', (a, 1), f"skin{i}")
for a, i in enumerate(['S_ALBINOPINK', 'S_ALBINOBLUE', 'S_ALBINORED', 'S_ALBINOVIOLET', 
        'S_ALBINOGREEN', 'S_ALBINOYELLOW']):
    sprites.make_group('skin2', (a, 2), f"skin{i}")


sprites.load_scars()
