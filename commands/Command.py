import time
import sys


class CommandManager:
    def __init__(self):
        self.commands = ["help", "north", "east", "south", "west", "exit"]
        self.coordChange = (0, 0)

    def TestForCommand(self):
        time.sleep(.5)
        statement = input(">>>")
        time.sleep(.25)

        if statement in self.commands:
            run = "self." + statement.title() + "()"
            exec(run)

        else:
            print()
            print("Enter a valid command")
            time.sleep(.5)
            print("Type help for a list of commands")

    def Help(self):
        print()
        print("Commands:")
        time.sleep(.5)

        for command in self.commands:
            print(command)
            time.sleep(.1)

    def North(self):
        print()
        print("You went North")
        self.coordChange = (0, -1)
        time.sleep(.5)

    def East(self):
        print()
        print("You went East")
        self.coordChange = (1, 0)
        time.sleep(.5)

    def South(self):
        print()
        print("You went South")
        self.coordChange = (0, 1)
        time.sleep(.5)

    def West(self):
        print()
        print("You went West")
        self.coordChange = (-1, 0)
        time.sleep(.5)

    def Exit(self):
        sys.exit()

    def setCoordChange(self, x=0, y=0):
        self.coordChange = (x, y)
