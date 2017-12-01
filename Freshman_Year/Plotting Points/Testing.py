from random import randint

WIDTH = 400
HEIGHT = 800


class Point(object):
    def __init__(self, x, y):
        self.x = randint(0, WIDTH - 1)
        self.y = randint(0, HEIGHT - 1)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value




def PointGen():
    for i in range(2500):
        i = Point(1,1)
        print "{},{}".format(i.x,i.y)

PointGen()