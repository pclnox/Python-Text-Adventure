import Data
import time


class LocationManager:
    def Update(self, x, y, previousX, previousY, biome):
        self.x = x
        self.y = y
        self.previousX = previousX
        self.previousY = previousY
        self.biome = biome

    def ChangeLocation(self, coordChange):
        self.previousX = self.x
        self.previousY = self.y
        self.x += coordChange[0]
        self.y += coordChange[1]

        if self.x < 0 or self.y < 0 or self.x >= len(Data.MAP[0]) or self.y >= len(Data.MAP):
            self.x = self.previousX
            self.y = self.previousY
            print("That's the sea;")
            time.sleep(2)
            print("Swim or run?")

        elif Data.MAP[self.y][self.x] == Data.SHORE.getMapValue():
            if self.biome == Data.SHORE:
                print("You are still on the beach;")
                time.sleep(2)
                print("It seems to stretch on forever, wrapping the island;")
                time.sleep(2)
                print("Swim, explore or run?")

            else:
                self.biome = Data.SHORE
                print("You have reached the shore;")
                time.sleep(2)
                print("Swim, explore or run?")

        elif Data.MAP[self.y][self.x] == Data.WOODS.getMapValue():
            if self.biome == Data.WOODS:
                print("You are still on the woods;")
                time.sleep(2)
                print("It seems to stretch on forever;")
                time.sleep(2)
                print("Explore or run?")

            else:
                self.biome = Data.WOODS
                print("You enter the woods;")
                time.sleep(2)
                print("Explore or run?")

        elif Data.MAP[self.y][self.x] == Data.PLAINS.getMapValue():
            if self.biome == Data.PLAINS:
                print("You are still on the plains;")
                time.sleep(2)
                print("It seems to stretch on forever, as far as the eye can see;")
                time.sleep(2)
                print("Explore or run?")

            else:
                self.biome = Data.PLAINS
                print("You are on the plains")
                time.sleep(2)
                print("Explore or run?")

        elif Data.MAP[self.y][self.x] == Data.MOUNTAINS.getMapValue():
            if self.biome == Data.MOUNTAINS:
                print("You are still in the mountains;")
                time.sleep(2)
                print("They seem to reach endlessly into the sky and on into the distance;")
                time.sleep(2)
                print("Explore or run?")

            else:
                self.biome = Data.MOUNTAINS
                print("You climb the mountains;")
                time.sleep(2)
                print("Explore or run?")

        elif Data.MAP[self.y][self.x] == Data.DESERT.getMapValue():
            if self.biome == Data.DESERT:
                print("You are still in the desert;")
                time.sleep(2)
                print("It seems to stretch on forever, or is that a mirage?")
                time.sleep(2)
                print("Explore or run?")

            else:
                self.biome = Data.DESERT
                print("You enter arid desert;")
                time.sleep(2)
                print("Explore or run?")

        elif Data.MAP[self.y][self.x] == Data.VOLCANO.getMapValue():
            self.biome = Data.VOLCANO
            print("You climb the lone volcano;")
            time.sleep(2)
            print("Explore or run?")

        else:
            self.x = self.previousX
            self.y = self.previousY
            print("That's the sea;")
            time.sleep(2)
            print("Swim or run?")

        return self.x, self.y, self.previousX, self.previousY, self.biome
