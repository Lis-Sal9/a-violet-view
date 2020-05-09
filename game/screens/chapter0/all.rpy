## Script for the chapter 0.
## This chapter is a prologue of this game. It allows to know the gameplay and its style to the player.


# Backgrounds
image room = "images/chapter0/room.png"
image street_home = "images/chapter0/street/street_home.png"
image street_all = "images/chapter0/street/street_all.png"
image editorial = "images/chapter0/editorial/editorial.png"
image nigeria = "images/chapter0/editorial/nigeria.png"
image salon_entrance = "images/chapter0/salon/salon_entrance.png"
image salon_discussion = "images/chapter0/salon/salon_discussion.png"
image salon_portrait = "images/chapter0/salon/salon_portrait.png"

# Characters
define mary_astell = Character("Mary Astell", color="#FED876")
define mary_wollstonecraft = Character("Mary Wollstonecraft", color="#AFCFEA")
define suzanne_voilquin = Character("Suzanne Voilquin", color="#F5B2AC")
define elizabeth_montagu = Character("Elizabeth Montagu", color="#8CBA51")


label chapter_0:
    play music "audio/music/chapter0.mp3" fadein 0.5

    ## Room scene ######################
    scene room
    "Riiiiiinnnngggg ..."
    "Bon dia, [tmpSavePlayer]! És hora de despertar-se!"
    user "Aiiiixxx ... quin dia més maco que fa avui."
    user "Què em posaré?"

    menu:
        "Roba casual":
            user "Ja ho tinc! Roba casual. Em ve de gust sortir a passejar una estona abans d'anar a treballar a l'editorial."
            "[tmpSavePlayer] es vesteix i surt de casa."
            call home
        "Roba elegant":
            user "Ja ho tinc! Roba elegant, que al saló solament van persones ben mudades!"
            "[tmpSavePlayer] es vesteix i surt de casa."
            call salon

    return

    ## Home / street scene ######################
    label home:
        scene street_home
        "De sobte, sent una veu que crida ... "
        unknown "[tmpSavePlayer]!!!!!!"

        menu:
            "Et gires i saludes":
                call mary_wollstonecraft

            "Ignores la veu i segueixes caminant":
                call editorial

        return


    ## Salon / street scene ######################
    label salon:
        scene street_all
        "De camí al saló ... "
        unknown "[tmpSavePlayer]!!! [tmpSavePlayer]!!! Atura't!!"
        unknown "Que em recordes?"

        menu:
            "I tant!":
                $ game_state.astell_is_nice = True
                user "Com podria oblidar una cara tan bonica, Mary!"
                "Aquella dona tan maca era Mary Astell, una amiga de la infància."
                call mary_astell

            "No se m'acosti, persona estranya!":
                $ game_state.astell_is_nice = False
                "[tmpSavePlayer] fuig corrent."
                "No obstant això, una intuïció dins seu li deia que aquella fisonomia li resultava estranyament familiar ..."
                call discussion

        return


    ## Mary Astell scene ######################
    label mary_astell:
        "S'abracen."
        user "Com estàs?"
        mary_astell "Doncs força bé! Ara justament m'has trobat de camí al saló."
        mary_astell "Avui fan un debat literari sobre poesia escrita per dones escandinaves."
        user "No m'ho puc creure! Jo també hi vaig! Quina casualitat!"
        "Però aquella trobada no era tan fortuïta com aparentment semblava ..."

        $ GiveGlossaryItemToPlayer(22)
        $ ShowItems()

        "De camí al saló, varen estar parlant de les seves inquietuds, de les seves vivències en aquest temps separades ... "
        call discussion

        return


    ## Discussion scene ######################
    label discussion:
        scene salon_entrance
        "Davant la porta del saló es podia llegir un gran cartell que posava:"
        "'{i}Bluestockings{/i}, reunió de ments: debat literari amb poetes escandinaves'"
        user "Ostres, quin munt de persones han vingut! Fins i tot, homes!!"

        if game_state.astell_is_nice:
            mary_astell "I tant! Tinc moltes ganes de començar el debat!"

        "Homes i dones havien estat congregades en aquell esdeveniment literari amb la finalitat de poder debatre com a iguals sobre literatura."
        "Novament, el saló d'Elizabeth Montagu tornava a ser un èxit rotund. Un saló artístic de gom a gom, crítiques literàries i escriptores vingudes d'arreu del món ... "

        scene salon_discussion
        elizabeth_montagu "Benvolgudes a un nou capítol dels {i}Bluestockings{/i}."

        $ GiveGlossaryItemToPlayer(11)
        $ ShowItems()

        elizabeth_montagu "Aquesta vegada, reflexionarem plegats sobre les poetes escandinaves més rellevants i sobre les seves idees."
        elizabeth_montagu "En plena {i}Era de la Llibertat{/i}, quan el govern va tenir el poder, es proliferà el debat polític i filosòfic, en el qual s'incloïa la demanda de llibertats per a les dones."
        unknown_boy "Sí, de fet, Sophia Elisabet Brenner va ser una de les primeres dones en reivindicar públicament que homes i dones mereixien els mateixos drets."
        unknown_girl "I no només això, recordem que creia fermament que la dona era intel·lectualment equivalent a l'home."
        unknown_girl "Equivalent en això i en tot, menys en l'aparença física!"

        $ GiveGlossaryItemToPlayer(33)
        $ ShowItems()

        unknown_boy "Teniu raó, però i què me'n diuen de Charlotta Nordenflycht? Forta, rebel i lliure, fins i tot signava els seus escrits amb el seu nom!!"
        unknown_girl "La Charlotta Nordenflycht?"
        "Va preguntar estranyada una noia de la sala ..."
        unknown_girl "Sí, dona, que defensava el dret a ser intel·lectualment activa i refutava la misoginia ..."
        unknown_girl "Doncs no la coneixia, fins ara ... "
        "Va contestar la mateixa noia de la sala ..."

        $ GiveGlossaryItemToPlayer(15)
        $ ShowItems()

        if game_state.astell_is_nice:
            mary_astell "Doncs jo estava especialment captivada per la seva amiga, Catherina Ahlgren, sobretot per aquelles cartes d'{i}Adelaide{/i} dirigides a homes i dones."
            user "És aquella dona de la qual em parlaves sovint quan tornàvem cap a casa després de l'escola?"
            mary_astell "Efectivament, ho és. Si la recordes, segur que també recordes com l'admirava per això."
            user "Com per oblidar-ho! Sempre em parlaves d'ella i encara recordo com se t'il·luminava la cara al fer-ho ..."
            "I, mentre seguien la seva conversa, el debat a sala continuava ..."
            unknown_boy "Doncs jo estava especialment captivat perquè en aquelles cartes parlava no solament de l'amistat, sinó de les consideracions morals i consells dirigits a les filles, i de l'amor veritable."
            unknown_girl "Jajaja. De veritat? El concepte de l'amor veritable? Jo no hi crec pas en això!! És tota una mentida!!!"
            "Va protestar una noia de la sala molt efusivament ..."
            unknown_boy "Considero que abans de protestar, hauries de deixar de ser ignorant."
            "Va replicar el noi. I va seguir amb el seu discurs ..."
            unknown_boy "Ella considerava que l'amor només pot ser veritable si home i dona es tracten com a iguals."
            "I, amb el cap cot, la noia va ser un pas enrere i ja no va tornar a dir res més en tot el transcurs del debat ..."

        else:
            unknown_boy "Doncs jo estava especialment captivat per la seva amiga, Catherina Ahlgren, sobretot per aquelles cartes d'{i}Adelaide{/i} dirigides a homes i dones."
            unknown_boy "Ja no només perquè parlessin de l'amistat, sinó per les consideracions morals i consells dirigits a les filles i, sobretot, perquè creia que l'amor veritable solament és viable quan home i dona es tracten com a iguals."
            unknown_boy "Jo els hi vaig ensenyar a les meves filles i, amb el pas del temps, m'ho han acabat agraïnt."
            unknown_girl "Ben fet, home! Hem de començar a ser fortes, valentes i lliures des de ben petites!!!"
            "Va cridar una noia a ple pulmó ..."

        $ GiveGlossaryItemToPlayer(6)
        $ ShowItems()

        elizabeth_montagu "Calmem-nos tots una mica. Teniu raó en tot allò que s'està debatint en aquesta sala."
        elizabeth_montagu "A més a més del què heu mencionat, jo també afegiria que tractava temes col·lectius com l'activisme social, la democràcia, la igualtat de gènere i la solidaritat entre dones respecte de la dominació masculina."

        "I així transcorregué el debat, cada cop més interessant i efusiu ..."
        "Unes hores més tard, amb el debat ja finalitzat ..."

        if game_state.astell_is_nice:
            mary_astell "Has vist la sala d'arts que hi ha al costat? És impressionant! Vols venir a veure-ho amb mi?"
        else:
            "[tmpSavePlayer] passejava pel saló, quan va trobar una sala d'arts i ..."

        if game_state.astell_is_nice:
            $ GiveGlossaryItemToPlayer(22)

        $ GiveGlossaryItemToPlayer(11)
        $ GiveGlossaryItemToPlayer(33)
        $ GiveGlossaryItemToPlayer(15)
        $ GiveGlossaryItemToPlayer(6)
        $ ShowItems()


        menu:
            "Et quedes al saló investigant":
                scene salon_portrait

                if game_state.astell_is_nice:
                    user "I tant! Em quedo amb tu. Anem a donar una volta per la sala."
                    "I, de sobte ..."
                    user "Ostres! Has vist quin quadre més impactant?"
                    mary_astell "Sí, a mi també em sembla un pèl estrany ..."

                else:
                    "[tmpSavePlayer] passeja per la sala d'arts quan, de sobte, s'atura davant d'un quadre que l'impacta."

                call portrait

            "Decideixes tornar cap a casa. Necessites descansar":
                if game_state.astell_is_nice:
                    user "Ostres, Mary. M'hauràs de disculpar però el dia se m'ha fet massa llarg i voldria tornar a casa a descansar si no et sap greu."
                    mary_astell "Vaja ... d'acord doncs, no seré jo qui t'obligui a quedar-te! M'ha agradat molt compartir avui part del dia amb tu."
                    user "Igualment, Mary. A mi també!"
                    "I, amb un somriure i una forta abraçada, [tmpSavePlayer] s'acomiada i emprèn camí cap a casa seva."

                else:
                    user "Per un moment, havia pensat que aquest quadre tenia alguna cosa especial ... o curiosament estranya. Qui sap."
                    user "Millor que me'n torni a casa, que ja començo a delirar i el cansament em pesa."
                    "I, amb decisió, [tmpSavePlayer] s'acomiada d'algunes companyes de debat i emprèn camí cap a casa seva."

        "Quan era a punt d'arribar a casa seva..."

        call home

        return


    ## Mary Wollstonecraft and Mary Shelley scene ######################
    label mary_wollstonecraft:
        "[tmpSavePlayer] es gira i es troba a Mary Wollstonecraft i a la seva filla, la Mary Shelley."
        "Curiosament, la nena petita sempre anava amb una espècie de nino de drap una mica peculiar."
        user "Hola, Mary's! Com està aquesta nena tan bonica?"
        "La petita Mary fa cara de vergonya i se la tapa amb el seu {i}amic{/i}."
        mary_wollstonecraft "Hola, [tmpSavePlayer]. Com es presenta avui el dia?"
        user "La veritat és que una mica llarg. Tantes coses a fer i em queda tant poc temps per fer-les."
        mary_wollstonecraft "Ostres, és veritat, aquell viatge ..."
        user "Sí ... és demà ..."
        mary_wollstonecraft "Què dius? Ja? Sí que passa el temps ràpid ..."
        user "Vola ..."
        mary_wollstonecraft "Sí. De fet, avui tinc una xerrada a l'escola de la Mary. I es pot fer estranyament pedant."
        user "Per què ho dius?"
        mary_wollstonecraft "Perquè ja em coneixes i jo no tinc pèls a la llengua."
        mary_wollstonecraft "En general, pel que m'he anat trobant, no és ben rebut escoltar que la dona ha d'emancipar-se de l'àmbit domèstic i deixar de ser exclusivament la joguina de l'home."
        mary_wollstonecraft "L'educació ha de ser igual per homes i dones, ja que més enllà dels estereotips de gènere, la realització intel·lectual i personal d'una dona està per sobre."
        mary_wollstonecraft "L'aparença, l'opinió dels homes i el matrimoni han estat massa sobrevalorats, i les dones massa infravalorades."
        mary_wollstonecraft "Les dones han de poder prendre el control de les seves vides."
        user "Ostres, Mary, em deixes sense paraules. Auguro una xerrada i posterior debat força interessants."
        user "Ara me'n he d'anar, però et faig arribar els meus millors desitjos. M'agradaria de tot cor que pogués servir ni que sigui per a què una sola dona trenqui amb els lligams que l'ofeguen."
        "I amb un somriure i una salutació d'adéu, [tmpSavePlayer] va deixant enrere de les seves passes a les dues Mary. Eren una parella peculiar."

        $ game_state.wollstonecraft_is_seen = True
        $ GiveGlossaryItemToPlayer(23)
        $ ShowItems()

        call editorial

        return


    ## Editorial scene ######################
    label editorial:
        scene street_all
        "Durant el camí cap a la feina, a [tmpSavePlayer] li agrada notar el sol a la cara i la brisa com li bufa els cabells."
        user "Avui és l'últim dia abans del meu viatge, s'aventura llarg."
        "I, mentre [tmpSavePlayer] es fon en els seus pensaments, gairebé es passa la seva propera parada."
        "{i}La Tribune des femmes{/i}."

        $ GiveGlossaryItemToPlayer(18)
        $ ShowItems()

        scene editorial
        "[tmpSavePlayer] acabava d'arribar a l'editorial."
        "La senyora Voilquin, com de costum, estava posant ordre. Era meticulosa amb la feina i volia que tot sortís a la perfecció."

        $ GiveGlossaryItemToPlayer(35)
        $ ShowItems()

        suzanne_voilquin "Bon dia, [tmpSavePlayer]. Ara mateix estava dient a les teves companyes que en breu tindrem una reunió plegades sobre el nostre nou projecte."
        user "D'acord, Suzanne. Vaig a fer-me un cafè i ara torno."
        "Una estona més tard ..."
        suzanne_voilquin "Benvolgudes. Us he reunit a totes per parlar-vos del proper projecte que durem a terme a l'editorial."
        suzanne_voilquin "Es tracta d'una investigació sobre l'educació de les dones, concretament de les {i}jajis{/i}."

        if game_state.wollstonecraft_is_seen:
            $ GiveGlossaryItemToPlayer(23)

        $ GiveGlossaryItemToPlayer(18)
        $ GiveGlossaryItemToPlayer(35)
        $ ShowItems()

        menu:
            "Segueixes escoltant perquè et resulta molt interessant":
                call nana_asmau
                "Cap al tard, [tmpSavePlayer] torna cap a casa. El dia ha estat força cansat i ha de carregar piles. L'endemà emprendrà un llarg viatge."
                "El que ningú sabia és que fos tan rellevant per a la seva vida futura allò que estava a punt de viure ... "

            "Desconnectes de la reunió perquè has dormit poc aquesta nit":
                user "Què llarg serà el viatge que m'espera ..."
                "El que ningú sabia és que fos tan rellevant per a la seva vida futura allò que estava a punt de viure ... "

        if game_state.asmau_is_seen:
            $ GiveGlossaryItemToPlayer(26)
            $ ShowItems()

        call train
        call end_chapter(CHAPTERS[0])
        return



    ## Nana Asma'u scene ######################
    label nana_asmau:
        user "Les {i}jajis{/i}? Qui són?"
        suzanne_voilquin "Espera, pas a pas. Primer cal conèixer d'on i quan varen aparèixer i, sobretot, gràcies a qui."
        unknown_girl "Suzanne, no siguis tan misteriosa."
        suzanne_voilquin "Jajaja, ho feia per veure si estaveu atentes. Ja veig que esteu molt interessades en el tema."
        suzanne_voilquin "Genial! Això vol dir que sortirà un projecte molt maco d'aquí!"
        user "No t'enrotllis més i explica-ho!"
        suzanne_voilquin "Està bé, està bé ... "
        "Suzanne va començar a narrar aquella història que semblà captivar a aquell grup de noies encuriosides ..."
        scene nigeria
        suzanne_voilquin "En l'islam, l'educació es considera un deure de totes les persones, ja que el coneixement és considerat part de la humanitat."
        suzanne_voilquin "Amb la tendència patriarcal dels homes en acaparar l'àmbit públic, les dones musulmanes van deixar de tenir accés a una mateixa educació."
        suzanne_voilquin "Però la saviesa i posició rellevant de Nana Asma'u va suposar per l'actual Nigèria un gran canvi."
        suzanne_voilquin "Ella era la filla del califa, però això no va ser allò que la va fer extraordinària."
        suzanne_voilquin "Nana Asma'u creia que l'educació de les nenes havia de ser institucionalitzada."
        suzanne_voilquin "Per aquest motiu, va decidir crear una xarxa de mestres itinerants conegudes com a {i}jajis{/i}, la missió de les quals era instruir a les dones en les seves pròpies cases."
        suzanne_voilquin "Avui dia, el llegat d'aquesta magnífica dona perviu a Nigèria i, a més a més, és un recordatori de l'anterior mandat de l'islam."

        $ game_state.asmau_is_seen = True
        $ GiveGlossaryItemToPlayer(26)
        $ ShowItems()

        scene editorial
        "Totes les noies es varen quedar bocabadades."
        "I Suzanne va continuar ..."
        suzanne_voilquin "Ara, la feina serà vostra d'investigar més a fons per a poder redactar un capítol de la revista sobre aquest tema."
        suzanne_voilquin "Endavant, noies!"
        "I així transcorregué el dia, amb aquell grup de treballadores de l'editorial focalitzades en la seva feina."

        return
