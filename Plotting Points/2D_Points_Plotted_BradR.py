######################################################################################################################
# Name: 
# Date: 
# Description: 
######################################################################################################################
from random import randint
from Tkinter import *

# the 2D point class
class Point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._x

    @y.setter
    def y(self, value):
        self._y = value



# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas,Point):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        Point.__init__(self, master)

        self.pack(fill=BOTH, expand=1)


    def plotPoints(self, n):
        for i in range(n):
            x = x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            self.plot(x, y)

    def plot(self, x, y):
        color1 = COLORS[randint(0, len(COLORS)-1)]
        color2 = COLORS[randint(0, len(COLORS)-1)]
        self.create_oval(x, y, x + 2 * POINT_RADIUS, y + 2 * POINT_RADIUS, outline = color1, fill = color1)

    # write your code for the coordinate system class here (and subsequently remove this comment)


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
