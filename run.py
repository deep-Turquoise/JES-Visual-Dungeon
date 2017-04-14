from game import *
class Run:
    # Run constructor below initializes Run class and its functions
    # Run class basically handles the player's input once entered
    def __init__(self):
        self.moves = 0
        self.directions = {"north": 0, "n": 0, "south": 1, "s": 1,
                           "east": 2, "e": 2, "west": 3, "w": 3}
        self.searchTerms = {"chest": 0, "bookcase": 0, "cabinets": 0, "dresser": 0, "room": 1}

        #self.myGame = Game()
        self.user_Input = ""
        while self.user_Input != "exit":
            self.user_Input = requestString("What you would like to do:")
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
                showInformation(
                    "You stumble, and realize you've eaten your fingers, you can no longer stand, but crawl")
            if self.moves == 74:
                showInformation("You see visions of food heaven, and lay motionless while eating your limbs...")
            if self.moves >= 75:
                showInformation(self.myGame.getPlayer().getName() + " you ran out of moves!")
                self.user_Input = "exit"
            self.moves += 1
            self.user_Input = self.user_Input or ""
            self.user_Input = self.user_Input.lower()
            if self.user_Input == "exit":
                printNow("You remain trapped forever and die of starvation, but not before eating your own limbs...")
            elif self.user_Input == "inventory":
                self.myGame.getPlayer().getItemList()
            elif self.user_Input == "help":
                help()
            elif self.user_Input == "scream":
                printNow("You screamed. Didn't do anything since you're alone.")
            elif self.user_Input == "inventory":
                self.myGame.printInventory()
            else:
                words = self.user_Input.split()
                words.append("foo")
                if words[0] == "go":
                    dir = words[1]
                    if dir in self.directions.keys():
                        self.myGame.move(self.directions[dir])
                        if self.myGame.getPlayer().getRoom().getNumber() == 9:
                            showInformation(
                                "Good job " + self.myGame.getPlayer().getName() + " you have escaped!\n YOU WIN!")
                            self.user_Input = "exit"
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
                        printNow("I did not understand that direction.")
                # error Handing
                else:
                    printNow("You entered someting wrong. Try again.")
                    self.moves -= 1