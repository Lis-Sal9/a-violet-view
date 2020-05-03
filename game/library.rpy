

## Script for the library scene.
## The library is the main menu of the game. It is the main scene for the player.



screen library():
    $ renpy.choice_for_skipping()
    key "K_ESCAPE" action MainMenu()

    imagemap:
        idle "images/library/library.png"
        ground "images/library/library.png"
        hotspot (1065, 414, 32, 80):
            clicked Jump("chapter_0")
            hovered ShowTransient("hover_library", img="images/library/library_chapter0.png")
            unhovered Hide("hover_library")

        if game_state.chapter > 0:
            hotspot (506, 749, 40, 101):
                clicked Jump("chapter_1")
                hovered ShowTransient("hover_library", img="images/library/library_chapter1.png")
                unhovered Hide("hover_library")

        if game_state.chapter > 1:
            hotspot (1180, 168, 29, 72):
                clicked Jump("chapter_2")
                hovered ShowTransient("hover_library", img="images/library/library_chapter2.png")
                unhovered Hide("hover_library")


screen hover_library(img):
    add img at truecenter
