from media import *
class Room:
    def __init__(self, num):                                    #Room constructor initializes the Room class and its functions
        self.number = num
        self.name = ""
        self.description = ""
        self.chest = None
        self.upperLeft = None
        self.lowerRight = None
        self.n = None
        self.s = None
        self.e = None
        self.w = None
    def setULLR(self, ul, lr):    #this function sets the upper left and lower rigt for rom redraws, it takes 2 tuples as an argument
        self.upperLeft = ul
        self.lowerRigt = lr
    def getULLR(self):
        return( (self.upperLeft, self.lowerRight) )                 #this function returns a tuple containing 2 tuples for the redraw corners
    def search(self):                                           #this function searches
        printNow(description)
    def setName(self, n):                                       #this function sets the name of a room created by the game
        self.name = n
    def getName(self):                                          #this function retrieves the name of a room
        return self.name
    def setDescription(self, n):                                #this function sets the description of a room
        self.description = n
    def printDescription(self):                                 #this function tells the player wherer there is a locked door in a certain direction
        printNow(self.description)
        if self.n and not self.n.getHidden():
          str = ""
          if self.n.getLocked():
            str = "locked "
          printNow("There is a " + str +" door to the north.")
        if self.s and not self.s.getHidden():
          str = ""
          if self.s.getLocked():
            str = "locked "
          printNow("There is a " + str +" door to the south.")
        if self.e and not self.e.getHidden():
          str = ""
          if self.e.getLocked():
            str = "locked "
          printNow("There is a " + str +" door to the east.")
        if self.w and not self.w.getHidden():
          str = ""
          if self.w.getLocked():
            str = "locked "
          printNow("There is a " + str +" door to the west.")
        if self.chest:
          printNow("There is a " + self.chest.getName() + " In the corner")
    def getNumber(self):                             #this function retrieves the room's unique number
        return self.number
    def setNorth(self, room):                        #this function sets the room in the North direction
        self.n = room
    def setSouth(self, room):                        #this function sets the room in the South direction
        self.s = room
    def setEast(self, room):                         #this function sets the room in the East direction
        self.e = room
    def setWest(self, room):                         #this function sets the room in the West direction
        self.w = room
    def getNorth(self):                              #this function retrieves and returns the room in the North direction
        return self.n
    def getSouth(self):                              #this function retrieves and returns the room in the South direction
        return self.s
    def getEast(self):                               #this function retrieves and returns the room in the East direction
        return self.e
    def getWest(self):                               #this function retrieves and returns the room in the West direction
        return self.w
    def getChest(self):                              #this function retrieves and returns a chest (if any) existing in a room
        return self.chest
    def setChest(self, chest):                       #this function creates and sets a chest in a room
        self.chest = chest


class Door:
  def __init__(self, cons, num):                     #Door constructor initializes Door class and its functions
    self.number = num                                #between each room exists a door that is either locked or unlocked
    self.connects = cons
    self.description = ""
    self.hidden = False
    self.locked = False
  def setConnections(conn):                                   #this function connects the rooms
    self.connects = conn
  def checkConnection(number):                                #this function checks whether the rooms are connected
    if connects[0] == number or connects[1] == number:
      return true
    else:
      return false
  def setDescription(desc):                                   #this function sets the description of the unique door
      self.description = desc
  def inspect():                                              #this function determines/notifies player whether the door is locked or unlocked
      printNow(self.description)
      if locked:
         printNow("The door is locked")
      else:
         printNow("The door is not locked")
  def getOtherRoom(self, room):                               #this function retrieves the room in the direction input by user
      if self.connects[0].getNumber() == room.getNumber():
          return self.connects[1]
      return self.connects[0]
  def setHidden(self, h):                                     #this function creates and sets a hidden room
      self.hidden = h
  def getHidden(self):                                        #this function retrieves and returns hidden room
      return self.hidden
  def setLocked(self, l):                                     #this function
      self.locked = l
  def getLocked(self):
      return self.locked
  def getNumber(self):                                        #this function returns the unique number that identifies a door
      return self.number