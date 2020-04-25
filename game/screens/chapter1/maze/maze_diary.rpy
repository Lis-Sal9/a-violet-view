
## This script defines the diary (objects panel) on maze.



label maze_diary:
    image eat = "images/chapter1/maze/maze_diary/eat.jpg"
    image protest = "images/chapter1/maze/maze_diary/protest.jpg"
    image ticket = "images/chapter1/maze/maze_diary/ticket.jpg"
    image force = "images/chapter1/maze/maze_diary/force.jpg"

    scene black

    user "Ostres, un diari personal! De qui deu ser?"
    "[tmpSavePlayer] obre el diari, tot i no saber de qui era, i comença a llegir ..."

    show ticket at truecenter
    "{i}Diumenge, dia 21 de juny: Avui ha estat un dia màgic.{/i}"
    "{i}Les suffragettes ens hem manifestat a Hyde Park i l'assistència ha estat massiva. Gairebé 500.000 persones !!!{/i}"
    "{i}La señora Pankhurst, líder de WSPU, i les noies Sylvia i Christabel, dues de les seves filles, estaven molt contentes. Bé, totes ho estàvem.{/i}"
    hide ticket with fade
    show protest at truecenter
    "{i}L'acollida va ser espectacular, les imatges que se'n poden recordar són precioses, amb carrers plens de gom a gom d'activistes.{/i}"
    "{i}Es podien llegir tots tipus de cartells, però eren força recurrents els que duïen escrits els lemes del grup: 'Votes for Women' i 'Deeds, not words'.{/i}"
    hide protest with fade
    "{i}...{/i}"

    show force at truecenter
    "{i}Hem passat a l'acció. El Primer Ministre Asquith ens ignora i estem cansades.{/i}"
    "{i}Hem trencat finestres amb el llançament de pedres a Downing Street. Algunes companyes s'han lligat a reixes. Ja n'hi ha prou!{/i}"
    "{i}Les autoritats ens han detingut a algunes de les dones, i hem acabat a presó. Quin mal tràngul.{/i}"
    "{i}Les condicions allà eren pèssimes i, per protestar sobre aquestes condicions, vàrem fer vaga de fam.{/i}"
    hide force with fade
    show eat at truecenter
    "{i}Va durar uns quants dies, fins que les autoritats ens varen alimentar a la força.{/i}"
    "{i}Érem lligades a una cadira o retingudes per guàrdies. Llavors el metge ens introduïa pel nas o la boca a través d'un tub de goma la mescla de pa, llet i brandy.{/i}"
    "{i}I empenyaven el tub de goma cap avall per la gola, amb la finalitat d'arribar a l'estómac.{/i}"
    "{i}Rara era la vegada que els teixits nasals i bucals no acabaven esquinçats ...{/i}"
    "{i}... però pitjor era quan el tub de goma s'inseria en la tràquia, ja que això provocava que el menjar passés als pulmons i es posés així en perill la vida de la persona.{/i}"
    "{i}Va ser un dels pitjors moments de la meva vida. No els hi perdonaré mai que ens tractin com un drap brut.{/i}"
    hide eat with fade
    "{i}...{/i}"

    user "Ostres ... què dur ..."
    user "No sé qui deu haver escrit aquest diari, però per les seves paraules, la lluita sufragista va ser força dura ..."

    "Amb aquest mal cos i rumiant, [tmpSavePlayer] va seguir caminant ..."

    call maze_label
    return
