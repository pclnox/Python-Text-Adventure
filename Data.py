from locations import Biome
import random
import time
from entities import Entity
from entities import SubEntity

# Defines what commands there are
COMMANDS = ["help", "north", "east", "south", "west", "run", "exit", "explore"]

# Defines the different biomes
SHORE = Biome.Biome("shore", 1, 0, 0, 50)
WOODS = Biome.Biome("woods", 2, 50, 70, 60)
PLAINS = Biome.Biome("plains", 3, 60, 50, 60)
MOUNTAINS = Biome.Biome("mountians", 4, 0, 0, 0)
DESERT = Biome.Biome("desery", 5, 0, 0, 0)
VOLCANO = Biome.Biome("volcano", 6, 0, 0, 0)
SEA = Biome.Biome("sea", -2, 0, 0, 0)

# Puts the biomes into one list which can be used when needing to iterate through the biomes
BIOMES = [SHORE, WOODS, PLAINS, MOUNTAINS, DESERT, VOLCANO]

# Defines the set game map
MAP = [[-2, 1, 1, 1, 1, 1, -2],
       [1,  1, 4, 2, 2, 1,  1],
       [1,  4, 2, 3, 2, 2,  1],
       [1,  4, 3, 5, 5, 5,  1],
       [1,  3, 3, 5, 6, 5,  1],
       [1,  3, 2, 3, 5, 5,  1],
       [1,  5, 5, 4, 4, 1,  1],
       [1,  1, 1, 1, 1, 1, -2]]

# Gives the player a random starting coordinate on the shore
for i in range(20):
    PLAYER_STARTING_X = random.randint(0, 6)
    PLAYER_STARTING_Y = random.randint(0, 7)

    if MAP[PLAYER_STARTING_Y][PLAYER_STARTING_X] == 1:
        break

    elif i == 19:
        PLAYER_STARTING_X = 0
        PLAYER_STARTING_Y = random.randint(1, 6)

# Iterates through the biomes to give the player the starting biome of its coordinate
# This will be more useful when different types of shore are added for the player to start on
for biome in BIOMES:
    if biome.getMapValue() == MAP[PLAYER_STARTING_Y][PLAYER_STARTING_X]:
        PLAYER_STARTING_BIOME = biome

# Defines the different entities
LAKE = Entity.Entity("lake", 1, 0, 100, 0, 40)
GROVE = Entity.Entity("grove", 2, 2, 0, 100, 40)
CAVE = Entity.Entity("cave", 2, 8, 0, 0, 40)

# Puts the entities into one list which can be used when needing to iterate through the entities
ENTITIES = [LAKE, GROVE, CAVE]

# Defines the different sub-entities
FISH = SubEntity.SubEntity("fish", 1, 150, 1, 1)
TREES = SubEntity.SubEntity("trees", 10, 20, 3, 4)
GROVE_LAKE = SubEntity.SubEntity("lake", 0, 0, 5, 5)
GROVE_FISH = SubEntity.SubEntity("fish", 0, 0, 6, 7)
CAVE_LAKE = SubEntity.SubEntity("lake", 0, 0, 11, 11)
CAVE_FISH = SubEntity.SubEntity("fish", 0, 0, 12, 13)

# Puts the sub-entities into one list which can be used when needing to iterate through the sub-entities
SUB_ENTITIES = [FISH, TREES, GROVE_LAKE, GROVE_FISH, CAVE_LAKE, CAVE_FISH]


# This method defines the starting message to print to the user
def StartingMessage():
    time.sleep(0.5)
    print("Welcome to the Abandoned Island!")
    time.sleep(1)
    print("-" * 30)
    time.sleep(1)
    print("You wake up on an abandoned island;")
    time.sleep(1.5)
    print("The storm destroyed your cruise ship;")
    time.sleep(1.5)
    print("You are the only survivor.")
    time.sleep(.5)
