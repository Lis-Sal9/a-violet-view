
## This is the script for the Seneca Falls Convention scene ###############################


label seneca_falls_convention:
    scene seneca_falls_act
    "[tmpSavePlayer] acaba d'arribar a la capella metodista. A grans trets, en un cop d'ull va poder comptar unes tres-cents persones."
    user "És espectacular !!!"
    unknown_girl "Oi que sí?"
    "[tmpSavePlayer] es girà. Una dona afroamericana somreia."
    user "Bona tarda, senyora. El meu nom és [tmpSavePlayer]."
    unknown_girl "Encantada de conèixer-te. Jo em dic Sojourner Truth."
    user "Un plaer, Sojourner. Ha vingut a la Convenció?"
    sojourner_truth "I tant ! Jo vull lluitar en aquest activisme polític contra l'esclavitud. Anem a agafar lloc."
    "[tmpSavePlayer] i Sojourner van entrar dins de la capella per buscar un lloc on seure's."
    unknown_girl "Hola, senyores. Podria seure amb vosaltres?"
    user "I tant que sí ! El meu nom és [tmpSavePlayer]. Com es diu aquesta nena tan maca?"
    unknown_girl "Em dic Charlotte Woodward."
    sojourner_truth "Hola, maca. Jo em dic Sojourner Truth."
    charlotte_woodward "Encantada de conèixer-vos. Estic molt emocionada pel dia d'avui."
    sojourner_truth "Sí, jo també ho estic."

    $ GiveGlossaryItemToPlayer(32)
    $ ShowItems()

    "I així, mentre la Convenció no començava, varen estar parlant sobre les seves vides i experiències."
    "Quinze minuts després ..."

    scene seneca_falls_full_act
    elizabeth_cady_stanton "Bona tarda a tothom. Som aquí reunides per debatre sobre els drets de les dones. L'home ha tingut tirania absoluta sobre la dona."
    lucrecia_mott "Som aquí per evidenciar que homes i dones són creats de la mateixa manera i que el Creador els atorga els mateixos drets."
    susan_b_anthony "Som aquí per combatre la manca de drets socials, civils i religiosos de les dones."
    lucy_stone "NWSA i AWSA han unit forces per formar NAWSA. Aquesta organització ha estat creada per advocar a favor del sufragi femení."
    elizabeth_cady_stanton "Feta aquesta petita introducció, procedim a la votació de les resolucions."

    elizabeth_cady_stanton "Primera qüestió. S'ha adjudicat un codi moral diferent per homes i dones."
    elizabeth_cady_stanton "Mitjançant aquest, les delinqüents morals (dones de la societat excloses) no són tolerades i són considerades de poca importància per l'home."
    elizabeth_cady_stanton "Estan d'acord amb què totes les lleis que impedeixen a la dona ocupar el lloc que desitgi en societat o que la posicionin per sota l'home, no tenen autoritat suficient perquè són contràries a la pròpia naturalesa?"

    $ renpy.choice_for_skipping()
    $ GiveGlossaryItemToPlayer(32)
    $ GiveGlossaryItemToPlayer(19)
    if game_state.contraception_is_found:
        $ GiveGlossaryItemToPlayer(21)
    if game_state.campoamor_is_seen:
        $ GiveGlossaryItemToPlayer(7)
    if game_state.langham_library_is_seen:
        $ GiveGlossaryItemToPlayer(1)
        $ GiveGlossaryItemToPlayer(36)
        $ GiveGlossaryItemToPlayer(24)
        $ GiveGlossaryItemToPlayer(27)
        if game_state.coverture_is_found:
            $ GiveGlossaryItemToPlayer(10)
            if game_state.mill_are_nice:
                $ GiveGlossaryItemToPlayer(14)
    $ ShowItems()
    $ seneca_agrees = 0

    call yes_or_not_question

    lucrecia_mott "Segona qüestió. Els homes han monopolitzat quasi totes les feines rendibles i, les dones que treballen reben una remuneració escassa."
    lucrecia_mott "Es tanquen portes cap a la riquesa i la distinció per a la dona, ja que es considera més honorable per l'home."
    lucrecia_mott "Estan d'acord amb què està en les nostres mans assegurar una participació igualitària a les dones respecte de feines, professions i comerç?"
    call yes_or_not_question

    susan_b_anthony "Tercera qüestió. L'home s'ha esforçat en destruir la confiança de la dona en els seus propis poders, en disminuir-li l'autoestima i en disposar-la a dur una vida dependent i abjecta."
    susan_b_anthony "Estan d'acord amb què la dona ja ha estat massa temps en els límits circumscrits en els costums corruptes i en l'aplicació perversa de les escriptures, i que ja és hora d'ampliar l'esfera que el seu Creador li ha assignat?"
    call yes_or_not_question

    lucy_stone "Ara, passem a l'última quëstió. No es permet exercir a la dona el seu dret a votar. Se la obliga a complir la llei, en la qual ella no té ni veu ni vot."
    lucy_stone "S'atorguen els seus drets als homes més ignorants i degradants, tant natius com estrangers."
    lucy_stone "Estan d'acord amb què les dones tenen el deure d'assegurar-se el seu sagrat dret a votar?"
    call yes_or_not_question

    lucrecia_mott "Molt bé doncs. Les persones signants juren emprar tots els mètodes disponibles al seu abast per combatre aquestes injustícies."
    elizabeth_cady_stanton "D'aquesta manera, donem per finalitzada la Convenció. Passeu a signar aquelles persones que ho desitgeu."
    "En aquell moment, moltes de les persones assistents varen apropar-se a les moderadores del debat per signar el document. Amb [tmpSavePlayer] es podien comptar unes cent persones."

    $ renpy.choice_for_skipping()
    $ GiveGlossaryItemToPlayer(9)
    $ ShowItems()
    $ renpy.show_screen("sf_document")
    "Així, quedava signat el document que passà a conèixer-se més tard com a {i}Declaració de Sentiments i Resolucions{/i}."
    $ renpy.hide_screen("sf_document")

    scene seneca_falls_street
    "[tmpSavePlayer] s'acomiadà de Sojourner i de Charlotte."
    "Era hora de tornar, així que va esperar-se al carrer a què passés un carruatge."
    "Al cap d'una estona, va aparèixer un carruatge i [tmpSavePlayer] s'hi muntà. Es dirigia a l'estació de tren."

    return



label yes_or_not_question:
    menu:
        "Sí":
            $ seneca_agrees = seneca_agrees + 1
            "[tmpSavePlayer] està d'acord amb la resolució anterior."
        "No":
            "[tmpSavePlayer] no està d'acord amb la resolució anterior."

    return


screen sf_document():
    fixed:
        align .5,.5

        image "images/chapter1/seneca_falls_convention/woman_rights_convention.png":
            align .5, 0

        if seneca_agrees >= 3:
            text _("Amb {b}[tmpSavePlayer]{/b}\ncom a persona\nconvidada"):
                font "fonts/lemon_tuesday.otf"
                size 15
                align .4, .22
                at transform:
                    rotate -5
