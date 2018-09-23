import time
import sys


class CommandManager:
    def __init__(self):
        self.commands = ["help", "north", "east", "south", "west", "exit"]

    def TestForCommand(self):
        statement = input(">>>")

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

        for command in self.commands:
            print(command)

    def North(self):
        # self.y -= 1
        print("You went North")

    def East(self):
        # self.x += 1
        print("You went East")

    def South(self):
        # self.y += 1
        print("You went South")

    def West(self):
        # self.x -= 1
        print("You went West")

    def Exit(self):
        sys.exit()
