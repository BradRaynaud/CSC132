from Tkinter import *

window = Tk()
l1 = Label(text = "A", bg = "red", fg = "green")
l1.pack(side = LEFT, expand = 1, fill = BOTH)

l2 = Label(text = "B", bg = "white", fg = "green")
l2.pack(side = LEFT, expand = 1, fill = BOTH)

l3 = Label(text = "C", bg = "blue", fg = "silver")
l3.pack(side = LEFT, expand = 1, fill = BOTH)




window.mainloop()
