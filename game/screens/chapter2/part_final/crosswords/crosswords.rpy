
## Script for the crosswords.
## The player has to fill the crosswords with the list of women names. These names are in The Dinner Party.


init -1 python:
    sidebar_is_open = False
    all_crosswords = []

    def checkSidebarIsOpen():
        global sidebar_is_open
        if sidebar_is_open:
            sidebar_is_open = False
        else:
            sidebar_is_open = True

    def showWord(position):
        global all_crosswords
        global tmpWord
        full_word = FULL_WORDS[position].upper()
        rendered_word = RENDERED_WORDS[position].upper()
        tmpWord = tmpWord.upper()
        if full_word == tmpWord or rendered_word == tmpWord:
            all_crosswords.append(position)
        else:
            renpy.notify(_("S'ha equivocat."))
        checkAllWords()

    def getRenderedWord(position):
        word = RENDERED_WORDS[position].upper()
        if position < len(RENDERED_CROSSINGS):
            for i in range(0, len(RENDERED_CROSSINGS[position])):
                tuple = RENDERED_CROSSINGS[position][i]
                if tuple[0] in all_crosswords:
                    word = word[:tuple[1]] + " " + word[tuple[1] + 1:]
        return word

    def OnChangeWordUpdate(value = ""):
        global tmpWord
        tmpWord = value

    def checkAllWords():
        global game_state
        if len(all_crosswords) == len(FULL_WORDS):
            GiveGalleryItemToPlayer(5)
            game_state.crosswords_done = True
            renpy.hide_screen("sidebar")
            renpy.end_interaction("")



label crosswords_label:
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)
    $ all_crosswords = []
    call screen crosswords
    return



screen crosswords():
    add "images/chapter2/part_final/crosswords/crosswords.png"
    python:
        y_fix = float(config.screen_height - renpy.get_physical_size()[1])

    fixed:
        imagebutton:
            idle "gui/arrows/return_white.png"
            hover "gui/arrows/return_hover.png"
            align .90, .9
            action Rollback()

        imagebutton:
            idle "images/chapter2/part_final/crosswords/bulb_off.png"
            hover "images/chapter2/part_final/crosswords/bulb_on.png"
            align .90, .05
            action [Function(checkSidebarIsOpen), If(sidebar_is_open, true=Hide("sidebar"), false=Show("sidebar"))]

        for i in range(len(COORD_WORDS)):
            if i in all_crosswords:
                if COORD_WORDS[i][2] == "down":
                    text getRenderedWord(i):
                        anchor 0.5, 0
                        font "fonts/courier_new.ttf"
                        kerning 3.4 + (y_fix / 600)
                        bold True
                        size 21
                        xpos COORD_WORDS[i][0] + 15 - int(y_fix / 200)
                        ypos COORD_WORDS[i][1] - 17 - int(y_fix / 20)
                        vertical True
                else:
                    text getRenderedWord(i):
                        anchor 0, 0.5
                        font "fonts/courier_new.ttf"
                        kerning 15.1
                        bold True
                        size 21
                        xpos COORD_WORDS[i][0] + 8
                        ypos COORD_WORDS[i][1] + 15
                        vertical False

            else:
                imagebutton:
                    idle "images/chapter2/part_final/crosswords/arrow.png"
                    xpos COORD_WORDS[i][0]
                    ypos COORD_WORDS[i][1]
                    action Show(screen="set_word", ok_action=Function(showWord, i))



screen set_word(ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Hide("set_word"), ok_action]

    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        input default "" length 22 allow "ABCÇDEFGHIJKLMNÑOPQRSTUVWXYZabcçdefghijklmnñopqrstuvwxyz" changed OnChangeWordUpdate

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action [Hide("set_word"), ok_action]
            textbutton _("Cancel") action Hide("set_word")


screen sidebar():
    fixed:
        align 0, 0
        xsize 400
        add Solid("#000000")

        vpgrid:
            cols 1
            xsize 400
            transpose True
            xoffset 10
            yoffset 10
            draggable True
            mousewheel True
            side_yfill True

            for i in range(0, len(FULL_WORDS)):
                $ is_in_list = False
                if i in all_crosswords:
                    $ is_in_list = True

                fixed:
                    xysize 400, 50
                    text FULL_WORDS[i]:
                        color "#ffffff"
                        size 30
                        strikethrough is_in_list
                        kerning 3.4
