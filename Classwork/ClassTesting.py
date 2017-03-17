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

##########################################

r1 = Rectangle(3, 7)
r1.draw()

r2 = Square(4)
r2.draw()