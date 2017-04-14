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
