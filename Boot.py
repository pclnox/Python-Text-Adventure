import Player
import Data

# Defines running for the game loop
running = True

# Initializes the player which will handle most of the game
player = Player.Player()

# Displays the starting message
Data.StartingMessage()

# Game loop and updates the player each iteration
while running:
    player.Update()
