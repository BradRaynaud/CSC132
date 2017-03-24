# Multiple inheriance

class Thing(object):
    def __init__(self):
        pass
    def __str__(self):
        return "thing"

class Fruit(Thing):
    def __init__(self, origin, fresh):
        Thing.__init__(self)
        self.origin = origin
        self.fresh = False

class Item(Thing):
    def __init__(self, price, weight):
        Thing.__init__(self)
        self.price = price
        self.weight = weight

    def __str__(self):
        return "Item"

class Banana(Fruit, Item):
    def __init__(self, price, weight, origin, fresh):
        Fruit.__init__(self, origin, fresh)
        Item.__init__(self, price, weight)

b1 = Banana(2.99, 1, "Mexico", True)
print b1