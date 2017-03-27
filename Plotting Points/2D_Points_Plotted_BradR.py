######################################################################################################################
# Name: Brad Raynaud
# Date: 3/26/2017
# Description: This program generates random points and plots them in a Python GUI
######################################################################################################################
from random import randint
from Tkinter import *


# the 2D point class
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = randint(0, WIDTH - 1)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = randint(0, HEIGHT - 1)


# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def plotPoints(self, n):
        for i in range(n):
            i = Point()
            self.plot(i.x, i.y)

    def plot(self, x, y):
        color1 = COLORS[randint(0, len(COLORS) - 1)]
        color2 = COLORS[randint(0, len(COLORS) - 1)]
        self.create_oval(x, y, x + 2 * POINT_RADIUS, y + 2 * POINT_RADIUS, outline=color1, fill=color1)


##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 400x400
WIDTH = 400
HEIGHT = 400
# the default point radius is 0 pixels (i.e., no center to the oval)
POINT_RADIUS = 1
# colors to choose from when plotting points
COLORS = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
# the number of points to plot
NUM_POINTS = 2500

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
