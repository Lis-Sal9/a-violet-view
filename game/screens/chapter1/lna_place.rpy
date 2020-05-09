
## This is the script for the Ladies National Association scene ###############################


init python:
    def addContraception():
        game_state.contraception_is_found = True
        GiveGlossaryItemToPlayer(21)
        ShowItems()


screen ladies_national_association():
    imagemap:
        idle "images/chapter1/lna/lna_place.jpg"
        ground "images/chapter1/lna/lna_place.jpg"
        hotspot (903, 93, 277, 148):
            clicked [Function(addContraception), Hide("ladies_national_association"), Hide("hover_lna")]
            hovered ShowTransient("hover_lna", img="images/chapter1/lna/lna_place_hover.jpg")
            unhovered Hide("hover_lna")


screen hover_lna(img):
    add img at truecenter

label contraception:
    scene lna_place
    "Caminant, arribà a una sala una mica peculiar. Es tractava d'una sala homenatge a l'Associació Nacional de Dames."
    "Sobre de la taula hi havia un paper ple de pols que explicava la història de l'associació."

    if not game_state.contraception_is_found:
        $ renpy.show_screen("ladies_national_association")

    user "{i}Aquesta associació fou creada per derogar la Llei de Malalties Infeccioses.{/i}"
    user "{i}Aquesta llei legalitza la prostitució i sotmet les dones involucrades a control policial i mèdic.{/i}"
    user "{i}Això suposa no només oficialitzar la situació, sinó un maltractament a les dones pobres.{/i}"
    user "Ostres, novament apareix el maltractament a les dones ... És un problema que s'ha d'erradicar ja !!"
    user "Més tríptics ..."
    user "{i}La doble moral sexual: homes amb activitat sexual i promiscuïtat ben vistes, però dones verges i pures fins el matrimoni.{/i}"
    user "{i}La prostitució és rebutjada per ser el mal social de la societat de tota dona respectable.{/i}"
    user "{i}No obstant això, és considerada una conseqüència inevitable de l'incontrolable desig sexual de l'home.{/i}"

    $ GiveGlossaryItemToPlayer(19)
    $ ShowItems()

    user "Quines excuses més barates, mare meva ... això és inacceptable."
    user "Ostres, en aquest altre tríptic hi ha un anunci ..."
    user "{i}Convenció a la capella metodista per parlar sobre els drets de les dones. Avui, a les 15:30h. {/i}"
    user "Hi vull anar!"
    "[tmpSavePlayer] decideix agafar el número d'una revista que hi havia sobre la taula i endur-se'l."
    "I, amb mal cos i cara de desconcert, marxa d'aquella sala ... i de Langham."

    $ renpy.hide_screen("ladies_national_association")
    call seneca_falls_convention
    return
