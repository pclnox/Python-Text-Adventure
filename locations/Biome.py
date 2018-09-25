# Defines the biome class to easily create new biomes which store their relevant data
class Biome:
    # The constructor takes arguments about the biome which will be stored and provided through getters
    def __init__(self, name, mapValue, lakeProb, groveProb, caveProb):
        self.name = name
        self.mapValue = mapValue
        self.entityProbs = [lakeProb, groveProb, caveProb]

    # The getters return the requested information about the biome to the caller
    def getName(self):
        return self.name

    def getMapValue(self):
        return self.mapValue

    def getEntityProbs(self):
        return self.entityProbs

    '''def FeatureGenerator(self, lakeProb, groveProb, caveProb):
        lakeCheck = random.randint(0, 100)
        groveCheck = random.randint(0, 100)
        caveCheck = random.randint(0, 100)
        if lakeCheck <= lakeProb:
            self.lake = True

        if groveCheck <= groveProb:
            self.grove = True

        if caveCheck <= caveProb:
            self.cave = True'''
