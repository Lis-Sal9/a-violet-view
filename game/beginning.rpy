
## Script for the beginning scene.
## Once upon a time ...


label beginning:

    $ title = Text(_("Once upon a time ..."), size=100, color="#ffffff")

    scene black
    show text title at truecenter
    with fade
    play music "audio/music/chapter0.mp3" fadein 0.5
    pause 3
    hide text
    with dissolve
