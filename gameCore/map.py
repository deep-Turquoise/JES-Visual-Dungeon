from image import *
from media import *
class Map:
  def __init__(self, left, right):
    self.startingMap = makePicture("images/startingMap.png")
    self.fullNormal  = makePicture("images/fullNormal.png")
    self.fullVisited = makePicture("images/fullVisited.png")
    self.zero        = makePicture("images/0.png")
    self.one         = makePicture("images/1.png")
    self.two         = makePicture("images/2.png")
    self.three       = makePicture("images/3.png")
    self.four        = makePicture("images/4.png")
    self.five        = makePicture("images/5.png")
    self.six         = makePicture("images/6.png")
    self.seven       = makePicture("images/7.png")
    self.eight       = makePicture("images/8.png")
    self.nine        = makePicture("images/9.png")
    self.numbers = ( self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine)
    self.setNumbers(left,right)
    show(self.startingMap)

  # this method copys only the 'red' parts of an image to a specified area
  # the number is a number, that it will take from the tuple of number images above
  # the start should be a tuple (xy coordinate to copy to)

  def pyCopyScreen(self, number, start):
    for x in range(45):
      for y in range(45):
        p = getPixel(self.numbers[number], x, y)
        color = getColor(p)
        if distance(red, color) < 130.0 :
          setColor(getPixel(self.startingMap, x + start[0], y + start[1]) , color)

  def setNumbers(self, left, right):
    self.pyCopy((650,55),(755,105), True)
    self.pyCopyScreen(left,  ( 655,55 ) )
    self.pyCopyScreen(right, ( 705,55) )

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
