# ====================================================================================================================
# Classes
# ====================================================================================================================


class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, description="", up=None, down=None,
                 items=None):
        if items is None:
            items = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.up = up
        self.down = down
        self.items = items


class Items(object):
    def __init__(self, name):
        self.name = name


class Fruit(Items):
    def __init__(self, name, color, type_of):
        super(Fruit, self).__init__(name)
        self.color = color
        self.type = type_of


class Liquids(Items):
    def __init__(self, name):
        super(Liquids, self).__init__(name)
        self.amount = 20


class Tools(Items):
    def __init__(self, name, type_of):
        super(Tools, self).__init__(name)
        self.type = type_of


class Fun(Items):
    def __init__(self, name):
        super(Fun, self).__init__(name)


class Utensil(Items):
    def __init__(self, name, type_of):
        super(Utensil, self).__init__(name)
        self.type = type_of


class CarParts(Items):
    def __init__(self, name):
        super(CarParts, self).__init__(name)


class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type):
        super(Car, self).__init__(name, engine_type)
        self.hull = False
        self.wheel = False
        self.engine = False
        self.engine_status = False  # because the engine is off
        self.fuel = 0

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car turns on.")

    def move_forward(self):
        self.fuel -= 1
        print("You move forward")

    def turn_left(self):
        self.fuel -= 1
        print("You turn left.")

    def turn_right(self):
        self.fuel -= 1
        print("You turn right.")

    def turn_off(self):
        self.engine_status = False
        print("You turn the engine off.")


class Weapon(Items):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


# ====================================================================================================================
# Items
# ====================================================================================================================


class Apple(Fruit):
    def __init__(self):
        super(Apple, self).__init__("Apple", "Red", "Special Seedless")


class Banana(Fruit):
    def __init__(self):
        super(Banana, self).__init__("Banana", "Yellow", "Ripe")


class BlackBerry(Fruit):
    def __init__(self):
        super(BlackBerry, self).__init__("BlackBerry", "Black", "Seedy")


class Gas(Liquids):
    def __init__(self):
        super(Gas, self).__init__("Gas")


class Paint(Liquids):
    def __init__(self):
        super(Paint, self).__init__("Paint")


class BaseballBat(Tools):
    def __init__(self):
        super(BaseballBat, self).__init__("BaseballBat", "Wooden")


class Baseball(Tools):
    def __init__(self):
        super(Baseball, self).__init__("Baseball", "White")


class Hammer(Tools):
    def __init__(self):
        super(Hammer, self).__init__("Hammer", "Thick")


class Screw(Tools):
    def __init__(self):
        super(Screw, self).__init__("Screw", "Small")


class Wrench(Tools):
    def __init__(self):
        super(Wrench, self).__init__("Wrench", "Small")


class Spoon(Utensil):
    def __init__(self):
        super(Spoon, self).__init__("Spoon", "Rusty")


class Key(Utensil):
    def __init__(self):
        super(Key, self).__init__("Key", "Car Key")


class Engine(CarParts):
    def __init__(self):
        super(Engine, self).__init__("Engine")


class Hull(CarParts):
    def __init__(self):
        super(Hull, self).__init__("Hull")


class Wheel(CarParts):
    def __init__(self):
        super(Wheel, self).__init__("Wheel")


class Diamonds(Fun):
    def __init__(self):
        super(Diamonds, self).__init__("Diamonds")


class Books(Fun):
    def __init__(self):
        super(Books, self).__init__("Books")

# ====================================================================================================================
# Characters
# ====================================================================================================================


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

# Character
# c1 = Character("Orc1", 100, sword, None)
# c2 = Character("Orc2", 100, sword2, None)
# c1.attack(c2)


wheel1 = Wheel()
wrench1 = Wrench()
key1 = Key()
hull1 = Hull()
engine1 = Engine()
gas1 = Gas()
hammer1 = Hammer()
paint1 = Paint()
screw1 = Screw()

# ====================================================================================================================
# Rooms
# ====================================================================================================================


R1A = Room('Lower Mid', "R1B", None, None, None,
           "You are at a narrow path and all you can do is go North, but behind you is a broken down car..."
           "Type in help for help",
           None, None, [Car("Vroom vroom", "gas")])
R1B = Room('Mid', "R1C", "R34", "R1A", "REST", "You are at a narrow path still and you have directions every way.",
           None, None)
REST = Room('Bench', None, "R1B", None, None, "This is just an old bench...and a Key on the floor", None, None, [key1])
R34 = Room('HayStack', None, "ALL", None, "R1B", "You are near a balcony and you can go West or East.", "RBIDY", None)
ALL = Room('Alley', "STR", None, "R34", None, "There is a door North of you and a BaseballBat on the floor.",
           None, None, [BaseballBat()])
STR = Room('Stairs', None, None, "ALL", None, "You can go Up some stairs and on the side there is a cars Hull.",
           "EAPT", None, [hull1])
RBIDY = Room('Balcony', "RWN", None, None, None,
             "You're on a balcony you can jump Down into the haystacks or go North through the window.", None, "R34")
RWN = Room('West of Bedroom', "WAPT", "REN", "RBIDY", None, "You are at the west end of a bedroom.", None, None)
REN = Room('East of Bedroom', None, None, None, "RWN",
           "You are at the west end of a bedroom there is a drawer and a bed to the east and a door in front of you.",
           None, None)
WAPT = Room('West Apartments', None, "EAPT", "RWN", None,
            "There are so stairs going Down and a hallway East plus a door behind you South.", None, "BLR")
EAPT = Room('East Apartments', "HALL", None, None, "WAPT", "You are next to a long hall North and West, stairs Down.",
            None, "STR")
HALL = Room('Long Hall', "DRO", None, "EAPT", None,
            "You are in the middle of a narrow and dark hall, but there is a Baseball on the floor.",
            None, None, [Baseball()])
DRO = Room('Door to second balcony', "BALL", None, "HALL", None,
           "You are next to a white wooden door North and the narrow hall South.", None, None)
BALL = Room('Second Balcony', None, None, "DRO", None,
            "You are at a very high place but you see a building if you go Down.", None, "VROOM")
BLR = Room('Boiler Room', "RBLD", None, None, None,
           "There's a boiler behind me and a door in front, North, plus some stairs Up, and a Wrench.", "WAPT", None,
           [wrench1])
R1C = Room('Upper Mid', None, "RBLD", "R1B", "RCLA",
           "There is a wall North and you have paths every other way.", None, None)
RCLA = Room('Close', None, "R1C", None, "LARCH", "It's a small corner you can go straight or back.", None, None)
RBLD = Room('Boiler Room Door', None, "PAT", "BLR", "R1C",
            "You are next to a nice wooden door to your South but there is also a path East.", None, None)
VROOM = Room('Hay Truck', None, None, None, None,
             "You are on a soft truck of hay you can jump Up onto a balcony or get Down...", "BALL", "TS")
TS = Room('Truck Side', "FGR", None, "PAT", "BOOT",
          "You are next to a wagon and a building, you can try jumping Up on the wagon, or take the Wheel.",
          "VROOM", None, [wheel1])
PAT = Room('Patio', "TS", None, None, "RBLD",
           "You are underneath a patio that has an Apple, Banana, and a BlackBerry on the floor...",
           None, None, [Apple(), Banana(), BlackBerry()])
LARCH = Room('Lower Arch Side', "UARCH", "RCLA", "CUB", None,
             "You can go into a little corner south or continue.", None, None)
CUB = Room('Cubby', "LARCH", None, None, None, "You are in a small corner with a huge wooden box that's open..."
                                               "You look at it...there is also an Engine inside this box. Leave North.",
           None, None, [engine1])
UARCH = Room('Upper Arch Side', "LDR", "MCRH", "LARCH", None,
             "You see a door in front of you and a building to your East.", None, None)
LDR = Room('Library', None, None, "UARCH", "KIT",
           "It smells like fresh paper and there are shelves of Books and a small hall West.", None, None, [Books()])
KIT = Room('Kitchen', None, "LDR", None, None, "There is a kitchen here with pots pans, empty cabinets, and a Gas can.",
           None, None, [gas1])
MCRH = Room('Moto Near Arch', "MOT", "OFF", None, "UARCH",
            "You are near a small corner to your North and a building East.", None, None)
MOT = Room('Moto', None, None, "MCRH", None,
           "You are in a small corner and there is a plain cardboard box with a Hammer.", None, None, [hammer1])
OFF = Room('Off A Site', None, "FGR", "AST", "MCRH", "There is a wall North but directions every way.", None, None)
FGR = Room('Front of Graveyard', "GRR", "PT", "TS", "OFF",
           "There is a graveyard north a slope east and a building west.", None, None)
GRR = Room('Graveyard', None, None, "FGR", None,
           "There are graves around you and one seems to be dug up already, but... inside the grave are Diamonds!",
           None, None, [Diamonds()])
AST = Room('A site', "OFF", "DEF", "BACK", None, "You can go South or East. You are near a patio.", None, None)
PT = Room('Pit', "NPT", None, None, "FGR", "You are near an enclosed area and a building South.", None, None)
BOOT = Room('Boost', "DEF", None, None, "PILL",
            "You are on a wooden box that seems very fragile and are under a patio.", None, None)
BACK = Room('Back A site', "AST", "PILL", None, None,
            "You are in a corner at the back of the site with a Paint bucket ont the floor.", None, None, [paint1])
DEF = Room('Default box', "FGR", "TS", "BOOT", "AST", "You are next to large boxes you can go multiple ways.",
           None, None)
NPT = Room('North of Pit', None, None, "PT", None,
           "You are in an enclosed area that looks very hidden with Spoons all over the floor.", None, None, [Spoon()])
PILL = Room('Pillar', None, "BOOT", None, "BACK",
            "You are hidden behind a pillar, with a Screw on the floor, you can go East or West.", None, None,
            [screw1])


# ====================================================================================================================
# Player
# ====================================================================================================================

class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """ This method moves a character to a new location

        :param new_location: The variable containing a room object
        :return:
        """
        self.current_location = new_location

    def check_win(self):
        items_needed = [wheel1, hull1, engine1, key1, wrench1, hammer1, screw1, paint1, gas1]
        for items in items_needed:
            if items not in self.inventory:
                return False

        return True

# def print_inventory(self):
# for item in self.inventory:
# print(item.name)

inven = []

player = Player(R1A)


# ====================================================================================================================
# Controller
# ====================================================================================================================
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while playing:
    CarRepair = False
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower()in directions:
        try:
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]

            player.move(room_object)
        except KeyError:
            print("**I can't go that way.**")
        except AttributeError:
            print("**I can't go that way.**")
    else:
        print("Command Not Recognized")

    if "take " in command:
        item_name = command[5:]

        found_item = None
        # print(player.current_location.items)
        # print(player.current_location.items[0].name)
        for item in player.current_location.items:
            if item.name == item_name:
                found_item = item
        if found_item is not None:
            player.inventory.append(found_item)
            player.current_location.items.remove(found_item)
            print("")
            print("You found a(n) %s" % found_item.name)
            # player.print_inventory()
            print("")
            inven.append(found_item.name)

    if player.check_win():
        print("")
        print("You have successfully repaired the car!!")
        print("Time to go home and live life!")
        print("")
        playing = False

    if 'Diamonds' in inven:
        print("!!!!")
        print("You fell into the whole while taking these Diamonds and you here someone...")
        print("They start throwing dirt on you while you're in the whole")
        print("YOU'VE BEEN BURIED ALIVE!!")
        print("")
        playing = False

    if "inventory" in command:
        print("")
        print(player.inventory[:6])
        print(player.inventory[6:])
        print("")

    if "list" in command:
        print('''
        You need: A Wheel, A Hull, A Engine,and A Key.
        You need: A Wrench, A Hammer, and A Screw.
        You need: Paint and Gas. Paint to look good ;)
        ''')

    if "help" in command:
        print("")
        print("To see your inventory just put, inventory. To see what supplies you need put, list")
        print("In order to win you need to get the supplies so you can leave in the broken car")
        print("")
