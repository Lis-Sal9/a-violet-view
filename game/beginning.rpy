
## Script for the beginning scene.
## Once upon a time ...


label beginning:

    $ title = Text(_("Once upon a time ..."), size=100, color="#ffffff")

    scene black
    show text title at truecenter
    with fade
    call screen hold_screen(3)
    hide text
    with dissolve
