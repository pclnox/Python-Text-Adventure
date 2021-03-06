from commands import Command
from locations import LocationManager
import Data


class Player:
    def __init__(self):
        self.x = Data.PLAYER_STARTING_X
        self.y = Data.PLAYER_STARTING_Y
        self.previousX = self.x
        self.previousY = self.y
        self.biome = Data.PLAYER_STARTING_BIOME

        self.commandManager = Command.CommandManager()
        self.locationManager = LocationManager.LocationManager()

    def Update(self):
        self.locationManager.Update(self.x, self.y, self.previousX, self.previousY, self.biome)
        self.commandManager.TestForCommand()

        if self.commandManager.coordChange != (0, 0):
            self.x, self.y, self.previousX, self.previousY, self.biome = self.locationManager.ChangeLocation(self.commandManager.coordChange)
            self.commandManager.setCoordChange()
