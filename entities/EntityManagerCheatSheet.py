import Data
import time
import random


# The entity manager manages the generation of entities for different locations
# It stores the generated data and relays that data to the user when exploring a location
class EntityManager:
    # The constructor initializes some temporary variables which store the entity data of each map coordinate
    def __init__(self):
        # [LakeCount, FishCount,
        #  GroveCount, TreeCount, TreeCount, GroveLakeCount, GroveLakeFishCount, GroveLakeFishCount,
        #  CaveCount, <Place for SubEntity in cave>, <SubEntity placeholder>, CaveLakeCount, CaveLakeFish, CaveLakeFish]
        self.entityMap = [[[None for i in range(14)] for j in range(len(Data.MAP[0]))] for k in range(len(Data.MAP))]

        # [boolean LocationExplored, boolean BigLake, boolean GroveLake, boolean CaveLake, boolean NoStuffAtLocation]
        self.exploredLocations = [[[None for i in range(5)] for j in range(len(Data.MAP[0]))] for k in range(len(Data.MAP))]

        for y in range(len(self.exploredLocations)):
            for x in range(len(self.exploredLocations[0])):
                self.exploredLocations[y][x][0] = False

    # Updates the necessary variables to be used in the other methods
    def Update(self, x, y):
        self.x = x
        self.y = y

    # If the location hasnt been explored before then it generates entities for the location then displays the results
    # Otherwise it just displays the results
    def SearchLocation(self, entityProbs):
        if not self.exploredLocations[self.y][self.x][0]:
            self.GenerateAllEntities(entityProbs)

            # If there arent any entities in that location then it sets the booleans to false
            # Sets NoStuffAtLocation to true
            if not self.AnyEntities():
                for i in range(4):
                    self.exploredLocations[self.y][self.x][i] = False

                self.exploredLocations[self.y][self.x][4] = True

            self.DisplayFound()

        else:
            print("You have already explored this location;")
            time.sleep(2)
            self.DisplayFound()

# DisplayFound() handles the location data and relays it to the user

    # Generates the entities
    def GenerateAllEntities(self, entityProbs):
        # The location has been explored
        self.exploredLocations[self.y][self.x][0] = True

        # i is used to cycle through entityProbs at the same time that entities is being iterated through
        # k is the generated amount of an entity e.g. 2 groves
        i, k = 0

        # Iterates through the entities
        for entity in Data.ENTITIES:
            # Iterates for the maximum amount of spawns they can have
            for j in range(entity.getMaxSpawns()):
                # Generates a random number to see whether there will be that entity
                if random.randint(1, 100) <= entityProbs[i]:
                    # Increases k
                    k += 1

            # Adds k to entityMap
            self.entityMap[self.y][self.x][entity.getEntityMapLocation()] = k
            # Increases i
            i += 1
            # Resets k
            k = 0
