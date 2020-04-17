
## This is the script for play a maze.
##
## In this scene, the player has to collect some objects.


init python:
    viewport_x = 19
    viewport_y = 11


screen maze():

    $ badge = Image("images/chapter1/maze/badge.png")
    $ map = Image("images/chapter1/maze/map.png")

    add Solid("000")

    fixed:
        xpos (coordinates[0] * -48) + 936
        ypos (coordinates[1] * -48) + 516
        add map

        python:
            min_x = max(0, coordinates[0] - viewport_x)
            min_y = max(0, coordinates[1] - viewport_y)
            max_x = min(len(maze_matrix[min_y]), coordinates[0] + viewport_x + 1)
            max_y = min(len(maze_matrix), coordinates[1] + viewport_y)

        for y in range(min_y, max_y):
            if y is coordinates[1]:
                for x in range(min_x, max_x):
                    if maze_matrix[y][x]:
                        button:
                            action Function(moveBadge, [x, y])
                            xsize 48
                            ysize 48
                            xpos x * 48
                            ypos y * 48
            elif maze_matrix[y][coordinates[0]]:
                button:
                    action Function(moveBadge, [coordinates[0], y])
                    xsize 48
                    ysize 48
                    xpos coordinates[0] * 48
                    ypos y * 48

    add badge:
        align 0.5, 0.5

    fixed:
        xysize 400, 200
        pos 20, 20

        image "images/chapter1/maze/maze_objects/objects_panel.png"

        if "key" not in game_state.maze_objects:
            image "images/chapter1/maze/maze_objects/key_disabled.png":
                pos 70, 45
        else:
            imagebutton:
                idle "images/chapter1/maze/maze_objects/key_enabled.png"
                action Jump("maze_key")
                pos 70, 45

        if "diary" not in game_state.maze_objects:
            image "images/chapter1/maze/maze_objects/diary_disabled.png":
                pos 140, 45
        else:
            imagebutton:
                idle "images/chapter1/maze/maze_objects/diary_enabled.png"
                action Jump("maze_diary")
                pos 140, 45

        if "hatchet" not in game_state.maze_objects:
            image "images/chapter1/maze/maze_objects/hatchet_disabled.png":
                pos 210, 45
        else:
            imagebutton:
                idle "images/chapter1/maze/maze_objects/hatchet_enabled.png"
                action Jump("maze_hatchet")
                pos 210, 45

        if "paper" not in game_state.maze_objects:
            image "images/chapter1/maze/maze_objects/paper_disabled.png":
                pos 280, 45
        else:
            imagebutton:
                idle "images/chapter1/maze/maze_objects/paper_enabled.png"
                action Show("maze_paper")
                pos 280, 45

        if "nightstick" not in game_state.maze_objects:
            image "images/chapter1/maze/maze_objects/nightstick_disabled.png":
                pos 105, 100
        else:
            imagebutton:
                idle "images/chapter1/maze/maze_objects/nightstick_enabled.png"
                action Jump("maze_nightstick")
                pos 105, 100

        if "scarf" not in game_state.maze_objects:
            image "images/chapter1/maze/maze_objects/scarf_disabled.png":
                pos 175, 100
        else:
            imagebutton:
                idle "images/chapter1/maze/maze_objects/scarf_enabled.png"
                action Jump("maze_scarf")
                pos 175, 100

        if "survival_kit" not in game_state.maze_objects:
            image "images/chapter1/maze/maze_objects/survival_kit_disabled.png":
                pos 245, 100
        else:
            imagebutton:
                idle "images/chapter1/maze/maze_objects/survival_kit_enabled.png"
                action Jump("maze_survival_kit")
                pos 245, 100
