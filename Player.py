from commands import Command
from locations import LocationManager
import Data
from entities import EntityManager


# Defines the player class which will handle most of the game
class Player:
    # The constructor initializes variables and instantiates other clases ready for use
    def __init__(self):
        self.x = Data.PLAYER_STARTING_X
        self.y = Data.PLAYER_STARTING_Y
        self.previousX = self.x
        self.previousY = self.y
        self.biome = Data.PLAYER_STARTING_BIOME

        self.commandManager = Command.CommandManager()
        self.locationManager = LocationManager.LocationManager()
        self.entityManager = EntityManager.EntityManager()

    # The update method updates the instantiated classes and tests for a command input from the user
    def Update(self):
        self.locationManager.Update(self.x, self.y, self.previousX, self.previousY, self.biome)
        self.entityManager.Update(self.x, self.y)
        self.commandManager.TestForCommand()

        # If the user requested to move then the player will update its variables to the new location
        if self.commandManager.coordChange != (0, 0):
            self.x, self.y, self.previousX, self.previousY,
            self.biome = self.locationManager.ChangeLocation(self.commandManager.coordChange)
            # The player has moved therefore coordChange can be reset
            self.commandManager.setCoordChange()

        # If the user requested to explore the location then the player calls that in the entity manager
        elif self.commandManager.explore:
                self.entityManager.SearchLocation(self.biome.getEntityProbs())
                # The player has explored the location therefore explore can be reset
                self.commandManager.setExplore()
