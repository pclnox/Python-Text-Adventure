from location import Biome


startingX = None
startingY = None

SHORE = Biome.Biome("shore", 1, 0, 0, 50)
WOODS = Biome.Biome("woods", 2, 50, 70, 60)
PLAINS = Biome.Biome("plains", 3, 60, 50, 60)
MOUNTAINS = Biome.Biome("mountians", 4, 0, 0, 0)
DESERT = Biome.Biome("desery", 5, 0, 0, 0)
VOLCANO = Biome.Biome("volcano", 6, 0, 0, 0)
SEA = Biome.Biome("sea", -2, 0, 0, 0)

MAP = [[-2, 1, 1, 1, 1, 1, -2],
       [1,  1, 4, 2, 2, 1,  1],
       [1,  4, 2, 3, 2, 2,  1],
       [1,  4, 3, 5, 5, 5,  1],
       [1,  0, 3, 5, 6, 5,  1],
       [1,  3, 2, 3, 5, 5,  1],
       [1,  5, 5, 4, 4, 1,  1],
       [1,  1, 1, 1, 1, 1, -2]]
