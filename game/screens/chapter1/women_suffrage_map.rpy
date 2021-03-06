
## This is script for the quiz of women's suffrage.


label suffrage_map:
    $ renpy.choice_for_skipping()

    if game_state.maze_is_seen:
        $ GiveGlossaryItemToPlayer(28)
        $ GiveGlossaryItemToPlayer(14)
        if len(game_state.maze_objects) == 7:
            $ GiveGlossaryItemToPlayer(40)
        $ ShowItems()

    $ setIsInSpecialScreen(True)
    $ shuffleStages()
    $ stages_completed = []
    $ num_selected_correct_options = 0
    call screen women_suffrage_map(num = 0)
    return


init python:
    import random

    OPTIONS = ["Abans de 1914", "1914 - 1920", "1921 - 1940", "1941 - 1955", "1956 - 1970", "Després de 1970", "Sense sufragi"]
    COLORS = ["#e5ffde", "#bbcbcb", "#9590a8", "#634b66", "#3e2739", "#18020c", "#ffffff"]
    STAGES = list(range(0, len(OPTIONS)))
    stages_completed = []
    num_selected_correct_options = 0

    def shuffleStages():
        global STAGES
        STAGES = list(range(0, len(OPTIONS)))
        random.shuffle(STAGES)

    def getRandomNumbers(stage):
        random_options = [STAGES[stage]]

        while len(random_options) < 4:
            num = random.randrange(len(OPTIONS))
            if num not in random_options:
                random_options.append(num)

        random.shuffle(random_options)
        return random_options

    def checkCorrectOption(option, stage):
        global num_selected_correct_options
        stages_completed.append(stage)
        if option == stage:
            num_selected_correct_options = num_selected_correct_options + 1

    def showCorrectStars():
        global game_state
        game_state.suffrage_map_done = True
        if num_selected_correct_options > 2:
            # achieve one item
            GiveGalleryItemToPlayer(0)
        if num_selected_correct_options > 5:
            # achieve two items
            GiveGalleryItemToPlayer(2)
        setIsInSpecialScreen(False)


screen women_suffrage_map(num):
    $ current_stage = STAGES[num]
    add "images/chapter1/suffrage_map/suffrage_map_bg.png"
    add "images/chapter1/suffrage_map/suffrage_map_[current_stage].png"

    imagebutton:
        idle "gui/arrows/return_white.png"
        hover "gui/arrows/return_hover_blue.png"
        align .03, .9
        action Rollback()

    text _("Sufragi femení"):
        size 70
        color "#ffffff"
        align .97, 0
        yoffset 5

    fixed:
        xysize 250, 250
        anchor 0.5, 0.5
        pos 1750, 300

        add Solid("0004")

        vbox:
            text _("Esculli l'interval :"):
                color "#ffffff"
                size 30
                align 0.5, 0.5
                yoffset 20

            $ random_options = getRandomNumbers(num)
            for i in range(0, 4):
                $ option = random_options[i]
                $ option_text = OPTIONS[option]
                fixed:
                    yoffset 40
                    ysize 40

                    text _(option_text):
                        color "#ffffff"
                        size 25
                        align 0.5, 0.5

                    imagebutton:
                        idle Solid("0000")
                        hover "images/chapter1/suffrage_map/map_item_hover.png"
                        align 0.5, 0.5
                        xysize 230, 40
                        action [Hide("women_suffrage_map"),
                                Function(checkCorrectOption, option, current_stage),
                                If(num == 6, true = Show("correct_suffrage_map"), false = Show("women_suffrage_map", num = num + 1))]



screen correct_suffrage_map():
    add "images/chapter1/suffrage_map/suffrage_map_correct.png"

    text _("Sufragi femení"):
        size 70
        color "#ffffff"
        align .97, 0
        yoffset 5

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
                        size 25
                        align 0.5, 0.5



screen show_map_result():
    python:
        setIsInSpecialScreen(False)

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
            color "#ffffff"
            size 50
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

        python:
            items_length = 0
            if num_selected_correct_options > 5:
                items_length = 2
            elif num_selected_correct_options > 2:
                items_length = 1

        text _("En el mapa del sufragi femení, [tmpSavePlayer] ha obtingut [num_selected_correct_options] estrelles.\nS'han desbloquejat [items_length] ítems a la {b}Galeria{/b}."):
            size 30
            color "#f0c388"
            yoffset 10
            xoffset 20

        textbutton _("OK"):
            xalign 0.99
            yoffset 30
            action [Hide("show_map_result"), Hide("correct_suffrage_map"), Return()]
