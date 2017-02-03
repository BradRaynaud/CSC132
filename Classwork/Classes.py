class Point(object):
    def __init__(self, x=0, y=0):
            self.x = x
            self.y =y
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < -10:
            self._x= -10
        elif value > 10:
            self._x = 10
        else:
            self._x = value

    @property
    def  y(self):
        return self._y

    @y.setter
    def y(self,value):
        if value < -10:
            self._y= -10
        elif value > 10:
            self._y = 10
        else:
            self._y = value
p1 = Point()
p2 = Point(5,5)
p3 = Point(-50,50)

print "p1 = ({},{})".format(p1.x,p1.y)
print "p2 = ({},{})".format(p2.x, p2.y)
print "p3 = ({},{})".format(p3.x, p3.y)