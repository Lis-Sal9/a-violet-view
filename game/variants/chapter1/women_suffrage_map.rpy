
## This is script for the quiz of women's suffrage.

screen correct_suffrage_map():
    variant "touch"

    add "images/chapter1/suffrage_map/suffrage_map_correct.png"

    text _("Sufragi femení"):
        size 50
        bold True
        color "#ffffff"
        align .97, 0
        yoffset 20

    imagebutton:
        idle Frame("gui/arrows/arrow_right.png")
        hover Frame("gui/arrows/arrow_right_hover.png")
        xpos 1800
        yalign .9
        xysize 110, 60
        action [Function(showCorrectStars), Show("show_map_result")]

    fixed:
        xysize 250, 350
        anchor 0.5, 0.5
        pos 1750, 350

        add Solid("0004")

        vbox:
            xoffset 20
            for i in range(0, 7):
                fixed:
                    yoffset 40
                    ysize 40

                    button:
                        background COLORS[i]
                        xysize 20, 20
                        yoffset 10
                        xoffset 10

                    text _(OPTIONS[i]):
                        color "#ffffff"
                        size 17
                        align 0.5, 0.5



screen show_map_result():
    # python:
    #     isInSuffrageMapSection(False)

    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action Hide("show_map_result")

    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 10

        text _("Resultat"):
            size 40
            xalign 0.5

        hbox:
            align .5, .5
            xysize 200, 50

            for i in range(0, len(OPTIONS)):
                fixed:
                    xysize 100, 100
                    yoffset 15
                    xoffset 15

                    imagebutton:
                        if i < num_selected_correct_options:
                            idle "gui/stars/star_full.png"
                        else:
                            idle "gui/stars/star_empty.png"
                            yoffset -9

                        yalign .1
                        action NullAction()

        $ items_length = str(len(game_state.gallery_items))
        text _("En el mapa del sufragi femení, [tmpSavePlayer] ha obtingut [num_selected_correct_options] estrelles.\nS'han desbloquejat [items_length] ítems a la {b}Galeria{/b}."):
            size 20
            yoffset 10
            xoffset 20

        textbutton _("OK"):
            xalign 0.99
            yoffset 30
            action [Hide("show_map_result"), Hide("correct_suffrage_map"), Return()]
