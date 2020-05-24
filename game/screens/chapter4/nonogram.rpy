init -10 python:
    MAX_LIVES = 3

    NONOGRAM_SOLUTION = [
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    NONOGRAM_SOLUTION_ROWS_ST = """        4
        8
      4 3
      2 3
2 1 2 2 2
  2 6 2 2
2 3 4 2 2
   2 2 16
2 3 3 2 2
2 2 2 2 2
2 3 2 2 2
      2 3
      3 3
        8
        5"""

    NONOGRAM_SOLUTION_COLUMNS_ST = """    1
    1
    1
    7
    7
    1
    1
    1
    5
    9
  313
  333
  262
  272
  242
21112
 2232
  272
  232
   22
   44
    7
    3"""

    nonogram_current = []
    remaining_lives = 0
    pencil = 1

    def init_nonogram():
        global nonogram_current
        global remaining_lives
        global pencil

        remaining_lives = MAX_LIVES
        pencil = 1

        nonogram_current = []
        for i in range(len(NONOGRAM_SOLUTION)):
            nonogram_current.append([])
            for j in range(len(NONOGRAM_SOLUTION[i])):
                nonogram_current[i].append(None)

    def set_cell_value(i, j, value):
        nonogram_current[i][j] = value
        check_cell_value(i, j)
        if check_game_over():
            renpy.show_screen("nonogram_game_over")
        elif check_success():
            renpy.show_screen("nonogram_success")

    def check_cell_value(i, j):
        global remaining_lives
        if nonogram_current[i][j] is not NONOGRAM_SOLUTION[i][j]:
            remaining_lives = remaining_lives - 1
            nonogram_current[i][j] = NONOGRAM_SOLUTION[i][j]

    def check_game_over():
        return remaining_lives is 0

    def check_success():
        for i in range(len(nonogram_current)):
            for j in range(len(nonogram_current[i])):
                if nonogram_current[i][j] is not 1 and NONOGRAM_SOLUTION[i][j] is 1:
                    return False
        return True

    def init_all_functions():
        renpy.choice_for_skipping()
        setIsInSpecialScreen(True)
        init_nonogram()



screen nonogram():
    add Solid("102")

    imagebutton:
        idle "gui/arrows/return_white.png"
        hover "gui/arrows/return_hover_blue.png"
        align .03, .1
        action Hide("nonogram")

    fixed:
        xysize 1440, 1000
        align 0.5, 0.5

        text NONOGRAM_SOLUTION_ROWS_ST:
            ypos 175
            size 40
            color "EEE"
            kerning 1
        text NONOGRAM_SOLUTION_COLUMNS_ST:
            vertical True
            xpos 145
            size 40
            color "EEE"
            kerning -20

        grid 23 15:
            pos 145, 175

            for i in range(15):
                for j in range(23):
                    $ tile_value = nonogram_current[i][j]
                    if tile_value is None:
                        imagebutton:
                            idle "images/chapter4/nonogram/tile_empty.png"
                            action Function(set_cell_value, i, j, pencil)
                    else:
                        image "images/chapter4/nonogram/tile_[tile_value].png"

    vbox:
        align 0.99, 0.2

        text _("VIDES"):
            color "EEE"
            xalign 0.5

        for i in range(MAX_LIVES):
            if i < remaining_lives:
                image "images/chapter4/nonogram/heart_full.png":
                    zoom 1.1
                    xalign 0.5
            else:
                image "images/chapter4/nonogram/heart_empty.png":
                    zoom 1.1
                    xalign 0.5

        add Null(height = 250)

        text _("LLAPIS"):
            color "EEE"
            xalign 0.5

        fixed:
            xysize 65, 65
            xalign 0.5
            if pencil == 1:
                add Solid("F70")
            else:
                add Solid("FFF")
            imagebutton:
                idle "images/chapter4/nonogram/tile_1.png"
                align 0.5, 0.5
                action SetVariable("pencil", 1)

        fixed:
            xysize 65, 65
            xalign 0.5
            if pencil == 0:
                add Solid("F70")
            else:
                add Solid("FFF")
            imagebutton:
                idle "images/chapter4/nonogram/tile_0_pencil.png"
                align 0.5, 0.5
                action SetVariable("pencil", 0)

screen nonogram_game_over():
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:
        has vbox:
            align .5, .5
            spacing 20

        text "GAME OVER":
            color "#ffffff"
            size 50
            xalign 0.5

        hbox:
            textbutton "REINTENTAR":
                action [Function(init_nonogram), Hide("nonogram_success"), Hide("nonogram_game_over")]

            add Null(width = 170)

            textbutton "SORTIR":
                action [Hide("nonogram"), Hide("nonogram_success"), Hide("nonogram_game_over")]

            add Null(width = 30)

screen nonogram_success():
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:
        has vbox:
            align .5, .5
            spacing 40

        text "FELICITATS!!!\nHas completat el nonograma!":
            color "#ffffff"
            size 50
            xalign 0.5
            text_align 0.5

        textbutton "SORTIR":
            action [Hide("nonogram"), Hide("nonogram_success"), Hide("nonogram_game_over"), Function(GiveGlossaryItemToPlayer,6), Function(ShowItems)]
            xalign 0.98
