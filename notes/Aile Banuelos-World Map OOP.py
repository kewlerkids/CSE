class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, description="", up=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.up = up
        self.down = down


# Option 1
# Add dependent rooms after
R19A = Room("R19A")
parking_lot = Room('The parking Lot', None, R19A)

R19A.north = parking_lot

# Option 2
# Put them in quotes
R19A = Room("R19A", "parking_lot")
parking_lot = Room('The parking Lot', None, R19A)

# "R1A", "R1B", "REST", "R34", "ALL", "STR", "RBIDY", "RWN", "REN", "WAPT", "EAPT", "HALL", "DRO",
# "BALL", "BLR", "R1C", "RCLA", "RBLD", "VROOM", "TS", "PAT", "LARCH", "CUB", "UARCH", "LDR", "KIT", "MCRH",
# "MOT", "OFF", "FGR", "GRR", "AST", "PT", "BOOT", "BACK", "DEF", "NPT", "PILL"

R1A = Room('Lower Mid', "R1B", None, None, None, "You are at a narrow path and all you can do is go forward.",
           None, None)
R1B = Room('Mid', "R1C", "R34", "R1A", "REST", "You are at a narrow path and you have directions every way.",
           None, None)
REST = Room('Bench', None, "R1B", None, None, "This is just an old bench...", None, None)
R34 = Room('HayStack', None, "ALL", None, "R1B", "You are near a balcony and you can go west or east.", "RBIDY", None)
ALL = Room('Alley', "STR", None, "R34", None, "There is a door in front of you.", None, None)
STR = Room('Stairs', None, None, "ALL", None, "You ca go up some stairs.", "EAPT", None)
RBIDY = Room('Balcony', "RWN", None, None, None,
             "You're on a balcony you can jump into the haystacks or go through the window.", None, "R34")
RWN = Room('West of Bedroom', "WAPT", "REN", "RBIDY", None, "You are at the west end of a bedroom.", None, None)
REN = Room('East of Bedroom', None, None, None, "RWN",
           "You are at the west end of a bedroom there is a drawer and a bed to the east and a door in front of you.",
           None, None)
WAPT = Room('West Apartments', None, "EAPT", "RWN", None,
            "There are so stairs going down and a hallway east plus a door behind.", None, "BLR")
EAPT = Room('East Apartments', "HALL", None, None, "WAPT", "You are next to a long hall and stairs.", None, "STR")
HALL = Room('Long Hall', "DRO", None, "EAPT", None, "You are in the middle of a narrow and dark hall.", None, None)
DRO = Room('Door to second balcony', "BALL", None, "HALL", None,
           "You are next to a white wooden door and the narrow hall.", None, None)
BALL = Room('Second Balcony', None, None, "DRO", None,
            "You are at a very high place but you see a building below.", None, "VROOM")
BLR = Room('Boiler Room', "RBLD", None, None, None,
           "There's a boiler behind me and a door in front plus some stairs.", "WAPT", None)
R1C = Room('Upper Mid', None, "RBLD", "R1B", "RCLA",
           "There is a wall North and you have paths every other way.", None, None)
RCLA = Room('Close', None, "R1C", None, "LARCH", "It's a small corner you can go straight or back.", None, None)
RBLD = Room('Boiler Room Door', None, "PAT", "BLR", "R1C",
            "You are next to a nice wooden door to your back but there is also a path right.", None, None)
VROOM = Room('Hay Wagon', None, None, None, None,
             "You are on a soft wagon of hay you can jump onto a balcony or get down...", "BALL", "TS")
TS = Room('Truck Side', "FGR", None, "PAT", "BOOT", "You are next to a wagon and a building.", "VROOM", None)
PAT = Room('Patio', "TS", None, None, "RBLD", "You are underneath a patio that has sacks on the floor...", None, None)
LARCH = Room('Lower Arch Side', "UARCH", "RCLA", "CUB", None,
             "You can go into a little corner south or continue.", None, None)
CUB = Room('Cubby', "LARCH", None, None, None, "You are in a small corner with a little wooden box...", None, None)
UARCH = Room('Upper Arch Side', "LDR", "MCRH", "LARCH", None,
             "You see a door in front of you and a building to your east.", None, None)
LDR = Room('Library', None, None, "UARCH", "KIT",
           "It smells like fresh paper and there are shelves of books and a small hall west.", None, None)
KIT = Room('Kitchen', None, "LDR", None, None, "There is a kitchen here with pots pans and cabinets.", None, None)
MCRH = Room('Moto Near Arch', "MOT", "OFF", None, "UARCH",
            "You are near a small corner to your north and a building east.", None, None)
MOT = Room('Moto', None, None, "MCRH", None, "You are in a small corner and there is a plain cardboard box.",
           None, None)
OFF = Room('Off A Site', None, "FGR", "AST", "MCRH", "There is a wall North but directions every way.", None, None)
FGR = Room('Front of Graveyard', "GRR", "PT", "TS", "OFF",
           "There is a graveyard north a slope east and a building west.", None, None)
GRR = Room('Graveyard', None, None, "FGR", None,
           "There are graves around you and one seems to be dug up already...", None, None)
AST = Room('A site', "OFF", "DEF", "BACK", None, "You can go to the back or east. You are near a patio.", None, None)
PT = Room('Pit', "NPT", None, None, "FGR", "You are near an enclosed area and a building.", None, None)
BOOT = Room('Boost', "DEF", None, None, "PILL",
            "You are on a wooden box that seems very fragile and are under a patio.", None, None)
BACK = Room('Back A site', "AST", "PILL", None, None, "You are in a corner at the back of the site.", None, None)
DEF = Room('Default box', "FGR", "TS", "BOOT", "AST", "You are next to large boxes you can go multiple ways.",
           None, None)
NPT = Room('North of Pit', None, None, "PT", None, "You are in an enclosed area that looks very sneaky.", None, None)
PILL = Room('Pillar', None, "BOOT", None, "BACK", "You are hidden behind a pillar you can go east or west.", None, None)

