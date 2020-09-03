# Name = Julian Bharadwaja
# Copyright Julian Bharadwaja 
import random
import sys
import os
# importing cycle for iterating list repeatedly
from itertools import cycle

# Dictionary, translating the "r/p/s" choice into actual words, not currently in use.
RPS_literal = {"r": "rock", "p": "paper", "s": "scissors"}
# Dictionary to convert the r/p/s choice into numbers, for the maths bit in verifyWinner
RPS_math = {"r": 0, "p": 1, "s": 2}


class Player(object):
    def __init__(self, name):
        self.lives = 3
        self.name = name
        self.userPoint = 0
        self.compPoint = 0

    def loseLife(self):  # Simple wrapper to reduce the game count.
        self.lives -= 1

    def gainPoint(self):  # Simple wrapper to add a point to the user
        self.userPoint += 1

    def gainComPoint(self):  # Simple wrapper to add a point to the computer
        self.compPoint += 1


class RPS(Player):
    def __init__(self, name):
        # Initialise the parent class. Read up on "Object-Oriented Inheritence"
        super(RPS, self).__init__(name)
        # Initialise the choices and pool for the cycle choice from the input
        self.choices = ["r", "p", "s"]
        self.pool = cycle(self.choices)
        self.p1Input = None  # Create the variable.
        self.compInput = None  # Create the variable.

    def clearUp(self):
        # Set the value to none, so the userChoice does fool it's own way out.
        self.p1Input = None
        self.compInput = None  # Set this to none, just for continuity.

    def computerChoice(self):
        # Set the random value to the computer Input
        self.compInput = random.choice(["r", "p", "s"])

    def randomChoice(self):
        # Set the random value to the user Input
        self.p1Input = random.choice(["r", "p", "s"])

    def onlyRockChoice(self):
        # Set the rock value to the user input for only rock game type
        self.p1Input = "r"

    def userChoice(self):
        # Keep asking until the user gives an actual input.
        while self.p1Input not in RPS_literal:
            self.p1Input = input(
                "Do you choose: Rock(r), Paper(p) or Scissors(s): ").lower()
            if self.p1Input == "":  # Check if the user even gave an input.
                print("You didn't choose anything. Please choose something :)")
            elif self.p1Input not in RPS_literal:  # Check if the user has given a valid input
                print("Invalid entry. Please choose one of the given choices.")

    def verifyWinner(self):
        p1Math = RPS_math.get(self.p1Input, None)
        compMath = RPS_math.get(self.compInput, None)

        if (p1Math+1) % 3 == compMath:
            # Make the user lose a life, once on 0, logic within the main while loop quits the game.
            self.loseLife()
            self.gainComPoint()
            print("\nUser Input-%s \t\t\t Computer Input-%s\n" %
                  (self.p1Input, self.compInput))
            print("\nSorry 'bout this. You lost. You now have %d lives left.\n" %
                  (self.lives))  # Print loss/win/draw to the terminal
        elif p1Math == compMath:  # If the two inputs match, it's clearly a draw.
            # Print loss/win/draw to the terminal
            print("\nUser Input-%s \t\t\t Computer Input-%s\n" %
                  (self.p1Input, self.compInput))
            print("\nAh shoot. You didn't win, you didn't lose though, so all's good!\n")
        else:
            # Print loss/win/draw to the terminal, this one wins by default.
            self.loseLife()
            self.gainPoint()
            print("\nUser Input-%s \t\t\t Computer Input-%s\n" %
                  (self.p1Input, self.compInput))
            print("\nWahoo! Well done, %s, you won!\n" % (self.name))

        self.clearUp()


def exit():
    print('\nBye Bye! See you later!!')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)


# is used to execute some code only if the file was run directly, and not imported
if __name__ == "__main__":

    # Setting game as a variable, so checking if RPS is instantiated as game is possible.
    game = None
    while True:
        try:
            # Check if game is an instantiated object.
            if not isinstance(game, RPS):
                # Setting input for the user name.
                temp_name = input("Enter your name: ")
                # Printing out the instruction after typing name
                print("Game Type \n (1) Random \n (2) Rock Only\n (3) Cycle\n (4) Input")
                # Checking the user input for interger and number input for the program
                while True:
                    try:
                        condition = True
                        while(condition):
                            game_type = int(
                                input("Which type of game will you be playing? Enter your number: "))
                            if(game_type >= 5 or game_type <= 0):
                                print("\n Please Type Between 1 and 4 :) \n")
                                condition = True
                            else:
                                condition = False
                        break
                    except:
                        print("\nPlease Type A Number!\n")
                # Instantiate RPS as 'game', passing the name just recorded as a parameter.
                game = RPS(temp_name)

                del temp_name  # Delete temp_name variable, cuz why not...

            elif game.lives == 0:  # Check if user is out of lives and exit the game.
                # Condition for checking the winner
                if game.compPoint > game.userPoint:
                    print("You Lost the game! %s Computer - %s %s" %
                          (game.compPoint, game.userPoint, game.name))
                else:
                    print("You Win!!!! %s Computer - %s %s" %
                          (game.compPoint, game.userPoint, game.name))
                print("Oh no! %s, you have run out of lives! Guess you'll have to try again later!" % (
                    game.name))
                exit()

            elif isinstance(game, RPS):

                # For Game Type 4 Input
                if game_type == 4:
                    game.userChoice()
                    game.computerChoice()
                    game.verifyWinner()
                    if input("Would you like to stop game? Type quit ").lower() == "quit":
                        exit()
                # For Game Type 1 Random
                elif game_type == 1:
                    game.randomChoice()
                    game.computerChoice()
                    game.verifyWinner()

                # For Game Type 2 Only Rock
                elif game_type == 2:
                    game.onlyRockChoice()
                    game.computerChoice()
                    game.verifyWinner()

                # For Game Type Cycle
                else:
                    # using next to grab the item but not the same index
                    game.p1Input = next(game.pool)
                    game.computerChoice()
                    game.verifyWinner()

        except KeyboardInterrupt:
            exit()
