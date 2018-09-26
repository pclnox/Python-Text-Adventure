# Defines the entity class to easily create new entities which store their relevant data
class Entity:
    # The constructor takes arguments about the entity which will be stored and provided to other classes through getters
    def __init__(self, name, maxSpawns, entityMapLocation, fishProb, treesProb, lakeProb):
        self.name = name
        self.maxSpawns = maxSpawns
        self.entityMapLocation = entityMapLocation
        self.subEntityProbs = [fishProb, treesProb, lakeProb]

    # The getters return the requested information about the entity to the caller
    def getName(self):
        return self.name

    def getMaxSpawns(self):
        return self.maxSpawns

    def getEntityMapLocation(self):
        return self.entityMapLocation

    def getSubEntityProbs(self):
        return self.subEntityProbs
