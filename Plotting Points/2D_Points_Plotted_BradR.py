######################################################################################################################
# Name: 
# Date: 
# Description: 
######################################################################################################################

# the 2D point class
class Point(object):
	# write your code for the point class here (and subsequently remove this comment)

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
	# write your code for the coordinate system class here (and subsequently remove this comment)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 400x400
WIDTH = 400
HEIGHT = 400
# the default point radius is 0 pixels (i.e., no center to the oval)
POINT_RADIUS = 0
# colors to choose from when plotting points
COLORS = [ "black", "red", "green", "blue", "cyan", "yellow", "magenta" ]
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
