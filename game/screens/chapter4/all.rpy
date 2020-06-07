
## Script for the chapter 4.
## This chapter explains the feminism between 2010 and nowadays.


label chapter_4:
    play music "audio/music/chapter4.mp3" fadein 0.5
    call desktop_label
    return


label credits:
    image title_credits_ca = "images/chapter4/title_credits/title_credits_ca.png"
    image title_credits_en = "images/chapter4/title_credits/title_credits_en.png"
    image title_credits_es = "images/chapter4/title_credits/title_credits_es.png"

    stop music fadeout .5
    scene black

    transform falling:
        xalign 0.05 ypos 1200
        linear 45.0 ypos -5000 xalign 0.85

    if _preferences.language == "catalan":
        show title_credits_ca at falling
    elif _preferences.language == "english":
        show title_credits_en at falling
    elif _preferences.language == "spanish":
        show title_credits_es at falling

    call screen hold_screen(45)

    $ phrase = Text(_("TOTHOM HAURIA DE SER FEMINISTA"), size=120, color="#ffffff")

    scene black
    show text phrase at truecenter
    with fade
    call screen hold_screen(2)
    hide text
    with dissolve

    $ renpy.movie_cutscene("video/credits.avi")

    $ title = Text(_("CONTINUARÀ ..."), size=120, color="#ffffff")

    stop music fadeout .5
    scene black
    show text title at truecenter
    with fade
    call screen hold_screen(3)
    hide text
    with dissolve

    return
