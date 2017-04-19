from gui import *
from media import *
from game import *
from text import *
class Run:
    # Run constructor below initializes Run class and its functions
    # Run class basically handles the player's input once entered
    def __init__(self):
        self.moves = 0

        self.directions = {"north": 0, "n": 0, "south": 1, "s": 1,
                           "east": 2, "e": 2, "west": 3, "w": 3}
        self.searchTerms = {"chest": 0, "bookcase": 0, "cabinet": 0, "dresser": 0, "room": 1}

        self.myGame = Game()
        input = ""
        self.myText = Text()

        self.window = Display("Dungeon Controller", 800, 600, 75, 75)

        # create ui Elements
        self.button1 = Button("Go North", self.moveNorth)
        self.button2 = Button("Go South", self.moveSouth)
        self.button3 = Button("Go East",  self.moveEast)
        self.button4 = Button("Go West",  self.moveWest)

        self.textControl = TextField("type command and hit <ENTER> ", 18, self.resolveAction )

        #Place ui elements on controller window
        self.window.place(self.button1, 60, 10)
        self.window.place(self.button2, 60, 110)
        self.window.place(self.button3, 110, 60)
        self.window.place(self.button4, 10, 60)

        self.window.place(self.textControl, 10, 160)
    def moveNorth(self):
        self.moveCounter()
        self.myGame.move(0) #north
    def moveSouth(self):
        self.moveCounter()
        self.myGame.move(1) #south
    def moveEast(self):
        self.moveCounter()
        self.myGame.move(2) #east
    def moveWest(self):
        self.moveCounter()
        self.myGame.move(3) #west

    def resolveAction(self, input):
        input = input or ""
        input = input.lower()
        if input == "exit":
            showInformation("You remain trapped forever and die of starvation, but not before eating your own limbs...")
        elif input == "inventory":
            self.myGame.getPlayer().getItemList()
        elif input == "help":
            self.myText.help()
        elif input == "scream":
            scream = makeSound("sounds/scream.wav")
            play(scream)
            showInformation("You screamed. Didn't do anything since you're alone.")
        elif input == "inventory":
            self.myGame.printInventory()
        else:
            words = input.split()
            words.append("foo")
            if words[0] == "go":
                dir = words[1]
                if dir in self.directions.keys():
                    self.myGame.move(self.directions[dir])
                    if self.myGame.getPlayer().getRoom().getNumber() == 9:
                        showInformation(
                            "Good job " + self.myGame.getPlayer().getName() + " you have escaped!\n YOU WIN!")
                        input = "exit"
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
                    showInformation("I did not understand that direction.")
            # error Handing
            else:
                showInformation("You entered someting wrong. Try again.")
                self.moves -= 1
        self.moveCounter()
        
    def moveCounter(self):
        a = (76 - self.moves) / 10
        b = (76 - self.moves) % 10
        self.myGame.getMap().setNumbers(a, b)
        self.moves += 1
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
        '''

            input = requestString("What you would like to do:")

            elif input == "inventory":
                self.myGame.getPlayer().getItemList()
            elif input == "help":
                self.myText.help()
            elif input == "scream":
                scream = makeSound("sounds/scream.wav")
                play(scream)
                showInformation("You screamed. Didn't do anything since you're alone.")
            elif input == "inventory":
                self.myGame.printInventory()
            else:
                words = input.split()
                words.append("foo")
                if words[0] == "go":
                    dir = words[1]
                    if dir in self.directions.keys():
                        self.myGame.move(self.directions[dir])
                        if self.myGame.getPlayer().getRoom().getNumber() == 9:
                            showInformation(
                                "Good job " + self.myGame.getPlayer().getName() + " you have escaped!\n YOU WIN!")
                            input = "exit"
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
                        showInformation("I did not understand that direction.")
                # error Handing
                else:
                    showInformation("You entered someting wrong. Try again.")
                    self.moves -= 1
        '''
