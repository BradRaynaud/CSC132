

#blueprint for a room
class Room(object):
    #the constructor
    def __init__(self,name):
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptables = []
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
            self._exitlocations.append(room)

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