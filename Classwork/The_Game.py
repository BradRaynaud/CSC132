

#blueprint for a room
class Room(object):
    #the constructor
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables= []

        @property
        def name(self):
            return self._name
        @name.setter
        def name(self,value):
            self._name = value

        @property
        def exits(self):
            return self._exits

        @exits.setter
        def exits(self,value):
            self._exits = value

        @property
        def exitLocations(self):
            return self._exitLocations

        @exitLocations.setter
        def exitLocations(self,value):
            self._exitLocations = value

        @property
        def items(self):
            return self._items

        @items.setter
        def items(self,value):
            self._items = value

        @property
        def itemDescriptions(self):
            return self._itemDescriptions

        @itemDescriptions.setter
        def itemDescriptions(self,value):
            self._itemDesciptions = value

        @property
        def grabbables(self):
            return self._grabbables

        @grabbables.setter
        def grabbables(self,value):
            self._grabbables = value

        def addExit(self,exit,room):
            self._exits.append(exit)
            self._exitLocations.append(room)

        def addItem(self, item, desc):
            self._items.append(item)
            self._itemDescriptions.append(desc)

        def addGrabbable(self,item):
            self._grabbable.append(item)

        def delGrabbable(self,item):
            self.grabbable.remove(item)

        def __str__(self):
            s = "You are in{}.\n".format(self.name)

            s += "You see:  "
            for item in self.items:
                s += item + "  "
            s += "\n"
            s += "Exits:  "
            for exit in self.exits:
                s += exit + "  "
            return s
###################################################
# creates the rooms

def createRooms():
    global currentRoom

    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")

    r1.addExit("east", r2)
    r1.addExit("south", r3)
    r1.addGrabbable("key")
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
    r1.additem("table", "it is made of oak. A golden key rests on it")

    r2.addExit("west", r1)
    r2.addExit("south", r4)
    r2.addItem("rug"), "It is nice and Indian. It also needs to be vacuumed"
    r2.addItem("fireplace", "It is full of ashes.")

    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addGrabbable("book")
    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("statue", "There is nothing special about it")
    r3.addItem("desk","The statue is resting on it. So is a book.")

    r4.addExit("north", r2)
    r4.addExit("west",r3)
    r4.addExit("south", None) # DEATH
    r4.addGrabbable("6-pack")
    r4.addItem("Brew_Rig", "Gourd is brewing some sort of oatmeal stout on the rig. A 6-pack is resting beside it.")

    currentRoom = r1

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
        status = "you are dead."

    # Display status
    print "=============================================================="
    print status

    # current room is none player is dead and exit game
    if currentRoom == None:
        #death()
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
    if (action == "quit" or action == "exit" or action == "bye"):
        break
    # set a default response
    response = "I don't understand. Try Verb Noun Valid verbs are go, look, and take"
    # splits input into words (words are separated by spaces)
    words = action.split()
    # the game only undertands two word inputs
    if len(words) == 2:
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if verb == "go":
            # sets default response
            response = "invalid exit."

            # check for valid exits in current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if noun  == currentRoom.exits[i]:
                    # change the current room to the one that is
                    # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]

                    #set the response (success)
                    response = "room changed"
                    # no need to check any more exits
                    break

        # The verb is: look
        elif verb == "look":
            # sets a default response
            response = "I dont see that item"
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
            response = "I dont see that item."
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

     # display the response
    print "\n{}".format(response)
