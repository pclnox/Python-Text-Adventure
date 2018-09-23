import time
import sys


class CommandManager:
    def __init__(self):
        self.commands = ["help", "north", "east", "south", "west", "exit"]

    def TestForCommand(self):
        statement =  input(">>>")

        if statement in self.commands:
            run = "self." + statement.title() + "()"
            exec(run)

            '''if statement == self.commands[0]:
                self.Help()

            elif statement == self.commands[1]:
                self.North()

            elif statement == self.commands[2]:
                self.East()

            elif statement == self.commands[3]:
                self.South()

            elif statement == self.commands[4]:
                self.West()

            elif statement == self.commands[5]:
                self.Exit()'''

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
