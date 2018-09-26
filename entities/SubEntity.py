# Defines the sub-entity class to easily create new sub-entities which store their relevant data
class SubEntity:
    # The constructor takes arguments about the sub-entity which will be stored and provided to other classes through getters
    def __init__(self, name, minSpawns, maxSpawns, entityMapLocationStart, entityMapLocationEnd):
        self.name = name
        self.minSpawns = minSpawns
        self.maxSpawns = maxSpawns
        self.entityMapLocationStart = entityMapLocationStart
        self.entityMapLocationEnd = entityMapLocationEnd

    # The getters return the requested information about the sub-entity to the caller
    def getName(self):
        return self.name

    def getMinSpawns(self):
        return self.minSpawns

    def getMaxSpawns(self):
        return self.maxSpawns

    def getEntityMapLocationStart(self):
        return self.entityMapLocationStart

    def getEntityMapLocationEnd(self):
        return self.entityMapLocationEnd
