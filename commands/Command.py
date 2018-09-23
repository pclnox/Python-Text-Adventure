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
            print("Enter a valid command")
            time.sleep(.5)
            print("Type help for a list of commands")

    def Help(self):
        print("Commands:")

        for command in self.commands:
            print(command)

    def North(self):
        pass

    def East(self):
        pass

    def South(self):
        pass

    def West(self):
        pass

    def Exit(self):
        sys.exit()
