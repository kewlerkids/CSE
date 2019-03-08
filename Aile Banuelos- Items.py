# Engine, hull, key, wrench, wheel, baseball bat, book, apple, paint, gas.


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


class Tools(Items):
    def __init__(self, location, name, type_of):
        super(Tools, self).__init__(location, name)
        self.type = type_of


class Hammer(Tools):
    def __init__(self):
        super(Hammer, self).__init__("CUB", "Hammer", "Thick")


class Screw(Tools):
    def __init__(self):
        super(Screw, self).__init__("MOT", "Screw Driver", "Small")


class Utensil(Items):
    def __init__(self, location, name, type_of):
        super(Utensil, self).__init__(location, name)
        self.type = type_of


class Spoon(Utensil):
    def __init__(self):
        super(Spoon, self).__init__("KIT", "Spoon", "Rusty")


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


berry = BlackBerry()
print(berry.name)
