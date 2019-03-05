# Engine, hull, key, wrench, wheel, baseball bat, book, apple, paint, gas.


class Items(object):
    def __init__(self, location, name):
        self.location = location
        self.name = name


class Fruit(Items):
    def __init__(self, location, name, color, type_of):
        super(Items, self).__init__(location, name, color, type_of)
        self.color = color
        self.type = type_of


class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type, body_type):
        super(Car, self).__init__(name, engine_type)
        self.body_type = body_type
        self.steering_wheel = True
        self.engine_status = False  # because the engine is off
        self.fuel = 100
