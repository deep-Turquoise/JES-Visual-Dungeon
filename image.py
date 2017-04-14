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
