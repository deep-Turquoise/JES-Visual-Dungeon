from media import *
class Chest:
    def __init__(self, num):  # Chest constructor initializes Chest class and its functions
        self.number = num
        self.name = ""
        self.item = None

    def addItem(self, item):  # this function adds an item to the player's chest
        self.items.append(item)

    def setName(self, n):  # this function sets the name of said Chest object (ex: bookcase, cabinets, etc.)
        self.name = n

    def getName(self):  # this function retrieves and returns the name of the Chest object
        return self.name

    def addItem(self, item):  # this function declares the item to be added
        self.item = item

    def takeItem(self):  # this function takes item from chest
        temp = self.item
        self.item = None
        return temp

    def setChest(self, name):  # this function allows the game to later create and set chests in its designated rooms
        self.chest = name

    def getChest(self):  # this function returns any existing chest(s) in a room
        return chest

    def printDescription(self):  # this function describes the type of chest (if any) existing in a room
        if self.item:
            printNow("You find a " + self.item.getName() + " in the " + self.name + ".")
        else:
            printNow("The " + self.name + " is empty.")
