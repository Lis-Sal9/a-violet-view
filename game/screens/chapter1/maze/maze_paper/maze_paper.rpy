
## This script defines the paper (objects panel) on maze.



screen maze_paper():
    add Solid("000")

    frame:
        xalign .5 yalign .5
        $ objects_panel = Image("images/chapter1/maze/maze_objects/objects_panel.png")


        imagebutton:
            idle "gui/arrows/arrow_right.png"
            hover "gui/arrows/arrow_right_hover.png"
            xpos 1800
            yalign .1
            yoffset -45
            action Return()
