
# The script of the game.


######## Global Variables ######################################################

# Define the player name
default player = ""
# Define the temporary last save name
default saveName = ""
default tmpSaveName = ""
# Define the achievements of player for the glossary
default items_player = []

# Define variables for conditions
default portrait_done = False
default astell_is_nice = False
default wollstonecraft_is_seen = False
default asmau_is_seen = False

#Define characters
define user = Character("[player]", color="#6E36CA")
define unknown = Character("...", color="#FFFFFF")
define unknown_girl = Character("Dona", color="#FFFFFF")
define unknown_boy = Character("Home", color="#231F20")

################################################################################



# The game starts here.

label start:

    python:
        glossary_unread_items = []
        items_player = []
        chapter = 0
        astell_is_nice = False
        portrait_done = False
        wollstonecraft_is_seen = False
        asmau_is_seen = False

    ## Beginning: once upon a time
    call beginning

    ## Library: main menu
    call screen library

    # This ends the game.
    return
