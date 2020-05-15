
## Script for the chapter 3.
## This chapter explains the feminism between 1990-1990.

# Backgrounds
image train_station_chpt3 = "images/train/train_station_chpt3.png"
image living_room = "images/chapter3/living_room.png"
image street_chpt3 = "images/chapter3/street.png"
image pib_ticket = "images/chapter3/drag_musical/paris_is_building_ticket.png"
image bll_ticket = "images/chapter3/drag_musical/black_lips_live_ticket.png"
image drag_musical_inside = "images/chapter3/drag_musical/drag_musical_inside.png"
image drag_musical_theatre_morning = "images/chapter3/drag_musical/theatre_morning.png"
image drag_musical_theatre_night = "images/chapter3/drag_musical/theatre_night.png"


# Characters
define julia_serano = Character("Julia Serrano", color="#e53935")
define emi_koyama = Character("Emi Koyama", color="#e53935")
define kate_bornstein = Character("Kate Bornstein", color="#e53935")
define unknown_actress = Character("Actriu", color="#e53935")
define viviane_k_namaste = Character("Viviane K. Namaste", color="#e53935")




label chapter_3:
    ## Train station scene ######################
    scene train_station_chpt3
    play music "audio/sound/train_station.mp3" fadein 0.5

    "El tren acaba d'arribar a l'estació."
    "[tmpSavePlayer] baixa del tren i es dirigeix a la sortida."

    stop music fadeout 0.5
    scene street_chpt3
    play music "audio/music/chapter3.mp3" fadein 0.5

    "Malgrat el cansament del viatge, decideix anar caminant fins a casa seva a descansar."
    "Quan duïa una estona de camí veié una figura familiar que s'apropava ..."

    call ibonne_street

    return


label ibonne_street:
    user "Ibonne !!!"
    user "Quina alegria veure't de nou !!!"
    p_ibonne "Bon dia, [tmpSavePlayer]! Com està?"
    user "Bé, acabo d'arribar de viatge. Vaig cap a casa. I qui és aquest nen tan maco?"
    "[tmpSavePlayer] es dirigia a la persona petita que tenia Ibonne agafada de la mà."
    unknown_little_girl "Sóc una nena ..."
    "Va contestar, molesta."
    user "Ostres, perdona'm ... i com et dius, bonica?"
    unknown_little_girl "Em dic Ivanna."
    user "Molt de gust, Ivanna."
    "Es donaren les mans."
    p_ibonne "Des de ja fa uns dies que es fa dir Ivanna. No vol que li diguem Matt."
    "[tmpSavePlayer] va fer cara estranya. No ho entenia."
    p_ibonne "Sí, al principi és lògic tenir aquesta expressió que té ara a la cara. Però per a mi ja és una qüestió totalment assolida."
    p_ibonne "La meva filla està passant pel mateix que vaig passar jo fa anys."
    p_ibonne "A casa, juga a vestir-se com una nena, es posa perruques, em demana pintallavis i vol pintar-se les ungles constantment de colors diferents."
    p_ibonne "També li agrada jugar a futbol i és una gran fran de Bikini Kill. Coneix el grup de música?"
    user "La veritat és que no ..."
    p_ibonne "Bé, no passa res. El que vull dir és que la meva filla ha començat la transició. Serà poc a poc, però a mi em tindrà sempre per recolzar-la en tot el que faci falta. Serà dur el procés, però jo només vull que sigui feliç."
    user "Sí, el més important és ser feliç. I, també és rellevant sentir-se un còmode i tranquil amb sí mateix."
    p_ibonne "Efectivament. De fet, ara som de camí a la botiga de roba. Vol un vestit per estrenar demà a l'escola, i també m'ha demanat fer-li dues cuetes. Està molt emocionada."
    p_ibonne "I també perquè avui han publicat el Bikini Kill Zine 2 i està impacient per llegir-lo."

    ## Manifiesto Riot Grrrl

    user "Me'n alegro moltíssim de que estigui tan il·lusionada."
    p_ibonne "Gràcies, [tmpSavePlayer]. Per a mi és molt important això que em diu."
    "Ivanna va abraçar a la seva mare. Era evident que per aquella nena, la seva mare era tot un exemple a seguir, plena de valentia i coratge. I també ho era que l'estimava incondicionalment."
    user "Bé doncs, no us entretinc més. Fins aviat!"
    "I, amb una salutació cordial, es varen acomiadar i [tmpSavePlayer] seguí el seu camí."
    "Estava feliç i la reflexió d'aquella conversa anterior li va fer passar el temps volant fins arribar a casa seva."

    call tomorrow_morning

    return


label tomorrow_morning:
    scene living_room
    "..."
    "Un nou dia havia començat."
    "Mentre [tmpSavePlayer] esmorzava, llegia el diari."
    "{i}Rebecca Walker publica 'Becoming the Third Wave' en la revista 'Ms.', després de la confirmació a formar part de la Cort Suprema del jutge Clarence Thomas, acusat d'assetjar sexualment a l'advocada Anita Hill.{i}"
    "{i}L'autora manifesta que la tercera onada del feminisme, una era postfeminista, ja ha començat.{/i}"
    "{i}Estableix que la tercera onada reconeix i s'enfronta al racisme, al classicisme i al sexisme, encara vigents en la societat, ja que per les dones de color i de minories la lluita no havia acabat.{/i}"
    "{i}L'autora rebutja l'opinió estesa de què, en aquesta era postfeminista, la majoria de les joves gaudien d'igualtat amb els homes i que el feminisme ja no era necessari.{/i}"
    "{i}Exposa la impotència que pateixen les dones per aturar l'assetjament sexual, físic i verbal, que les envolta.{/i}"
    "{i}Amb els canvis polítics de caire conservador, les activistes manifesten les seves experiències quotidianes amb la misogínia, el racisme, el classicisme i l'homofòbia, considerades productes del clima polític de l'època.{/i}"
    "{i}D'aquesta manera, la tercera onada reconeix els assoliments de l'anterior onada, però es segueix qüestionant quines dones pertanyien a 'la germanor és poderosa'.{/i}"
    "{i}O el dret de les dones a expressar la seva sexualitat i poder gaudir del sexe. O per què els mitjans de comunicació pretenen celebrar la llibertat de les dones però alhora les sexualitzen per obtenir beneficis.{/i}"
    "..."
    user "Ostres, se'm fa tard ..."
    "[tmpSavePlayer] mirà el rellotge. Les 12:19h. Havia de córrer si volia ser puntual."

    call drag_musical_morning

    return


label drag_musical_morning:
    scene drag_musical_theatre_morning
    "[tmpSavePlayer] acabava d'arribar al teatre."
    "En la sessió familiar, anava a veure {i}Paris is building{/i}, un espectacle de {i}drag queens{/i} d'un dels sectors més implicats en el moviment, com són les persones transgènere."
    scene black
    show pib_ticket at truecenter
    "El guàrdia de seguretat li demanà l'entrada, així que se la tregué de la butxaca i li entregà."
    "Afortunadament, les entrades estaven numerades, així que un cop dins, buscà el seu seient a l'espera de l'inici de la funció."
    "..."
    scene drag_musical_inside
    "Una estona més tard, ja amb el teló alçat i les llums apagades ..."
    julia_serano "Em dic Julia Serrano i sóc una persona transgènere!"
    julia_serano "I us preguntareu per què emfatitzo aquest detall. Doncs bé, perquè vull!"
    julia_serano "Jajaja, és broma, és broma. No se'm despisteu."
    julia_serano "És important perquè avui es parlarà sobre l'absència i la desatenció de les dones trans en el moviment feminista."
    julia_serano "Sobre què significa ser una dona trans en una societat patriarcal i sobre què és una vida trans com a tal."
    julia_serano "Perquè sense el reconeixement de la comunitat trans, de vegades oblidat en el moviment feminista i sempre oblidat en el sistema cisgènere-heteronormatiu i patriarcal, no hi ha justícia."
    "El públic aplaudeix mentre l'actriu es retira i el teló s'abaixa per donar pas a la següent escena."
    "S'alça el teló ..."
    unknown_actress "Mai seràs una dona!! Fas fàstic!!"
    unknown_actress "Quina aberració!!"
    "Un grup d'actrius cridaven insults transfòbics a una altra dona que caminava per l'escenari."
    "Seguidament, aparegué una altra."
    emi_koyama "De segur que alguna vegada t'han insultat pel carrer amb frases com les anteriors ... d'entre un llarg etcètera possible."
    emi_koyama "Resulta obvi que existeix una violència masclista contra les dones trans, de la mateixa manera que existeix la violència masclista contra les dones cigènere."
    emi_koyama "És així perquè totes vivim com a dones. I ser una dona en una societat misògina és perillós perquè alguns factors ens fan més vulnerables quan som onjectius de violència sexual i domèstica."
    emi_koyama "Imaginem-nos per un moment que un home ataca una dona trans amb la finalitat de violar-la, sense saber que ho és. Quan se'n adona de la seva 'anatomia masculina', l'atac pot anar in crescendo impulsat per l'homofòbia i la transfòbia."
    emi_koyama "I aquests casos quasi mai són tractats seriosa o compassivament pels mitjans de comunicació i les autoritats."
    emi_koyama "A més a més, les dones trans són més vulnerables a l'abús emocional i verbal per les seves parelles, ja que acostumen a tenir una autoestima baixa, una imatge corporal negativa, i dificultat per trobar feina."
    kate_bornstein "I són objectius també per ser {i}queer{/i}!"
    kate_bornstein "D'acord. No feu aquesta cara tan estranya. Si no n'heu escoltat mai a parlar, avui serà el primer dia!"
    kate_bornstein "La teoria {i}queer{/i} és un conjunt d'idees que considera sexe i gènere no inscrits en la naturalesa humana, sinó com a construcció social, que varia en cada societat i durant la vida de cada persona."
    kate_bornstein "Hi ha identitats que es constitueixen de forma cultural a través de processos ideològics i segons les normes de cada societat en cada moment."
    kate_bornstein "Per a mi, el gènere no binari mai va ser una opció. A partir de les meves pròpies experiències, vaig poder explorar i questionar-me les normes socials de gènere."
    kate_bornstein "Vaig ser criada com un nen, i castigada i controlada per no conformar-me amb les normes masculines."
    kate_bornstein "Quan vaig poder qüestionar-me el gènere que se'm va assignar al néixer, creia que havia de ser una dona transgènere, però no m'identificava ni com a masculina ni com a femenina."
    kate_bornstein "Així que vaig decidir escriure sobre això per compartir-ho, i aquests escrits varen passar a ser claus per teoritzar el gènere no binari."
    viviane_k_namaste "Però les teòriques {i}queer{/i} formulen hipòtesi sobre les persones transgènere com a simples exemples, sense tenir en compte la crua realitat de les seves vides, com pot ser la vulnerabilitat davant la violència que s'ha comentat abans."
    viviane_k_namaste "De totes maneres, aquesta teoria no es desenvolupa com una afirmació a favor de les identitats marginades, sinó com a crítica a les polítiques identitàries."
    viviane_k_namaste "Es tracta de desestabilitzar les categories d'identitat fixes, sovint limitants, que segueixin la ideologia que considera superior l'heterosexualitat i que estigmatitza l'atracció entre persones del mateix sexe."
    viviane_k_namaste "No obstant això, les teòriques {i}queer{/i} de color critiquen aquesta teoria perquè diuen que únicament està construïda sobre la intersecció amb les persones blanques i la seva problemàtica."
    emi_koyama "Inclús moltes feministes recelen de l'abandonament de la política identitària quan un gran nombre de persones continua patint opressió, desigualtat i violència pel seu gènere o la seva sexualitat."
    julia serrano "És per aquest motiu que enlloc d'aferrar-nos a la divisió entre les feministes cisgènere i les persones trans, hauríem de coalitzar-nos per combatre la transfòbia i la misogínia."
    julia serrano "Les dones trans també patim ambdós tipus de violència. Totes les dones som diferents, però les nostres experiències se solapen."
    emi_koyama "El problema passa perquè les feministes cisgènere exclouen les dones trans per considerar que no saben què és ser dona, i perquè la seva feminitat és ridiculitzada, tant per homes com dones cisgènere."
    julia_serrano "I la feminitat és igual a la masculinitat, igual que les dones són iguals als homes."
    emi_koyama "Tot i que algunes dones trans hagin pogut experimentar el privilegi masculí, també pateixen opressió de diferents maneres, especialment les de color, les pobres i les de classe treballadora."
    emi_koyama "En aquest sentit, hi ha múltiples tipus de privilegi i opressió, i totes les feministes han d'assumir la responsabilitat de les seves formes de privilegi, sense deixar de sentir-se justificades per parlar de la seva experiència de l'opressió."
    emi_koyama "Les feministes també haurien d'assumir la lluita amb la imatge corporal i la disfòria de gènere de les dones trans, és a dir, el patiment corporal pel gènere, qüestió que se sumaria a donar la mateixa consideració a la violència que s'exerceix sobre elles."
    emi_koyama "Existeixen paral·lelismes entre la lluita de les feministes cisgènere per la justícia i el control reproductius, i les campanyes de les dones trans per l'autonomia corporal en l'assitència sanitària."
    "Les actrius es retiraren de l'escenari mentre el teló s'abaixava."

    "..."
    "Una hora més tard ..."
    "La funció acabava de finalitzar."
    user "Ostres, quina funció més impactant. Quina sensació d'espessor amb tanta informació de cop ..."

    return
