
## Script for moving bus.



label moving_bus:
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)

    image bg_bus = "images/chapter3/bus/bus_bg.png"
    image img_bus = "images/chapter3/bus/bus.png"

    transform moving_knight_bus_bg:
        xpos -4250
        linear 10.0 xpos 0

    transform moving_knight_bus:
        xpos 2500
        ypos 1080
        yanchor 1.0
        linear 10.0 xpos -1800

    stop music fadeout 0.5
    scene bg_bus at moving_knight_bus_bg
    $ renpy.show_screen("show_return", x=100, y=100, img="return.png", img_hover="return_hover.png")
    play music "audio/sound/bus.mp3" fadein 0.5
    show img_bus at moving_knight_bus
    call screen hold_screen(8)
    stop music fadeout 0.5
    $ renpy.hide_screen("show_return")

    $ setIsInSpecialScreen(False)

    return
