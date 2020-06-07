
## This is script for New York Radical Women protest.


label nyrw_protest:
    "..."
    "[tmpSavePlayer] portava una estona de camí gaudint del paisatge quan, de sobte ..."
    show taxist at left
    unknown_boy "Però què és això ?????"
    hide taxist
    "El conductor del taxi havia frenat molt bruscament. Estava enfurismat."
    "[tmpSavePlayer] es va espantar, però de seguida va veure què estava succeïnt."
    "Moltes dones havien pres els carrers per manifestar-se."
    scene black
    show nyrw_protest at truecenter
    show taxist at left
    unknown_boy "Ostres, no sabia que avui hi havia una manifestació convocada. Disculpi."
    hide taxist
    user "No pateixi, no passa res. Esperarem doncs."
    hide nyrw_protest
    show nyrw_rally at truecenter
    "Així, mentre [tmpSavePlayer] veia passar aquella multitud, aprofitava per llegir les pancartes i escoltar els crits des del taxi."
    "No ploris: resisteix !!!!! No estàs sola !!! - cridaven."
    "Les dones radicals són amb tu !! Juntes vetllarem pel nostre benestar !!"
    hide nyrw_rally
    show nyrw_dont_cry at truecenter
    "Enterrem la feminitat tradicional !! La germanor és poderosa !!!"

    $ game_state.nyrw_is_seen = True
    $ GiveGlossaryItemToPlayer(37)
    $ ShowItems()

    "..."
    show taxist at left
    unknown_boy "Sembla que estan emprenent camí cap al carrer paral·lel i podrem moure'ns en breu."
    hide taxist
    user "Perfecte."
    "[tmpSavePlayer] es quedà pensant en la gran quantitat de persones que estaven concentrades en aquella manifestació ..."
    hide nyrw_dont_cry
    scene now_building
    show taxist at left
    unknown_boy "Hem arribat."
    hide taxist
    user "Ja?"
    "Així, [tmpSavePlayer] pagà i baixà del taxi. Havia arribat a la seva destinació."

    return
