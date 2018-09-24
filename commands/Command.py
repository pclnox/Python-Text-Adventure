import time
import sys


class CommandManager:
    def __init__(self):
        self.commands = ["help", "north", "east", "south", "west", "run", "exit"]
        self.coordChange = (0, 0)

    def TestForCommand(self):
        print()
        time.sleep(.5)
        statement = input(">>>")
        time.sleep(.25)

        if statement in self.commands:
            run = "self." + statement.title() + "()"
            exec(run)

        else:
            print("Enter a valid command")
            time.sleep(.5)
            print("Type help for a list of commands")

    def Help(self):
        print("Commands:")
        time.sleep(.5)

        for command in self.commands:
            print(command)
            time.sleep(.1)

    def North(self):
        print("You went North")
        self.coordChange = (0, -1)
        time.sleep(.5)

    def East(self):
        print("You went East")
        self.coordChange = (1, 0)
        time.sleep(.5)

    def South(self):
        print("You went South")
        self.coordChange = (0, 1)
        time.sleep(.5)

    def West(self):
        print("You went West")
        self.coordChange = (-1, 0)
        time.sleep(.5)

    def Run(self):
        print("Where to?")
        time.sleep(.5)
        print("North, east, south or west?")

    def Exit(self):
        sys.exit()

    def setCoordChange(self, x=0, y=0):
        self.coordChange = (x, y)
