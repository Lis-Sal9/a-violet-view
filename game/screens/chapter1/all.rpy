## Script for the chapter 1.
## This chapter explains the sufragism, mostly.

# Backgrounds
image train_station = "images/chapter1/train_station.png"
image near_train_station = "images/chapter1/near_train_station.png"

# Characters
define liam = Character("Liam", color="#FED876")


label chapter_1:
    $ game_state.chapter = 1

    ## Train station scene ######################
    scene train_station
    play music "audio/sound/train_station.mp3" fadein 0.5

    "El tren acaba d'arribar a l'estació."
    "[tmpSavePlayer] baixa del tren i emprèn camí cap a la sortida."
    "A meitat de camí, sent un nen que crida ..."
    unknown_little_boy "Notícies fresques d'avui !!! Compri'n aquí el diari !!!"

    menu:
        "Vas a recollir el diari":
            "[tmpSavePlayer] decideix apropar-se al nen."
            call train_station_discussion
        "No t'interessen les notícies":
            "[tmpSavePlayer] passa de llarg."

    "[tmpSavePlayer] segueix caminant per l'estació fins a trobar la porta de sortida."
    stop music fadeout 0.5
    "[tmpSavePlayer] surt de l'estació."
    call near_station

    return


## Inside train station scene ######################
label train_station_discussion:
    user "Hola! Com es diu aquest nen tan maco?"
    unknown_little_boy "El meu nom és Liam."
    "Li digué aquell nen amb un dolç somriure."
    user "Hola, Liam. Series tan amable de donar-me un diari, si us plau?"
    liam "I tant que sí! Tingui."
    "Liam li va apropar el diari a [tmpSavePlayer], que va pagar i va girar cua."

    return


## Outside train station scene ######################
label near_station:
    scene near_train_station
    play music "audio/music/chapter1.mp3" fadein 0.5

    pause 60
