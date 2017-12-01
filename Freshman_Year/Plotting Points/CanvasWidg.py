from Tkinter import *
from random import randint

###############################
# Constants

WIDTH = 800
HEIGHT = 800
POINT_COLORS = ["black", "green", "blue", "forest green", "pink", "yellow"]
POINT_RADIUS = 1
NUM_POINTS = 2500

###############################
# Class

class Bbox(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill = BOTH, expand = 1)

    def plotPoints(self, n):
        for i in range(n):
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            self.plot(x, y)
        #for i in range(WIDTH):
        #    self.plot(i,i)
        #    self.plot(i,WIDTH - i -1)

    def plot(self, x, y):
        color1 = POINT_COLORS[randint(0,len(POINT_COLORS)- 1)]
        color2= POINT_COLORS[randint(0, len(POINT_COLORS) - 1)]
        self.create_oval(x, y, x + 2 * POINT_RADIUS , y + 2 * POINT_RADIUS, outline=color1, fill = color2)

###############################
#Main program

window = Tk()
window.geometry("{}x{}".format(WIDTH,HEIGHT))
window.title("Beat boxing these points")
p = Bbox(window)
p.plotPoints(NUM_POINTS)
window.mainloop()