

# Backgrounds
image portrait_dinner = "images/chapter2/part_final/crosswords/the_dinner_party.png"
image art_studio = "images/chapter2/part_final/art_studio.png"
image street_studio = "images/chapter2/part_final/street.png"


## Final enigma scene ######################
label chapter_2c:
    call new_day
    call moving_car
    call art_studio

    if not game_state.crosswords_done:
        #crossword is not done
        $ renpy.call_in_new_context("crosswords_label")
    else:
        #crossword is done
        "Ja has fet les encreuades de {i}The Dinner Party{/i}. Vols tornar-les a fer?"
        menu:
            "Sí":
                $ renpy.call_in_new_context("crosswords_label")
            "No":
                "D'acord. Continues amb la mateixa història com si les haguessis fet."

    call see_dinner_party

    return



## Art studio scene #######################
label art_studio:
    scene art_studio
    play music "audio/music/chapter2b.mp3" fadein 0.5

    "[tmpSavePlayer] havia arribat a l'estudi d'art de Judy Chicago."
    "Tal com havien quedat, ella tenia una proposta en la qual [tmpSavePlayer] podia donar-li un cop de mà."

    user "Bon dia, Judy! Com va?"
    show judy_chicago_pic at truecenter
    judy_chicago "Bon dia, [tmpSavePlayer]! Ha vingut!"
    user "I tant! Li vaig donar la meva paraula que l'ajudaria després del favor que em va fer."
    judy_chicago "No és per tant. Deixem-nos de punyetes i comencem a treballar."
    hide judy_chicago_pic
    "Judy va ensenyar l'estudi a [tmpSavePlayer] i li va presentar l'obra que volia crear que, segons ella, seria un símbol emblemàtic de l'art feminista."
    "Ja amb tot el material necessari a punt, començaren la creació ..."

    return



## The Dinner Party scene #######################
label see_dinner_party:
    python:
        setIsInSpecialScreen(False)

    scene black
    show portrait_dinner at truecenter
    user "Què bonic ens ha quedat !!!"
    show judy_chicago_pic at right
    judy_chicago "I tant que sí !!! Sense dubte, jo tenia raó. Serà un símbol emblemàtic !!"
    judy_chicago "És una obra que explica la història simbòlica de la dona en la civilització occidental."
    judy_chicago "I que el seu objectiu és finalitzar el cicle d'invisibilitat al qual han estat sotmeses les dones al llarg de la història."
    user "Sí, i sobretot és molt maco que tota l'obra estigui feta al detall, i que cada detall tingui un per què."
    judy_chicago "Sí. La forma de triangle és tradicionalment vinculada a la feminitat, i les tretze dones que hi ha a cada costat del triangle equilàter fa referència a les persones que assistiren a l'últim sopar."
    user "Una comparació molt interessant, tenint en compte que en aquell sopar varen ser tot homes i aquí són tot dones."
    judy_chicago "Efectivament ... ja tinc el nom de l'obra! Es dirà {i}The Dinner Party{/i}!!"
    hide judy_chicago_pic
    "I, amb alegria, recolliren el material usat i s'acomiadaren."

    scene street_studio
    "[tmpSavePlayer] havia de tornar a l'estació. Va decidir fer-ho caminant, ja que volia reflexionar sobre tot el què havia viscut recentment. Molta informació i moltes emocions de cop."

    call train
    call other_day
    call end_chapter(CHAPTERS[4])

    return
