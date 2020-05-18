
## Script for the series enigma.


init -1 python:
    all_series = []
    FULL_NUMBERS = ["7", "20", "4"]

    def OnChangeNumberUpdate(value = ""):
        global tmpNumber
        if value:
            tmpNumber = str(int(value))

    def checkAllNumbers():
        global game_state
        if len(all_series) == len(FULL_NUMBERS):
            GiveGalleryItemToPlayer(4)
            game_state.series_done = True
            renpy.end_interaction("")

    def addNumber(position):
        global all_series
        global tmpNumber
        full_number = FULL_NUMBERS[position]
        if full_number == tmpNumber:
            all_series.append(position)
        else:
            renpy.notify(_("S'ha equivocat."))
        checkAllNumbers()


label series_label:
    $ GiveGlossaryItemToPlayer(37)
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)
    $ all_series = []
    call screen series_scene
    return


screen series_scene:
    add "images/chapter3/series/series.png"

    imagebutton:
        idle "gui/arrows/return_white.png"
        hover "gui/arrows/return_hover_blue.png"
        align .03, .9
        action Rollback()

    if 0 in all_series:
        text FULL_NUMBERS[0]:
            size 90
            align .18, .48
    else:
        imagebutton:
            idle "images/chapter3/series/question_mark.png"
            hover "images/chapter3/series/question_mark_hover.png"
            align .18, .48
            action Show(screen="set_number", ok_action=Function(addNumber, 0))

    if 1 in all_series:
        text FULL_NUMBERS[1]:
            size 90
            align .56, .92
    else:
        imagebutton:
            idle "images/chapter3/series/question_mark.png"
            hover "images/chapter3/series/question_mark_hover.png"
            align .55, .9
            action Show(screen="set_number", ok_action=Function(addNumber, 1))

    if 2 in all_series:
        text FULL_NUMBERS[2]:
            size 90
            align .87, .51
    else:
        imagebutton:
            idle "images/chapter3/series/question_mark.png"
            hover "images/chapter3/series/question_mark_hover.png"
            align .87, .51
            action Show(screen="set_number", ok_action=Function(addNumber, 2))


screen set_number(ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Hide("set_number"), ok_action]

    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        input default "" length 2 allow "0123456789" changed OnChangeNumberUpdate

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action [Hide("set_number"), ok_action]
            textbutton _("Cancel") action Hide("set_number")




label series_result:
    scene email_susan

    susan_faludi "Molt bé!! Ho has resolt!!"
    susan_faludi "Ara ja puc obrir el fitxer que m'ha adjuntat el meu pare!"
    "Susan va obrir el fitxer."
    "{i}He reflexionat i ja estic farta d'encarnar al mascle agressiu que mai he dut a dins.{/i}"
    user "Susan, Susan, estàs bé??"
    "A Susan li faltava l'aire. Li costava respirar. El seu pare li parlava com a dona?!"
    "Tenia setanta sis anys i havia passat per una transició de gènere?"
    "Aquestes i moltes més són preguntes que es feia."
    susan_faludi "He d'anar a Hongria a veure'l. Sigui com sigui."
    user "Segur? Estàs molt afectada ..."
    susan_faludi "Doncs vine amb mi si tant et preocupa."
    "I així va ser com Susan i [tmpSavePlayer] varen trobar-se l'endemà per emprendre camí cap a Hongria."

    call train
    call end_chapter(CHAPTERS[5])

    return
