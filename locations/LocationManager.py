# import Player


class LocationManager:
    def __init__(self, grid):
        self.map = grid.getMap()

    def Update(self, x, y, previousX, previousY):
        self.currentLocation = (x, y)
        self.previousLocation = (previousX, previousY)

    def ChangeLocation(self, coordChange):
        self.previousLocation = self.currentLocation
        self.currentLocation = (self.currentLocation[0] + coordChange[0], self.currentLocation[1] + coordChange[1])

        return self.currentLocation, self.previousLocation


class TileGrid:
    pass
