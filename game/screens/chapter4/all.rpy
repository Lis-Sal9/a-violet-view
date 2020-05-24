
## Script for the chapter 4.
## This chapter explains the feminism between 2010 and nowadays.


label chapter_4:
    play music "audio/music/chapter4.mp3" fadein 0.5
    call desktop_label
    return


init -1 python:
    def getCredits():
        if _preferences.language == "english":
            return "images/chapter4/title_credits/title_credits_en.png"
        elif _preferences.language == "spanish":
            return "images/chapter4/title_credits/title_credits_es.png"
        elif _preferences.language == "catalan":
            return "images/chapter4/title_credits/title_credits_ca.png"


label credits:
    image title_credits = getCredits()

    stop music fadeout .5
    scene black

    transform falling:
        xalign 0.05 ypos 1200
        linear 45.0 ypos -5000 xalign 0.85

    show title_credits at falling
    call screen hold_screen(45)

    $ renpy.movie_cutscene("video/credits.avi")

    $ title = Text(_("CONTINUARÀ ..."), size=100, color="#ffffff")

    stop music fadeout .5
    scene black
    show text title at truecenter
    with fade
    call screen hold_screen(3)
    hide text
    with dissolve

    return
