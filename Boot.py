import Player
import Data

running = True

player = Player.Player()

Data.StartingMessage()

while running:
    player.Update()
