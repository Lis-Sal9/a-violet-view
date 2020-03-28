

## Script for the library scene.
## The library is the main menu of the game. It is the main scene for the player.



screen library():
    key "K_ESCAPE" action MainMenu()

    imagemap:
        ground "images/library.png"
        hotspot (1065, 414, 32, 80) action Jump("chapter_0")
