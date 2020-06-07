

label curtain_down_inside():
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)

    image bg_img = "images/chapter3/drag_musical/drag_musical_inside.png"
    image img_curtain = "images/chapter3/drag_musical/drag_musical_inside_curtain.png"

    transform curtain_down:
        ypos -800 -0.99 xpos 465
        linear 5.0 xpos 465 yalign 0

    stop music fadeout .5
    scene bg_img
    $ renpy.show_screen("show_return", x=80, y=980, img="return.png", img_hover="return_hover_blue.png")
    show img_curtain at curtain_down
    call screen hold_screen(5)

    $ renpy.hide_screen("show_return")
    $ setIsInSpecialScreen(False)


    return



label curtain_up_inside():
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)

    image bg_img = "images/chapter3/drag_musical/drag_musical_inside.png"
    image img_curtain = "images/chapter3/drag_musical/drag_musical_inside_curtain.png"

    transform curtain_up:
        yalign 0 xpos 465
        linear 5.0 xpos 465 yalign -0.99

    stop music fadeout .5
    scene bg_img
    $ renpy.show_screen("show_return", x=80, y=980, img="return.png", img_hover="return_hover_blue.png")
    show img_curtain at curtain_up
    call screen hold_screen(5)
    hide img_curtain

    $ renpy.hide_screen("show_return")
    $ setIsInSpecialScreen(False)

    return


label curtain_down_night():
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)

    image bg_img_night = "images/chapter3/drag_musical/drag_musical_inside_night.png"
    image img_curtain = "images/chapter3/drag_musical/drag_musical_inside_curtain.png"

    transform curtain_down:
        ypos -800 -0.99 xpos 465
        linear 5.0 xpos 465 yalign 0

    stop music fadeout .5
    scene bg_img_night
    $ renpy.show_screen("show_return", x=80, y=980, img="return.png", img_hover="return_hover_blue.png")
    show img_curtain at curtain_down
    call screen hold_screen(5)

    $ renpy.hide_screen("show_return")
    $ setIsInSpecialScreen(False)


    return


label curtain_up_night():
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)

    image bg_img_night = "images/chapter3/drag_musical/drag_musical_inside_night.png"
    image img_curtain = "images/chapter3/drag_musical/drag_musical_inside_curtain.png"

    transform curtain_up:
        yalign 0 xpos 465
        linear 5.0 xpos 465 yalign -0.99

    stop music fadeout .5
    scene bg_img_night
    $ renpy.show_screen("show_return", x=80, y=980, img="return.png", img_hover="return_hover_blue.png")
    show img_curtain at curtain_up
    call screen hold_screen(5)
    hide img_curtain

    $ renpy.hide_screen("show_return")
    $ setIsInSpecialScreen(False)

    return
