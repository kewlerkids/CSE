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
RBLD = Room('', None, None, None, None, "", None, None)
VROOM = Room('', None, None, None, None, "", None, None)
TS = Room('', None, None, None, None, "", None, None)
PAT = Room('', None, None, None, None, "", None, None)
LARCH = Room('', None, None, None, None, "", None, None)
CUB = Room('', None, None, None, None, "", None, None)
UARCH = Room('', None, None, None, None, "", None, None)
LDR = Room('', None, None, None, None, "", None, None)
KIT = Room('', None, None, None, None, "", None, None)
MCRH = Room('', None, None, None, None, "", None, None)
MOT = Room('', None, None, None, None, "", None, None)
OFF = Room('', None, None, None, None, "", None, None)
FGR = Room('', None, None, None, None, "", None, None)
GRR = Room('', None, None, None, None, "", None, None)
AST = Room('', None, None, None, None, "", None, None)
PT = Room('', None, None, None, None, "", None, None)
BOOT = Room('', None, None, None, None, "", None, None)
BACK = Room('', None, None, None, None, "", None, None)
DEF = Room('', None, None, None, None, "", None, None)
NPT = Room('', None, None, None, None, "", None, None)
PILL = Room('', None, None, None, None, "", None, None)

