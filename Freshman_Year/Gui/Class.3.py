from Tkinter import *


class Gooey(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setupGooey(self):
        l1 = Label(self.master, text="A Label")
        l1.grid(row=0, column=0, sticky=W)

        l2 = Label(self.master, text="another Label")
        l2.grid(row=1, column=0, sticky=W)

        l3 = Label(self.master, text="A third label centered")
        l3.grid(row=2, column=0, columnspan=2, sticky=E + W)

        img = PhotoImage(file="smiley3.gif")

        l4 = Label(self.master, image=img)
        l4.image = img
        l4.grid(row=2, column=0, columnspan=2, rowspan=2, sticky=N + S + E + W)

        e1 = Entry(self.master)
        e1.grid(row=0, column=1)

        e2 = Entry(self.master)
        e2.insert(END, "user input")
        e2.grid(row=1, column=1)

        c1 = Checkbutton(self.master, text="some check button")
        c1.grid(row=3, column=0, columnspan=2, sticky=W)

        b1 = Button(self.master, text="A button")
        b1.grid(row=3, column=2)

        b2 = Button(self.master, text="A button")
        b2.grid(row=3, column=3)


window = Tk()
t = Gooey(window)
t.setupGooey()
window.mainloop()

