
## Script for the Consciousness Raising session on Chapter 2 Part 2.


init -1 python:
    cr_rate = 0
    def addRateScore(score):
        global cr_rate
        cr_rate = cr_rate + score


label cr_session:
    scene cr_adriennerich
    user "Bon dia. Em dic [tmpSavePlayer]. M'havien convidat a la sessió d'aquest grup."
    unknown_girl "Sí, passi. En breu farem la benvinguda."
    "La moderadora va assenyalar on podia seure i immediatament després, va començar la sessió."
    unknown_girl "Benvingudes a totes les persones assistents. Novament, avui sumem una sessió més del grup d'autoconsciència."

    $ GiveGlossaryItemToPlayer(9)
    $ ShowItems()

    unknown_girl "Per les noves incorporacions, jo em dic Adrienne Rich i seré la moderadora del grup durant el transcurs del mateix."
    "Bon dia, Adrienne !! - varen contestar en veu alta totes les noies del grup alhora."

    $ GiveGlossaryItemToPlayer(0)
    $ ShowItems()

    stop music fadeout 0.5
    scene cr_einstein
    play music "audio/sound/einstein.mp3" fadein 0.5
    adrienne_rich "I aquest reiet d'aquí es diu Einstein. Veureu que ens farà molta companyia. És una peça fonamental en la germanor i la lleialtat."
    "Les noies i [tmpSavePlayer] miraren la cara d'aquell gos tan adorable. Movia la cua. Estava content."
    stop music fadeout 0.5
    play music "audio/music/chapter2a.mp3" fadein 0.5

    scene cr_session
    $ cr_rate = 0
    show adrienne_rich_pic at right
    adrienne_rich "Avui, tenim una persona convidada a la sessió. Es diu [tmpSavePlayer]. Com a cronista, ha vingut per compartir-nos la seva experiència i coneixement sobre el feminisme de la diferència."
    hide adrienne_rich_pic
    user "En efecte, Adrienne. Un plaer ser aquí amb vosaltres avui."
    "Bon dia, [tmpSavePlayer] !! - digueren les noies."

    show adrienne_rich_pic at right
    adrienne_rich "Molt bé, noies. Doncs donem per començada la sessió d'avui."
    adrienne_rich "Parlarem del feminisme de la diferència i de com afecta a cada col·lectiu de manera particular."
    adrienne_rich "Formin part del col·lectiu que sigui, la pobresa, la desigualtat salarial, la discriminació laboral i el repartiment desigual de tasques domèstiques són fets que afecten les dones."
    adrienne_rich "Ens trobem davant de la feminització de la pobresa. A causa de l'opressió estructural, les dones viuen en la pobresa, ja que les institucions i la societat limiten els seus recursos econòmics i les seves oportunitats."
    hide adrienne_rich_pic
    participant "Sí, i a les dones negres ens afecta també el racisme estructural. - digué Alicia, una dona negra de trenta anys."
    show p_alicia_pic at truecenter
    p_alicia "Qualsevol dels sistemes d'opressió, discriminació i/o dominació actuen interrelacionats i suposen identitats socials solapades.."
    p_alicia "És a dir, la interseccionalitat és un risc múltiple, ja que el sexisme s'agreuja en combinació amb el racisme i altres opressions, com la classe."
    hide p_alicia_pic

    $ GiveGlossaryItemToPlayer(18)
    $ ShowItems()

    user "Sí. De fet, les feministes negres i de classe treballadora denuncien el racisme i els prejudicis subjacents a la germanor del feminisme."
    user "Malgrat les dones negres poguessin votar, l'activisme pels drets laborals, la llibertat sexual o el control de la natalitat segueix dominat per dones blanques de classe mitjana."
    user "Per aquest motiu, el feminisme de la diferència acull aquestes particularitats de cadascun dels diferents col·lectius, per acollir la dona com a gènere, raça, classe i/o grup social."
    show adrienne_rich_pic at right
    adrienne_rich "Crec recordar que hi havia una autora que parlava d'aquest tema ... Com es deia? ... No ho recordo."
    adrienne_rich "Però venia a dir que el feminisme estava definit i dominat per dones blanques de classe mitjana, la qual cosa fa que ignori el racisme i alhora contribueixi a ell."
    adrienne_rich "Les dones negres no solament pateixen la desigualtat racial, sinó també la de gènere. Estan més oprimides que les dones blanques."
    hide adrienne_rich_pic
    show p_alicia_pic at truecenter
    p_alicia "Necessitem un feminisme propi, que consideri els problemes de les dones negres també. L'opressió racial i la de classe."
    hide p_alicia_pic

    $ GiveGlossaryItemToPlayer(2)
    $ ShowItems()

    user "Considero que això es remunta més enllà ..."
    user "Ja en les societats esclavistes la dona negra era considerada sexualment {i}fàcil{/i}, a qui es culpava quan s'abusava d'ella física i sexualment. Ja era present aquest estereotip llavors."
    user "Sí que les dones blanques no ho tenien pas millor, ja que eren considerades dèbils i delicades, però a les negres s'esperava que treballessin com homes per ser considerades poc femenines o refinades."
    participant "La meva mare, en pau descansi, va ser esclava i va haver de viure sota aquestes condicions durant molts anys. Per sort, va poder fugir i viure la vida que li restava en pau i a la muntanya, com a ella li agradava. - digué Lynn, una dona negra de quaranta anys."
    show adrienne_rich_pic at right
    adrienne_rich "Ostres, Lynn. Quin mal tràngul ... per sort, l'esclavisme ja va acabar fa anys."
    hide adrienne_rich_pic
    show p_lynn_pic at truecenter
    p_lynn "Sí, però encara segueixo sense trobar explicació a què a una amiga de la meva mare l'esterilitzessin sense consentiment, igual que a altres companyes seves de classe treballadora, mentre que a les dones blanques se les animava a tenir descendència."
    hide p_lynn_pic

    $ GiveGlossaryItemToPlayer(3)
    $ ShowItems()

    user "La violació en l'esclavitud era la manera rutinària dels propietaris de les esclaves per atemorir-les i recordar als esclaus negres que no podien protegir-les."
    show p_lynn_pic at truecenter
    p_lynn "Però la violació no està motivada per la luxúria?"
    hide p_lynn_pic

    $ GiveGlossaryItemToPlayer(9)
    $ GiveGlossaryItemToPlayer(0)
    $ GiveGlossaryItemToPlayer(18)
    $ GiveGlossaryItemToPlayer(2)
    $ GiveGlossaryItemToPlayer(3)
    $ ShowItems()

    call true_or_false_question("rape_luxury")

    participant "El més important és no culpabilitzar-se. El meu pare abusava de mi quan era una nena petita i, si no fos pel recolzament de centres d'ajuda com aquest, jo no hauria pogut tirar endavant. - digué Serena, una noia blanca de 20 anys."
    show adrienne_rich_pic at right
    adrienne_rich "Exactament, Serena. Gràcies per compartir-ho amb nosaltres."
    adrienne_rich "És important crear centres d'ajuda per oferir recolzament i refugi a les víctimes, així com mobilitzar-se per canviar les lleis al respecte."
    adrienne_rich "I no només això, sinó amb iniciatives de persecució de violacions que vagin en contra de la culpabilització de la víctima, amb èmfasi en l'educació pública sobre el consentiment i amb millors pràctiques en hospitals, tribunals i mitjans de comunicació."
    hide adrienne_rich_pic
    show p_serena_pic at truecenter
    p_serena "Hem d'exigir que aquest tipus de delictes es prenguin més seriosament. Prou de considerar-los asumptes estranys o tabú. - va manifestar efusivament."
    hide p_serena_pic
    show adrienne_rich_pic at right
    adrienne_rich "Per això, és important animar a les víctimes d'aquest tipus de delictes que denunciïn i que demanin ajuda per poder superar el mal psicològic que han patit."
    hide adrienne_rich_pic
    show p_alicia_pic at truecenter
    p_alicia "Jo sempre havia cregut que la violació és perpetrada per estranys."
    hide p_alicia_pic

    call true_or_false_question("rape_author")

    show adrienne_rich_pic at right
    adrienne_rich "Després d'aquest tema un pèl espinós, podem continuar."
    adrienne_rich "Seguint el fil que hem començat al principi, també el feminisme chicana, moviment anticolonialista, considera que el feminisme de les dones blanques no es preocupa per les problemàtiques de les dones chicanes."
    adrienne_rich "Concretament, no es preocupa per la discriminació racial i de classe que patien elles, a més a més del sexisme."
    hide adrienne_rich_pic
    participant "Gloria Anzaldúa és una dona estudiant dels moviments inclusius, centrada en la jerarquia dins del colonialisme i en com s'hi entrellacen qüestions de gènere, raça, classe i salut. - explicà Gloria, una noia mexicana."
    show p_gloria_pic at truecenter
    p_gloria "Aquesta dona subratlla l'entrellaçament de les diferents identitats i opressions, i el considera una forma de neocolonialisme."
    hide p_gloria_pic
    show p_alicia_pic at truecenter
    p_alicia "És que la perspectiva feminista occidental de la dona del tercer món redueix a la dona real a un estereotip invariable i uniforme, de manera similar al què succeeïx amb les dones negres."
    p_alicia "Per això, el feminisme postcolonial segueix reclamant un moviment feminista inclusiu i útil, basat en valors compartits per dones de tot el món, que ajudi a comprendre millor els seus objectius i lluites particulars."
    hide p_alicia_pic
    user "És veritat que en els llibres s'acostuma a estudiar el feminisme des del punt de vista occidental ..."
    show p_gloria_pic at truecenter
    p_gloria "Sí, fins i tot les dones indígenes pateixen una doble opressió. Per motius de gènere i ètnics."
    p_gloria "I, per combatre-la, les dones indígenes s'impliquen més en la lluita ètnica i criden l'atenció en qüestions respectives de les dones, vinculant així l'autonomia femenina i l'ètnia."
    p_gloria "Però la realitat és molt més crua. Moltes varen ser esterilitzades forçosament, desaparegudes i, fins i tot, assassinades."
    hide p_gloria_pic

    $ GiveGlossaryItemToPlayer(33)
    $ ShowItems()

    user "Cada vegada resulta més necessari el recolzament pràctic i emocional als grups de dones de comunitats amb major risc per erradicar la violació dels drets humans."
    user "De la mateixa manera que la clau per prevenir aquest tipus de violacions roman en l'educació, ja que acostuma a donar-se en sectors menys instruïts."
    participant "Jo ... mmm ... quan tenia deu anys, la meva família estava plena de deutes, i per posar-hi fi, va decidir casar-me forçosament amb un home que em triplicava l'edat. - va dir Houda, una dona musulmana de trenta-cinc anys."
    show p_houda_pic at truecenter
    p_houda "No passarà res, em deien ... tu fes el què et digui aquest home sempre i tot anirà bé. - es posà a plorar."
    p_houda "Aquell home era fastigós. M'obligava a tenir relacions sexuals amb ell, tot i els meus crits de negació, em tocava sempre que se li passava pel cap ... Mai oblidaré la seva cara. - plorant."
    p_houda "Afortunadament, sembla que els miracles existeixen. Vaig poder fugir a un altre país i mai més en vaig tornar a saber res. Vaig perdre tot el contacte amb la meva família però, sincerament, és un sacrifici que faig sense penedir-me. - ja més calmada."
    hide p_houda_pic
    show adrienne_rich_pic at right
    adrienne_rich "Gràcies per compartir-ho amb nosaltres, Houda. És que, fins i tot, es pot dir que els matrimonis forçats estan vinculats al tràfic d'éssers humans. I això és més que sèrio."
    adrienne_rich "Per això, com a dones, hem de cedir a allò que l'home ens digui, faci o ens faci fer, independentment de la nostra voluntat i/o consentiment?"
    hide adrienne_rich_pic

    $ GiveGlossaryItemToPlayer(33)
    $ ShowItems()

    call no_is_yes

    show adrienne_rich_pic at right
    adrienne_rich "D'acord, aturem motors un moment. Respirem fons i continuem. Ja hem passat l'equador i ara comencem l'última part de la sessió."
    adrienne_rich "Ara, emprenem el tema de la sexualitat."
    adrienne_rich "Hi ha un corrent, el lesbianisme polític que estableix que una dona solament pot ser realment lliure de la violència i el control de l'home si l'exclou de la seva vida sentimental i sexual."
    adrienne_rich "D'aquesta manera, deixar enrere la sexualitat voluntàriament seria una manera de comprometre's amb el moviment d'alliberació."
    user "Però si es posen tots els homes en el mateix sac, al final s'està discriminant també. No tothom és igual."
    adrienne_rich "És cert això que diu. No obstant això, és veritat que la sexualitat de la dona està condicionada per l'home."
    adrienne_rich "Per exemple, la pornografia. Per un sector de la comunitat, la pornografia és la sexualitat essencial del poder masculí."
    adrienne_rich "En aquesta, les dones són maltractades i coaccionades, erotitzant la subordinació. Cada vegada que l'espectador repeteix la seva visualització, es va insensibilitzant, fins al punt de necessitar pornografia més violenta per excitar-se."
    hide adrienne_rich_pic
    show p_houda_pic at truecenter
    p_houda "Jo crec que s'hauria d'il·legalitzar la pornografia. La considero moralment depravada i una amenaça per la societat i el matrimoni."
    hide p_houda_pic
    show p_serena_pic at truecenter
    p_serena "Doncs jo penso que s'hauria d'il·legalitzar també, però perquè la dona és representada com un objecte sexual i no com a ésser humà, i això fomenta la violència contra elles."
    hide p_serena_pic
    show adrienne_rich_pic at right
    adrienne_rich "Interessants punts de vista els vostres. Llavors, considereu la pornografia violenta i misògina?"
    hide adrienne_rich_pic
    participant "No considero que sigui pas així. La pornografia és alliberadora, ja que la censura de la sexualitat quasi sempre té un impacte repressiu sobre les sexualitats marginades. - va explicar Ibonne, una noia trans."
    show p_ibonne_pic at truecenter
    p_ibonne "S'ha de promoure el plaer físic, i l'experimentació i educació sexuals. És important emfatitzar la llibertat sexual de les dones, i dels grups LGTBQ en general."
    p_ibonne "Acceptar la bisexualitat, el lesbianisme i la fluidesa del gènere és necessari per aconseguir l'alliberació de les dones."
    p_ibonne "Les restriccions socials i legals del sexe consentit entre adults són mecanismes dels governs patriarcals que segueixen usant per discriminar la sexualitat de les dones."
    hide p_ibonne_pic
    show adrienne_rich_pic at right
    adrienne_rich "Ostres, Ibonne, jo no podria haver exposat millor què és el positivisme sexual."
    "Ibonne va mirar amb cara de vergonya a la resta de les dones del grup."
    adrienne_rich "I, amb la consigna 'Accepta i respecta' ens acomiadem de la sessió d'avui."

    call rate_options
    call other_day
    call end_chapter(CHAPTERS[3])

    return



label rate_options:
    if cr_rate >= 3:
        $ GiveGalleryItemToPlayer(3)
        user "Moltes gràcies per convidar-me. La sessió ha estat molt participativa, dinàmica i interessant. M'encantaria tornar un altre dia."
        adrienne_rich "I tant que sí!"
        "I, amb abraçades, agraïments i salutacions amigables, les dones del grup, la moderadora i [tmpSavePlayer] s'acomiadaren."
    elif cr_rate >= 0:
        user "Moltes gràcies per convidar-me. La sessió ha estat correcta."
        adrienne_rich "Sí, tot i haver diferències entre nosaltres, la sessió s'ha desenvolupat amb respecte i consideració."
        "I, amb salutacions cordials, totes les dones participants s'acomiadaren unes d'altres."
    elif cr_rate < 0:
        adrienne_rich "No obstant això, aquesta és la primera i última vegada que convido a un ésser tan intolerant com vostè, amb tots els respectes."
        user "Disculpi'm. En cap moment he tingut la intenció de faltar el respecte a ningú. Sóc una persona ignorant i, com a tal, vull aprendre dels meus errors."
        adrienne_rich "No passa res. Aquí totes estem per aprendre. Per respectar. Per construir una consciència real del problema."
        user "Gràcies a totes per escoltar-me i ensenyar-me que la germanor en aquests casos és fonamental."
        "I, amb agraïments i salutacions, les dones del grup s'acomiadaren."

    hide adrienne_rich_pic
    return


label rape_luxury(result):
    if result:
        $ addRateScore(-2)
        user "És clar. La luxúria de l'home. Ja se sap que quan un home està excitat, no pot fer res per controlar la seva necessitat sexual."
        "Totes les dones de la sala es varen quedar petrificades."
        show p_alicia_pic at truecenter
        p_alicia "De veritat pensa això que està dient?"
        hide p_alicia_pic
        call true_or_false_question("sex_need")

    else:
        $ addRateScore(3)
        user "No. La violació està motivada pel poder i la violència."
        user "La violació és política. Es dóna permís als homes perquè, per una banda, existeix la creença de que el cos de la dona és perquè sigui posseït per l'home i, d'altra banda, perquè així es manté la situació de subordinació de les dones."

    return

label sex_need(result):
    if result:
        $ addRateScore(-3)
        user "És clar. La sexualitat femenina incita a violar."
        "Totes es posaren les mans al cap, menys una noia una mica peculiar."
        show adrienne_rich_pic at right
        adrienne_rich "[tmpSavePlayer] no és la persona convidada per ensenyar aquest tipus de barbaritats."
        hide adrienne_rich_pic
        participant "Però si té raó!!! Sinó mireu com va aquell farsant vestit de dona. Travelo, més que travelo !!!! - cridà una noia jove del grup a una persona assistent trans."
        show unknown_girl_terf at truecenter
        participant "Tu i els que són com tu esteu mentalment malalts!! No ens envaireu els espais de les dones!! No ho permetrem!!! - manifestà encara més efusivament."
        participant "Coses com vosaltres que us feu dir dones sí que mereixeu ser violades!!! I molt més!!! - s'aixecà de la cadira."
        hide unknown_girl_terf
        show adrienne_rich_pic at right
        adrienne_rich "Per favor, surt de la sala. Aquí estem per aprendre de la diferència, per respectar-la i acceptar-la. No perquè hi hagin atacs com aquests a les companyes. No tornis més."
        hide adrienne_rich_pic
        "I aquella noia marxà de la sala amb un fort cop de porta."
        "Adrienne, pensativa, va preguntar-se en veu alta ..."
        show adrienne_rich_pic at right
        adrienne_rich "Ho ha dit perquè sabia que probablement saltaria en contra, oi?"
        hide adrienne_rich_pic
        "Es dirigia a [tmpSavePlayer]."

        menu:
            "Sí":
                user "Sí. La meva intuïció em deia que la noia formava part del TERF, sobretot per les cares que anava fent."
            "No":
                user "Per a res. Però sí que em sembla una frase polèmica. Ha estat tota una sorpresa que la noia formés part del TERF."

        show adrienne_rich_pic at right
        adrienne_rich "Per qui no ho sàpiga, existeix una branca del feminisme radical anomenada transexclusiva."
        adrienne_rich "Com ja diu la pròpia paraula, aquest feminisme està en contra de la validesa de les persones trans i reforcen els perjudicials estereotips del binarisme de gènere."
        adrienne_rich "Però jo us convido a qüestionar-vos si és o no una falta de respecte cap a la identitat d'aquestes persones. Què respecta més a l'altre, l'exclusió o l'inclusió? Rumieu-ho vosaltres mateixes."
        hide adrienne_rich

    else:
        $ addRateScore(3)
        user "És clar que no !!! No hi ha cap justificació possible per la violació."
        "Amb cara de tranquil·litat, les dones suspiren. Per un moment, havien anat amb l'ai al cor."

    return


label rape_author(result):
    if result:
        $ addRateScore(-1)
        user "Efectivament. Si fos un assumpte ordinari se'n parlaria més, i ara no se'n parla gairebé."
        show p_serena_pic at truecenter
        p_serena "Però vostè d'on ha sortit?! Si no se'n parla és per por a represàlies!!!"
        hide p_serena_pic
        call true_or_false_question("rape_fear")
    else:
        $ addRateScore(2)
        user "No, això és un mite!!"
        user "El violador acostuma a ser algú conegut o proper a la víctima, aparentment una persona respectable."

    return


label rape_fear(result):
    if result:
        $ addRateScore(3)
        user "Té raó, Serena. Existeix el que es coneix com la cultura del silenci, que envolta aquests tipus de temes per por a parlar-ne."
        show p_serena_pic at truecenter
        p_serena "En el primer centre d'ajuda on vaig ser, ja m'ho van comentar això. De fet, a mi mateixa em passava. Parlar-ne m'implicava conscienciar-me d'haver-ho viscut, i només volia oblidar-me'n."
        hide p_serena_pic
        show adrienne_rich_pic at right
        adrienne_rich "Afortunadament, a hores d'ara ja has après a viure amb aquesta experiència i a què no t'afecti en el teu dia a dia."
        hide adrienne_rich_pic
        show p_serena_pic at truecenter
        p_serena "Sí, tot i que encara hi ha dies no tan bons ... - amb el cap cot."
        hide p_serena_pic

    else:
        $ addRateScore(-2)
        user "No. Si no se'n parla és perquè, en el cas de violació a les dones, aquestes fan acusacions falses per venjança. Resulta innecessari escampar-ho o fer-ho públic sense perdre reputació."
        show p_serena_pic at truecenter
        p_serena "No em puc creure el què està dient ...  - es va quedar petrificada."
        p_serena "Però quin percentatge es pensa que hi ha d'acusacions falses? - s'estava enfurismant més."
        hide p_serena_pic
        menu:
            "Entre 10-20":
                user "Entre un 10 i un 20 del total, m'atreviria a dir."
                show p_serena_pic at truecenter
                p_serena "Doncs s'equivoca. El percentatge no és més que en altres delictes, i és inferior a 10."
                p_serena "No se'n vagi per les branques. - bastant molesta."
                hide p_serena_pic
            "Menys d'un 10":
                $ addRateScore(1)
                user "Crec que inferior al 10 del total."
                show p_serena_pic at truecenter
                p_serena "Efectivament, no més que en altres delictes."
                p_serena "Llavors, tingui una mica més de respecte. - bastant molesta."
                hide p_serena_pic
                user "D'acord. Disculpi si l'he molestada."
    return


label no_is_yes:
    $ renpy.choice_for_skipping()
    menu:
        "Quan una dona diu que no, en realitat vol dir que sí":
            $ addRateScore(-3)
            user "Però si una dona no diu explícitament que no, això vol dir que en el fons vol dir que sí perquè no ha mostrat la seva negació."
            show p_houda_pic at truecenter
            p_houda "Rotundament NO. Si la dona no explicita el seu consentiment, no es poden suposar altres desitjos d'ella. Ningú té dret a anar en contra dels desitjos d'algú altre. - bastant molesta."
            p_houda "Llavors, les vegades que aquell home em va violar sexualment sense el meu consentiment? Ho considera desig meu? - enfurismada."
            p_houda "Ni que anés a resar a Déu aquest podria fer realitat el miracle de donar-li una neurona ... - amb sàtira i molt enfadada."
            hide p_houda_pic

        "Ha ocorregut una vegada, no passarà més":
            $ addRateScore(1)
            user "Pot ser que l'home et digui que aquesta serà l'única vegada, que no tornarà a ocórrer."
            show p_houda_pic at truecenter
            p_houda "Sí, però la violència no és un incident aïllat, sinó que forma part d'un patró de violència en augment."
            p_houda "Ho dic per pròpia experiència."
            hide p_houda_pic

        "És clar, perquè sinó l'home es pot posar violent":
            $ addRateScore(-2)
            user "Si no es compleix allò que l'home violent diu, acabarà exercint la violència sobre la dona. I llavors serà com si ella s'ho hagués buscat."
            show p_houda_pic at truecenter
            p_houda "Per començar, no tots els homes són violents per naturalesa i, de fet, aquests no es mostren així fora de casa."
            p_houda "I encara menys que sigui culpa de la dona per 'haver fet alguna cosa malament'. No hi ha excusa que justifiqui la violència."
            p_houda "De la mateixa manera que una violació no pot ser excusada per l'home a través de la desacreditació de la dona, dient que vestia provocativa o que tenia mala reputació i que ell només es va limitar a donar-li allò que li estava demanant."
            hide p_houda_pic

    return



label true_or_false_question(label_name):
    $ renpy.choice_for_skipping()
    menu:
        "Vertader":
            $ renpy.call(label_name, True)
        "Fals":
            $ renpy.call(label_name, False)

    return
