

## Script for the library scene.
## The library is the main menu of the game. It is the main scene for the player.



screen library():
    variant "touch"
    $ renpy.choice_for_skipping()
    key "K_ESCAPE" action MainMenu()

    imagemap:
        idle "images/library/library.png"
        ground "images/library/library.png"

        # Prologue
        hotspot (1065, 414, 32, 80):
            clicked Jump("chapter_0")
            hovered ShowTransient("hover_library", img="images/library/library_chapter0.png")
            unhovered Hide("hover_library")

        # Chapter 1
        if CHAPTERS[0] in game_state.chapters_completed:
            hotspot (506, 749, 40, 101):
                clicked Jump("chapter_1")
                hovered ShowTransient("hover_library", img="images/library/library_chapter1.png")
                unhovered Hide("hover_library")

        # Chapter 2
        if CHAPTERS[1] in game_state.chapters_completed:
            # Part 1
            hotspot (1180, 168, 29, 72):
                clicked Jump("chapter_2a")
                hovered ShowTransient("hover_library", img="images/library/library_chapter2a.png")
                unhovered Hide("hover_library")
            # Part 2
            hotspot (1143, 651, 20, 69):
                clicked Jump("chapter_2b")
                hovered ShowTransient("hover_library", img="images/library/library_chapter2b.png")
                unhovered Hide("hover_library")

        if CHAPTERS[2] in game_state.chapters_completed and CHAPTERS[3] in game_state.chapters_completed:
            # Part Final
            hotspot (488, 225, 126, 25):
                clicked Jump("chapter_2c")
                hovered ShowTransient("hover_library", img="images/library/library_chapter2c.png")
                unhovered Hide("hover_library")

        # Chapter 3
        if CHAPTERS[4] in game_state.chapters_completed:
            hotspot (667, 633, 21, 92):
                clicked Jump("chapter_3")
                hovered ShowTransient("hover_library", img="images/library/library_chapter3.png")
                unhovered Hide("hover_library")

        # Chapter 4
        if CHAPTERS[5] in game_state.chapters_completed:
            hotspot (840, 418, 25, 83):
                clicked Jump("chapter_4")
                hovered ShowTransient("hover_library", img="images/library/library_chapter4.png")
                unhovered Hide("hover_library")

    ## Quick menu ########################################
    hbox:
        style_prefix "quick"
        xalign 0.5
        yalign 1.0
        spacing 5

        imagebutton:
            action Show('pause')
            xysize mobile_icon_size, mobile_icon_size
            idle Frame("gui/icons/pause.png")
            hover Frame("gui/icons/pause_border.png")

        imagebutton:
            action ShowMenu('glossary')
            xysize mobile_icon_size, mobile_icon_size
            hover Frame("gui/icons/glossary_new_icon.png")
            if len(game_state.glossary_items_unread) > 0:
                idle Frame("gui/icons/glossary_new_icon.png")
            else:
                idle Frame("gui/icons/glossary_icon.png")

        imagebutton:
            action ShowMenu('gallery')
            xysize mobile_icon_size, mobile_icon_size
            hover Frame("gui/icons/gallery_new_icon.png")
            if len(game_state.gallery_items_unread) > 0:
                idle Frame("gui/icons/gallery_new_icon.png")
            else:
                idle Frame("gui/icons/gallery_icon.png")

        imagebutton:
            if is_in_special_screen:
                action NullAction()
                hover Frame("gui/icons/save.png")
            else:
                action [Show(screen="save_menu"), FileTakeScreenshot()]
                hover Frame("gui/icons/save_border.png")
                xysize mobile_icon_size, mobile_icon_size
            idle Frame("gui/icons/save.png")

    ######################################################


screen hover_library(img):
    variant "touch"
    add img at truecenter

    ## Quick menu ########################################
    hbox:
        style_prefix "quick"
        xalign 0.5
        yalign 1.0
        spacing 5

        imagebutton:
            action Show('pause')
            xysize mobile_icon_size, mobile_icon_size
            idle Frame("gui/icons/pause.png")
            hover Frame("gui/icons/pause_border.png")

        imagebutton:
            action ShowMenu('glossary')
            xysize mobile_icon_size, mobile_icon_size
            hover Frame("gui/icons/glossary_new_icon.png")
            if len(game_state.glossary_items_unread) > 0:
                idle Frame("gui/icons/glossary_new_icon.png")
            else:
                idle Frame("gui/icons/glossary_icon.png")

        imagebutton:
            action ShowMenu('gallery')
            xysize mobile_icon_size, mobile_icon_size
            hover Frame("gui/icons/gallery_new_icon.png")
            if len(game_state.gallery_items_unread) > 0:
                idle Frame("gui/icons/gallery_new_icon.png")
            else:
                idle Frame("gui/icons/gallery_icon.png")

        imagebutton:
            if is_in_special_screen:
                action NullAction()
                hover Frame("gui/icons/save.png")
            else:
                action [Show(screen="save_menu"), FileTakeScreenshot()]
                hover Frame("gui/icons/save_border.png")
                xysize mobile_icon_size, mobile_icon_size
            idle Frame("gui/icons/save.png")

    ######################################################
