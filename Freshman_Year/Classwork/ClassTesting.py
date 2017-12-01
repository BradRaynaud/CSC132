class Shape(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def draw(self):
        for i in range(self.width):
            print "*" * self.length
        print

class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self, length, width)
        self.length = length
        self.width = width

class Square(Shape):
    def __init__(self, side):
        Shape.__init__(self, side, side)
        self.length = side

class Triangle(Shape):
    def __init__(self, base):
        Shape.__init__(self, base, base)
        self.base = base

    def draw(self):
        for i in range(self.width):
            print "*" * (self.length - i)
        print


##########################################

r1 = Rectangle(3, 7)
r1.draw()

r2 = Square(4)
r2.draw()

t1 = Triangle(4)
t1.draw()