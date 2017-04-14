class Player:
    def __init__(self, room):  # Player constructor initializes Player class and its functions
        self.item = None
        self.location = room
        self.name = requestString("Please enter your name.")

    def addItem(self, item):  # this function adds a new item to the player's inventory
        self.item = item
        printNow("You now have the" + item.getName())

    def getItem(self):  # this function retrieves the player's item
        return self.item

    def useItem(self):  # this function uses up the item, clearing it from the player's inventory
        self.item = None

    def getItemList(self):  # this function retrieves and returns the list of player's items (if any)
        if not item:
            printNow("You have no items")
        else:
            printNow("You hold a " + item.getName())

    def setRoom(self, x):  # this function sets the player in x location (room)
        self.location = x

    def getRoom(self):  # this function returns the player's current location
        return self.location

    def getName(self):  # this function allows you to display the player's name
        return self.name
