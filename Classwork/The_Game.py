########################################################
# Name: Brad Raynaud
# Date: 2/10/2017
# Description: This program is a game where the objective is to escape the house
########################################################
# Change Log(list of improvements)
# Added the verb usage along with usage text for every item in the game
# created a second floor labeled attic with a piece of cake and a puzzle box inside it
# Created a special case for the puzzle box usage so that the puzzle box could only be opened if I had the key in my inventory
# Upon opening of the box the first key was removed and the window_key was added
# Using that key you are able to use the go command on the window
#
# I was unable to implement a case where the window returned a response "The window is locked"
# Commands in order to complete game: 1) take key 2) go east 3) go stairs 4) use puzzle_box 5) go stairs 6) go south
#  7) go window
#
#

# Blueprint for a room
class Room(object):
    # The constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        self.usage = []

    # getters and setters for instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property # getter for usage verb
    def usage(self):
        return self._usage

    @usage.setter # setter for usage verb
    def usage(self, value):
        self._usage = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
    # adds an exit to the room
    # the exit is a string e.g. north
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)
    # adds an item to the room
    # the item is a string
    # the desc is a description of the item
    # the usage is a string with the response from the verb use
    def addItem(self, item, desc, usage): # added usage to addItem
        # appends the item, description, and usage to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)
        self._usage.append(usage) # appends arg(usage) to the usage list for item
    # adds a grabbable item to the room
    # the item is a string
    def addGrabbable(self,item):
        # append the item to the list
        self._grabbables.append(item)
    # removes a grabbable item from the room
    # the item is a string
    def delGrabbable(self,item):
        # remove the item from the list
        self.grabbables.remove(item)

    # Returns a string description of the room
    def __str__(self):
        # first the room name
        s = "You are in {}.\n".format(self.name)

        # next the items in the room
        s += "You see:  "
        for item in self.items:
            s += item + "  "
        s += "\n"

        # next the exits from the room
        s += "Exits:  "
        for exit in self.exits:
            s += exit + "  "
        return s
###################################################
# creates the rooms


def createRooms():
    # r1 through r4 are the four rooms on the bottom floor
    # r5 is the attic with the puzzle box and cake
    # currentRoom is the room the player is currently in
    # current room is global because it needs to be changed in the main part of the program
    global currentRoom

    # gave the rooms names based off their contents
    r1 = Room(" the Office")
    r2 = Room(" the Living Room")
    r3 = Room(" the Study")
    r4 = Room(" the Kitchen")
    r5 = Room(" the Attic")

    # adds exits to r1
    r1.addExit("east", r2)
    r1.addExit("south", r3)
    # add grabbable to r1
    r1.addGrabbable("key")
    # add items to r1
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.", "I could sit in this, but I won't")
    r1.addItem("table", "it is made of oak. A golden key rests on it", "I can't use this")

    # add exits to r2
    r2.addExit("stairs", r5)
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    # add items to r2
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed", "I can't use this, too dusty")
    r2.addItem("fireplace", "It is full of ashes.", "Don't want to burn the house down")

    # add exits to r3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    # add grabbable to r3
    r3.addGrabbable("book")
    # add items to r3
    r3.addItem("bookshelves", "They are empty. Go figure.", "Books eww")
    r3.addItem("statue", "There is nothing special about it", "Nothing happens")
    r3.addItem("desk","The statue is resting on it. So is a book.", "I could study, But I won't")

    # add exits to r4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("window", None)  # DEATH
    # add grabbable to r4
    r4.addGrabbable("6-pack")
    # add item to r4
    r4.addItem("Brew_Rig", "Gourd is brewing some sort of oatmeal stout on the rig. A 6-pack is resting beside it.", "Better leaving brewing to Gourd")

    # add exit to r5(attic)
    r5.addExit("stairs", r2)  # Adds an exit to the attic
    # adds items to Exit
    r5.addItem("cake", "It looks tasty", "Made of chocolate, but tastes like lies")  # creates item: cake
    r5.addItem("puzzle_box", "Looks intricate but it does have a keyhole", "The key from downstairs might unlock this")  # Creates item: puzzle_box

    currentRoom = r1

# displays an appropriate "message" when the player dies
def death():
    print " " * 17 + "u" * 7
    print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
    print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
    print " " * 9 + "u" + "$" * 21 + "u"
    print " " * 8 + "u" + "$" * 23 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 +"\"" + " " * 3 + "\"" + "$" * 6 + "u"
    print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7+ "$" * 4 + "\""
    print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" +"$" * 3
    print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3
    print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 +"$" * 3 + "u" * 2 + "$" * 4 + "\""
    print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7+ "\""
    print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
    print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
    print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$"* 2 + " " * 7 + "u" * 3
    print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4
    print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 +"\"" + " " * 5 + "u" * 2 + "$" * 6
    print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 +"u" * 4 + "$" * 10
    print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2+ "$" * 9 + "\"" * 3 + "$" * 3 + "\""
    print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 +" " + "\"" * 2 + "$" + "\"" * 3
    print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
    print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 +" \"\"" + "$" * 11 + "u" * 3 + "$" * 3
    print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" *11 + "\""
    print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" *4 + "\"\""
    print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""
############################################
#START THE GAME

inventory = [] # nothing in inventory
createRooms() # creates the rooms

# play forever (until game is over or player asks to quit)
while True:
    # Sets status so player has situational awareness
    # The status has room and inventory information
    status = "{} \n You are carrying: {}\n".format(currentRoom, inventory)

    #if current room is none the player is dead and game over
    # above condition only happens when the player goes south when in room 4
    if currentRoom == None:
        status = "You are Dead."

    # Display status
    print "=============================================================="
    print status

    # current room is none player is dead and exit game
    if currentRoom == None:
        death()
        break

    #prompt the player for input
    # game supports simple language <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    # use raw_input here to treat input as a string instead of a numeric value
    action = raw_input("What to do? ")
    # Set users input to lowercase for easier comparison
    action = action.lower()
    # exit the game if the player wants to leave (supports quit exit or bye
    if (action == "quit" or action == "exit" or action == "bye" or action == "use"):
        break
    # set a default response
    response = "I don't understand. Try Verb Noun Valid verbs are go, look, take, and use"
    # splits input into words (words are separated by spaces)
    words = action.split()
    # the game only understands two word inputs
    if len(words) == 2:
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if verb == "go":
            # sets default response
            response = "Invalid Exit."
            # check for valid exits in current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if noun == currentRoom.exits[i]:
                    response = "Room changed" # sets response
                    # adds special case for window, player is unable to use the window as an exit until key is in inventory
                    if noun == "window":
                        # checks inventory for item "window_key"
                        for item in inventory:
                            if item == "window_key": # if window key is found window unlocks and player dies
                                response = "You unlock the window and fall to your death." # sets response
                                # changes the current room to the one associated with specified exit
                                currentRoom = currentRoom.exitLocations[i]
                                break
                            else:
                                response = "The window is locked" # was unable to make this response work
                    else:
                        # changes the current room to the one associated with specified exit
                        currentRoom = currentRoom.exitLocations[i]
                    # no need to check any more exits
                    break

        # The verb is: look
        elif verb == "look":
            # sets a default response
            response = "I don't see that item"
            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if noun == currentRoom.items[i]:
                    # sets the response to item's description
                    response = currentRoom.itemDescriptions[i]
                    # no need to check any more items
                    break

        # the verb is: take
        elif verb == "take":
            # sets a default response
            response = "I don't see that item."
            # checks for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable was found
                if noun == grabbable:
                    # add grabbable to players inventory
                    inventory.append(grabbable)
                    # remove grabbable from room
                    currentRoom.delGrabbable(grabbable)
                    # set the response (success)
                    response = "item grabbed"
                    # no need to check for more grabbables
                    break
        elif verb == "use":
            response = "Nothing happens"
            # Sets a default response
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if noun == currentRoom.items[i]:
                    response = currentRoom.usage[i] # sets response to the items usage
                    if noun =="puzzle_box": # adds special case for puzzle box
                        # looks for item in inventory if item not found response defaults to "The key from downstairs might unlock this"
                        for item in inventory:
                            if item == "key":
                                response = "The box opens and you find another key" # creates a new response
                                inventory.append("window_key") # adds window_key to inventory
                                inventory.remove(item) # removes key from inventory
                            break
                    break

    # displays the response
    print "\n{}".format(response)
