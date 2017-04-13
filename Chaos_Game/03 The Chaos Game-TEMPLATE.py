######################################################################################################################
# Name: Brad Raynaud
# Date: 4/5/2017
# Description: This program completes the Chaos Game assignment
######################################################################################################################
from Tkinter import *
from random import *
from math import sqrt


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

    # Midpoint function
    def midpt(self, arg):
        x = (self.x + arg.x) / 2
        y = (self.y + arg.y) / 2
        return Point(x, y)

    def dist(self, arg):
            return (sqrt((arg.x - self.x) ** 2 + (arg.y - self.y) ** 2))


# the chaos game class
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
    def __init__(self, master):
        # calls the constructor for the Canvas class
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def play(self, n):
        # Creates the vertices
        P1 = Point(300, 10)
        P2 = Point(10, 510)
        P3 = Point(590, 510)
        # creates a list with the three Vertices
        Plist = [P1, P2, P3]
        # Plot the vertices
        self.plot(P1, "Red", VERTEX_RADIUS)
        self.plot(P2, "Green", VERTEX_RADIUS)
        self.plot(P3, "Blue", VERTEX_RADIUS)
        P4 = P1  # Initializes P4
        for i in range(n):
            Randpoint = Plist[randint(0, len(Plist) - 1)]  # Chooses a random vertex from the list Plist
            P4 = P4.midpt(Randpoint)  # Calculates the midpoint between P4 and the random vertex
            self.plot(P4, self.determinecolor(P4), POINT_RADIUS)  # Plots the new point

    def determinecolor(self, point):
        P1 = Point(300, 10) # Vertice 1
        P2 = Point(10, 510) # Vertice 2
        P3 = Point(590, 510) # Vertice 3
        A = point.dist(P1) # Red FF0000
        B = point.dist(P2) # Green 00FF00
        C = point.dist(P3) # Blue 0000FF
        if A < B and A < C: # If closer to Vertice A return Red
            return "#FF0000"
        if B < A and B < C: # If closer to Vertice B return Green
            return "#00FF00"
        if C < A and C < B: # If closer to Vertice C return Blue
            return "#0000FF"



    # Function that plots ovals on the Tkinter Canvas
    def plot(self, point, Color, Radius):
        # Creates an oval using a Point and sets the Color
        self.create_oval(point.x, point.y, point.x + 2 * Radius, point.y + 2 * Radius, outline=Color, fill=Color)


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
