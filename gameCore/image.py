from image import *
class Image:
  def __init__(self):
    self.startingMap    = makePicture(startingMap.jpg)
    self.fullNormal  = makePicture(fullNormal.jpg)
    self.fullVisited = makePicture(fullVisited.jpg)
    show(self.startingMap)
  def moveRooms( old, new):
    None

  # this function copies a section from one of the 'full maps' to the startingMap
  # ul = upper left a tuple (x,y) for the starting position to copy
  # br = bottom right, a tuple (x,y) for the ending position of copy
  # current should be a bool, yes if its the room you are ending up in, no otherwise.
  def pyCopy(self, ul, br, current):
    for x in range (ul[0], br[0] - ul[0]):
      for y in range (ul[1], br[1] - ul[1]):
        if current:
          foreground = self.fullVisited
        else:
          foreground = self.fullNormal

        p = getPixel(foreground, x, y)
        color = getColor(p)
        setColor(getPixel(self.startingMap, x , y , color))

  # this
  def moveRooms(self, fromRoom, toRoom):
    ul,lr = fromRoom.getULLR()
    self.pyCopy(ul,lr, False)

    ul,lr = toRoom.getULLR()
    self.pyCopy(ul, lr, True)

    repaint(self.startingMap)
