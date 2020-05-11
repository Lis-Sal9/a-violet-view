
## Script for moving car.



label moving_car:
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)

    image bg_car = "images/chapter2/car/bg_car.png"
    image img_car = "images/chapter2/car/img_car.png"

    transform moving_delorean:
        rotate -2
        yalign 0.85 xpos 2500
        linear 10.0 xpos -1800 yalign 0.85

    stop music fadeout 0.5
    scene bg_car
    $ renpy.show_screen("show_return", x=100, y=100, img="return.png", img_hover="return_hover.png")
    play music "audio/sound/car.mp3" fadein 0.5
    show img_car at moving_delorean
    call screen hold_screen(8)
    stop music fadeout 0.5
    $ renpy.hide_screen("show_return")

    $ setIsInSpecialScreen(False)

    return
