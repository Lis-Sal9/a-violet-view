
## Script for moving car.



label moving_car:
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)

    image bg_car = "images/chapter2/car/bg_car.png"
    image img_car = "images/chapter2/car/img_car.png"

    transform moving_delorean:
        rotate -2
        yalign 0.85 xpos 2200
        linear 10.0 xpos -2500 yalign 0.85

    stop music fadeout 0.5
    scene bg_car
    play music "audio/sound/car.mp3" fadein 0.5
    show img_car at moving_delorean
    call screen hold_screen(7)
    stop music fadeout 0.5

    $ setIsInSpecialScreen(False)

    return
