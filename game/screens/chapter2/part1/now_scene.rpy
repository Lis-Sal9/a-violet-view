
## This is script for National Organization Women scene.


label now_scene:
    "[tmpSavePlayer] va entrar dins de l'organització."
    "Volia assistir a la conferència impartida per Betty Friedan, que presentava la Declaració de NOW."
    "A més a més, a la conferència assistia Simone de Beauvoir i Kate Millet com a persones convidades."
    "[tmpSavePlayer] anà a la sala on seria impartida i esperà el seu inici."
    "..."
    scene now_conference
    "Més tard ..."
    betty_friedan "Bon dia a totes les persones assistents. És un plaer per a mi estar avui aquí amb totes vosaltres."
    "Betty Friedan es presentà, igual que posteriorment presentà a les persones convidades."
    betty_friedan "I no solament per aquest motiu, sinó perquè comptem amb la companyia de Simone de Beauvoir i Kate Millet aquí presents."
    simone_de_beauvoir "Bon dia a totes! Moltes gràcies, Betty. El plaer és meu."
    kate_millet "Gràcies, Betty. Bon dia a totes !"
    betty_friedan "Com ja hauran vist, avui és un dia especial. Els carrers estan plens de persones manifestants."
    betty_friedan "És molt important impactar des d'un primer pla la consciència pública per evidenciar l'opressió comercial i social de les dones, així com la sexualització."
    betty_friedan "Aquestes grans protestes públiques que estem duent a terme en aquest denominat {i}Moviment per l'Alliberació de la Dona{/i} pretenen donar a conèixer els mecanismes opressors considerats 'naturals' de les dones."
    betty_friedan "I no només això, sinó que amb destresa intel·lectual i una nova manera de fer política pretenem aconseguir la desvinculació de la maternitat i la procreació de la pràctica sexual."
    betty_friedan "Hem de gaudir de llibertat sexual i autonomia en les nostres relacions de parella."
    betty_friedan "Dit això, dóno per iniciada la conferència."

    $ GiveGlossaryItemToPlayer(5)
    $ ShowItems()

    "Totes les persones assitents aplaudiren."
    betty_friedan "NOW es basa en el principi de què les dones som, per sobre de tot, éssers humans que han de tenir l'ocasió de desenvolupar en la seva plenitud el seu potencial humà."
    betty_friedan "D'aquesta manera, en la Declaració que he escrit, es reivindica la inclusió de les dones en la societat, amb els seus béns i privilegis."
    betty_friedan "És necessari canviar el sistema per aconseguir la igualtat entre sexes, ja que les dones es troben en situació de desigualtat."
    betty_friedan "El problema principal és l'exclusió de les dones en l'esfera pública."
    betty_friedan "És per aquest motiu que es promou la inclusió de les dones en el mercat laboral i en càrrecs polítics."

    $ GiveGlossaryItemToPlayer(28)
    $ ShowItems()

    kate_millet "El patriarcat, com a sistema bàsic de dominació en el qual es recolzen tota la resta, és política sexual, com anomeno el meu llibre, és a dir, es refereix a l'establiment de les relacions."
    kate_millet "El factor econòmic és un instrument de dominació, i el mite i la religió són instruments ideològics relegats a 'altres'."
    kate_millet "Per tant, el sexe és una categoria social impregnada de política i el govern té domini econòmic sobre les dones."
    kate_millet "Però això no és tot, sinó que la família i l'educació reforcen aquest patriarcat, ja que és on s'aprenen les {i}falàcies virils{/i}."
    kate_millet "Les {i}falàcies virils{/i} són mentides, repetides durant segles, que estan tan arrelades que resulta complicat inclús detectar-les. Són els mites creats que mantenen el sexisme."
    kate_millet "Es tracta de qüestionar-se tot això per no seguir repetint el mateix patró."
    kate_millet "I és que la socialització és tan eficient que no requereix l'ús de la força, exceptuant el cas de violació."
    kate_millet "El patriarcat està tan incrustat en la psicologia de la família i l'educació que l'estructura de caràcter que crea en ambdós sexes és més un hàbit mental i un mode de vida, que un sistema polític."

    simone_de_beauvoir "Exactament. Ser dona, o el concepte de feminitat, és un constructe sociocultural format al llarg de les generacions i és allà on radiquen les causes d'opressió."
    simone_de_beauvoir "Les dones, considerades {i}allò altre{/i} o com esmento en el meu llibre {i}el segon sexe{/i}, són obligades a acceptar la pèrdua d'autonomia i llibertat."
    simone_de_beauvoir "I també a viure vides insatisfactòries i farragoses, ja que se les condiciona per ser éssers dependents dels homes, no subjectes actius com ells."
    simone_de_beauvoir "Concretament, són responsables de les feines més tedioses, de ser mares, i de ser esclaves sexuals."
    simone_de_beauvoir "Al final, la dona es veu a sí mateixa i pren les seves decisions no conforme a la seva naturalesa vertadera, sinó a com la defineix l'home. I aquí radica l'arrel de l'opressió."
    simone_de_beauvoir "Per tant, si bé es consideren els processos biològics de la dona, això no determina que ella tingui un destí fix i inevitable."

    if game_state.witch_is_seen:
        betty_friedan "Sí, i en relació a aquesta part més biològica de la dona, cal esmentar que les dones han de definir elles mateixes la seva pròpia salut."
        betty_friedan "Cal iniciar una revolució contra el control mèdic i masculí sobre les dones, ja que ens mereixem el coneixement i el poder sobre el nostre propi cos."
        betty_friedan "Per exemple, en el cas de l'avortament, existeixen vàries raons per les quals s'hauria de legalitzar."
        betty_friedan "La dona, com a propietària del seu cos i les seves decisions, ha de tenir els mateixos drets que l'home, que no experimenta l'embaràs, i dret a la privacitat."
        betty_friedan "A més a més, el fetus no és considerat persona fins que és viable i l'avortament protegeix les dones mental i físicament."
        betty_friedan "Solament es justifica la seva regulació si existeix un interès imperiós de l'Estat."
        simone_de_beauvoir "Casualment, jo mateixa vaig signar el {i}Manifeste des 343 salopes{/i}, conforme el qual tres-centes quaranta-dues dones més i jo s'autoinculpàvem d'haver avortat quan era il·legal i ens exposàvem a ser criminalment processades."
        betty_friedan "Com es pot observar, el control de la natalitat i els drets de les dones estan molt vinculats."
        betty_friedan "Per aquest motiu, proposem a totes les persones assitents participar segons les instruccions que tenen escrites en el paper que tenen ara mateix a les mans."
    else:
        betty_friedan "En relació a les qüestions relatives al patriarcat en la societat, la llei, l'economia i la violència que pateixen les dones arreu, proposem a totes les persones assitents participar en un petit joc que hem preparat."
        betty_friedan "Les instruccions de participació romanen escrites en el paper que ara mateix tenen a les mans."

    betty_friedan "La idea és trobar, mínim, set diferències, fins a un màxim de deu, entre les dues fotografies que s'hi mostren."
    betty_friedan "Les persones que aconsegueixin trobar-les, hauran d'adreçar-se al mostrador que hi ha al final de la sala perquè tenim un petit obsequi de regal."

    "Quan escoltà això, [tmpSavePlayer] no s'ho pensà més i començà a buscar-les."

    if game_state.nyrw_is_seen:
        $ GiveGlossaryItemToPlayer(31)

    $ GiveGlossaryItemToPlayer(5)
    $ GiveGlossaryItemToPlayer(28)
    $ ShowItems()

    if not game_state.find_differences_done:
        $ renpy.call_in_new_context("find_differences_label")
    else:
        "Ja has trobat almenys set diferències. Vols tornar-ho a intentar?"
        menu:
            "Sí":
                $ renpy.call_in_new_context("find_differences_label")
            "No":
                "D'acord. Continues amb la mateixa història com si les haguessis trobat."

    scene now_conference
    "[tmpSavePlayer] ha resolt correctament l'enigma de les diferències, així que s'apropa al mostrador."
    unknown_girl "Molt bé! Ho ha aconseguit!"
    unknown_girl "Tingui, aquí té el nostre petit obsequi."

    if game_state.witch_is_seen:
        unknown_girl "És el nou número de la revista {i}Our Bodies, Our Selves{/i}."
        unknown_girl "No sé si la coneix, però és una revista que pretén exhibir el tracte sexista i condescendent per part dels metges cap a les dones."
        user "No, no la coneixia. Moltes gràcies per la informació."
    else:
        unknown_girl "És el nou número de la revista sobre feminisme indi, {i}Manushi{/i}."
        user "Moltes gràcies. Molt amable."

    "Així, [tmpSavePlayer] decidí marxar de la sala amb la revista en mà. Ja tenia un entreteniment més pel viatge."

    call end_chapter(CHAPTERS[2])

    return
