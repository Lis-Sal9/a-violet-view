## Script for the chapter 1.
## This chapter explains the sufragism, mostly.

# Backgrounds
image train_station = "images/train/train_station.png"
image near_train_station = "images/train/near_train_station.png"
image langham = "images/chapter1/langham_place/langham.png"
image langham_inside = "images/chapter1/langham_place/langham_inside.png"
image langham_stairs = "images/chapter1/langham_place/langham_stairs.png"
image langham_library = "images/chapter1/langham_place/langham_library.png"

# Characters
define liam = Character("Liam", color="#FED876")
define emily_davison = Character("Emily Davison", color="#F5B2AC")
define mary_richardson = Character("Mary Richardson", color="#8CBA51")
define edith_garrud = Character("Edith Garrud", color="#231F20")
define emmeline_pankhurst = Character("Emmeline Pankhurst", color="#FFFFFF")
define rosa_mary_billinghurst = Character("Rosa Mary Billinghurst", color="#FF4F6F")
define rosa_luxemburg = Character("Rosa Luxemburg", color="#FED876")
define clara_zetkin = Character("Clara Zetkin", color="#F5B2AC")
define john_stuart_mill = Character("John Stuart Mill", color="#231F20")
define harriet_taylor_mill = Character("Harriet Taylor Mill", color="#FFFFFF")
define clara_campoamor = Character("Clara Campoamor", color="#FF4F6F")


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

    unknown_girl "Aiiiiiaaaaaaaaaaahhhh ..."
    "[tmpSavePlayer] i aquella dona havien xocat i se li havia caigut la pila de llibres que duïa a terra."

    menu:
        "Ajudes a la dona a recollir els llibres":
            user "Disculpi, senyora, em sap molt de greu. No l'he vista."
            unknown_girl "No pateixi, no passa res. Gràcies per ajudar-me a recollir els llibres."
            $ game_state.mill_are_nice = True
            $ is_secret_revealed = False ############ review
        "Et disculpes":
            user "Disculpi, senyora, no l'he vista."
            unknown_girl "Podria almenys ajudar-me a recollir els llibres, no? O és massa demanar?"
            user "Podria, però no ho faré perquè m'ha escridassat. Que l'ajudi la seva parella."
            "I, deixant-la amb la paraula a la boca, [tmpSavePlayer] toca el dos."
            $ is_secret_revealed = False  ############ review
        "Però miri per on va, senyora !!!":
            "La senyora escridassa a [tmpSavePlayer] mentre l'home que l'acompanya l'ajuda a recollir els llibres."
            user "Què histèrica !!!"
            $ is_secret_revealed = False   ############ review

    "[tmpSavePlayer] s'aturdeix una mica, però decideix no pensar-hi més i seguir curiosejant Langham."

    menu:
        "Explores la biblioteca":
            call langham_library
        "Interactues amb alguns personatges de la sala":
            call langham_inside_interaction
        "Marxes del saló":
            "[tmpSavePlayer] decideix marxar de la sala perquè considera que ja ho té tot vist."
            scene langham_stairs
            "Al sortir d'aquella sala, es trobà amb unes escales precioses, que conduïen a algun lloc. Volia esbrinar-ho."
            "Així, [tmpSavePlayer] anava pujant les escales i cada vegada més veia un passadís, fosc i molt llarg. Feia una mica de respecte."
            "No obstant això, seguí caminant fins que va arribar a una porta, aparentment tancada."
            "[tmpSavePlayer] va girar el pom per obrir-la i ..."
            ############ CALL OPEN DOOR
            call screen maze

    "[tmpSavePlayer] segueix curiosejant per Langham."
    "..."

    return


## Langham library out scene ###############################
label langham_inside_out:
    "[tmpSavePlayer] es disposa a baixar les escales."

    if is_secret_revealed: ############ review
        "Quan és al pis de baix, sent una veu coneguda que crida ..."
        unknown_girl "Vingui, vingui !!!"
        user "[tmpSavePlayer] es gira i pregunta si ha de ser la persona interessada."
        "Rep un gest afirmatiu i s'apropa a la dona que crida."
        unknown_girl "Per cert, em dic Harriet Mill. Aquest és el meu marit, en John Stuart Mill."
        john_stuart_mill "Un plaer."
        user "El plaer és meu."
        harriet_taylor_mill "Com a senyal d'agraïment, podria quedar-se a la nostra xerrada que farem en breu. Li ve de gust?"
        user "De què parlaran?"
        harriet_taylor_mill "El meu marit i jo hem escrit plegats un assaig que tracta sobre el matrimoni i el divorci."
        user "Sembla interessant, però ara mateix he de complir una altra missió. Hauran de disculpar-me."
        john_stuart_mill "D'acord, no es preocupi pas. Era un simple oferiment. Sempre pot llegir l'assaig quan ho desitgi."
        "I així, [tmpSavePlayer] s'acomiadà d'aquella parella tan peculiar."

    "[tmpSavePlayer] decidí sortir d'aquella sala."

    return


## Langham library interaction scene ###############################
label langham_inside_interaction:
    user "Bon dia, tingui. Puc acompanyar-la?"
    unknown_girl "Sí, és clar ! El meu nom és Clara Campoamor. Com es diu vostè?"
    user "Jo em dic [tmpSavePlayer]. Què hi fa aquí vostè?"
    clara_campoamor "He vingut a impartir una xerrada sobre l'actuació política que vaig emprendre en la lluita per aconseguir el dret a vot de les dones a Espanya."
    user "Ostres, Clara, em deixa amb la boca oberta. M'encantaria quedar-m'hi, però he de complir una missió."
    clara_campoamor "No pateixi, [tmpSavePlayer]. Podrà tenir al seu abast, si així ho desitja, la meva obra titulada {i}El vot femení i jo: el meu pecat mortal{/i}."
    user "I tant, no ho dubti ! Moltes gràcies per aquesta conversa tan interessant."
    clara_campoamor "A vostè ! A reveure !"
    "[tmpSavePlayer] s'acomiadà de la senyora Campoamor i es retirà de la sala."

    return
