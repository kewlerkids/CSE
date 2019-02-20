class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


# Option 1
# Add dependent rooms after
R19A = Room("R19A")
parking_lot = Room('The parking Lot', None, R19A)

R19A.north = parking_lot

# Option 2
# Put them in quotes
R19A = Room("R19A", "parking_lot")
parking_lot = Room('The parking Lot', None, R19A)


R1A = Room("R1A", "R1B", "REST", "R34", "ALL", "STR", "RBIDY", "RWN", "REN", "WAPT", "EAPT", "HALL", "DRO",
           "BALL", "BLR", "R1C", "RCLA", "RBLD", "VROOM", "TS", "PAT", "LARCH", "CUB", "UARCH", "LDR", "KIT", "MCRH",
           "MOT", "OFF", "FGR", "GRR", "AST", "PT", "BOOT", "BACK", "DEF", "NPT", "PILL")

R1B = Room('Mid', R1C, R34, R1A, REST, 'You are at a narrow path and you have directions every way.')

