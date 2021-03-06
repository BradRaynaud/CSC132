# classwork covered in 132
from random import randint
from math import pi


class Engine(object):
    def __init__(self, fuel):
        self.fuel = fuel

    def __str__(self):
        return str(self.fuel)


class Vehicle(object):
    def __init__(self, name):
        self.owner = name
        self.engine = Engine("Gas")
        self.tires = 4

    def __str__(self):
        return "Vehicle: Owner = {}, \t engine = {}, \t tires = {}".format(self.owner, self.engine, self.tires)


class Cycle(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 2

    def makeNoise():
        print"Vroom!" * 3


class Car(Vehicle):
    def __init__(self, name):
        Vehicle.__init__(self, name)


class Bicycle(Cycle):
    def __init__(self, name):
        Cycle.__init__(self, name)
        self.engine = Engine(None)

    def __str__(self):
        return "Bike:      \t\t"


class Motorcycle(Cycle):
    def __init__(self, name):
        Cycle.__init__(self, name)
        self.engine = Engine("Gas")

    def __str__(self):
        return "Motorcycle:\t\t" + Cycle.__str__(self)


##############################################################
c1 = Car("Mr.Bean")
b1 = Bicycle("Mr. Peabody")
m1 = Motorcycle("Vroomy")
c2 = Cycle("John")
v1 = Vehicle("Jane")
print c1
print b1
print m1
print c2
print v1

# c1.makeNoise()
b1.makeNoise()
m1.makeNoise()
c2.makeNoise()
# v1.makeNoise()
