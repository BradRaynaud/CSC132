import abc
class Animal(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, owner):
        self.owner = owner
    @abc.abstractmethod

class Snail(Animal):
    def __init__(self, owner):
        Animal.__init__(self, owner)

s1 = Snail("Anky")
print s1


a1 = Animal("dude")