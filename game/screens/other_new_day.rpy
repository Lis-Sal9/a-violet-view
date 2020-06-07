


label new_day:
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)

    image sunrise = "images/day/sunrise.png"
    image sunrise_sun = "images/day/sunrise_sun.png"

    transform moving_sunrise_sun:
        yalign 0.50 xpos 2200
        linear 8.0 xpos 1400 yalign 0.2

    stop music fadeout .5
    scene sunrise
    $ renpy.show_screen("show_return", x=80, y=980, img="return.png", img_hover="return_hover_blue.png")
    show sunrise_sun at moving_sunrise_sun
    call screen hold_screen(10)
    hide sunrise_sun

    $ renpy.hide_screen("show_return")
    $ setIsInSpecialScreen(False)


    return



label other_day:
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)

    image sunset = "images/day/sunset.png"
    image sunset_sun = "images/day/sunset_sun.png"

    transform moving_sunset_sun:
        yalign 0.30 xpos 1400
        linear 8.0 xpos 2200 yalign 0.6

    stop music fadeout .5
    scene sunset
    $ renpy.show_screen("show_return", x=80, y=980, img="return.png", img_hover="return_hover_blue.png")
    show sunset_sun at moving_sunset_sun
    call screen hold_screen(8)
    hide sunset_sun

    $ renpy.hide_screen("show_return")
    $ setIsInSpecialScreen(False)

    return
