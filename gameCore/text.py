from media import *
from textwrap import dedent
class Text:
  def __init__(self):
    None
  def intro_Outputs(self):  # this function serves as an introduction upon initialization of the game
    info = dedent("""
    Welcome to the dungeon! Try to find your away around.
    In this dungeon you must find 3 keys to escape.
    At least one of the keys is in a hidden room!
    You have 75 moves before you die.
    Enter help for command information.
    Good Luck!""")
    printNow(info)
    showInformation(info)

  def help(self):  # this function lists the possible commands a player can enter
    info = dedent("""
    Use the direction buttons to move.
    
    Use these commands for actions:
    help - to list the commands you need
    scream - you scream
    inventory - get list of items you are carrying.
    search <location> - Search a room or bookcase etc. e.g. search Bookcase
    take <item> - Take an item e.g. take key
    unlock <direction> - Unlock the door in the specified direction e.g. unlock w
    """)
    printNow(info)
    showInformation(info)
