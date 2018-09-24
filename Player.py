from commands import Command
from locations import Location
import Data


class Player:
    def __init__(self):
        self.x = Data.startingX
        self.y = Data.startingY
        self.previousX = self.x
        self.previousY = self.y

        self.commandManager = Command.CommandManager()
        self.locationManager = Location.LocationManager()

    def Update(self):
        self.locationManager.Update(self.x, self.y, self.previousX, self.previousY)
        self.commandManager.TestForCommand()

        if self.commandManager.coordChange != (0, 0):
            self.locationManager.ChangeLocation(self.commandManager.coordChange)
            self.commandManager.setCoordChange()
