###########################################################################################
# Name: Brad Raynaud
# Date: 3/26/2017
# Description: This program adds a GUI to the Room Adventure activity
###########################################################################################
# List of improvements
# Added a 5th room with a puzzle box and a cake
# Added a use verb and provided usage text for all items in the game
# The Go verb and addExit were modified to allow any exit to be locked
# The south exit of room 4 can only be accessed after retrieving the key from the puzzle box
# the puzzle box can only be opened using the key from room 1
##############################################
# Commands required to complete game
# 1) look table 2) take key 3) go east 4) go stairs 5) use puzzle_box 6) go stairs 7) go south 8) go south
##############################################
# Imports
from Tkinter import *
from time import sleep


##############################################
# the Room class

class Room(object):
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
        # and grabbables (things that can be taken into inventory)
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room, islocked=False, key=None):
        # append the exit, room, islocked, and key to the appropriate dictionary
        self._exits[exit] = [room, islocked, key]

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc, usage):
        # append the item, description, and usage to the appropriate dictionary
        self._items[item] = [desc, usage]

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "

        return s


#############################################
# the Game class
# inherits from the Frame class of Tkinter

class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        # r1 through r4 are the four rooms in the mansion
        # currentRoom is the room the player is currently in (which
        # can be one of r1 through r4)
        # create the rooms and give them meaningful names and an
        # image in the current directory
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")
        r5 = Room("Room 5", "Attic.gif")

        # add exits to room 1
        r1.addExit("east", r2)  # to the east of room 1 is room 2
        r1.addExit("south", r3)
        # add grabbables to room 1
        r1.addGrabbable("key")
        # add items to room 1
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.", "I could sit in this, but I won't")
        r1.addItem("table", "it is made of oak. A golden key rests on it", "I can't use this")
        # add exits to room 2
        r2.addExit("stairs", r5)
        r2.addExit("west", r1)
        r2.addExit("south", r4)
        # add items to room 2
        r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed", "I can't use this, too dusty")
        r2.addItem("fireplace", "It is full of ashes.", "Don't want to burn the house down")

        # add exits to room 3
        r3.addExit("north", r1)
        r3.addExit("east", r4)
        # add grabbables to room 3
        r3.addGrabbable("book")
        # add items to room 3
        r3.addItem("bookshelves", "They are empty. Go figure.", "Books eww")
        r3.addItem("statue", "There is nothing special about it", "Nothing happens")
        r3.addItem("desk", "The statue is resting on it. So is a book.", "I could study, But I won't")

        # add exits to room 4
        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", None, True, "window_key")  # DEATH!
        # add grabbables to room 4
        r4.addGrabbable("6-pack")
        # add items to room 4
        r4.addItem("brew_rig",
                   "Gourd is brewing some sort of oatmeal stout on the rig. A 6-pack is resting beside it.",
                   "Better leaving brewing to Gourd")

        # add exit to r5(attic)
        r5.addExit("stairs", r2)  # Adds an exit to the attic
        # adds items to r5
        r5.addItem("cake", "It looks tasty", "Made of chocolate, but tastes like lies")  # creates item: cake
        r5.addItem("puzzle_box", "Looks intricate but it does have a keyhole",
                   "The key from downstairs might unlock this")  # Creates item: puzzle_box

        # set room 1 as the current room at the beginning of the
        # game
        Game.currentRoom = r1

        # initialize the player's inventory
        Game.inventory = []




        # sets up the GUI

    # Sets up the GUI
    def setupGUI(self):
        # Organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a a Tkinter Entry
        # set its background to white and bind the return to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesnt have to click on it

        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a TKinter label
        # don't let the image control the widget size
        img = None
        Game.image = Label(self, width=WIDTH / 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 2)
        # widget is a TKINTER Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    # sets the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="skull.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)
        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "\nYou are dead. The only thing you can do now is quit.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) + \
                             "\nYou are carrying: " + str(Game.inventory) + \
                             "\n\n" + status)
            Game.text.config(state=DISABLED)

    # plays the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")

    # processes the player's input
    def process(self, event):

        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to compare the verb and noun to known values
        action = action.lower()

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye"):
            quit(0)
        # set a default response
        response = "I don't understand.  Try verb noun.  Valid verbs are go, look, take, and use"

        # if the player is dead if goes/went south from room 4
        if Game.currentRoom == None:
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]

            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."

                # a valid exit is found
                if noun in Game.currentRoom.exits:
                    # checks to see if room is locked
                    if Game.currentRoom.exits[noun][1] == False:  # if room is unlocked
                        # change the current room to the one that is associated with the specified exit
                        Game.currentRoom = Game.currentRoom.exits[noun][0]
                        # set the response (success)
                        response = "Room changed."
                    elif Game.currentRoom.exits[noun][1] == True:  # if room is locked
                        # sets default response
                        response = "It is locked."
                        # checks inventory for key
                        for item in Game.inventory:
                            if item == Game.currentRoom.exits[noun][2]:  # if item is equal to the required key
                                # change the current room to the one that is associated with the specified exit
                                Game.currentRoom = Game.currentRoom.exits[noun][0]  #
                                # set the response (success)
                                response = "Room changed"


            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."

                # check for valid items in the current room
                for item in Game.currentRoom.items:
                    # a valid item is found
                    if noun == item:
                        # set the response to the item's description
                        response = Game.currentRoom.items[noun][0]
                        # no need to check any more items

            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."

                # check for valid grabbable items in the current room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if noun == grabbable:
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable items
                        break

            # the verb is: look
            elif (verb == "use"):
                # set a default response
                response = "I can't use this"

                # check for valid items in the current room
                for item in Game.currentRoom.items:
                    # a valid item is found
                    # set the response to the item's description
                    response = Game.currentRoom.items[noun][1]
                    # if player has key unlock puzzle box and remove key and add window_key to inv
                    if noun == "puzzle_box":
                        # checks inventory for item
                        for item in Game.inventory:
                            # sets response
                            response = "You unlock the box and find another key"
                            if item == "key":
                                Game.inventory.append("window_key")  # adds window_key to inventory
                                Game.inventory.remove("key")  # remove key from inventory

        # Display the response on the right of the GUI
        # Display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)


#############################################
# the default size of the GUI is 800x600

WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
