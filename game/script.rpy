﻿# The script of the game.



default persistent.playername = ""
default player = persistent.playername

# The game starts here.

label start:

    scene bg room

    "HI THERE, [player]"

    # This ends the game.
    return
