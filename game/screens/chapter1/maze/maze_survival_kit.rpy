
## This script defines the survival kit (objects panel) on maze.



label maze_survival_kit:
    image bill = "images/chapter1/maze/maze_survival_kit/conciliation_bill.jpg"
    image paint = "images/chapter1/maze/maze_survival_kit/paint_1.png"
    image weapons = "images/chapter1/maze/maze_survival_kit/weapons.jpg"

    scene black

    user "Què deu contenir aquesta caixa?"
    "[tmpSavePlayer] obre la caixa i ..."
    show weapons at truecenter
    user "Ostres, hi ha àcid, una caixa de llumins, una espècie d'eines metàl·liques ..."
    user "Per a què es deuen usar totes aquestes eines i objectes?"
    hide weapons with fade

    show bill at truecenter
    emmeline_pankhurst "El govern liberal ens ha traït. Guanya les eleccions novament prometent una reforma del dret de sufragi, i l'únic que els importa és el sufragi masculí, no el nostre."
    unknown_girl "Traïdors !!!!!"
    emmeline_pankhurst "Hem de protestar! Això no es pot quedar així! Ens han enganyat !!!"
    hide bill with fade
    "La líder de la NUWSS, Millicent Fawcett, decideix trencar vincles amb la WSPU perquè no comparteix els mètodes de la seva líder."
    "Així, la WSPU decideix organitzar una campanya massiva per iniciar tot tipus d'activitats de protesta al carrer."
    show paint at truecenter
    "Es trenquen vidres, es bombardeja la mansió del ministre d'Hisenda, en David Lloyd George, s'escriu amb àcid el lema {i}Votes for Women{/i}, es danyen les bústies dels carrers ..."
    "Les protestes acabaren amb la detenció i posterior incorporament a presó de moltes de les suffragettes."
    hide paint with fade
    "Malgrat això, la líder de la WSPU va decidir aturar les protestes pel vot femení, a causa de l'arribada de la guerra."
    "Contràriament, la líder de la NUWSS va decidir seguir fent campanya política respecte el sufragi femení per vies pacífiques."

    user "Fins i tot entre sufragistes hi havia divergències ... però, tot i així, es respectaven, que és el més important ..."
    user "La germanor en lluites per una causa comuna és un atribut que no pot mancar."
    "D'aquesta manera, [tmpSavePlayer] ja no té cara de raresa per la caixa que ha trobat i, novament, emprèn camí."

    call screen maze
    return
