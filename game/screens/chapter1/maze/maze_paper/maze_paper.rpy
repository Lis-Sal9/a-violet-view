
## This script defines the paper (objects panel) on maze.


label maze_paper_label:
    call screen maze_paper

screen maze_paper():
    $ paper = Image("images/chapter1/maze/paper.png")
    $ all_countries = GetMazeObjectsByLanguage()

    fixed:
        add paper
        align .5, .5

        imagebutton:
            idle "gui/arrows/arrow_right.png"
            hover "gui/arrows/arrow_right_hover.png"
            xpos 1800
            yalign .1
            yoffset -45
            action Rollback()

        vbox:
            align .56, .55

            text _("Sufragisme femení"):
                size 30
                align 1, 1
                xpos 350
                yoffset -30
                bold True

            grid 3 29:
                transpose True
                xspacing 30
                yspacing 7
                for i in range(0, len(all_countries)):
                    $ name = all_countries.get(i)["name"] + ", " + all_countries.get(i)["year"]
                    text name:
                        size 13
                add Null()
                add Null()