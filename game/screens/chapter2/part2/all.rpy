
## Script for the chapter 2 Part 2.
## This chapter explains the feminism between 1945-1990.

# Backgrounds
image train_station_chpt2b = "images/train/train_station_chpt2b.png"
image near_train_station_chpt2b = "images/train/near_train_station_chpt2b.png"
image car = "images/chapter2/part2/car.png"
image nyrw_outside = "images/chapter2/part2/nyrw/nyrw_outside.png"
image nyrw_inside = "images/chapter2/part2/nyrw/nyrw_inside.png"
image cr_adriennerich = "images/chapter2/part2/nyrw/cr_adriennerich.png"
image cr_einstein = "images/chapter2/part2/nyrw/cr_einstein.png"
image cr_session = "images/chapter2/part2/nyrw/cr_session.png"


# Characters
define judy_chicago = Character("Judy Chicago", color="#e53935")
define adrienne_rich = Character("Adrienne Rich", color="#d81b60")
define participant = Character(_("Participant"), color="#8e24aa")




label chapter_2b:
    ## Train station scene ######################
    scene train_station_chpt2b
    play music "audio/sound/train_station.mp3" fadein 0.5

    "El tren acaba d'arribar a l'estació."
    "[tmpSavePlayer] baixa del tren i es dirigeix a l'aparcament de l'estació. Hi té el cotxe."

    stop music fadeout 0.5
    scene near_train_station_chpt2b
    play music "audio/music/chapter2a.mp3" fadein 0.5

    "Malgrat el cansament del viatge, té sessió amb el grup d'autoconsciència i no pot arribar tard."
    "Així que engega el cotxe i es dirigeix a la seva destinació."

    call moving_car
    stop music fadeout 0.5
    play music "audio/music/chapter2a.mp3" fadein 0.5
    call nyrw_building

    return



label nyrw_building:
    scene nyrw_outside
    "Ja ha arribat a l'edifici de NYRW. Aparca i entra."

    scene nyrw_inside
    user "Bon dia, em dic [tmpSavePlayer]. M'han convidat al grup d'autoconsciència que es realitza en breu."
    unknown_girl "Deixi'm comprovar-ho un moment."
    "La dona del mostrador d'informació estava comprovant si [tmpSavePlayer] tenia accés o no."
    unknown_girl "M'haurà de disculpar, però en la llista de persones alienes que tenen permís per accedir a l'edifici no figura cap persona amb el nom [tmpSavePlayer]."
    "[tmpSavePlayer] començà a notar com els nervis envaïen el seu cos. I ara què faria?"
    unknown_girl "Kathie, deixi passar a aquesta persona. Ve al grup que porta l'Adrienne."
    "[tmpSavePlayer] mirà a aquella dona que s'apropà. Tenia una cara familiar, però no aconseguia esbrinar d'on la coneixia."
    unknown_girl "Perdoni, [tmpSavePlayer]. Disculpi les molèsties. Acompanyi a la senyora Chicago."
    "Així, Judy Chicago i [tmpSavePlayer] marxaren cap a la sala."
    judy_chicago "Em dic Judy. Vostè és [tmpSavePlayer]. M'equivoco?"
    user "No. Un plaer. Gràcies pel cop de mà."
    user "Sap què? Em resulta familiar la seva cara però ara no sé d'on ..."
    judy_chicago "Doncs no tinc ni idea. La veritat és que ara que ho menciona, a mi també em passa el mateix."
    user "Ostres ..."
    judy_chicago "Sigui com sigui, ara ja ens coneixem. Miri, tinc una proposta per fer-li, si li ve de gust."
    user "I tant. Endavant."
    judy_chicago "Farà un temps, vaig estar en la conferència de NOW, repartint obsequis. En breu, faré una exposició d'art allà mateix."
    judy_chicago "A part de donar-li una invitació per si hi vol assistir, voldria oferir-li que m'ajudés amb la meva obra estrella."
    judy_chicago "La veritat és que la porto bastant endarrerida i no em vindria pas malament un parell de mans més."
    "[tmpSavePlayer] es quedà rumiant ... "
    judy_chicago "[tmpSavePlayer], s'ha quedat pensant en les musaranyes ..."
    user "Perdoni, Judy, sí, serà un plaer ajudar-la. Serà la meva manera de tornar-li el petit favor que m'ha fet."
    "[tmpSavePlayer] posà cara de vergonya, però assentí amb el cap."
    judy_chicago "Moltes gràcies. Ai, miri, és aquí el grup."
    "Acabaven d'arribar a la sala. S'acomiadà de la senyora Chicago amb complicitat i, mentre ella s'allunyava, [tmpSavePlayer] trucà a la porta i entrà."

    call cr_session

    return
