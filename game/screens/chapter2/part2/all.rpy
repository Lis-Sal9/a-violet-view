
## Script for the chapter 2 Part 2.
## This chapter explains the feminism between 1945-1990.

# Backgrounds
image train_station_chpt2b = "images/train/train_station_chpt2b.png"
image near_train_station_chpt2b = "images/train/near_train_station_chpt2b.png"
image car = "images/chapter2/part2/car.png"


# Characters




label chapter_2b:
    ## Train station scene ######################
    scene train_station_chpt2b
    play music "audio/sound/train_station.mp3" fadein 0.5

    "El tren acaba d'arribar a l'estació."
    "[tmpSavePlayer] baixa del tren i es dirigeix a l'aparcament de l'estació. Hi té el cotxe."

    stop music fadeout 0.5
    scene near_train_station_chpt2b
    play music "audio/music/chapter2a.mp3" fadein 0.5

    "Malgrat el cansament del viatge, té sessió amb el grup d'autoconsciència de NYRW i no pot arribar tard."
    "Així que engega el cotxe i es dirigeix a la seva destinació."

    call moving_car

    return


label moving_car:
    scene black
    show car
    return
