
## Script for the chapter 2 Part 1.
## This chapter explains the feminism between 1945-1990.

# Backgrounds
image train_station_chpt2a = "images/train/train_station_chpt2a.png"
image near_train_station_chpt2a = "images/train/near_train_station_chpt2a.png"
image taxi = "images/chapter2/part1/taxi.png"
image pizzey_hostel = "images/chapter2/part1/hostel/pizzey_hostel.png"
image pizzey_hostel_room = "images/chapter2/part1/hostel/pizzey_hostel_room.png"
image amazonas_hostel = "images/chapter2/part1/hostel/amazonas_hostel.png"
image amazonas_hostel_room = "images/chapter2/part1/hostel/amazonas_hostel_room.png"
image miss_figure = "images/chapter2/part1/protests/misses/miss_figure.png"
image miss_inside = "images/chapter2/part1/protests/misses/miss_inside.png"
image miss_trash = "images/chapter2/part1/protests/misses/miss_trash.jpg"
image miss_welcome = "images/chapter2/part1/protests/misses/miss_welcome.png"
image now_building = "images/chapter2/part1/now/now_building.png"
image now_conference = "images/chapter2/part1/now/now_conference.png"
image nyrw_dont_cry = "images/chapter2/part1/protests/nyrw/nyrw_dont_cry.png"
image nyrw_protest = "images/chapter2/part1/protests/nyrw/nyrw_protest.jpg"
image nyrw_rally = "images/chapter2/part1/protests/nyrw/nyrw_rally.png"
image gerri_santoro = "images/chapter2/part1/protests/redstockings_witch/gerri_santoro.png"
image witch_dancing = "images/chapter2/part1/protests/redstockings_witch/witch_dancing.jpeg"
image witch_rally = "images/chapter2/part1/protests/redstockings_witch/witch_rally.jpg"

# Characters
define erin_pizzey = Character("Erin Pizzey", color="#00bcd4")
define betty_friedan = Character("Betty Friedan", color="#009688")
define simone_de_beauvoir = Character("Simone de Beauvoir", color="#4caf50")
define kate_millet = Character("Kate Millet", color="#8bc34a")



label chapter_2a:
    ## Train station scene ######################
    scene train_station_chpt2a
    play music "audio/sound/train_station.mp3" fadein 0.5

    "El tren acaba d'arribar a l'estació."
    "[tmpSavePlayer] baixa del tren i es dirigeix a la sortida."
    "El viatge ha estat llarg i decideix anar a descansar a la pensió més propera."

    stop music fadeout 0.5
    scene near_train_station_chpt2a
    play music "audio/music/chapter2a.mp3" fadein 0.5

    "Mentre espera un taxi prop de l'estació, s'atura en el quiosc i s'encurioseix pel titular d'un llibre."
    "{i}Le Rire de la Méduse{/i}, d'Hélène Cixous."
    "Li dóna la volta i llegeix ..."
    "{i}Per sobre del falogocentrisme, existeix la necessitat d'una 'escriptura femenina', ja que aquesta és la clau per al canvi social.{/i}"
    "{i}El cos de les dones és una qüestió molt important en aquesta necessitat i per això és important que ens cuidem nosaltres mateixes i mútuament unes a altres.{/i}"
    "{i}Com estableix el lesbianisme polític, és de vital importància crear vincles amb altres dones i cultivar el potencial bisexual de cadascú ...{/i}"
    "[tmpSavePlayer] no s'ho va pensar més i va comprar aquell llibre. El taxi ja havia arribat."

    scene taxi

    user "Porti'm a la pensió més propera."
    unknown_boy "És la Pensió Amazones. Li està bé?"

    menu:
        "Sí, m'és indiferent":
            unknown_boy "D'acord."
            $ game_state.pizzey_is_seen = False

        "Sí, quin nom més interessant":
            user "El nom de la pensió és força interessant."
            unknown_boy "Vostè creu? No és especialment coneguda aquesta pensió ..."
            "[tmpSavePlayer] s'estranyà pel comentari del taxista, però ràpidament se li marxà del cap quan visualitzà el llibre que s'acabava de comprar."
            $ game_state.pizzey_is_seen = False

        "Uff, no, busqui'n una altra":
            user "No. Ves a saber què em puc trobar allà."
            unknown_boy "Qui sap. La següent és la Pensió Pizzey."
            user "D'acord. Porti'm a aquesta."
            $ game_state.pizzey_is_seen = True

    "De camí a la pensió, [tmpSavePlayer] aprofità per començar a llegir el llibre."
    call hostel

    return



## Inside hostel scene ######################
label hostel:
    "{i}El llenguatge reflecteix les estructures de poder masculines tradicionals, la qual cosa comporta el predomini patriarcal en la literatura i la cultura.{/i}"
    "{i}És per aquest motiu que el postestructuralisme reclama una deconstrucció, ja que no existeix cap veritat única, universal i absoluta.{/i}"
    "{i}D'aquesta manera, s'insta les dones a crear una nova escriptura femenina que condueixi al canvi social.{/i}"
    "{i}La dona ha de ser inclosa en el text per la seva pròpia iniciativa ...{/i}"

    if game_state.pizzey_is_seen:
        scene pizzey_hostel
    else:
        scene amazonas_hostel
        if not game_state.vaginal_orgasm_is_found:
            $ renpy.show_screen("the_myth_of_the_vaginal_orgasm")

    unknown_boy "Hem arribat."
    user "Moltes gràcies."

    "[tmpSavePlayer] baixà del taxi i s'aproximà a la pensió. Tenia un aspecte aparentment estàndard."

    $ renpy.hide_screen("the_myth_of_the_vaginal_orgasm")
    $ renpy.hide_screen("hover_vaginal_orgasm")

    if game_state.pizzey_is_seen:
        "Va entrar i una dona va saludar."
        unknown_girl "Bon dia tingui. En què podria ajudar?"
        user "Bon dia, senyora. El meu nom és [tmpSavePlayer]. Disposa d'una habitació lliure?"
        unknown_girl "Encantada, [tmpSavePlayer]. Jo em dic Erin Pizzey, sóc la propietària d'aquest refugi per a dones maltractades."
        user "Dones maltractes ... ? Ostres, pensava que era una pensió. Disculpi."
        erin_pizzey "No, no, no pateixi. Llavors entenc que no ens coneixia abans ..."
        user "No, em sap greu. He vingut de pas ..."
        erin_pizzey "D'acord, no passa res. Aquest espai és molt gran i es pot quedar aquí per un dia."
        user "Li ho agraeixo de tot cor. Però no faré nosa si aquest és un centre d'ajuda?"
        erin_pizzey "No, no es preocupi per això. Aquí oferim recolzament material i emocional a víctimes de violència domèstica."
        erin_pizzey "Vaig obrir aquest refugi per donar a conèixer aquest problema, abans considerat com un assumpte entre marit i muller, alhora que per ajudar-les."
        erin_pizzey "Però no es quedarà al carrer avui."
        user "Moltíssimes gràcies, Erin. De veritat que li ho agraeixo molt."
        "I així, va pagar un dia d'hostalatge. Ja seguiria amb el seu viatge l'endemà."

        scene pizzey_hostel_room
        if not game_state.eunuch_is_found:
            $ renpy.show_screen("the_female_eunuch")

    else:
        "Va entrar i va pagar un dia d'hostalatge. Ja seguiria amb el seu viatge l'endemà."
        scene amazonas_hostel_room

    "Ja a l'habitació, es relaxà, s'estirà dins del llit i seguí amb la lectura."
    "{i}... Luce Irigay, companya de la professió, ha desenvolupat la 'teoria de la transacció' amb la finalitat de defensar la importància de l'escriptura de les dones com a mitjà per subvertir el domini masculí de la comunicació i la producció literària.{/i}"
    "{i}Exposa que, sota el capitalisme, les dones han estat reduïdes a mercaderies que homes polígams intercanvien i acumulen de manera similar a actius financers.{/i}"
    "{i}I, a més a més, fa èmfasi en què les dones tenen el dret a forjar una subjectivitat feminina ocupant la posició del 'jo'.{/i}"
    "{i}Per tant, s'hauria de reconèixer la diferència sexual i proposa que la societat abandoni la idea de jerarquia sexual on els homes són subjectes i les dones 'allò altre' ...{/i}"
    "[tmpSavePlayer] s'havia adormit amb el llibre obert sobre el pit."

    $ renpy.hide_screen("the_female_eunuch")
    $ renpy.hide_screen("hover_eunuch")

    call morning

    return



## Next morning scene ######################
label morning:
    "..."
    "[tmpSavePlayer] es despertà. Ja era de dia."

    if game_state.pizzey_is_seen:
        scene pizzey_hostel
    else:
        scene amazonas_hostel

    "Es vestí i deixà la pensió. Estava esperant un taxi."
    "..."
    "Al cap d'una estona ..."

    scene taxi
    user "Bon dia, senyor. A NOW, l'Organització Nacional per les Dones."
    unknown_boy "D'acord. Pel camí curt o llarg?"

    if game_state.eunuch_is_found:
        $ GiveGlossaryItemToPlayer(15)
    if game_state.vaginal_orgasm_is_found:
        $ GiveGlossaryItemToPlayer(4)
    $ ShowItems()

    menu:
        "Camí curt":
            user "Millor arribar abans."
            unknown_boy "Com vulgui."
            $ game_state.witch_is_seen = False
            call misses_protest

        "Camí llarg":
            user "Millor si mentrestant puc gaudir del paisatge."
            unknown_boy "Com vulgui."
            $ game_state.witch_is_seen = False
            call nyrw_protest

        "M'és indiferent":
            user "Com vostè prefereixi."
            unknown_boy "D'acord."
            $ game_state.witch_is_seen = True
            call redstockings_witch_protest

    call now_scene
    return
