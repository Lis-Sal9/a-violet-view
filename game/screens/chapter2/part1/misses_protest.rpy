
## This is script for Miss America and Miss Black America protests.


label misses_protest:
    "..."
    "[tmpSavePlayer] portava una estona de camí quan, de sobte ..."
    show taxist at left
    unknown_boy "Però què és això ?????"
    hide taxist
    "El conductor del taxi havia frenat molt bruscament. Estava enfurismat."
    "[tmpSavePlayer] es va espantar, però de seguida va veure què estava succeïnt."
    "Moltes dones havien pres els carrers per manifestar-se."
    show taxist at left
    unknown_boy "Disculpi, un grup de dones amargades han tallat els carrers per queixar-se. Ara haurem d'esperar una bona estona fins que se'ls passi la bestiesa."
    hide taxist

    menu:
        "Disculpi, senyor, però vostè és un mal educat":
            user "Em permeto la llicència de faltar-li el respecte igual que ha fet a aquestes dones vostè. És un autèntic mal educat."
            "La furor l'aclaparava, així que sense pagar [tmpSavePlayer] baixà del taxi i s'endinsà entre la multitud."
            call inside_misses_protest

        "Ostres, un altre cop protestant. Sempre s'estan queixant per tot":
            user "Què pesades, sempre tenen alguna qüestió de la què queixar-se."
            "[tmpSavePlayer] es resignà i mirà des del taxi la progressió de la manifestació."
            scene black
            show miss_welcome at truecenter
            "Les dones anaven caminant poc a poc, com si fos una processó, a crits de 'Prou de cosificar les dones' i 'No som la fantasia de l'home'."
            "Al fons, es veien pancartes, s'escoltaven més crits."
            hide miss_welcome
            show miss_inside at truecenter
            "Era innegable que aquella gran protesta pública passaria a la història."
            "Passaren dues hores fins que la manifestació no va permetre al taxi avançar pels carrers novament."
            hide miss_inside
            scene taxi
            show taxist at left
            unknown_boy "Ja s'ha acabat la neciesa i podem continuar el trajecte."
            hide taxist
            scene now_building
            "Una estona més tard, el taxi ja havia arribat a la seva destinació."
            user "Gràcies, senyor."
            "Assentint amb el cap, el conductor es va acomiadar mentre [tmpSavePlayer] pagava i baixava del taxi."

    return



label inside_misses_protest:
    scene black
    show miss_welcome at truecenter
    "Era impressionant. Moltíssimes persones s'havien reunit pels carrers de la ciutat per manifestar-se en contra dels concursos de bellesa."
    "Pel que va poder esbrinar [tmpSavePlayer], concretament es tractaven dels concursos de Miss America i Miss Black America."
    "Ja n'hi ha prou !!! Prou de cosificar les dones !!! - va cridar una dona manifestant."
    hide miss_welcome
    show miss_figure at truecenter
    "Pel que es veia en les pancartes, la manifestació pretenia denunciar les moltes formes en què els homes reifiquen les dones."
    "Però no només això, sinó el racisme existent en aquest tipus de concursos."
    "Particularment, les dones negres pateixen una doble discriminació: sexista i racista."
    "Més enllà, algú cridava ..."
    show unknown_girl_protest at left
    unknown_girl "Destruïm la mirada masculina en la pantalla !!!"
    hide miss_figure
    hide unknown_girl_protest
    show miss_inside at truecenter
    show unknown_girl_protest at left
    unknown_girl "Abolim el punt de vista actiu i masculí de la càmara i el paper passiu de la dona en la pantalla !!!"
    unknown_girl "No som la fantasia de l'home !!! Ni ens han de projectar conforme a això !!!"
    unknown_girl "Fem que no ens converteixin en objectes eròtics de desig de ningú, ni pels propis personatges ni pel públic !!!"
    hide unknown_girl_protest
    hide miss_inside
    show miss_trash at truecenter
    "Juntes cap a la llibertat !!!!! - varen cridar moltes persones alhora."
    "[tmpSavePlayer] continuava caminant entre la multitud mentre observava detingudament l'acte de rebel·lió."
    hide miss_trash
    scene now_building
    "Als pocs minuts de seguir caminant, va arribar a la seva destinació."
    "{i}Per fi, ja he arribat. Pensava que m'engoliria, la manifestació.{/i} - va pensar [tmpSavePlayer]."

    return
