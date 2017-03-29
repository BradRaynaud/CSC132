import abc

class Animal(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """constructs a new animal"""

    def __str__(self):
        return "Animal"

class Mammal(Animal):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        Animal.__init__(self)

    def __str__(self):
        return "mammal"

class Ape(Mammal):
    def __init__(self, owner = "Cincinnati Zoo"):
        Mammal.__init__(self)
        self.owner = owner

    def __str__(self):
        return "{}".format(self.owner) + " Ape" + Mammal.__str__(self)

class Wolf(Mammal):
    def __init__(self):
        Mammal.__init__(self)

    def __str__(self):
        return "Wolf"

class Snail(Animal):
    def __init__(self):
        Animal.__init__(self)


a1 = Ape()
a2 = Ape("Kong")
w1 = Wolf()
s1 = Snail()
print a1
print a2
print w1
print s1