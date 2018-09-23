from commands import Command


class Player:
    def __init__(self):
        self.x = None
        self.y = None
        self.previousX = self.x
        self.previousY = self.y
        self.commandManager = Command.CommandManager(self)
        self.commandManager = Command.CommandManager()

    def Update(self):
        self.commandManager.TestForCommand(self)
        self.commandManager.TestForCommand()
