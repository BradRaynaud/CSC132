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
        P1 = Point(300,10)
        P2 = Point(10,510)
        P3 = Point(590,510)
        # creates a list with the three Vertices
        Plist = [P1,P2,P3]
        # Plot the vertices
        self.plot(P1, VERTEX_COLOR, VERTEX_RADIUS)
        self.plot(P2, VERTEX_COLOR, VERTEX_RADIUS)
        self.plot(P3, VERTEX_COLOR, VERTEX_RADIUS)
        P4 = P1 # Initializes P4
        for i in range(n):
            Randpoint = Plist[randint(0,len(Plist)-1)] # Chooses a random vertex from the list Plist
            P4 = P4.midpt(Randpoint) # Calculates the midpoint between P4 and the random vertex
            self.plot(P4, POINT_COLOR, POINT_RADIUS) # Plots the new point

    # Function that plots ovals on the Tkinter Canvas
    def plot(self, point, Color, Radius):
        # Creates an oval using a Point and sets the Color
        self.create_oval(point.x, point.y, point.x + 2 * Radius, point.y + 2 * Radius, outline=Color,
                         fill=Color)

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
