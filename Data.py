from locations import Biome
import random
import time

SHORE = Biome.Biome("shore", 1, 0, 0, 50)
WOODS = Biome.Biome("woods", 2, 50, 70, 60)
PLAINS = Biome.Biome("plains", 3, 60, 50, 60)
MOUNTAINS = Biome.Biome("mountians", 4, 0, 0, 0)
DESERT = Biome.Biome("desery", 5, 0, 0, 0)
VOLCANO = Biome.Biome("volcano", 6, 0, 0, 0)
SEA = Biome.Biome("sea", -2, 0, 0, 0)

BIOMES = [SHORE, WOODS, PLAINS, MOUNTAINS, DESERT, VOLCANO]

MAP = [[-2, 1, 1, 1, 1, 1, -2],
       [1,  1, 4, 2, 2, 1,  1],
       [1,  4, 2, 3, 2, 2,  1],
       [1,  4, 3, 5, 5, 5,  1],
       [1,  3, 3, 5, 6, 5,  1],
       [1,  3, 2, 3, 5, 5,  1],
       [1,  5, 5, 4, 4, 1,  1],
       [1,  1, 1, 1, 1, 1, -2]]

for i in range(20):
    PLAYER_STARTING_X = random.randint(0, 6)
    PLAYER_STARTING_Y = random.randint(0, 7)

    if MAP[PLAYER_STARTING_Y][PLAYER_STARTING_X] == 1:
        break

    elif i == 19:
        PLAYER_STARTING_X = 0
        PLAYER_STARTING_Y = random.randint(1, 6)

for biome in BIOMES:
    if biome.getMapValue() == MAP[PLAYER_STARTING_X][PLAYER_STARTING_Y]:
        PLAYER_STARTING_BIOME = biome


def StartingMessage():
    time.sleep(0.5)
    print("Welcome to the Abandoned Island!")
    time.sleep(1)
    print("-" * 30)
    time.sleep(1)
    print("You wake up on an abandoned island;")
    time.sleep(2)
    print("The storm destroyed your cruise ship;")
    time.sleep(2)
    print("You are the only survivor.")
