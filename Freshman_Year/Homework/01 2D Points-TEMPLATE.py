######################################################################################################################
# Name: Brad Raynaud
# Date: 3/17/2017
# Description: This program furfills the requirements for the 2D points assignment
######################################################################################################################
from math import sqrt  # importing sqrt for distance function


# the 2D point class
class Point(object):
    def __init__(self, x=0.0, y=0.0): # defaults x and y to 0.0 if information isn't provided
        self.x = x
        self.y = y

    # Getter for x
    @property
    def x(self):
        return self._x

    # Setter for x
    @x.setter
    def x(self, value):
        self._x = float(value)

    # Getter for y
    @property
    def y(self):
        return self._y

    # Setter for y
    @y.setter
    def y(self, value):
        self._y = float(value)

    # Str function that returns the points in (x,y) format
    def __str__(self):
        return "({},{})".format(self.x, self.y)

    # Function that calculates Distance between two points
    def dist(self, arg):
        return (sqrt((arg.x - self.x) ** 2 + (arg.y - self.y) ** 2))

    # Function that calculates the midpoint between two points
    def midpt(self, arg):
        x = (self.x + arg.x) / 2
        y = (self.y + arg.y) / 2
        return (x, y)


##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print "p1:", p1
print "p2:", p2
print "p3:", p3
# calculate and display some distances
print "distance from p1 to p2:", p1.dist(p2)
print "distance from p2 to p3:", p2.dist(p3)
print "distance from p1 to p3:", p1.dist(p3)
# calculate and display some midpoints
print "midpt of p1 and p2:", p1.midpt(p2)
print "midpt of p2 and p3:", p2.midpt(p3)
print "midpt of p1 and p3:", p1.midpt(p3)
