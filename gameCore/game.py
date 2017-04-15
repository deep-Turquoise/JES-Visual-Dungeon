from media import *
from room import *
from key import *
from player import *
from chest import *
from map import *

class Game:
    def __init__(self):  # Game constructor initializes Game class and its functions
        # Make rooms
        self.map = Map()
        self.rooms = []
        self.foyer = Room(1)
        self.foyer.setULLR( (361, 450), (474, 510) )
        self.foyer.setName("Foyer")
        self.foyer.setDescription("It is very dark. You can barely make out what is ahead")
        self.rooms.append(self.foyer)
        self.frontHall = Room(2)
        self.frontHall.setULLR( (381, 330), (451, 437) )
        self.frontHall.setName("Front Hall")
        self.frontHall.setDescription("There doesn't seem to be anyone around.")
        self.rooms.append(self.frontHall)
        self.livingRoom = Room(3)
        self.livingRoom.setULLR( (236, 329), (365, 436) )
        self.livingRoom.setName("Living Room")
        self.livingRoom.setDescription("There is dust all over the furniture.")
        self.rooms.append(self.livingRoom)
        self.kitchen = Room(4)
        self.kitchen.setULLR( (463, 329), (592, 319) )
        self.kitchen.setName("Kitchen")
        self.kitchen.setDescription("It reaks in here. All the food is spoiled.")
        self.rooms.append(self.kitchen)
        self.den = Room(5)
        self.den.setULLR( (418, 212), (592, 319) )
        self.den.setName("Den")
        self.den.setDescription("There is a telvision playing an old film with no sound.")
        self.rooms.append(self.den)
        self.backCorridor = Room(6)
        self.backCorridor.setULLR( (236, 212), (406, 319) )
        self.backCorridor.setName("Back Corridor")
        self.backCorridor.setDescription(
            "There are bloody handprints on the wall. There is some red light coming from a small crack on the west wall.")
        self.rooms.append(self.backCorridor)
        self.bedroom = Room(8)
        self.bedroom.setULLR( (258, 92), (387, 199) )
        self.bedroom.setName("Bedroom")
        self.bedroom.setDescription("All of the furniture is thrown on onto the floor.")
        self.rooms.append(self.bedroom)
        self.secretRoom = Room(7)
        self.secretRoom.setULLR( (99, 213), (228, 320) )
        self.secretRoom.setName("Secret Room")
        self.secretRoom.setDescription("There is only a flickering faint red light on.")
        self.rooms.append(self.secretRoom)
        self.out = Room(9)
        self.out.setULLR( (301, 529), (529, 588) )
        self.rooms.append(self.out)
        self.out.setName("Front Yard!")
        self.out.setDescription("You got out, you win!")

        # make doors
        self.door1 = Door((self.foyer, self.frontHall), 1)
        self.foyer.setNorth(self.door1)
        self.frontHall.setSouth(self.door1)

        self.door2 = Door((self.frontHall, self.livingRoom), 2)
        self.frontHall.setWest(self.door2)
        self.livingRoom.setEast(self.door2)

        self.door3 = Door((self.frontHall, self.kitchen), 3)
        self.frontHall.setEast(self.door3)
        self.kitchen.setWest(self.door3)

        self.door4 = Door((self.livingRoom, self.backCorridor), 4)
        self.livingRoom.setNorth(self.door4)
        self.backCorridor.setSouth(self.door4)

        self.door5 = Door((self.backCorridor, self.den), 5)
        self.backCorridor.setEast(self.door5)
        self.den.setWest(self.door5)

        self.door6 = Door((self.den, self.kitchen), 6)
        self.den.setSouth(self.door6)
        self.kitchen.setNorth(self.door6)

        self.door7 = Door((self.backCorridor, self.bedroom), 7)
        self.backCorridor.setNorth(self.door7)
        self.bedroom.setSouth(self.door7)
        self.door7.setLocked(True)

        self.door8 = Door((self.backCorridor, self.secretRoom), 8)
        self.backCorridor.setWest(self.door8)
        self.secretRoom.setEast(self.door8)
        self.door8.setLocked(True)
        self.door8.setHidden(True)

        self.door9 = Door((self.foyer, self.out), 9)
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

        # Make Keys
        self.key1 = Key(self.door8)
        self.key1.setName("Secret Key")
        self.key2 = Key(self.door7)
        self.key2.setName("Skeleton Key")

        self.key3 = Key(self.door9)
        self.key3.setName("Exit Key")

        # Place Keys
        self.chest3.addItem(self.key1)
        self.chest4.addItem(self.key2)
        self.chest5.addItem(self.key3)
        self.livingRoom.setChest(self.chest1)
        self.kitchen.setChest(self.chest2)
        self.den.setChest(self.chest3)
        self.secretRoom.setChest(self.chest4)
        self.bedroom.setChest(self.chest5)

    def getDoorforDir(self,direction):  # this function retrieves the door in either the North, South, East, or West direction
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

    def unlock(self, direction):  # this function notifies the player whether they have access to a certain door
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

    def move(self, direction):  # this function moves the player into new room if it is possible
        currentRoom = self.player.getRoom()
        door = self.getDoorforDir(direction)
        if door:
            if door.getHidden():
                printNow("You found a door here!")
                door.setHidden(False)
            if door.getLocked():
                printNow("This door is locked, you need to find a key to open it.")
                printNow("You are still in the " + self.player.getRoom().getName())
            else:
                newRoom = door.getOtherRoom(currentRoom)
                self.map.moveRooms(currentRoom, newRoom)
                self.player.setRoom(newRoom)
                printNow("You have entered the " + self.player.getRoom().getName())
        else:
            printNow("You hit your head. Ouch!")
            printNow("You are still in the " + self.player.getRoom().getName())

    def search(self, loc, thing):  # this function allows the player to search
        if loc == 0:  # and see if there is anything in the room they're in
            theChest = self.player.getRoom().getChest()
            if theChest:
                theChest.printDescription()
            else:
                printNow("There is no " + thing + " in this room")
        else:
            self.player.getRoom().printDescription()

    def printInventory(self):  # this function prints the inventory for the player
        self.player.getItemList()

    def getPlayer(self):  # this function returns the player created in the program
        return self.player

    def takeItem(self):  # this function allows the player to take an item if present in a chest
        chest = self.player.getRoom().getChest()
        if chest:
            item = chest.takeItem()
            if item:
                self.player.addItem(item)
            else:
                printNow("The " + chest.getName() + " is empty.")
        else:
            printNow("The room has no items to take.")