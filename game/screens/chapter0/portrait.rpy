
## Script for the portrait scene on the art hall.
## Here, there is the first puzzle.

## Portrait scene ######################
label portrait:

    "El quadre tenia un aspecte inquietant. En certa manera, cridava l'atenció ..."
    "Alguna cosa, aparentment estranya, li havia succeït, ja que estava esmicolat completament."
    "[user] tenia curiositat, ja que no comprenia el per què, així que va decidir esbrinar-ho."

    if not game_state.portrait_done:
        #puzzle is not done
        scene black
        call puzzle
    else:
        #puzzle is done
        "Ja has fet el puzzle anteriorment. Vols tornar-lo a fer?"

        menu:
            "Sí":
                scene black
                call puzzle
            "No":
                "D'acord. Continues amb la mateixa història com si l'haguessis fet."

    if game_state.portrait_done:
        $ GiveGlossaryItemToPlayer(17)
        $ ShowItems()

    scene salon_portrait

    if game_state.astell_is_nice:
        mary_astell "Diràs 'ho hem aconseguit' ..."
        user "Però si ho he fet tot jo!"
        mary_astell "Nye, nye, nye ..."
        "[tmpSavePlayer] la mira malament ..."
        mary_astell "D'acooooord, tens raó ... però, de totes maneres, em sorprèn que tinguin el quadre de Delacroix aquí ..."
        mary_astell "El coneixes?"

        menu:
            "Al quadre o a de qui és l'obra?":
                mary_astell "Tu sempre tan burleta ..."
                user "Jajaja. Era broma dona, no t'ho prenguis així ..."
                mary_astell "Nye, nye, nye ... és igual, t'ho explicaré igualment ..."
                user "Ja ho donava per suposat que ho faries de totes maneres ..."
                mary_astell "Ohhhhmmmm ... ohhhmmmmmm ..."
                "Mary va respirar dos segons i va començar ..."

            "Sí, coneixia el quadre però no sabia de qui era":
                mary_astell "Sí, això és el més comú. No pateixis, t'ho explico ..."

            "No, no em sona de res":
                mary_astell "Vaja, pensava que eres una persona que valia la pena ..."
                user "Ololololooooo ..."
                mary_astell "Jajaja. És broma dona. T'explico ..."

        mary_astell "Eugène Delacroix és el pintor de {i}La Liberté guidant le peuple{/i}. Aquest quadre simbolitza la Revolució de les {i}Trois Glorieuses{/i}, concretament el dia 28 de juliol."
        mary_astell "El més important és que el pintor va plasmar la llibertat com a guia que condueix el poble, un poble constituït per membres de classe social mitjana i baixa."
        mary_astell "Però això no és tot, sinó que el concepte de llibertat és una al·legoria, en aquest cas, una dona dotada de molta bellesa."
        user "És curiós que justament sigui la dona qui representi el concepte de llibertat, quan aquest col·lectiu és el menys lliure ..."
        mary_astell "Sí, totalment d'acord amb la teva afirmació. Tanmateix, sí que durant l'època de Revolució Francesa hi va haver alguna dona rellevant."
        user "Ah sí? Explica-me'n més!"
        mary_astell "Sí. Olympe de Gouges va reivindicar drets iguals per a les dones en la Declaració dels drets de la dona i de la ciutadania."
        mary_astell "En aquesta obra, va exposar quins i com els valors de la Il·lustració podien canviar la vida de les dones."
        mary_astell "I recordem que la Il·lustració promovia els principis igualitaris i l'individualisme."
        user "Sí, crec que n'havia escoltat a parlar d'aquesta obra, però no sabia ben bé el seu origen ni res la seva autora ..."

        $ GiveGlossaryItemToPlayer(31)
        $ ShowItems()

        scene salon_entrance
        "I, amb aquesta conversa tan interessant, es van acomiadar al sortir del saló amb una gran abraçada."
        scene street_all
        "[tmpSavePlayer] va tornar a casa seva passejant i pensant en els moments anteriors que havia viscut."

    else:
        user "Què deu voler dir? ..."
        scene street_all
        "[tmpSavePlayer] va sortir del saló. Tornava cap a casa tot rumiant ..."
        user "Què hi devia fer aquell quadre allà? Segur que em volia transmetre alguna cosa que no he sabut interpretar ..."
        "No parava de preguntar-se [tmpSavePlayer] ..."

    if game_state.astell_is_nice:
        $ GiveGlossaryItemToPlayer(31)
        $ ShowItems()

    return
