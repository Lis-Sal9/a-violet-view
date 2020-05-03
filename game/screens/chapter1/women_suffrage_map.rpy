
## This is script for the quiz of women's suffrage.


init -10 python:
    is_in_suffrage_map = False
    def isInSuffrageMapSection(result):
        global is_in_suffrage_map
        is_in_suffrage_map = result


label suffrage_map:
    $ renpy.choice_for_skipping()

    if game_state.maze_is_seen:
        $ GiveGlossaryItemToPlayer(17)
        $ GiveGlossaryItemToPlayer(6)
        if len(game_state.maze_objects) == 7:
            $ GiveGlossaryItemToPlayer(23)
        $ ShowItems()

    $ isInSuffrageMapSection(True)
    call screen women_suffrage_map(num = 0)
    return


init python:
    import random

    OPTIONS = ["Abans de 1914", "1914 - 1920", "1921 - 1940", "1941 - 1955", "1956 - 1970", "Després de 1970", "Sense sufragi"]
    COLORS = ["#e5ffde", "#bbcbcb", "#9590a8", "#634b66", "#3e2739", "#18020c", "#ffffff"]
    stage = 0
    num_selected_correct_options = 0


    def getRandomNumbers():
        random_options = []
        random_options.append(stage)
        i = 0
        while i < 3:
            num = random.randrange(7)
            if num not in random_options:
                random_options.append(num)
                i = i + 1
        random.shuffle(random_options)
        return random_options

    def checkCorrectOption(option):
        global num_selected_correct_options
        global stage
        if option == OPTIONS[stage]:
            num_selected_correct_options = num_selected_correct_options + 1
        stage = stage + 1

    def showCorrectStars():
        global game_state
        game_state.suffrage_map_done = True
        if num_selected_correct_options > 2 and num_selected_correct_options < 6:
            # achieve one item
            GiveGalleryItemToPlayer(0)
        elif num_selected_correct_options == 6 or num_selected_correct_options == 7:
            # achieve two items
            GiveGalleryItemToPlayer(0)
            GiveGalleryItemToPlayer(2)
        isInSuffrageMapSection(False)


screen women_suffrage_map(num):
    add "images/chapter1/suffrage_map/suffrage_map_bg.png"
    add "images/chapter1/suffrage_map/suffrage_map_[num].png"

    text _("Sufragi femení"):
        size 50
        bold True
        color "#ffffff"
        align .97, 0
        yoffset 20

    fixed:
        xysize 250, 250
        anchor 0.5, 0.5
        pos 1750, 300

        add Solid("0004")

        vbox:
            text _("Esculli l'interval :"):
                bold True
                color "#ffffff"
                size 20
                align 0.5, 0.5
                yoffset 20

            $ random_options = getRandomNumbers()
            for i in range(0, 4):
                fixed:
                    yoffset 40
                    ysize 40

                    text _(OPTIONS[random_options[i]]):
                        color "#ffffff"
                        size 17
                        align 0.5, 0.5

                    imagebutton:
                        idle Solid("0000")
                        hover "images/chapter1/suffrage_map/map_item_hover.png"
                        align 0.5, 0.5
                        xysize 230, 40
                        action [Hide("women_suffrage_map"), Function(checkCorrectOption, OPTIONS[random_options[i]]), If(num == 6, true=Show("correct_suffrage_map"), false=Show("women_suffrage_map", num=num + 1))]



screen correct_suffrage_map():
    add "images/chapter1/suffrage_map/suffrage_map_correct.png"

    text _("Sufragi femení"):
        size 50
        bold True
        color "#ffffff"
        align .97, 0
        yoffset 20

    imagebutton:
        idle "gui/arrows/arrow_right.png"
        hover "gui/arrows/arrow_right_hover.png"
        xpos 1800
        yalign .9
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
    python:
        isInSuffrageMapSection(False)

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
