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

    # Getter for x
    @property
    def x(self):
        return self._x

    # Setter for x
    @x.setter
    def x(self, value):
        self._x = value

    # Getter for y
    @property
    def y(self):
        return self._y

    # Setter for y
    @y.setter
    def y(self, value):
        self._y = value


# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
    def __init__(self, master):
        # calls the constructor for the Canvas class
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def plotPoints(self, n):
        # Repeats n times
        for i in range(n):
            # Generates a random x value in the bounds of the Canvas
            randomX = randint(0, WIDTH - 1)
            # Generates a random y value in the bounds of the Canvas
            randomY = randint(0, HEIGHT - 1)
            # Creates an instance of the Point class using the two previously generated values
            i = Point(randomX, randomY)
            self.plot(i)

    # Function that plots ovals on the Tkinter Canvas
    def plot(self, point):
        # Randomly choose a color for the circle
        color1 = COLORS[randint(0, len(COLORS) - 1)]
        # Creates an oval using a Point and sets the Color to color1
        self.create_oval(point.x, point.y, point.x + 2 * POINT_RADIUS, point.y + 2 * POINT_RADIUS, outline=color1,
                         fill=color1)


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
