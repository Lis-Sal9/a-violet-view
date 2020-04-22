
## This is script for the quiz of women's suffrage.


label suffrage_map:
    call screen women_suffrage_map(num = 0)
    return

init python:
    import random

    OPTIONS = ["Abans de 1914", "1914 - 1920", "1921 - 1940", "1941 - 1955", "1956 - 1970", "Després de 1970", "Sense sufragi"]
    COLORS = ["#e5ffde", "#bbcbcb", "#9590a8", "#634b66", "#3e2739", "#18020c", "#ffffff"]
    stage = 0


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
            text _("Escull l'interval :"):
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

                    text _(str(random_options[i])):
                        color "#ffffff"
                        size 17
                        align 0.5, 0.5

                    imagebutton:
                        idle Solid("0000")
                        hover "images/chapter1/suffrage_map/map_item_hover.png"
                        selected_idle "images/chapter1/suffrage_map/map_item_hover.png"
                        selected_hover "images/chapter1/suffrage_map/map_item_hover.png"
                        align 0.5, 0.5
                        xysize 230, 40
                        action [Hide("women_suffrage_map"), If(num == 6, true=Show("correct_suffrage_map"), false=Show("women_suffrage_map", num=num + 1))]



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
        action [Hide("correct_suffrage_map"), Return()]

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
