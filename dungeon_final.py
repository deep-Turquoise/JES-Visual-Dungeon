#Silicon Beach Software
#Lab 13 redo of lab 12
#David Henderson
#Chris Calderon
#Nicholas Nelson
#Nathan Muaga
#Haley Dimapilis


#This Lets us pick a media folder, and then not have to ask for each file
setMediaFolder(pickAFolder())
#This is just to deal with JES oddities, so our code can find the rest of our modules
sys.path.append(getMediaPath())

from game import *
from room import *
from image import *
from player import *
from run import *
from text import *
from chest import *
from key import *


def main():                                                                        #this function prompts the player upon initialization of the game
      intro_Outputs()
      help()
      printNow("We are having you start off at the Foyer")
      printNow("The door suddenly locks behind you. You must now find a way out.")
      go = Run()



main()
