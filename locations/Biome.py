class Biome:
    def __init__(self, name, mapValue, lakeProb, groveProb, caveProb):
        self.name = name
        self.mapValue = mapValue
        self.entityProbs = [lakeProb, groveProb, caveProb]

    def getName(self):
        return self.name

    def getMapValue(self):
        return self.mapValue

    def getEntityProbs(self):
        return self.entityProbs
