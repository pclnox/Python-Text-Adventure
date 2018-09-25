import time
import sys
import Data


# The command manager will test for and execute inputed commands
class CommandManager:
    # The constructor defines coordChange which will store the direction the user wants to move
    def __init__(self):
        self.coordChange = (0, 0)
        self.explore = False

    # This method tests the users input to see if its a command and runs it
    def TestForCommand(self):
        print()
        time.sleep(.5)
        statement = input(">>>")
        print()
        time.sleep(.25)

        if statement in Data.COMMANDS:
            run = "self." + statement.title() + "()"
            # exec allows for an efficient way of running the necessary method instead of using lots of if statements
            exec(run)

        # If the input isnt a valid command then the command manager follows up on that
        else:
            print("Enter a valid command")
            time.sleep(.5)
            print("Type help for a list of commands")

    # Help() prints out all the possible commands the user can do
    def Help(self):
        print("Commands:")
        time.sleep(.5)

        for command in Data.COMMANDS:
            print(command)
            time.sleep(.1)

    # North(), East(), South() and West() adjust coordChange to show the direction the player will move
    def North(self):
        print("You went North;")
        self.coordChange = (0, -1)
        time.sleep(.5)

    def East(self):
        print("You went East;")
        self.coordChange = (1, 0)
        time.sleep(.5)

    def South(self):
        print("You went South;")
        self.coordChange = (0, 1)
        time.sleep(.5)

    def West(self):
        print("You went West;")
        self.coordChange = (-1, 0)
        time.sleep(.5)

    # Explore() sets explore to true so that the player class knows to call Search() in the entity manager
    def Explore(self):
        print("You search the nearby area;")
        self.explore = True
        time.sleep(.5)

    # Run() asks which way the user wants to run to
    def Run(self):
        print("Where to?")
        time.sleep(.5)
        print("North, east, south or west?")

    # Exit() exits the game immediately
    # Save features will be implemented later on before the game exits
    def Exit(self):
        sys.exit()

    # Defines a setter for coordChange and defaults to reseting coordChange completely
    def setCoordChange(self, x=0, y=0):
        self.coordChange = (x, y)

    # Defines a setter for explore and defaults to resetting explore to false
    def setExplore(self, boolean=False):
        self.explore = boolean
