#Silicon Beach Software
#Lab 13 redo of lab 12
#David Henderson
#Chris Calderon
#Nicholas Nelson
#Nathan Muaga
#Haley Dimapilis

# This is the base code for our final dungeon project


class Player:                                  
  def __init__(self, room):                          #Player constructor initializes Player class and its functions
    self.item = None
    self.location = room
    self.name = requestString("Please enter your name.")
  def addItem(self, item):                           #this function adds a new item to the player's inventory
    self.item = item
    printNow("You now have the" + item.getName())
  def getItem(self):                                 #this function retrieves the player's item
    return self.item
  def useItem(self):                                 #this function uses up the item, clearing it from the player's inventory
    self.item = None
  def getItemList(self):                             #this function retrieves and returns the list of player's items (if any)
    if not item:
      printNow("You have no items")
    else:
        printNow("You hold a " + item.getName())
  def setRoom(self, x):                              #this function sets the player in x location (room)
        self.location = x
  def getRoom(self):                                 #this function returns the player's current location
      return self.location
  def getName(self):                                 #this function allows you to display the player's name
      return self.name
      
class Key:
  def __init__(self, door):                          #Key constructor initializes Key class and its functions
    self.door = door
    self.name = ""
  def setName(self, n):                              #this function sets the name of the key
    self.name = n
  def getName(self):                                 #this function retrieves the name of the key
    return self.name
  def getDoor(self):                                 #this function returns the door parameter passed                                
    return self.door

class Chest:
  def __init__(self, num):                           #Chest constructor initializes Chest class and its functions
    self.number = num
    self.name = ""
    self.item = None
  def addItem(self, item):                           #this function adds an item to the player's chest
    self.items.append(item)
  def setName(self, n):                              #this function sets the name of said Chest object (ex: bookcase, cabinets, etc.)
    self.name = n
  def getName(self):                                 #this function retrieves and returns the name of the Chest object
    return self.name
  def addItem(self, item):                           #this function declares the item to be added
    self.item = item
  def takeItem(self):                                #this function takes item from chest
    temp = self.item
    self.item = None
    return temp
  def setChest(self, name):                          #this function allows the game to later create and set chests in its designated rooms
      self.chest = name
  def getChest(self):                                #this function returns any existing chest(s) in a room  
      return chest
  def printDescription(self):                        #this function describes the type of chest (if any) existing in a room
      if self.item:
        printNow("You find a " + self.item.getName() + " in the " + self.name + "." )
      else:
        printNow("The " + self.name + " is empty.")
              
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
      
class Room:
    def __init__(self, num):                                    #Room constructor initializes the Room class and its functions
        self.number = num
        self.name = ""
        self.description = ""
        self.chest = None
        self.n = None
        self.s = None
        self.e = None
        self.w = None
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

 #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
class Game:
  def __init__(self):                                #Game constructor initializes Game class and its functions
    # Make rooms
    self.rooms = []
    self.foyer = Room(1)
    self.foyer.setName("Foyer")
    self.foyer.setDescription("It is very dark. You can barely make out what is ahead")
    self.rooms.append(self.foyer)
    self.frontHall = Room(2)
    self.frontHall.setName("Front Hall")
    self.frontHall.setDescription("There doesn't seem to be anyone around.")
    self.rooms.append(self.frontHall)
    self.livingRoom = Room(3)
    self.livingRoom.setName("Living Room")
    self.livingRoom.setDescription("There is dust all over the furniture.")
    self.rooms.append(self.livingRoom)
    self.kitchen = Room(4)
    self.kitchen.setName("Kitchen")
    self.kitchen.setDescription("It reaks in here. All the food is spoiled.")
    self.rooms.append(self.kitchen)
    self.den = Room(5)
    self.den.setName("Den")
    self.den.setDescription("There is a telvision playing an old film with no sound.")
    self.rooms.append(self.den)
    self.backCorridor = Room(6)
    self.backCorridor.setName("Back Corridor")
    self.backCorridor.setDescription("There are bloody handprints on the wall. There is some red light coming from a small crack on the west wall.")
    self.rooms.append(self.backCorridor)
    self.bedroom = Room(8)
    self.bedroom.setName("Bedroom")
    self.bedroom.setDescription("All of the furniture is thrown on onto the floor.")
    self.rooms.append(self.bedroom)
    self.secretRoom = Room(7)
    self.secretRoom.setName("Secret Room")
    self.secretRoom.setDescription("There is only a flickering faint red light on.")
    self.rooms.append(self.secretRoom)
    self.out = Room(9)
    self.rooms.append(self.out)
    self.out.setName("Front Yard!")
    self.out.setDescription("You got out, you win!")
    
    #make doors
    self.door1 = Door( (self.foyer,self.frontHall), 1 )
    self.foyer.setNorth(self.door1)
    self.frontHall.setSouth (self.door1)
    
    self.door2 = Door( (self.frontHall,self.livingRoom), 2 )
    self.frontHall.setWest(self.door2)
    self.livingRoom.setEast(self.door2)
    
    self.door3 = Door( (self.frontHall,self.kitchen), 3 )
    self.frontHall.setEast(self.door3)
    self.kitchen.setWest(self.door3)
    
    self.door4 = Door( (self.livingRoom,self.backCorridor), 4 )
    self.livingRoom.setNorth(self.door4)
    self.backCorridor.setSouth(self.door4)
    
    self.door5 = Door( (self.backCorridor,self.den), 5 )
    self.backCorridor.setEast(self.door5)
    self.den.setWest(self.door5)
    
    self.door6 = Door( (self.den,self.kitchen), 6 )
    self.den.setSouth(self.door6)
    self.kitchen.setNorth(self.door6)
    
    self.door7 = Door( (self.backCorridor,self.bedroom), 7 )
    self.backCorridor.setNorth(self.door7)
    self.bedroom.setSouth(self.door7)
    self.door7.setLocked(True)
    
    self.door8 = Door( (self.backCorridor,self.secretRoom), 8 )
    self.backCorridor.setWest(self.door8)
    self.secretRoom.setEast(self.door8)
    self.door8.setLocked(True)
    self.door8.setHidden(True)
    
    self.door9 = Door( (self.foyer, self.out), 9 )
    self.door9.setLocked(True)
    self.foyer.setSouth(self.door9)
    
    # Make player
    self.player = Player(self.foyer)
    # Make chests
    self.chest1 = Chest(1)
    self.chest1.setName("BookCase")
    self.chest2 = Chest(2)
    self.chest2.setName("Cabinets")
    self.chest3 = Chest(3)
    self.chest3.setName("BookCase")
    self.chest4 = Chest(4)
    self.chest4.setName("Dresser")
    self.chest5 = Chest(5)
    self.chest5.setName("Dresser")

    #Make Keys
    self.key1 = Key(self.door8)
    self.key1.setName("Secret Key")
    self.key2 = Key(self.door7)
    self.key2.setName("Skeleton Key")
    
    self.key3 = Key(self.door9)
    self.key3.setName("Exit Key")
    
    #Place Keys
    self.chest3.addItem(self.key1)
    self.chest4.addItem(self.key2)
    self.chest5.addItem(self.key3)
    self.livingRoom.setChest(self.chest1)
    self.kitchen.setChest(self.chest2)
    self.den.setChest(self.chest3)
    self.secretRoom.setChest(self.chest4)
    self.bedroom.setChest(self.chest5)

  def getDoorforDir(self, direction):          #this function retrieves the door in either the North, South, East, or West direction
     currentRoom = self.player.getRoom()
     if direction == 0:
       door = currentRoom.getNorth()
     elif direction == 1:
       door = currentRoom.getSouth()
     elif direction == 2:
       door = currentRoom.getEast()
     elif direction == 3:
       door = currentRoom.getWest()
     return door

  def unlock(self, direction):                 #this function notifies the player whether they have access to a certain door 
    door = self.getDoorforDir(direction)
    if not door:
        printNow("There is no door in that direction.")
        return 
    if not door.getLocked():
        printNow("This door isn't locked.")
        return
    key = self.player.getItem()
    if not key:
        printNow("You don't have a key!")
        return
    if key.getDoor().getNumber() == door.getNumber():
        door.setLocked(False)
        self.player.useItem()
        printNow("The door unlocks...")
    else:
        printNow("This key doesn't work for this door.")
    
  def move(self, direction):                                                  #this function moves the player into new room if it is possible
     currentRoom = self.player.getRoom()
     door = self.getDoorforDir(direction)
     if door:
       if door.getHidden():
         printNow("You found a door here!")
         door.setHidden(False)
       if door.getLocked():
         printNow("This door is locked, you need to find a key to open it.")
         printNow("You are still in the " + self.player.getRoom().getName() )
       else:
         newRoom = door.getOtherRoom(currentRoom)
         self.player.setRoom(newRoom)
         printNow("You have entered the " + self.player.getRoom().getName())
     else:
       printNow("You hit your head. Ouch!")
       printNow("You are still in the " + self.player.getRoom().getName())

    
  def search(self, loc, thing):                                  #this function allows the player to search
      if loc == 0:                                               #and see if there is anything in the room they're in
          theChest = self.player.getRoom().getChest()
          if theChest:
             theChest.printDescription()
          else:
              printNow("There is no " + thing + " in this room")
      else:
          self.player.getRoom().printDescription()
    
  def printInventory(self):                                      #this function prints the inventory for the player
      self.player.getItemList()
  def getPlayer(self):                                           #this function returns the player created in the program
      return self.player
  def takeItem(self):                                            #this function allows the player to take an item if present in a chest
      chest = self.player.getRoom().getChest()
      if chest:
        item = chest.takeItem()
        if item:
          self.player.addItem(item)
        else:
          printNow("The " + chest.getName() + " is empty.")
      else:
        printNow("The room has no items to take.")
      
class Run:
  #Run constructor below initializes Run class and its functions
  #Run class basically handles the player's input once entered
  def __init__(self):                        
    self.moves = 0
    self.directions = {"north" : 0, "n" : 0, "south" : 1, "s" : 1, 
                       "east"  : 2, "e" : 2, "west"  : 3, "w" : 3}
    self.searchTerms = {"chest" : 0, "bookcase" : 0, "cabinets" : 0, "dresser" : 0, "room" : 1}
    
    self.myGame = Game()
    self.user_Input = ""
    while self.user_Input != "exit":
        self.user_Input = requestString("What you would like to do:")
        if self.moves == 3:
            showInformation("Your stomache growls, you realize you haven't eaten in days...")
        if self.moves == 10:
            showInformation("You are starting to feel fatigued...")
        if self.moves == 25:
            showInformation("Your hunger is making you dizzy...")
        if self.moves == 50:
            showInformation("You are moving slower, and are considering eating your shoes...")
        if self.moves == 60:
            showInformation("You stumble from fatigue, and taste your shoes...but get up and keep going")
        if self.moves == 70:
            showInformation("Your hunger is too much to bear at this point, you start gnawing on your fingers...")
        if self.moves == 72:
            showInformation("You move very slow, and continue to chew on your bloody fingers")
        if self.moves == 73:
            showInformation("You stumble, and realize you've eaten your fingers, you can no longer stand, but crawl")
        if self.moves == 74:
            showInformation("You see visions of food heaven, and lay motionless while eating your limbs...")
        if self.moves >= 75:
            showInformation(self.myGame.getPlayer().getName() + " you ran out of moves!")
            self.user_Input = "exit"
        self.moves += 1
        self.user_Input = self.user_Input or ""
        self.user_Input = self.user_Input.lower()
        if self.user_Input == "exit":
          printNow("You remain trapped forever and die of starvation, but not before eating your own limbs...")
        elif self.user_Input == "inventory":
            self.myGame.getPlayer().getItemList()
        elif self.user_Input == "help":
            help()
        elif self.user_Input == "scream":
            printNow("You screamed. Didn't do anything since you're alone.")
        elif self.user_Input == "inventory":
            self.myGame.printInventory()
        else:
            words = self.user_Input.split()
            words.append("foo")
            if words[0] == "go":
              dir = words[1]
              if dir in self.directions.keys():
                  self.myGame.move(self.directions[dir])
                  if self.myGame.getPlayer().getRoom().getNumber() == 9:
                      showInformation("Good job " + self.myGame.getPlayer().getName() + " you have escaped!\n YOU WIN!")
                      self.user_Input = "exit"
              else:
                printNow("I did not understand that direction.")
            elif words[0] == "search":
              if words[1] in self.searchTerms.keys():
                self.myGame.search(self.searchTerms[words[1]], words[1])
            elif words[0] == "take":
              self.myGame.takeItem()
            elif words[0] == "unlock":
              dir = words[1]
              if dir in self.directions.keys():
                self.myGame.unlock(self.directions[dir])
              else:
                printNow("I did not understand that direction.")
            # error Handing
            else:
               printNow("You entered someting wrong. Try again.")
               self.moves -= 1
               
def intro_Outputs():                                                               #this function serves as an introduction upon initialization of the game
    info ="""
Welcome to the dungeon! Try to find your away around.
In this dungeon you must find 3 keys to escape.
At least one of the keys is in a hidden room!
You have 75 moves before you die.
Enter help for command information.
Good Luck!"""
    showInformation(info)

def help():                                                                        #this function lists the possible commands a player can enter
      printNow("""
  Type one of these commands:
  exit - to exit the program
  help - to list the commands you need
  scream - you scream
  inventory - get list of items you are carrying.
  go <direction>  -  To move to a different room. e.g. go North
  search <location> - Search a room or bookcase etc. e.g. search Bookcase
  take <item> - Take an item e.g. take key
  unlock <direction> - Unlock the door in the specified direction e.g. unlock west
  """   )
      
def main():                                                                        #this function prompts the player upon initialization of the game
      intro_Outputs()
      help()
      printNow("We are having you start off at the Foyer")
      printNow("The door suddenly locks behind you. You must now find a way out.")
      go = Run()



main()
