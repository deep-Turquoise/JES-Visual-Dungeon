from media import *
class Image:
  def __init__(self):
    self.startingMap    = makePicture(startingMap.jpg)
    self.fullNormal  = makePicture(fullNormal.jpg)
    self.fullVisited = makePicture(fullVisited.jpg)
    self.hiddenNormal  = makePicture(hiddenNormal.jpg)
    self.hiddenVisited = makePicture(hiddenVisited.jpg)
    show(self.startingMap)
  def moveRooms( old, new):
    None

  def pyCopyScreen(self, foreground, ul, br):
    for x in range (ul[0], br[0] - ul[0]):
      for y in range (ul[1], br[1] - ul[1]):
        p = getPixel(foreground, x, y)
        color = getColor(p)
        setColor(getPixel(self.startingMap, x , y , color))

  def moveRooms(self):
