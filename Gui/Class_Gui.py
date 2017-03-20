#  Gui in class 3/20/2017
from Tkinter import *


####################################

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.button1 = Button(master, text="Bye!", fg="Green",bg = "BLUE", command=self.quit)
        self.button1.pack(side=LEFT)

        self.button2 = Button(master, text="HI!", fg="Green", bg = "BLUE" , command=self.woof)
        self.button2.pack(side=LEFT)

        self.button2 = Button(master, text="CADE!!!!!", fg="Green", bg = "BLUE" , command=self.saythis)
        self.button2.pack(side=RIGHT)

    def woof(self):
        print "Button has been clicked"

    def saythis(self):
        print "I am watching you"


####################################

window = Tk()
app = App(window)
window.mainloop()
