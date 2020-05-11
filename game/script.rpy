
# The script of the game.


######## Global Variables ######################################################

# General game progress state
default game_state = GameState()

#Define characters
define user = Character("[tmpSavePlayer]", color="#9575cd")
define unknown = Character("...", color="#e57373")
define unknown_girl = Character(_("Dona"), color="#7986cb")
define unknown_boy = Character(_("Home"), color="#f06292")
define unknown_little_boy = Character(_("Nen"), color="#ba68c8")

################################################################################



# The game starts here.

label start:

    python:
        game_state.clear()
        is_secret_revealed = False
        seneca_agrees = 0

    ## Beginning: once upon a time
    call beginning

    ## Library: main menu
    call screen library

    # This ends the game.
    return



screen hold_screen(seconds=0):
    timer seconds action Return("")

screen show_return(x,y,img,img_hover):
    imagebutton:
        idle "gui/arrows/" + img
        hover "gui/arrows/" + img_hover
        xpos x
        ypos y
        action Rollback()
