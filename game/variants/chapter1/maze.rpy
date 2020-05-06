screen maze():
    variant "touch"

    $ mobile_maze_panel_icon_size = [78, 78]
    $ badge = Image("images/chapter1/maze/badge.png")
    $ map = Image("images/chapter1/maze/map.png")
    $ setIsInSpecialScreen(True)

    add Solid("000")

    fixed:
        xpos (game_state.maze_coords[0] * -48) + 936
        ypos (game_state.maze_coords[1] * -48) + 516
        add map

        python:
            min_x = max(0, game_state.maze_coords[0] - viewport_x)
            min_y = max(0, game_state.maze_coords[1] - viewport_y)
            max_x = min(len(maze_matrix[min_y]), game_state.maze_coords[0] + viewport_x + 1)
            max_y = min(len(maze_matrix), game_state.maze_coords[1] + viewport_y)

        for y in range(min_y, max_y):
            if y is game_state.maze_coords[1]:
                for x in range(min_x, max_x):
                    if maze_matrix[y][x]:
                        button:
                            action Function(moveBadge, [x, y])
                            xsize 48
                            ysize 48
                            xpos x * 48
                            ypos y * 48
            elif maze_matrix[y][game_state.maze_coords[0]]:
                button:
                    action Function(moveBadge, [game_state.maze_coords[0], y])
                    xsize 48
                    ysize 48
                    xpos game_state.maze_coords[0] * 48
                    ypos y * 48

    add badge:
        align 0.5, 0.5

    fixed:
        xysize 600, 300
        pos 20, 20

        add Frame("images/chapter1/maze/maze_objects/objects_panel.png", xysize = [600, 300])

        if "key" not in game_state.maze_objects:
            add Frame("images/chapter1/maze/maze_objects/key_disabled.png", xysize = mobile_maze_panel_icon_size, pos = [105, 66])
        else:
            imagebutton:
                idle Frame("images/chapter1/maze/maze_objects/key_enabled.png", xysize = mobile_maze_panel_icon_size)
                action Jump("maze_key")
                xysize mobile_maze_panel_icon_size
                pos 105, 66

        if "diary" not in game_state.maze_objects:
            add Frame("images/chapter1/maze/maze_objects/diary_disabled.png", xysize = mobile_maze_panel_icon_size, pos = [210, 66])
        else:
            imagebutton:
                idle Frame("images/chapter1/maze/maze_objects/diary_enabled.png", xysize = mobile_maze_panel_icon_size)
                action Jump("maze_diary")
                xysize mobile_maze_panel_icon_size
                pos 210, 66

        if "hatchet" not in game_state.maze_objects:
            add Frame("images/chapter1/maze/maze_objects/hatchet_disabled.png", xysize = mobile_maze_panel_icon_size, pos = [315, 66])
        else:
            imagebutton:
                idle Frame("images/chapter1/maze/maze_objects/hatchet_enabled.png", xysize = mobile_maze_panel_icon_size)
                action Jump("maze_hatchet")
                xysize mobile_maze_panel_icon_size
                pos 315, 66

        if "paper" not in game_state.maze_objects:
            add Frame("images/chapter1/maze/maze_objects/paper_disabled.png", xysize = mobile_maze_panel_icon_size, pos = [420, 66])
        else:
            imagebutton:
                idle Frame("images/chapter1/maze/maze_objects/paper_enabled.png", xysize = mobile_maze_panel_icon_size)
                action Jump("maze_paper_label")
                xysize mobile_maze_panel_icon_size
                pos 420, 66

        if "nightstick" not in game_state.maze_objects:
            add Frame("images/chapter1/maze/maze_objects/nightstick_disabled.png", xysize = mobile_maze_panel_icon_size, pos = [156, 150])
        else:
            imagebutton:
                idle Frame("images/chapter1/maze/maze_objects/nightstick_enabled.png", xysize = mobile_maze_panel_icon_size)
                action Jump("maze_nightstick")
                xysize mobile_maze_panel_icon_size
                pos 156, 150

        if "scarf" not in game_state.maze_objects:
            add Frame("images/chapter1/maze/maze_objects/scarf_disabled.png", xysize = mobile_maze_panel_icon_size, pos = [262, 150])
        else:
            imagebutton:
                idle Frame("images/chapter1/maze/maze_objects/scarf_enabled.png", xysize = mobile_maze_panel_icon_size)
                action Jump("maze_scarf")
                xysize mobile_maze_panel_icon_size
                pos 262, 150

        if "survival_kit" not in game_state.maze_objects:
            add Frame("images/chapter1/maze/maze_objects/survival_kit_disabled.png", xysize = mobile_maze_panel_icon_size, pos = [368, 150])
        else:
            imagebutton:
                idle Frame("images/chapter1/maze/maze_objects/survival_kit_enabled.png", xysize = mobile_maze_panel_icon_size)
                action Jump("maze_survival_kit")
                xysize mobile_maze_panel_icon_size
                pos 368, 150
