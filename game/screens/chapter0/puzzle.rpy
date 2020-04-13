
##### This is the script for the puzzle.



# Define images
image puzzle_background = "images/chapter0/portrait_puzzle/background_puzzle.png"
image chosen_img = "images/chapter0/portrait_puzzle/portrait.png"


init -10 python:
    is_in_puzzle = False
    def isInPuzzleSection(result):
        global is_in_puzzle
        is_in_puzzle = result

init python:
    ## Manage dragged pieces
    def piece_dragged(drags, drop):
        if not drop:
            return

        p_x = drags[0].drag_name[0]
        p_y = drags[0].drag_name[1]
        t_x = drop.drag_name[0]
        t_y = drop.drag_name[1]

        if p_x == t_x and p_y == t_y:
            my_x = int(p_x)*100+25
            my_y = int(p_y)*80+25
            drags[0].snap(my_x,my_y)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True
            for i in range(10):
                for j in range(10):
                    if placedlist[i,j] == False:
                        return
            return True
        return


## Create the picture puzzle and its parts. ####################################
screen jigsaw_puzzle:
    draggroup:
        for i in range(10):
            for j in range(10):
                $ name = "%s%s"%(i,j)
                $ my_x = i*100+50
                $ my_y = j*80+50
                drag:
                    drag_name name
                    child "images/chapter0/portrait_puzzle/blank_space.png"
                    draggable False
                    xpos my_x ypos my_y

        for i in range(10):
            for j in range(10):
                $ name = "%s%s piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    droppable False
                    dragged piece_dragged
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]
################################################################################


## Make a puzzle object. #######################################################
label puzzle:
    scene puzzle_background

    python:
        isInPuzzleSection(True)
        mainimage = im.Composite((1050, 850),(25, 25), "images/chapter0/portrait_puzzle/portrait.png")
        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        for i in range(10):
            for j in range(10):
                piecelist[i,j] = [renpy.random.randint(400, 1000)+700, renpy.random.randint(40, 880)]
                tempimage = im.AlphaMask(mainimage,"images/chapter0/portrait_puzzle/puzzle_pieces/%s_%s.png"%(j+1,i+1))
                imagelist[i,j] = im.Crop(tempimage, i*100,j*80, 150, 130)
                placedlist[i,j] = False

    call screen jigsaw_puzzle
    jump puzzle_done
################################################################################


## Call it when the puzzle is done. ############################################
label puzzle_done:
    python:
        isInPuzzleSection(False)
        game_state.portrait_done = True

    show black as bg_puzzle
    show chosen_img as puzzle_img at truecenter
    with dissolve

    user "Ho he aconseguit!!!"

    $ GiveGlossaryItemToPlayer(3)
    $ ShowItems()

    hide bg_puzzle
    hide puzzle_img

    return
################################################################################
