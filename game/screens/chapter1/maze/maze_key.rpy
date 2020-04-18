
## This script defines the key (objects panel) on maze.



label maze_key:
    image key_fight = "images/chapter1/maze/maze_key/key_fight.jpg"
    image young_women = "images/chapter1/maze/maze_key/young_women.jpg"
    image fight = "images/chapter1/maze/maze_key/fight.jpg"
    image poster = "images/chapter1/maze/maze_key/poster.png"

    scene black
    user "Una clau. Deu ser per obrir aquesta porta tancada d'aquí ..."

    show key_fight at truecenter
    edith_garrud "D'aquesta manera, podreu subjectar millor a la persona ..."
    "[tmpSavePlayer] es trobava en la sala secreta de les suffragettes, en la qual Edith estava ensenyant l'art marcial del jiu-jitsu a les seves companyes."
    unknown_girl "Senyora Garrud, podria repetir aquesta última clau? No l'he acabada d'entendre ..."
    hide key_fight with fade
    show young_women at truecenter
    edith_garrud "I tant que sí. L'explicaré amb una demostració que faran dues companyes teves. Elisa i Beth, per favor, feu-ne una demostració."
    "I, mentre Edith tornava a repetir detalladament els passos, les noies els reproduïren."
    hide young_women with fade
    edith_garrud "Molt bé noies, la classe ha finalitzat. Recordeu que sempre heu d'estar alerta i, si cal, defenseu-vos."
    show fight at truecenter
    edith_garrud "Ja coneixeu la història de quan em vaig haver de defensar jo del policia que em volia retenir a la força."
    "Edith feia referència a una manifestació que varen realitzar temps enrere, en la qual es va veure forçada a fer ús de les seves tècniques marcials per defensar-se de les autoritats."
    hide fight with fade
    "{i}Gràcies, senyora Garrud !!{/i} - varen cridar totes les noies alhora i varen marxar."
    "Edith s'havia proposat ensenyar aquest art marcial a les seves companyes perquè aprenguessin a defensar-se en qualsevol moment, sobretot en la lluita per la causa."
    show poster at truecenter
    "En aquella sala, en la qual hi havia una espècie de pòster amb claus, es reunien les suffragettes clandestinament per planejar els seus moviments."
    "Així, aprofitaven alhora per fer-hi aquestes classes també."
    hide poster with fade

    user "Genial!! Crec que és totalment necessari conèixer algun art marcial, sobretot si és per defensar-se en cas d'atac contra la pròpia persona, i més si s'és una dona!!"
    user "Bé, també està genial fer-ho per plaer ..."
    "[tmpSavePlayer] es va quedar pensant. I, mentrestant, va seguir el seu camí ..."

    call screen maze
    return
