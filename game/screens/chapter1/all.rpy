## Script for the chapter 1.
## This chapter explains the sufragism, mostly.

# Backgrounds
image train_station = "images/train/train_station.png"
image near_train_station = "images/train/near_train_station.png"
image langham = "images/chapter1/langham_place/langham.png"
image langham_inside = "images/chapter1/langham_place/langham_inside.png"

# Characters
define liam = Character("Liam", color="#FED876")
define emily_davison = Character("Emily Davison", color="#F5B2AC")
define mary_richardson = Character("Mary Richardson", color="#8CBA51")
define edith_garrud = Character("Edith Garrud", color="#231F20")
define emmeline_pankhurst = Character("Emmeline Pankhurst", color="#FFFFFF")
define rosa_mary_billinghurst = Character("Rosa Mary Billinghurst", color="#FF4F6F")


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
            $ game_state.newspaper_is_read = True
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

    "[tmpSavePlayer] atura un carruatge i s'hi munta. Es dirigeix cap al 19 de Langham Place."
    "De camí, [tmpSavePlayer] observa els carrers, plens de gom a gom de persones agitades."

    if game_state.newspaper_is_read:
        user "Ostres, ara ho entenc tot ..."
        "Es diu per dins, mentre observa detingudament el diari ..."
        call screen reading_newspaper

    else:
        user "Què deu estar passant? Què boig el món ..."
        "Es diu per dins, mentre segueix observant els carrers que transita ..."

    call langham_place
    return


## Langham Place scene ###############################
label langham_place:
    scene langham
    unknown_boy "És aquí."
    user "Gràcies, senyor."
    "[tmpSavePlayer] paga i baixa del carruatge. És davant del 19 de Langham Place."
    "[tmpSavePlayer] entra a dins."
    scene langham_inside
    user "Ostres, què gran que és aquest lloc! És preciós!"
    "Mentrestant, [tmpSavePlayer] va fent una ullada a la sala d'estar. És plena de llibres que encurioseixen."
    "Està passejant quan, de sobte ..."

    call screen maze
    return
