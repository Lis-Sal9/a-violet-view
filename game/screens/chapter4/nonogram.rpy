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

    def check_cell_value(i, j):
        global remaining_lives
        if nonogram_current[i][j] is not NONOGRAM_SOLUTION[i][j]:
            remaining_lives = remaining_lives - 1
            set_cell_value(i, j, NONOGRAM_SOLUTION[i][j])

label nonogram_label:
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)
    $ init_nonogram()
    call screen nonogram
    return

screen nonogram():
    add Solid("102")

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

        text _("LLÀPIS"):
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
