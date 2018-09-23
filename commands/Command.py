import time
import sys


class CommandManager:
    def __init__(self):
        self.commands = ["help", "north", "east", "south", "west", "exit"]

    def TestForCommand(self):
        statement = "help"  # input(">>>")

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

    def Exit(self):
        sys.exit()


c = CommandManager()
c.TestForCommand()
