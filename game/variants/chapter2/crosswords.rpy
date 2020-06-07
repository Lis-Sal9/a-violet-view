
## Script for the crosswords.
## The player has to fill the crosswords with the list of women names. These names are in The Dinner Party.

screen crosswords():
    variant "touch"
    image "images/chapter2/part_final/crosswords/crosswords.png":
         align 0.5, 0.5
         zoom 1.15

    python:
        y_fix = float(config.screen_height - renpy.get_physical_size()[1])

    fixed:
        imagebutton:
            idle "gui/arrows/return_white.png"
            hover "gui/arrows/return_hover.png"
            align .95, .95
            action Rollback()

        imagebutton:
            idle "images/chapter2/part_final/crosswords/bulb_off.png"
            hover "images/chapter2/part_final/crosswords/bulb_on.png"
            align .95, .05
            action [Function(checkSidebarIsOpen), If(sidebar_is_open, true=Hide("sidebar"), false=Show("sidebar"))]

        for i in range(len(COORD_WORDS)):
            if i in all_crosswords:
                if COORD_WORDS[i][2] == "down":
                    text getRenderedWord(i):
                        anchor 0.5, 0
                        font "fonts/courier_new.ttf"
                        kerning 6.75 + (y_fix / 600)
                        bold True
                        size 23
                        xpos int((COORD_WORDS[i][0] - 124) * 1.15) + 17 - int(y_fix / 200)
                        ypos int((COORD_WORDS[i][1] - 70) * 1.15) - 15 - int(y_fix / 20)
                        vertical True
                else:
                    text getRenderedWord(i):
                        anchor 0, 0.5
                        font "fonts/courier_new.ttf"
                        kerning 18.45
                        bold True
                        size 23
                        xpos int((COORD_WORDS[i][0] - 124) * 1.15) + 10
                        ypos int((COORD_WORDS[i][1] - 70) * 1.15) + 17
                        vertical False

            else:
                imagebutton:
                    idle Frame("images/chapter2/part_final/crosswords/arrow.png")
                    xysize 34, 34
                    xpos int((COORD_WORDS[i][0] - 124) * 1.15)
                    ypos int((COORD_WORDS[i][1] - 70) * 1.15)
                    action Show(screen="set_word", ok_action=Function(showWord, i))
