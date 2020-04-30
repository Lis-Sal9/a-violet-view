## Script for the chapter 1.
## This chapter explains the sufragism, mostly.

# Backgrounds
image train_station = "images/train/train_station.png"
image near_train_station = "images/train/near_train_station.png"
image langham = "images/chapter1/langham_place/langham.png"
image langham_inside = "images/chapter1/langham_place/langham_inside.png"
image langham_stairs = "images/chapter1/langham_place/langham_stairs.png"
image langham_library = "images/chapter1/langham_place/langham_library.png"
image patio = "images/chapter1/langham_place/patio.png"
image lna_place = "images/chapter1/lna/lna_place.jpg"
image free_women_place = "images/chapter1/free_women_place.png"
image seneca_falls_act = "images/chapter1/seneca_falls_convention/act.png"
image seneca_falls_full_act = "images/chapter1/seneca_falls_convention/full_act.png"
image seneca_falls_street = "images/chapter1/seneca_falls_convention/sfc_street.png"

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
define emma_goldman = Character("Emma Goldman", color="#FED876")
define sojourner_truth = Character("Sojourner Truth", color="#231F20")
define charlotte_woodward = Character("Charlotte Woodward", color="#FF4F6F")
define elizabeth_cady_stanton = Character("Elizabeth Cady Stanton", color="#F5B2AC")
define lucrecia_mott = Character("Lucrecia Mott", color="#8CBA51")
define susan_b_anthony = Character("Susan B. Anthony", color="#231F20")
define lucy_stone = Character("Lucy Stone", color="#FF4F6F")



label chapter_1:
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
            $ game_state.newspaper_is_read = False
            "[tmpSavePlayer] passa de llarg."

    "Segueix caminant per l'estació fins a trobar la porta de sortida."
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

    "Un carruatge s'atura i [tmpSavePlayer] s'hi munta. Es dirigeix cap al 19 de Langham Place."
    "De camí, va observant els carrers, plens de gom a gom de persones agitades."

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

    $ GiveGlossaryItemToPlayer(12)
    $ ShowItems()

    "[tmpSavePlayer] entra a dins."
    scene langham_inside
    user "Ostres, què gran que és aquest lloc! És preciós!"
    "Mentrestant, [tmpSavePlayer] va fent una ullada a la sala d'estar. És plena de llibres que encurioseixen."
    "Està passejant quan, de sobte ..."

    unknown_girl "Aiiiiiaaaaaaaaaaahhhh ..."
    "[tmpSavePlayer] i aquella dona havien xocat i se li havia caigut la pila de llibres que duïa a terra."

    $ GiveGlossaryItemToPlayer(12)
    $ ShowItems()

    menu:
        "Ajudes a la dona a recollir els llibres":
            user "Disculpi, senyora, em sap molt de greu. No l'he vista."
            unknown_girl "No pateixi, no passa res. Gràcies per ajudar-me a recollir els llibres."
            $ game_state.mill_are_nice = True
        "Et disculpes":
            user "Disculpi, senyora, no l'he vista."
            unknown_girl "Podria almenys ajudar-me a recollir els llibres, no? O és massa demanar?"
            user "Podria, però no ho faré perquè m'ha escridassat. Que l'ajudi la seva parella."
            "I, deixant-la amb la paraula a la boca, [tmpSavePlayer] toca el dos."
            $ game_state.mill_are_nice = False
        "Però miri per on va, senyora !!!":
            "La senyora escridassa a [tmpSavePlayer] mentre l'home que l'acompanya l'ajuda a recollir els llibres."
            user "Què histèrica !!!"
            $ game_state.mill_are_nice = False

    "[tmpSavePlayer] s'aturdeix una mica, però decideix no pensar-hi més i seguir curiosejant Langham."

    menu:
        "Explores la biblioteca":
            call langham_library
            $ game_state.langham_library_is_seen = True
            call patio
        "Interactues amb un personatge de la sala":
            call langham_inside_interaction
            call patio
        "Marxes del saló":
            "[tmpSavePlayer] decideix marxar de la sala perquè considera que ja ho té tot vist."
            scene langham_stairs
            "Al sortir d'aquella sala, es trobà amb unes escales precioses, que conduïen a algun lloc. Volia esbrinar-ho."
            "Així, [tmpSavePlayer] anava pujant les escales i cada vegada més veia un passadís, fosc i molt llarg. Feia una mica de respecte."
            "No obstant això, seguí caminant fins que va arribar a una porta, aparentment tancada."
            "[tmpSavePlayer] va girar el pom per obrir-la i ..."

            scene black

            $ renpy.choice_for_skipping()
            $ renpy.movie_cutscene("video/open_door.mkv")

            if not game_state.maze_is_seen:
                call maze_label
            else:
                #maze is done
                "Ja has fet el laberint anteriorment. Vols tornar-lo a fer?"

                menu:
                    "Sí":
                        $ game_state.maze_coords = [36, 0]
                        call maze_label
                    "No":
                        "D'acord. Continues amb la mateixa història com si l'haguessis fet."
                        call patio

    return


## Langham patio scene ###################################
label patio:
    scene patio
    "[tmpSavePlayer] segueix curiosejant per Langham."

    if game_state.maze_is_seen:
        call free_women
    else:
        call contraception

    call return_to_train_station
    return


## Langham library out scene ###############################
label langham_inside_out:
    "[tmpSavePlayer] es disposa a baixar les escales."

    if game_state.mill_are_nice and game_state.coverture_is_found:
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

        $ GiveGlossaryItemToPlayer(7)
        $ ShowItems()

        "I així, [tmpSavePlayer] s'acomiadà d'aquella parella tan peculiar."

    "[tmpSavePlayer] decidí sortir d'aquella sala."

    $ renpy.hide_screen("langham_library_secret")
    $ renpy.hide_screen("hover_langham_library")

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

    $ GiveGlossaryItemToPlayer(2)
    $ ShowItems()
    $ game_state.campoamor_is_seen = True

    "[tmpSavePlayer] s'acomiadà de la senyora Campoamor i es retirà de la sala."

    return


## Free Women scene ###############################
label free_women:
    scene free_women_place
    "Caminant, arribà a una sala on hi havia persones que treballaven. Semblava una redacció."
    user "Perdoni, aquest lloc és una redacció?"
    "La dona mirà a [tmpSavePlayer] i, amb amabilitat i aprofitant l'ocasió, li va fer una mica de publicitat."
    unknown_girl "Bon dia. El meu nom és Emma Goldman. Aquí ens reunim les persones associades a l'organització de Dones Lliures."

    $ GiveGlossaryItemToPlayer(17)
    $ ShowItems()

    emma_goldman "La coneix?"
    user "La veritat és que no. Me'n podria fer cinc cèntims?"
    emma_goldman "I tant que sí! Nosaltres recolzem a mort el moviment anarcosindicalista, però els nostres companys homes segueixen mantenint aquest sexisme persistent."
    emma_goldman "Per molt que el moviment busqui abolir la dominació i la jerarquia, ells segueixen contribuïnt a marginar-nos-hi."
    emma_goldman "I ja no parlem de les condicions de les dones a la feina, en la cultura i en la vida en general. Però pitjor ho tenen les dones de classe treballadora."
    emma_goldman "D'aquesta manera, hem decidit formar una organització específica per a dones per a poder desenvolupar plenament les nostres condicions i lluita política."
    user "Ostres, per sobre de tot hauria d'estar la persona, les seves capacitats i aptituds, no si té pits i vulva o una salsitxa penjant entre les cames."
    user "M'enfada molt aquesta situació."
    emma_goldman "Si vol, li deixo un tríptic d'informació sobre l'organització, per si decideix afiliar-s'hi en algun moment."
    emma_goldman "I, cortesia de la casa, li faig entrega del nou número que hem publicat recentment les altres dones de la revista i jo. Tingui."
    user "Moltes gràcies, Emma! Molt amable!"

    $ GiveGlossaryItemToPlayer(6)
    $ ShowItems()

    "Abans de marxar, [tmpSavePlayer] va observar detingudament de nou aquell espai. Semblava amagar alguna cosa, però alhora semblava tenir les idees molt clares."

    scene langham
    "Era hora de tornar, així que va esperar-se al carrer a què passés un carruatge."
    "Al cap d'una estona, va aparèixer un carruatge i [tmpSavePlayer] s'hi muntà. Es dirigia a l'estació de tren."


## Return to train station scene ###############################
label return_to_train_station:
    scene near_train_station
    "El carruatge acaba d'arribar a l'estació. [tmpSavePlayer] baixa i paga."
    user "Gràcies, senyor!"
    "El senyor del carruatge mou el cap assentint i [tmpSavePlayer] entra a l'estació."

    stop music fadeout 0.5
    play music "audio/sound/train_station.mp3" fadein 0.5

    scene train_station
    "Mentre espera l'arribada del tren, recorda que té un llibre una mica peculiar. L'obre i veu que hi ha un test. Decideix fer-lo."

    if not game_state.suffrage_map_done:
        #suffrage map is not done
        call suffrage_map
    else:
        #suffrage map is done
        "Ja has fet el mapa del sufragi femení anteriorment. Vols tornar-lo a fer?"

        menu:
            "Sí":
                call suffrage_map
            "No":
                "D'acord. Continues amb la mateixa història com si l'haguessis fet."

    scene train_station
    "Acabat el test, el tren ja era a l'andana. Marxaria en breu."
    call train
    return
