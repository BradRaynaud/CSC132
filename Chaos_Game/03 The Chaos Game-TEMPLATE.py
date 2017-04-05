######################################################################################################################
# Name: 
# Date: 
# Description: 
######################################################################################################################
from Tkinter import *
from random import *

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

    def midpt(self, arg):
        x = (self.x + arg.x) / 2
        y = (self.y + arg.y) / 2
        return Point(x,y)

# the chaos game class
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
    def __init__(self, master):
        # calls the constructor for the Canvas class
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def play(self, n):
        # Creates the vertices
        P1 = Point(300,0)
        P2 = Point(0,520)
        P3 = Point(600,520)
        Plist = [P1,P2,P3]
        self.plotV(P1)
        self.plotV(P2)
        self.plotV(P3)
        P4 = P1
        for i in range(n):
            Randpoint = Plist[randint(0,len(Plist)-1)]
            P4 = P4.midpt(Randpoint)
            self.plot(P4)



    # Function that plots ovals on the Tkinter Canvas
    def plot(self, point):
        # Creates an oval using a Point and sets the Color
        self.create_oval(point.x, point.y, point.x + 2 * POINT_RADIUS, point.y + 2 * POINT_RADIUS, outline=POINT_COLOR,
                         fill=POINT_COLOR)

    def plotV(self, point):
        # Creates an oval using a Point and sets the Color
        self.create_oval(point.x, point.y, point.x + 2 * VERTEX_RADIUS, point.y + 2 * VERTEX_RADIUS, outline=VERTEX_COLOR,
                         fill=VERTEX_COLOR)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
# the default vertex radius is 2 pixels and color is red
VERTEX_RADIUS = 2
VERTEX_COLOR = "red"
# the default point radius is 0 pixels and color is black
POINT_RADIUS = 0
POINT_COLOR = "black"
# the number of midpoints to plot
NUM_POINTS = 50000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
# create the chaos game as a Tkinter canvas inside the window
s = ChaosGame(window)
# play the chaos game with at least 50000 points
s.play(NUM_POINTS)
# wait for the window to close
window.mainloop()
