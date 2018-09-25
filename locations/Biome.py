import random

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
