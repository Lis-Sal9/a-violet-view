
# The script of the game.


######## Global Variables ######################################################

# General game progress state
default game_state = GameState()

#Define characters
define user = Character("[tmpSavePlayer]", color="#6E36CA")
define unknown = Character("...", color="#FFFFFF")
define unknown_girl = Character("Dona", color="#FFFFFF")
define unknown_boy = Character("Home", color="#231F20")
define unknown_little_boy = Character("Nen", color="#231F20")

################################################################################



# The game starts here.

label start:

    python:
        game_state = GameState()

    ## Beginning: once upon a time
    call beginning

    ## Library: main menu
    call screen library

    # This ends the game.
    return



screen hold_screen(seconds=0):
    timer seconds action Return("")
