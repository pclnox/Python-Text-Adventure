from commands import Command


class Player:
    def __init__(self):
        self.x = None
        self.y = None
        self.previousX = self.x
        self.previousY = self.y
        self.commandManager = Command.CommandManager()
        # self.biome = Location.

    def Update(self):
        self.commandManager.TestForCommand()
