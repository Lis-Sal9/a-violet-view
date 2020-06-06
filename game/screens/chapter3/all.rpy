
## Script for the chapter 3.
## This chapter explains the feminism between 1900 and 2010.

# Backgrounds
image train_station_chpt3 = "images/train/train_station_chpt3.png"
image living_room = "images/chapter3/living_room.png"
image street_chpt3 = "images/chapter3/street/street.png"
image street_night_chpt3 = "images/chapter3/street/street_night.png"
image pib_ticket = "images/chapter3/drag_musical/paris_is_building_ticket.png"
image bll_ticket = "images/chapter3/drag_musical/black_lips_live_ticket.png"
image drag_musical_inside = "images/chapter3/drag_musical/drag_musical_inside.png"
image drag_musical_inside_night = "images/chapter3/drag_musical/drag_musical_inside_night.png"
image drag_musical_theatre_morning = "images/chapter3/drag_musical/theatre_morning.png"
image drag_musical_theatre_night = "images/chapter3/drag_musical/theatre_night.png"
image ong_session = "images/chapter3/ong/ong_session.png"
image ong_garden = "images/chapter3/ong/ong_garden.png"
image bus_stop = "images/chapter3/bus/bus_stop.png"
image restaurant_lis = "images/chapter3/restaurant.png"
image pole_academy = "images/chapter3/pole_academy.png"
image wfwi = "images/chapter3/wfwi/wfwi.png"
image wfwi_inside = "images/chapter3/wfwi/wfwi_inside.png"
image serie1 = "images/chapter3/series/serie1.png"
image serie2 = "images/chapter3/series/serie2.png"
image serie3 = "images/chapter3/series/serie3.png"
image email_susan = "images/chapter3/series/mail.png"


# Characters
define julia_serano = Character("Julia Serano", color="#e53935")
define emi_koyama = Character("Emi Koyama", color="#ff5c8d")
define kate_bornstein = Character("Kate Bornstein", color="#280680")
define unknown_actress = Character("Actriu", color="#6f74dd")
define viviane_k_namaste = Character("Viviane K. Namaste", color="#1e88e5")
define rosemary_garland_thomson = Character("Rosemarie Garland-Thomson", color="#006db3")
define jenny_morris = Character("Jenny Morris", color="#00897b")
define zainab_salbi = Character("Zainab Salbi", color="#00701a")
define waris_dirie = Character("Waris Dirie", color="#7cb342")
define loretta_ross = Character("Loretta Ross", color="#8c9900")
define judith_butler = Character("Judith Butler", color="#c6a700")
define michel_foucault = Character("Michel Foucault", color="#c68400")
define eve_kosofsky_sedgwick = Character("Eve Kosofsky Sedgwick", color="#fb8c00")
define lisbeth_polancer = Character("Lisbeth Polancer", color="#b91400")
define susan_faludi = Character("Susan Faludi", color="#6d4c41")
define alicia_miyares = Character("Alicia Miyares", color="#757575")

# Character images
image ibonne_child_pic = "images/chapter3/characters/ibonne_child.png"
image julia_serano_pic = "images/chapter3/characters/julia_serano.png"
image emi_koyama_pic = "images/chapter3/characters/emy_koyama.png"
image kate_bornstein_pic = "images/chapter3/characters/kate_bornstein.png"
image viviane_k_namaste_pic = "images/chapter3/characters/viviane_k_namaste.png"
image rosemarie_garland_thomson_pic = "images/chapter3/characters/rosemarie_garland_thomson.png"
image jenny_morris_pic = "images/chapter3/characters/jenny_morris.png"
image lisbeth_polancer_pic = "images/chapter3/characters/lisbeth_polancer.png"
image loretta_ross_pic = "images/chapter3/characters/loretta_ross.png"
image susan_faludi_pic = "images/chapter3/characters/susan_faludi.png"
image susan_faludi_black_pic = "images/chapter3/characters/susan_faludi_black.png"
image waris_dirie_pic = "images/chapter3/characters/waris_dirie.png"
image zainab_salbi_pic = "images/chapter3/characters/zainab_salbi.png"
image lila_abulughod_pic = "images/chapter3/characters/lila_abulughod.png"
image musawah_pic = "images/chapter3/characters/musawah.png"
image judith_butler_pic = "images/chapter3/characters/judith_butler.png"
image michel_foucault_pic = "images/chapter3/characters/michel_foucault.png"
image alicia_miyares_pic = "images/chapter3/characters/alicia_miyares.png"
image eve_kosofsky_sedgwick_pic = "images/chapter3/characters/eve_kosofsky_sedgwick.png"



label chapter_3:
    call new_day
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
    show ibonne_child_pic at truecenter
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
    p_ibonne "A més a més, venim de comprar el Bikini Kill Zine 2 i està impacient per llegir-la. N'hem comprat dues, tingui una."

    $ GiveGlossaryItemToPlayer(35)

    scene serie1
    "Ibonne li va donar la revista a [tmpSavePlayer], que la va fullejar i es va trobar amb una sèrie matemàtica una mica peculiar."
    hide ibonne_child_pic


    scene street_chpt3
    user "Me'n alegro moltíssim de que estigui tan il·lusionada."
    show ibonne_child_pic at truecenter
    p_ibonne "Gràcies, [tmpSavePlayer]. Per a mi és molt important això que em diu."
    "Ivanna va abraçar a la seva mare. Era evident que per aquella nena, la seva mare era tot un exemple a seguir, plena de valentia i coratge. I també ho era que l'estimava incondicionalment."
    user "Bé doncs, no us entretinc més. Fins aviat!"
    "I, amb una salutació cordial, es varen acomiadar i [tmpSavePlayer] seguí el seu camí."
    hide ibonne_child_pic
    "Estava feliç i la reflexió d'aquella conversa anterior li va fer passar el temps volant fins arribar a casa seva."

    call tomorrow_morning

    return


label tomorrow_morning:
    call other_day
    call new_day
    "Un nou dia havia començat."
    scene living_room
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

    stop music fadeout 0.5
    play music "audio/sound/ring.mp3" fadein 0.5

    $ GiveGlossaryItemToPlayer(35)
    menu:
        "Agafes el telèfon":
            stop music fadeout 0.5
            play music "audio/music/chapter3.mp3" fadein 0.5
            $ game_state.answer_phone = True
            user "Digui?"
            rosemary_garland_thomson "[tmpSavePlayer]!! Què fas encara a casa??"
            user "Rosemary, ets tu?"
            rosemary_garland_thomson "És clar que sóc jo!! Fa mitja hora que t'estem esperant a l'ONG!!"
            user "Com que mitja hora?? Però no havia de ser-hi a l'hora de dinar??"
            rosemary_garland_thomson "No, no recordes que abans venia la senyora Morris a parlar del model social de la discapacitat?"
            user "Ostres, pensava que era l'endemà ... Em sap greu, em vesteixo ràpid i vaig. En breu hi sóc."
            "Així, [tmpSavePlayer] deixà l'esmorzar i el diari a mitges, es vestí i sortí ràpidament de casa."
            call ong

        "Deixes sonar el telèfon":
            $ game_state.answer_phone = False
            user "Ostres, se'm fa tard ..."
            "[tmpSavePlayer] mirà el rellotge. Les 12:19h. Havia de córrer si volia ser puntual."
            stop music fadeout 0.5
            play music "audio/music/chapter3.mp3" fadein 0.5
            call drag_musical_morning

    return


label drag_musical_morning:
    scene drag_musical_theatre_morning
    "[tmpSavePlayer] acabava d'arribar al teatre."
    "En la sessió familiar, anava a veure {i}Paris is building{/i}, un espectacle de {i}drag queens{/i} d'un dels sectors més implicats en el moviment, com són les persones transgènere."
    scene black
    show pib_ticket at truecenter
    "El guàrdia de seguretat li va fer entrega d'una revista publicitària de l'obra i li demanà l'entrada, així que se la tregué de la butxaca i li donà."
    "Afortunadament, les entrades estaven numerades, així que un cop dins, buscà el seu seient a l'espera de l'inici de la funció."
    scene serie2
    "[tmpSavePlayer] aprofità aquell temps mort per fullejar la revista quan va adonar-se d'una sèrie matemàtica una mica peculiar."

    call curtain_up_inside

    "Una estona més tard, ja amb el teló alçat i les llums apagades ..."
    scene drag_musical_inside
    show julia_serano_pic at truecenter
    julia_serano "Em dic Julia Serano i sóc una persona transgènere!"
    julia_serano "I us preguntareu per què emfatitzo aquest detall. Doncs bé, perquè vull!"
    julia_serano "Jajaja, és broma, és broma. No se'm despisteu."
    julia_serano "És important perquè avui es parlarà sobre l'absència i la desatenció de les dones trans en el moviment feminista."
    julia_serano "Sobre què significa ser una dona trans en una societat patriarcal i sobre què és una vida trans com a tal."
    julia_serano "Perquè sense el reconeixement de la comunitat trans, de vegades oblidat en el moviment feminista i sempre oblidat en el sistema cisgènere-heteronormatiu i patriarcal, no hi ha justícia."
    hide julia_serano_pic
    call curtain_down_inside
    "El públic aplaudeix mentre l'actriu es retira i el teló s'abaixa per donar pas a la següent escena."
    "S'alça el teló ..."
    call curtain_up_inside

    unknown_actress "Mai seràs una dona!! Fas fàstic!!"
    unknown_actress "Quina aberració!!"
    "Un grup d'actrius cridaven insults transfòbics a una altra dona que caminava per l'escenari."
    "Seguidament, aparegué una altra."
    show emi_koyama_pic at truecenter
    emi_koyama "De segur que alguna vegada t'han insultat pel carrer amb frases com les anteriors ... d'entre un llarg etcètera possible."
    emi_koyama "Resulta obvi que existeix una violència masclista contra les dones trans, de la mateixa manera que existeix la violència masclista contra les dones cigènere."
    emi_koyama "És així perquè totes vivim com a dones. I ser una dona en una societat misògina és perillós perquè alguns factors ens fan més vulnerables quan som onjectius de violència sexual i domèstica."
    emi_koyama "Imaginem-nos per un moment que un home ataca una dona trans amb la finalitat de violar-la, sense saber que ho és. Quan se'n adona de la seva 'anatomia masculina', l'atac pot anar in crescendo impulsat per l'homofòbia i la transfòbia."
    emi_koyama "I aquests casos quasi mai són tractats seriosa o compassivament pels mitjans de comunicació i les autoritats."
    emi_koyama "A més a més, les dones trans són més vulnerables a l'abús emocional i verbal per les seves parelles, ja que acostumen a tenir una autoestima baixa, una imatge corporal negativa, i dificultat per trobar feina."
    hide emi_koyama_pic
    show kate_bornstein_pic at truecenter
    kate_bornstein "I són objectius també per ser {i}queer{/i}!"
    kate_bornstein "D'acord. No feu aquesta cara tan estranya. Si no n'heu escoltat mai a parlar, avui serà el primer dia!"
    kate_bornstein "La teoria {i}queer{/i} és un conjunt d'idees que considera sexe i gènere no inscrits en la naturalesa humana, sinó com a construcció social, que varia en cada societat i durant la vida de cada persona."
    kate_bornstein "Hi ha identitats que es constitueixen de forma cultural a través de processos ideològics i segons les normes de cada societat en cada moment."
    kate_bornstein "Per a mi, el gènere no binari mai va ser una opció. A partir de les meves pròpies experiències, vaig poder explorar i questionar-me les normes socials de gènere."
    kate_bornstein "Vaig ser criada com un nen, i castigada i controlada per no conformar-me amb les normes masculines."
    kate_bornstein "Quan vaig poder qüestionar-me el gènere que se'm va assignar al néixer, creia que havia de ser una dona transgènere, però no m'identificava ni com a masculina ni com a femenina."
    kate_bornstein "Així que vaig decidir escriure sobre això per compartir-ho, i aquests escrits varen passar a ser claus per teoritzar el gènere no binari."
    hide kate_bornstein_pic
    show viviane_k_namaste_pic at truecenter
    viviane_k_namaste "Però les teòriques {i}queer{/i} formulen hipòtesi sobre les persones transgènere com a simples exemples, sense tenir en compte la crua realitat de les seves vides, com pot ser la vulnerabilitat davant la violència que s'ha comentat abans."
    viviane_k_namaste "De totes maneres, aquesta teoria no es desenvolupa com una afirmació a favor de les identitats marginades, sinó com a crítica a les polítiques identitàries."
    viviane_k_namaste "Es tracta de desestabilitzar les categories d'identitat fixes, sovint limitants, que segueixin la ideologia que considera superior l'heterosexualitat i que estigmatitza l'atracció entre persones del mateix sexe."
    viviane_k_namaste "No obstant això, les teòriques {i}queer{/i} de color critiquen aquesta teoria perquè diuen que únicament està construïda sobre la intersecció amb les persones blanques i la seva problemàtica."
    hide viviane_k_namaste_pic
    show emi_koyama_pic at left
    emi_koyama "Inclús moltes feministes recelen de l'abandonament de la política identitària quan un gran nombre de persones continua patint opressió, desigualtat i violència pel seu gènere o la seva sexualitat."
    show julia_serano_pic at right
    julia_serano "És per aquest motiu que enlloc d'aferrar-nos a la divisió entre les feministes cisgènere i les persones trans, hauríem de coalitzar-nos per combatre la transfòbia i la misogínia."
    julia_serano "Les dones trans també patim ambdós tipus de violència. Totes les dones som diferents, però les nostres experiències se solapen."
    emi_koyama "El problema passa perquè les feministes cisgènere exclouen les dones trans per considerar que no saben què és ser dona, i perquè la seva feminitat és ridiculitzada, tant per homes com dones cisgènere."
    julia_serano "I la feminitat és igual a la masculinitat, igual que les dones són iguals als homes."
    emi_koyama "Tot i que algunes dones trans hagin pogut experimentar el privilegi masculí, també pateixen opressió de diferents maneres, especialment les de color, les pobres i les de classe treballadora."
    emi_koyama "En aquest sentit, hi ha múltiples tipus de privilegi i opressió, i totes les feministes han d'assumir la responsabilitat de les seves formes de privilegi, sense deixar de sentir-se justificades per parlar de la seva experiència de l'opressió."
    emi_koyama "Les feministes també haurien d'assumir la lluita amb la imatge corporal i la disfòria de gènere de les dones trans, és a dir, el patiment corporal pel gènere, qüestió que se sumaria a donar la mateixa consideració a la violència que s'exerceix sobre elles."
    emi_koyama "Existeixen paral·lelismes entre la lluita de les feministes cisgènere per la justícia i el control reproductius, i les campanyes de les dones trans per l'autonomia corporal en l'assitència sanitària."
    hide julia_serano_pic
    hide emi_koyama_pic
    "Les actrius es retiraren de l'escenari mentre el teló s'abaixava."

    call curtain_down_inside

    "Una hora més tard ..."
    "La funció acabava de finalitzar."
    user "Ostres, quina funció més impactant. Quina sensació d'espessor amb tanta informació de cop ..."
    user "Aniré passejant fins la parada d'autobús ..."

    scene bus_stop
    "Al cap de deu minuts ..."
    user "Ostres, ja hi tornem a ser amb la publicitat enganyosa sobre la bellesa ..."

    $ GiveGlossaryItemToPlayer(30)

    "A la parada de l'autobús, hi havia una fotografia d'una noia vestida amb llenceria fina."
    "L'autobús acabava d'arribar i [tmpSavePlayer] pujà."

    call moving_bus
    call wfwi_foundation

    return


label ong:
    scene ong_session
    "Al cap d'una estona, [tmpSavePlayer] va arribar a l'ONG."
    "Rosemary estava neguitosa. Al veure a [tmpSavePlayer], li va fer senyals perquè s'apropés el més ràpid possible on era ella."
    show rosemarie_garland_thomson_pic at right
    rosemary_garland_thomson "Per fi!! Hem intentat allargar el màxim possible l'espera per a què no et perdessis cap detall."
    user "Moltíssimes gràcies. T'ho agraeixo molt."
    hide rosemarie_garland_thomson_pic
    "Rosemary va fer senyals a la senyora Morris, i aquesta començà a parlar."
    show jenny_morris_pic at left
    jenny_morris "Benvolgudes a totes! Em dic Jenny Morris, i avui us parlaré sobre el {i}model social de la discapacitat{/i} i les dones."
    jenny_morris "El model social té una forta base reivindicativa que pretén la revisió de les definicions que s'han fet del què és i què no és la {i}discapacitat{/i} i de la seva construcció."
    jenny_morris "En el meu llibre {i}Pride Against Prejudice{/i} exposo el {i}doble inconvenient{/i} que suposa ser dona i ser {i}discapacitada{/i}."
    jenny_morris "Aquestes dones són objectualitzades perquè no es tenen en compte les seves experiències personals i perquè es limiten a intentar discernir què és 'pitjor' per les oportunitats de vida d'una dona."
    jenny_morris "De res val la pena si l'enfocament sobre les barreres externes ignora l'experiència del cos i altres aspectes importants, com els drets reproductius de les dones i la vida del fetus físicament impedit."
    jenny_morris "D'aquesta manera, les dones {i}discapacitades{/i} tenen dificultats per fer-se escoltar, ja sigui en el moviment feminista o en el moviment de {i}discapacitats{/i}."
    jenny_morris "Són justament les polítiques socials, a priori destinades a ajudar, les que acaben reforçant la dependència produïda per les estructures econòmiques i culturals."
    jenny_morris "És a dir, en aquesta situació la persona amb {i}discapacitat{/i} és representada com una persona dependent."
    jenny_morris "Però les defensores del feminisme de la {i}discapacitat{/i} i del model social mantenen que el gènere i la {i}discapacitat{/i} són creacions socials, i que l'eliminació de les barreres creades per la societat permetrà a les persones {i}discapacitades{/i} aconseguir la igualtat."
    hide jenny_morris_pic
    show rosemarie_garland_thomson_pic at right
    rosemary_garland_thomson "De fet, mitjançant l'ús del llenguatge el constructe social de la {i}discapacitat{/i} s'hauria d'evitar relacionar amb la paraula 'impediment' per descriure-la, ja que així s'oprimeix a aquestes persones per deficients, sent les persones {i}no discapacitades{/i} superiors."
    rosemary_garland_thomson "És necessari emfatitzar la importància del reconeixement de les diferències dins de la {i}discapacitat{/i} i les categories socials o culturals paral·leles a aquesta (gènere, raça, classe, sexualitat), ja que totes s'entrecreuen i són presents en la societat."
    rosemary_garland_thomson "I, dit això, ja podem donar per conclusa aquesta breu xerrada. Oferim a la senyora Morris un fort aplaudiment."
    hide rosemarie_garland_thomson_pic
    "Totes les persones assistents varen aplaudir."
    scene ong_garden
    show rosemarie_garland_thomson_pic at truecenter
    rosemary_garland_thomson "Poc a poc, podem anar al jardí. Hem preparat un petit dinar de germanor."
    rosemary_garland_thomson "Espera! Has vist el diari d'avui? Mira què interessant ..."
    hide rosemarie_garland_thomson_pic
    "[tmpSavePlayer] va observar el diari que no havia pogut acabar de llegir de bon matí i va veure una sèrie matemàtica molt curiosa."

    scene serie2

    "Fins tard, [tmpSavePlayer] es va quedar a l'ONG cuidant i jugant amb totes aquelles persones especials."

    call date_with_lis

    return


label date_with_lis:
    scene pole_academy
    "Al vespre, [tmpSavePlayer] tenia una cita."
    "Per donar-li una sorpresa, va apropar-se a l'acadèmia de pole dance on era fent classe la Lisbeth, la seva amiga."
    ## Vídeo gif
    "A l'entrar dins de l'acadèmia, la va veure allà, {i}fent el mico{/i}, com li agradava dir a ella. Lluïnt."
    "Uns minuts més tard, la classe va finalitzar i ella va apropar-se."
    show lisbeth_polancer_pic at truecenter
    lisbeth_polancer "Ei, [tmpSavePlayer]!!! Com estàs??"
    "Li va dir mentre l'abraçava."
    lisbeth_polancer "Anem a sopar!! Tinc una gana que em moro!!"
    hide lisbeth_polancer_pic
    scene restaurant_lis
    "Així que varen anar a sopar al seu restaurant xinès preferit. Ja havien perdut el compte de quantes vegades hi havien anat a menjar."
    show lisbeth_polancer_pic at truecenter
    lisbeth_polancer "Saps què? Avui hem tingut una classe de pole una mica filosòfica."
    user "Ui, aquest to irònic em fa tremolar ..."
    "La Lisbeth va somriure emmurriament."
    lisbeth_polancer "Una de les noies no parava de fer-se fotografies sense prestar atenció a la professora per enviar-se-les al seu nuvi. Tu creus?"
    lisbeth_polancer "Jo li he fet saber que per a mi ha estat una falta de respecte brutal cap a la professora, tot i que ja coneixes les meves formes. Però no he estat la única."
    lisbeth_polancer "Ariel Levy, aquella companya meva feminista, li ha dit que, com a jove que és, participava en l'objectualització social de sí mateixa i de les altres noies amb el que estava fent."
    lisbeth_polancer "Li ha dit que el seu comportament {i}raunchy{/i} no estava basat en els seus propis desitjos, sinó en un intent d'atraure al seu home, i als homes en general."
    lisbeth_polancer "Que aquesta caricatura de la sexualitat femenina, tal com l'ha anomenada, és perjudicial perquè espera d'ella que tingui aquesta actitud per ser considerada atractiva i alliberada, i no ser una estreta o una retrògrada."
    lisbeth_polancer "Li ha dit que fent això només busca una {i}llibertat{/i} sexual desencaminada i perjudicial que promou els interessos de la cultura misògina. Que l'objectualització sexual existeix i que un exemple era allò que estava fent ella."
    lisbeth_polancer "Llavors, la professora ha posat una mica d'ordre i hem pogut continuar la classe, per sort, tot i que aquella noia ha marxat força enfurismada poca estona després."
    lisbeth_polancer "Em fa molta ràbia que les noies es deixin manipular per aquests pallassos i que acabin fent allò que desitgen ells i no el que elles desitgen."
    lisbeth_polancer "Ja saps que parlo per pròpia experiència. Fa temps que penso que inclús les persones bisexuals com jo hauríem de renunciar als homes. Al final, resultarà que les lesbianes de la segona onada del feminisme tindran raó en això."
    hide lisbeth_polancer_pic
    "Amb aquesta conversa tan efusiva i detallada, varen passar hores. No obstant això, de matinada, [tmpSavePlayer] tenia una cita i volia ser puntual."
    "D'aquesta manera, s'acomiadaren amb una forta abraçada fins una altra."
    "Per a [tmpSavePlayer], Lisbeth era una persona meravellosa i sempre que estava amb ella sortia amb les piles renovades."
    "Feliç, caminava fins al teatre."

    call drag_musical_night

    return


label wfwi_foundation:
    "[tmpSavePlayer] baixà a la seva parada. Avui va a fer voluntariat a {i}Women for Women International{/i}."
    scene wfwi
    "WFWI és una organització humanitària sense ànim de lucre que proporciona suport pràctic i emocional a les dones supervivents de la guerra."
    "Zainab Salbi, la seva fundadora, va iniciar aquest projecte quan va conèixer l'existència dels 'camps de violacions' en la guerra de Bòsnia. De petita, va tenir experiència amb la violència."
    "Ella defensa que l'ajuda a les dones en zones de guerra ha de ser més que un simple recolzament material, i que solament reforçant el paper de les dones en els processos de pau s'aconseguirà un canvi real."
    "Avui, havia congregat una sèrie de companyes d'altres organitzacions amb la finalitat de celebrar l'èxit del Pla d'Acció a la IV Conferència Mundial de Dones de les Nacions Unides."
    "Malgrat el Vaticà i alguns estats musulmans estiguessin en contra, es reconegueren per primera vegada els drets de les dones com a drets humans."
    "Concretament, els drets bàsics de les dones de tot el món, a controlar la seva pròpia sexualitat i el procés reproductiu i, a tenir accés a la mateixa educació i crèdits bancaris."
    "A més a més, es denunciaren els delictes de mutilació genital femenina, declarat dos anys enrere com una forma de violència contra les dones, i el maltractament de dones a casa i al carrer."
    scene wfwi_inside
    show zainab_salbi_pic at truecenter
    zainab_salbi "Hola, [tmpSavePlayer]! Com estàs?"
    user "Bona tarda, Zainab. Tot bé. És una alegria la notícia. Ha reunit a moltes persones avui."
    zainab_salbi "Sí, avui és un dia per celebrar. Estic molt emocionada."
    "Zainab abraçà a [tmpSavePlayer]."
    zainab_salbi "Bé, ves a donar una volta per aquí, que a mi m'ha entrat una brosseta a l'ull."
    "Digué Zainab mentre s'eixugava una petita llàgrima que queia per la seva galta. I es retirà."
    hide zainab_salbi_pic

    $ GiveGlossaryItemToPlayer(30)

    menu:
        "Tant de disgust t'ha fet entrar gana":
            $ game_state.serie_with_susan = False
            "Es dirigí a la zona de menjar, i allà escoltà sense voler la conversa de dues dones que alçaven una mica la veu."
            show lila_abulughod_pic at left
            unknown_girl "Estic farta de que la noció occidental culpi la religió per la desigualtat de gènere argumentant que la probresa i l'autoritarisme són les causes clau de la falta de llibertat de les dones en les societats islàmiques."
            unknown_girl "El feminisme occidental acostuma a menysprear l'islam com a inherentment hostil a la dona, i això no és així."
            unknown_girl "Si jo porto el {i}hiyab{/i} és per pròpia elecció, igual que moltes altres dones musulmanes, i crec fermament en què l'islam encarna els nostres drets humans bàsics."
            unknown_girl "Ja ho sé, Lila, però no tothom creu en la certesa del mateix."
            "Es referia a Lila Abu-Lughod."
            show musawah_pic at right
            unknown_girl "Et convido a la nostra organització, {i}Musawah{/i}, que, com bé ja sabràs, significa igualtat en àrab."
            unknown_girl "Aquesta organització està dirigida per dones amb la finalitat de promoure la justícia i la igualtat en l'islam."
            unknown_girl "Considerem que homes i dones són essencialment iguals i que l'Alcorà és inherentment favorable a les dones, però ha estat interpretat de forma misògina pel patriarcat."
            unknown_girl "El nostre objectiu és desenvolupar i compartir coneixements sobre igualtat i justícia en la família, ajudar a crear organitzacions similars, i recolzar a grups pro drets humans amb objectius similars al nostre."
            unknown_girl "Pel que em comentes, penso que et podria anar força bé venir algun dia per a què puguis compartir la teva opinió."
            "Lila assentí amb el cap."
            hide lila_abulughod_pic
            hide musawah_pic
            "L'aclaparament va envair a [tmpSavePlayer], i va decidir marxar perquè s'estava atabalant amb tanta gent en tants pocs metres quadrats."
            "Necessitava descansar la ment una mica, així que tornà a casa caminant."
            "Ja a casa descansant ..."
            call go_to_concert

        "L'angoixa t'ha tancat l'estómac i decideixes passejar una mica per la sala":
            $ game_state.serie_with_susan = False
            "Passejant per la sala, s'adonà de que l'autora Waris Dirie estava fent la presentació de la seva autobiografia, {i}Desert Flower{/i}."
            show waris_dirie_pic at right
            waris_dirie "Als tres anys, vaig ser mutilada genitalment. I als tretze, vaig ser lliurada a un home molt major per a casar-m'hi. Per sort, vaig poder aconseguir fugir d'aquella vida miserable."
            waris_dirie "En aquesta autobiografia parlo de la mutilació genital femenina."
            waris_dirie "Aquesta, no és específica de cap religió o grup ètnic, sinó que està associada a nocions de puresa i castedat, a una forma de control dels impulsos sexuals, i a garantir la virginitat fins el matrimoni i la seva posterior fidelitat."
            waris_dirie "Òbviament, els danys que causa són permanents i, a més a més, en molts casos no hi ha cap altra opció possible. Aquestes qüestions converteixen a la mutilació genital femenina en una violació dels drets humans."
            hide waris_dirie_pic
            "[tmpSavePlayer] s'estava començant a trobar pitjor. Entre l'angoixa prèvia i ara haver escoltat a la senyora Dirie ..."
            "No obstant això, decidí fer un petit esforç i quedar-s'hi una estona més."
            "Mentre seguia passejant per la sala, una dona l'aturà. En la seva enganxina hi havia escrit el nom 'Loretta Ross'."
            show loretta_ross_pic at truecenter
            loretta_ross "Bon dia, tingui! Em dic Loretta Ross. Estic divulgant informació sobre la meva organització, {i}SisterSong{/i}."
            loretta_ross "Aquesta organització preté lluitar per l'assistència sanitària familiar per les dones pobres."
            loretta_ross "En cas que volgués col·laborar amb nosaltres, li deixo aquest tríptic amb més informació. Moltes gràcies per la seva atenció."
            hide loretta_ross_pic
            "[tmpSavePlayer] assentí i, mentre Loretta seguia passejant per la sala, va llegir el tríptic."
            "{i}Jo, Loretta Ross, denuncio la situació de les dones pobres, sobretot les de color, que tenen poques de les opcions d'assitència mèdica disponibles per a les més acomodades.{/i}"
            "{i}Exigeixo justícia reproductiva per les dones, és a dir, els diferents drets a la maternitat que poden exercir les dones de diferents races i classes socials{/i}."
            user "Uff ... què malament em sento ... he d'anar cap a casa, necessito descansar ..."
            "Així, amb el tríptic a mig llegir a la mà, va decidir agafar l'autobús per arribar més ràpid a casa."
            call moving_bus
            "Ja a casa descansant ..."
            call go_to_concert

        "Decideixes marxar perquè se t'ha quedat mal cos i ningú se'n adonarà de la teva absència":
            "[tmpSavePlayer] té un malestar general, produït per l'emoció d'aquell munt de persones reunit per aquell motiu."
            "Decideix marxar perquè no se sent bé, i creu que ningú se'n adonarà que no hi és."
            "Però quan era a punt de sortir per la porta, sent una veu que crida ..."
            show susan_faludi_black_pic at truecenter
            unknown "[tmpSavePlayer], ets tu?"
            hide susan_faludi_black_pic

            menu:
                "Et gires, tens curiositat":
                    show susan_faludi_pic at truecenter
                    "[tmpSavePlayer] es girà i la veié. Bonica i amb un somriure com sempre."
                    user "Susan!!! Oh, Susy!!!"
                    "I es van abraçar."
                    user "Com estàs? Et veig molt maca."
                    susan_faludi "Gràcies. Estic molt feliç. Fa uns dies que acabo de guanyar el Premi Pulitzer pel reportatge divulgatiu que vaig realitzar."
                    user "Moltíssimes felicitats!! No en sabia res!!"
                    susan_faludi "Moltes gràcies. Justament, ara vaig a fer una petita xerrada al respecte. Només he passat per aquí per celebrar la notícia d'avui amb les companyes."
                    susan_faludi "Mira, et dóno aquest tríptic sobre la xerrada, per si t'interessa."
                    susan_faludi "Si et sembla bé, et trucaré per fer un cafè un dia d'aquests i parlem més tranquil·lament. Ara me'n he d'anar."

                    $ game_state.serie_with_susan = True
                    $ GiveGlossaryItemToPlayer(41)

                    user "Perfecte, Susan. Quedem així doncs."
                    hide susan_faludi_pic
                    scene street_chpt3
                    "I, amb un comiat efusiu, Susan marxava a la seva xerrada i [tmpSavePlayer] tornava cap a casa seva, aquest cop passejant."
                    "Mentre caminava, va fullejar el tríptic i es va adonar que hi havia una sèrie matemàtica una mica peculiar."

                    scene serie3

                    "A l'arribar a casa, necessitava relaxar-se, així que es banyà i es posà a dormir per descansar el cap fins l'endemà."
                    call go_to_hungary

                "Ignores la veu, no et trobes bé i no tens ganes de fer bona cara":
                    $ game_state.serie_with_susan = False
                    "[tmpSavePlayer] va fer com si no hagués escoltat res i seguí el seu camí cap a casa. Tornava a agafar l'autobús perquè volia arribar el més aviat possible."
                    call moving_bus
                    "Ja a casa descansant ..."
                    call go_to_concert

    return


label go_to_concert:
    scene living_room
    user "Quina raó tenia la petita Ivanna. Aquest grup és fantàstic!"
    "[tmpSavePlayer] s'havia aficionat a escoltar Bikini Kill. Tant era així, que va decidir que agafaria un tren per anar a veure-les cantar en directe a la província del costat."
    call other_day
    call new_day
    "I, així va ser com dies després, anà a l'estació de tren."

    call train
    call end_chapter(CHAPTERS[5])

    return


label go_to_hungary:
    scene living_room
    "Ja era de dia ..."
    "[tmpSavePlayer] s'acaba de llevar quan, de sobte ..."
    stop music fadeout 0.5
    play music "audio/sound/ring.mp3" fadein 0.5
    "El telèfon estava sonant."
    "[tmpSavePlayer] atengué."
    stop music fadeout 0.5
    play music "audio/music/chapter3.mp3" fadein 0.5
    susan_faludi "[tmpSavePlayer]!! Sóc la Susan!! He de parlar amb tu!! Necessito mostrar-te una cosa molt estranya!!"
    user "És massa d'hora encara. Tan urgent és?"
    susan_faludi "Sí!! Sí!! Ara vinc a casa teva!!"
    "I penja. [tmpSavePlayer] no va poder dir paraula, solament anar a vestir-se."
    "Al cap de mitja hora, Susan aparegué."
    show susan_faludi_pic at truecenter
    susan_faludi "Obre l'ordinador!! Corre!!!"
    "Susan va entrar a casa de [tmpSavePlayer] molt agitada."
    user "Però què et passa? Per a què necessites el meu ordinador?"
    susan_faludi "No hi ha temps per explicacions. Corre, el temps és or!!"
    "Amb presses, encengueren l'ordinador. Susan va entrar al seu servidor de correu electrònic."
    susan_faludi "Mira, això és el què et volia ensenyar!! El meu pare m'ha enviat aquest correu tan estrany. Què deuen voler dir aquests símbols?!"
    hide susan_faludi_pic
    scene email_susan
    "[tmpSavePlayer] els mirà atentament. D'algun lloc li sonaven, però no aconseguia recordar d'on."
    susan_faludi "Sempre li ha agradat molt al meu pare amagar missatges. I a mi em posa molt nerviosa!!!"
    user "Ja ho tinc!!! No sabia de què em sonaven, però ara ja me'n he recordat. Espera."
    "Va anar a buscar els papers que s'havia trobat el darrer dia."

    if game_state.serie_with_susan:
        user "Mira, això em vaig trobar!! I també està el tríptic que tu em vas donar!!"
        susan_faludi "El que jo et vaig donar? ... Ah, sí!! El tríptic de la xerrada!! Ni m'hi havia fixat en els símbols ..."
        user "És igual això ara, no importa. Podrien estar tots els papers relacionats ... Anem a descobrir-ho!"
    else:
        user "Mira, això em vaig trobar!! Podrien estar tots relacionats ... Anem a descobrir-ho!"

    if not game_state.series_done:
        # series is not done
        $ renpy.call_in_new_context("series_label")
    else:
        # series is done
        "Ja has resolt les sèries. Vols tornar-les a fer?"
        menu:
            "Sí":
                $ renpy.call_in_new_context("series_label")
            "No":
                "D'acord. Continues amb la mateixa història com si les haguessis fet."

    call series_result

    return



label drag_musical_night:
    scene drag_musical_theatre_night
    "[tmpSavePlayer] acabava d'arribar al teatre."
    "En la sessió de les golfes, anava a veure {i}Black Lips Live{/i}, un espectacle de {i}drag queens{/i} gòtics que parlaven del gènere i la teoria {i}queer{/i}."
    scene black
    show bll_ticket at truecenter
    "El guàrdia de seguretat li va fer entrega d'una revista publicitària de l'obra i li demanà l'entrada, així que se la tregué de la butxaca i li donà."
    "Afortunadament, les entrades estaven numerades, així que un cop dins, buscà el seu seient a l'espera de l'inici de la funció."
    "[tmpSavePlayer] aprofità aquell temps mort per fullejar la revista quan va adonar-se d'una sèrie matemàtica una mica peculiar."

    scene serie3

    "Les 00:19 ..."

    call curtain_up_night

    "El teló s'alça i les llums s'apaguen ..."

    scene drag_musical_inside_night

    show judith_butler_pic at truecenter
    judith_butler "Em dic Judith Butler i us presentaré el gènere en disputa."
    judith_butler "Debatrem, farem intercanvi d'opinions i, si cal, discutirem sobre el concepte."
    judith_butler "Començaré dient que el gènere no és una identitat estable, sinó una dèbilment constituïda en el temps, instituïda en un espai exterior mitjançant una repetició estilitzada d'actes. És a dir, el gènere és una temporalitat social constituïda."
    hide judith_butler_pic
    show michel_foucault_pic at right
    michel_foucault "Partint de teories postestructuralistes, considerem la realitat social com una cosa constituïda mitjançant el llenguatge usat per descriure-la. Per això, ens centrem en estructures lingüístiques, en el discurs i en actes."
    michel_foucault "Jo, Michel Foucault, mantinc que la sexualitat no és un fet biològic, sinó un fet construït socialment. Rebutjo els tòpics i considero que les prohibicions sexuals indiquen una fascinació pel sexe."
    michel_foucault "De fet, anomenar, regular i castigar les perversions fa que l'Estat pugui controlar i regular la sexualitat."
    hide michel_foucault_pic
    show judith_butler_pic at left
    judith_butler "Jo em qüestiono la idea {i}natural{/i} de i sobre els cossos i les identitats de gènere i sexuals."
    judith_butler "La societat es basa en un marc regulatori que reforça l'heterosexualitat com a orientació sexual {i}natural{/i}, donant per suposat l'existència de dos gèneres diferents i oposats: masculí i femení."
    judith_butler "És per aquest motiu que critico les feministes precedents per suposar que l'heterosexualitat és un estat natural de l'ésser."
    judith_butler "El binarisme o dimorfisme de gènere existeix en gran mesura per recolzar aquesta imposició de la societat, aquesta {i}identificació coherent{/i} en la qual sexe, sexualitat i gènere estan alineats."
    judith_butler "Aquesta identificació s'ha repetit tant que s'ha convertit en una norma cultural, és a dir, en heteronormativitat. I, tota desviació és castigada perquè l'heterosexualitat és la força dominant considerada normal, natural i ideal."
    judith_butler "Al final, les relacions de gènere estan determinades pel sexe. És opressiu considerar binari el sexe i no ho és construir una jerarquia sobre aquesta diferència."
    judith_butler "Al respecte, el feminisme estableix que no es produeix opressió si s'aboleix el gènere, no si es reconeixen infinitat de categories."
    show eve_kosofsky_sedgwick_pic at right
    eve_kosofsky_sedgwick "Doncs jo poso en dubte aquesta divisió binària entre heterosexuals i homosexuals, i insisteixo en el reconeixement de les diferències de gènere entre els gais i les lesbianes."
    eve_kosofsky_sedgwick "Justament per això m'agrada parlar en aquests casos de la teoria {i}queer{/i}."
    eve_kosofsky_sedgwick "Aquesta teoria es resisteix a la categorizació de les persones, desafia la idea de les identitats sexuals, qüestiona els binarismes i les relacions de poder subjacents, i assegura que la comprensió del sexe, del gènere i la identitat és contextual."
    hide eve_kosofsky_sedgwick_pic
    hide judith_butler_pic
    show judith_butler_pic at right
    judith_butler "Bé, el que és cert és que la percepció del gènere també s'aplica al sexe, i això porta a moltes persones intersexuals a recórrer a la cirugia per adequar el seu cos al que mèdicament es considera 'mascle' o 'femella'."
    judith_butler "D'aquesta manera, es pot observar que el sexe és construït socialment perquè el llenguatge emprat per descriure els genitals és el mateix que l'emprat pel gènere. En aquest cas, el sexe ja està condicionat a allò que suposa ser 'masculí' o 'femení'."
    judith_butler "En un context social, hi ha regles i restriccions sobre com ha d'actuar una persona en funció de les espectatives socials. Aquesta distinció de gènere o binarisme es manté mitjançant actes, com són l'aspecte, els gestos i la parla."
    judith_butler "Els individus repeteixen constant i insconscientment aquests actes de gènere al llarg de la seva vida, i és aquesta repetició que produeix la falsa impressió d'un binarisme de gènere fix i natural."
    judith_butler "Aquesta repetició constant d'actes que crea i manté el gènere es dóna en un determinat context, per això considero que el gènere, i també la sexualitat, és performatiu."
    judith_butler "El gènere és allò que les persones fem, no allò que som de forma innata!!"
    judith_butler "Les persones no neixem amb una identitat de gènere que ens duu a actuar d'una manera determinada, sinó que tenim una identitat de gènere per com caminem, com parlem, com ens presentem."
    judith_butler "No concebeixo la performativitat com una opció lliure, sinó que és com una trampa en la qual les persones repeteixen els actes que reforcen unes normes de gènere restrictives i opressores, sent aquestes normes construccions socials que situen a 'homes' i 'dones' en pols oposats."
    judith_butler "Per aquest motiu, critico que les feministes hagin creat noves construccions del què significa ser dona, ja que suposen que el gènere és real i que les dones com a grup comparteixen alguna classe de naturalesa comuna o realitat cultural."
    judith_butler "I és inexistent aquesta essència comuna en una 'dona', ja que cap experiència vital és compartida per totes les dones i, per tant, no permet agrupar-les en una única categoria."
    judith_butler "Novament, aquestes suposades característiques comunes entre dones són sovint associades a la conjunció entre gènere i cos femenins."
    show alicia_miyares_pic at left
    alicia_miyares "El problema és que el què tu esmentes no és feminisme, és teoria de la identitat. La teoria {i}queer{/i} converteix el gènere en una categoria d'identitat."
    alicia_miyares "A més a més, qüestiones a les dones com a subjectes polítics femenins, i consideres que el patriarcat capitalista ja no és el nostre enemic, sinó que ho és la categoria amb la qual les dones s'empenyen en identificar-se per conformar un front de lluita."
    alicia_miyares "L'heteropatriarcat acaba invisibilitzant la misogínia entre altres persones."
    alicia_miyares "El {i}feminisme emotiu{/i} no conforma els drets col·lectius, sinó que pretén qüestionar i aïllar les dones enlloc de qüestionar-se el patriarcat."
    alicia_miyares "És el patriarcat que emmascara la desigualtat estructural al prioritzar la discriminació de diversos col·lectius i despolititzar per evitar la creació d'un subjecte global que lluiti contra la desigualtat."
    alicia_miyares "Discriminació i desigualtat no són conceptes equivalents. La desigualtat existeix quan una classe o grup social, en aquest cas les dones, és exclòs de totes les esferes de realització."
    alicia_miyares "La diversitat i la identitat són substituts de la igualtat política."
    "I, aquest debat continuà durant una hora més, fins que les actrius es retiraren de l'escenari mentre el teló s'abaixava."
    hide alicia_miyares_pic
    hide judith_butler_pic

    call curtain_down_night

    user "Ostres, quina funció més impactant. Quina sensació d'espessor amb tanta informació de cop ..."
    user "Vaig cap a casa, que ja és tard."
    "Així, [tmpSavePlayer] marxà passejant cap a casa, reflexionant sobre l'espectacle que acabava de veure."
    scene street_night_chpt3
    "Quan portava una estona caminant, sentí una veu que cridava ..."
    call susan_calling

    return


label susan_calling:
    show susan_faludi_black_pic at truecenter
    unknown "[tmpSavePlayer], ets tu?"
    hide susan_faludi_black_pic

    menu:
        "Et gires, tens curiositat":
            show susan_faludi_pic at truecenter
            "[tmpSavePlayer] es girà i la veié. Bonica i amb un somriure com sempre."
            user "Susan!!! Oh, Susy!!!"
            "I es van abraçar."
            user "Com estàs? Et veig molt maca."
            susan_faludi "Gràcies. Estic molt feliç. Fa uns dies que acabo de guanyar el Premi Pulitzer pel reportatge divulgatiu que vaig realitzar."
            user "Moltíssimes felicitats!! No en sabia res!!"
            susan_faludi "Moltes gràcies. Ara vinc del teatre, he anat a veure {i}Black Lips Live{/i}."
            user "Què dius ara? Jo també!!"
            susan_faludi "Quina casualitat!! I què t'ha semblat??"
            user "Molt interessant, però ara tinc massa informació al cap i necessito descansar."
            susan_faludi "Sí, el mateix em passa a mi. Però molt interessant l'espectacle."
            susan_faludi "Si et sembla bé, et trucaré per fer un cafè un dia d'aquests i parlem més tranquil·lament. Ara me'n he d'anar cap a casa."

            $ game_state.serie_with_susan = False
            $ GiveGlossaryItemToPlayer(41)

            user "Perfecte, Susan. Quedem així doncs."
            hide susan_faludi_pic
            "I, amb un comiat efusiu, Susan i [tmpSavePlayer] tornaven cadascú a les seves respectives cases passejant."
            "Necessitava un descans, així que es banyà i es posà a dormir per descansar el cap fins l'endemà."
            call go_to_hungary

        "Ignores la veu, tens son i vols anar cap a casa":
            "[tmpSavePlayer] va fer com si no hagués escoltat res i seguí el seu camí cap a casa. Volia arribar el més aviat possible."
            "Ja a casa descansant ..."
            call go_to_concert

    return
