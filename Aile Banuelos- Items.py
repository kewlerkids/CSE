class Items(object):
    def __init__(self, location, name):
        self.location = location
        self.name = name


class Fruit(Items):
    def __init__(self, location, name, color, type_of):
        super(Fruit, self).__init__(location, name)
        self.color = color
        self.type = type_of


class Apple(Fruit):
    def __init__(self):
        super(Apple, self).__init__("PAT", "Apple", "Red", "Special Seedless")


class Banana(Fruit):
    def __init__(self):
        super(Banana, self).__init__("PAT", "Banana", "Yellow", "Ripe")


class BlackBerry(Fruit):
    def __init__(self):
        super(BlackBerry, self).__init__("PAT", "Black Berry", "Black", "Seedy")


class Liquids(Items):
    def __init__(self, location, name):
        super(Liquids, self).__init__(location, name)
        self.amount = 20


class Gas(Liquids):
    def __init__(self):
        super(Gas, self).__init__("KIT", "Gasoline")


class Paint(Liquids):
    def __init__(self):
        super(Paint, self).__init__("BOOT", "Bucket of paint")


class Tools(Items):
    def __init__(self, location, name, type_of):
        super(Tools, self).__init__(location, name)
        self.type = type_of


class BaseballBat(Tools):
    def __init__(self):
        super(BaseballBat, self).__init__("LBD", "Baseball Bat", "Wooden")


class Baseball(Tools):
    def __init__(self):
        super(Baseball, self).__init__("BACK", "Baseball", "White")


class Hammer(Tools):
    def __init__(self):
        super(Hammer, self).__init__("CUB", "Hammer", "Thick")


class Screw(Tools):
    def __init__(self):
        super(Screw, self).__init__("MOT", "Screw Driver", "Small")


class Wrench(Tools):
    def __init__(self):
        super(Wrench, self).__init__("PIT", "Wrench", "Small")


class Utensil(Items):
    def __init__(self, location, name, type_of):
        super(Utensil, self).__init__(location, name)
        self.type = type_of


class Spoon(Utensil):
    def __init__(self):
        super(Spoon, self).__init__("KIT", "Spoon", "Rusty")


class Key(Utensil):
    def __init__(self):
        super(Key, self).__init__("Rest", "Key", "Car Key")


class CarParts(Items):
    def __init__(self, location, name):
        super(CarParts, self).__init__(location, name)


class Engine(CarParts):
    def __init__(self):
        super(Engine, self).__init__("HALL", "Engine")


class Hull(CarParts):
    def __init__(self):
        super(Hull, self).__init__("R34", "Hull")


class Wheel(CarParts):
    def __init__(self):
        super(Wheel, self).__init__("Vroom", "Wheel")


class Fun(Items):
    def __init__(self, location, name):
        super(Fun, self).__init__(location, name)


class Diamonds(Fun):
    def __init__(self):
        super(Diamonds, self).__init__("GRA", "Diamonds")


class Books(Fun):
    def __init__(self):
        super(Books, self).__init__("LIB", "Books")


class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type, body_type):
        super(Car, self).__init__(name, engine_type)
        self.body_type = body_type
        self.hull = False
        self.steering_wheel = False
        self.engine_status = False  # because the engine is off
        self.fuel = 0


berry = BlackBerry()
print(berry.name)
