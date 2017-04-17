from image import *
from media import *
class Map:
  def __init__(self):
    self.startingMap    = makePicture("images/startingMap.png")
    self.fullNormal  = makePicture("images/fullNormal.png")
    self.fullVisited = makePicture("images/fullVisited.png")
    show(self.startingMap)

  def pyCopy(self, ul, lr, current):
    for x in range (ul[0], lr[0]):
      for y in range (ul[1], lr[1]):
        if current:
          p = getPixel(self.fullVisited, x, y)
        else:
          p = getPixel(self.fullNormal, x, y)

        color = getColor(p)
        setColor(getPixel(self.startingMap, x , y), color)

  # this function copies a section from one of the 'full maps' to the startingMap
  # ul = upper left a tuple (x,y) for the starting position to copy
  # br = bottom right, a tuple (x,y) for the ending position of copy
  # current should be a bool, yes if its the room you are ending up in, no otherwise.
  def moveRooms(self, fromRoom, toRoom):
    ul,lr = fromRoom.getULLR()
    self.pyCopy(ul,lr, False)

    ul,lr = toRoom.getULLR()
    self.pyCopy(ul, lr, True)

    repaint(self.startingMap)
