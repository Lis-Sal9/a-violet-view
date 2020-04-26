

## Script for the newspaper scene. This scene is a zoom in.


screen reading_newspaper():
    $ renpy.choice_for_skipping()

    frame:
        xalign .5 yalign .5
        add "images/chapter1/newspaper/newspaper.png"

        imagebutton:
            idle "gui/arrows/arrow_right.png"
            hover "gui/arrows/arrow_right_hover.png"
            xpos 1800
            yalign .1
            yoffset -45
            action Return()

        text _("STEPHEN KUNG, Editor"):
            font "fonts/courier_new.ttf"
            size 17
            xalign 0.05
            yalign 0.22

        text _("THE CHANGE JOURNAL, Editorial"):
            font "fonts/courier_new.ttf"
            size 17
            xalign 0.97
            yalign 0.22

        vbox:
            xsize 1000
            ypos 100
            spacing 10
            xpos 50

            fixed:
                text _("{b}Sindicalisme: Les dones de la fàbrica Lowell tornen als carrers{/b}"):
                    font "fonts/courier_new.ttf"
                    size 20
                    yalign 0.25
                    xalign 0.25

                imagebutton:
                    idle "images/chapter1/newspaper/lowell_mill_girls_2.png"
                    xalign 0.1
                    yalign 0.38
                    action NullAction()

                text _("Font: Flanagan, A. K. (2006). {i}The Lowell Mill Girls{/i}. Minneapolis: Compass Point Books."):
                    font "fonts/courier_new.ttf"
                    size 9
                    yalign 0.52
                    xalign 0.1

                hbox:
                    xsize 450
                    ypos 560

                    text _("Vuit anys enrere, les dones de la fàbrica Lowell, el sindicat, varen sortir al carrer amb pancartes per protestar en contra de les normes restrictives de l’empresa. Ara, 1500 treballadores abandonen la fàbrica de ple i detenen la producció, amb la finalitat d’exigir millors salaris i un millor tracte per part dels seus patrons."):
                        font "fonts/courier_new.ttf"
                        size 15
                        yoffset 40
                        xoffset 60
                        xalign 0.1
                        line_spacing 15
                        justify True

                imagebutton:
                    idle "images/chapter1/newspaper/lowell_mill_girls_1.png"
                    xalign 0.8
                    xoffset 100
                    yalign 0.78
                    action NullAction()

                text _("Font: Flanagan, A. K. (2006). {i}The Lowell Mill Girls{/i}. Minneapolis: Compass Point Books."):
                    font "fonts/courier_new.ttf"
                    size 9
                    yalign 0.8
                    yoffset 50
                    xalign 0.9
                    xoffset 65

                hbox:
                    xsize 450
                    ypos 300
                    xpos 600
                    text _("A la revista mensual publicada pel personal de la fàbrica, {i}Lowell Offering{/i}, s’idealitza el dia a dia de les treballadores quan, la realitat es traduïa en baixos salaris i llargues jornades. La reacció a aquest fet ha estat considerablement potent, i els patrons han acusat les dones treballadores de ser desagraïdes i inmorals. Aquesta vaga ha suposat un inici d’acció col·lectiva arreu del món, amb diferents motivacions."):
                        font "fonts/courier_new.ttf"
                        size 15
                        yalign 0.3
                        yoffset 20
                        xoffset -20
                        line_spacing 15
                        justify True

        vbox:
            xsize 900
            ypos 100
            spacing 10
            xpos 1250

            fixed:
                text _("{b}La {i}dona nova{/i} en la plana internacional{/b}"):
                    font "fonts/courier_new.ttf"
                    size 20
                    yalign 0.25
                    xalign 0.2

                hbox:
                    xsize 450
                    ypos 300
                    text _("Raicho Hiratsuka, membre de la societat literària anomenada Societat de Dones Escriptores ({i}Keishu Bungakukai{/i}), fundà el grup de les {i}Seitosha{/i} (Mitges Blaves), en honor a les {i}Bluestockings{/i} de Montagu, per difondre amb la revista {i}Seito{/i} l’escriptura creativa entre les dones japoneses i cultivar la imatge de la {i}dona nova{/i}. Aquest grup s’enfrontà a les actituds feudalistes tradicionals i foren censurades pel govern, acusades de difondre idees revolucionàries. No obstant això, aquest fet va obrir camí a l’aparició d’una nova associació. La Nova Asociació de Dones ({i}Shin Fujin Kyokai{/i}), sota el lideratge de Fusae Ichikawa, fa campanya pels drets polítics de les dones, tot plantejant l’emancipació entre els intel·lectuals japonesos i promovent l’ideal de {i}dona nova{/i} que pretenia deixar enrere els vincles feudals i el patriarcat japonesos."):
                        font "fonts/courier_new.ttf"
                        size 15
                        yalign 0.01
                        yoffset 20
                        xoffset 100
                        xalign 0.9
                        line_spacing 15
                        justify True
