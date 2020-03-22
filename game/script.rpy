# The script of the game.

######## Global Variables ################
# Define the player name
default persistent.playername = ""
default player = persistent.playername

#Define characters
define user = Character("[player]", color="#6E36CA")
define unknown = Character("...", color="#FFFFFF")
define unknown_girl = Character("Dona", color="#FFFFFF")
define unknown_boy = Character("Home", color="#231F20")


#########################################



# The game starts here.

label start:

    $ chapter = 0
    $ astell_is_nice = False

    ## Beginning: once upon a time
    call beginning

    ## Library: main menu
    call screen library

    # This ends the game.
    return
