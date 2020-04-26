
## This script defines the langham library scenes. ##############


label langham_library:
    "[tmpSavePlayer] puja les escales de la sala per anar a la biblioteca del primer pis."
    scene langham_library
    user "A veure què hi ha per aquí ..."
    user "{i}Una habitació pròpia{/i}, de Virginia Woolf ... vaig a llegir la sinopsi ... "

    $ GiveGlossaryItemToPlayer(25)
    $ ShowItems()

    "Mentre [tmpSavePlayer] llegia la sinopsi d'aquella obra, dues dones prop seu estaven alçant la veu en un debat d'opinió."
    unknown_girl "Que no, ja veuràs, anem a preguntar-li a aquesta persona que hi ha aquí."
    unknown_girl "Disculpi, podria venir un moment?"
    "Aquella dona estava cridant a [tmpSavePlayer] per a què s'apropés on éren ..."
    user "I tant. En què les podria ajudar?"
    unknown_girl "Gràcies. Jo em dic Clara Zetkin."
    unknown_girl "Jo sóc la Rosa Luxemburg."
    user "Molt de gust. Jo em dic [tmpSavePlayer]."
    clara_zetkin "Un plaer, [tmpSavePlayer]."
    rosa_luxemburg "Per favor, diga-li a la meva amiga que l'obra {i}Dones i sexe{/i} exposa d'una manera més clarificadora el feminisme des d'un punt de vista marxista."

    $ GiveGlossaryItemToPlayer(19)
    $ ShowItems()

    clara_zetkin "Ja saps que no estic d'acord, Rosa. Per a mi, ho fa millor l'obra {i}Els fonaments socials de la qüestió femenina{/i}. T'ho he dit moltes vegades !"

    $ GiveGlossaryItemToPlayer(0)
    $ ShowItems()

    "[tmpSavePlayer] feia cara d'estranyesa."
    user "M'hauran de disculpar, però no sé de què estan parlant ... no conec cap de les dues obres ..."
    "Aquelles dones van mirar a [tmpSavePlayer] amb cara de sorpresa i ràbia al mateix temps."
    rosa_luxemburg "Ja t'ho deia jo que aquesta persona no valia la pena. Anem ..."
    clara_zetkin "Sí, en això tenies raó ..."

    $ GiveGlossaryItemToPlayer(16)
    $ ShowItems()

    "Aquelles dones van marxar enfurismades amb [tmpSavePlayer], com si fos una aberració no conèixer aquelles obres."
    user "Ostres, quin caràcter que té el personal ..."

    if game_state.mill_are_nice and not game_state.coverture_is_found:
        $ renpy.show_screen("langham_library_secret")

    call langham_inside_out
    return


screen langham_library_secret():
    imagemap:
        idle "images/chapter1/langham_place/langham_library.png"
        ground "images/chapter1/langham_place/langham_library.png"
        hotspot (719, 587, 6, 72):
            clicked [Hide("langham_library_secret"), Hide("hover_langham_library"), Jump("langham_library_book")]
            hovered ShowTransient("hover_langham_library", img="images/chapter1/langham_place/langham_library_hover.png")
            unhovered Hide("hover_langham_library")

screen hover_langham_library(img):
    add img at truecenter

label langham_library_book:
    user "Oh, quin és aquest llibre tan vell?"
    user "Sembla una espècie de llibre legal o de llei ..."
    user "{i}Llei coverture: absorció dels drets de les dones casades{/i}"

    $ GiveGlossaryItemToPlayer(4)
    $ ShowItems()

    user "Al final, una dona soltera acaba tenint més drets que una dona casada. Això és el món al revés."

    $ game_state.coverture_is_found = True
    call langham_inside_out
    return
