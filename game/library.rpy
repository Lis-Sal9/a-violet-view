

## Script for the library scene.
## The library is the main menu of the game. It is the main scene for the player.



screen library():
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
            hotspot (488, 217, 103, 10):
                clicked Jump("chapter_2c")
                hovered ShowTransient("hover_library", img="images/library/library_chapter2c.png")
                unhovered Hide("hover_library")


screen hover_library(img):
    add img at truecenter
