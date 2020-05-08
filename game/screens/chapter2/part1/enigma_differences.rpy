
# This script is for one of the enigmas of chapter 2.
##
### The player has to find, minimum, seven differences between two images to collect two gifts: a gallery item and a journal.

init -10 python:
    found_differences = []

    def addFoundDifference(id):
        global found_differences
        if not id in found_differences:
            found_differences.append(id)
            checkSevenDifferences()
            checkTenDifferences()

    def checkSevenDifferences():
        if len(found_differences) == 7:
            renpy.notify(_("Has aconseguit l'obsequi!"))

    def checkTenDifferences():
        if len(found_differences) == 10:
            GiveGalleryItemToPlayer(1)
            renpy.jump("enigma_differences")



label enigma_differences:
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


screen find_differences:
    $ renpy.choice_for_skipping()

    if game_state.witch_is_seen:
        imagemap:
            idle "images/chapter2/part1/find_differences/our_bodies_our_selves.png"
            ground "images/chapter2/part1/find_differences/our_bodies_our_selves.png"
            
            if 1 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1035
                    ypos 745
                    action NullAction()
            else:
                hotspot (1035, 745, 18, 51):
                    action Function(addFoundDifference, id=1)

            if 2 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1270
                    ypos 782
                    action NullAction()
            else:
                hotspot (1270, 782, 16, 24):
                    action Function(addFoundDifference, id=2)

            if 3 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1200
                    ypos 690
                    action NullAction()
            else:
                hotspot (1200, 690, 36, 29):
                    action Function(addFoundDifference, id=3)

            if 4 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1255
                    ypos 642
                    action NullAction()
            else:
                hotspot (1255, 642, 40, 38):
                    action Function(addFoundDifference, id=4)

            if 5 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1437
                    ypos 548
                    action NullAction()
            else:
                hotspot (1437, 548, 30, 25):
                    action Function(addFoundDifference, id=5)

            if 6 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1397
                    ypos 415
                    action NullAction()
            else:
                hotspot (1397, 415, 30, 28):
                    action Function(addFoundDifference, id=6)

            if 7 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1532
                    ypos 525
                    action NullAction()
            else:
                hotspot (1532, 525, 44, 42):
                    action Function(addFoundDifference, id=7)

            if 8 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1193
                    ypos 290
                    action NullAction()
            else:
                hotspot (1193, 290, 37, 39):
                    action Function(addFoundDifference, id=8)

            if 9 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1405
                    ypos 212
                    action NullAction()
            else:
                hotspot (1405, 212, 27, 35):
                    action Function(addFoundDifference, id=9)

            if 10 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1645
                    ypos 838
                    action NullAction()
            else:
                hotspot (1645, 838, 28, 29):
                    action Function(addFoundDifference, id=10)

    else:
        imagemap:
            idle "images/chapter2/part1/find_differences/manushi.png"
            ground "images/chapter2/part1/find_differences/manushi.png"

            if 1 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1167
                    ypos 253
                    action NullAction()
            else:
                hotspot (1167, 253, 25, 20):
                    action Function(addFoundDifference, id=1)

            if 2 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1605
                    ypos 247
                    action NullAction()
            else:
                hotspot (1605, 247, 25, 18):
                    action Function(addFoundDifference, id=2)

            if 3 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1356
                    ypos 181
                    action NullAction()
            else:
                hotspot (1356, 181, 23, 25):
                    action Function(addFoundDifference, id=3)

            if 4 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1230
                    ypos 498
                    action NullAction()
            else:
                hotspot (1230, 498, 45, 35):
                    action Function(addFoundDifference, id=4)

            if 5 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1327
                    ypos 727
                    action NullAction()
            else:
                hotspot (1327, 727, 38, 37):
                    action Function(addFoundDifference, id=5)

            if 6 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1497
                    ypos 742
                    action NullAction()
            else:
                hotspot (1497, 742, 39, 30):
                    action Function(addFoundDifference, id=6)

            if 7 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1395
                    ypos 695
                    action NullAction()
            else:
                hotspot (1395, 695, 43, 49):
                    action Function(addFoundDifference, id=7)

            if 8 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1465
                    ypos 410
                    action NullAction()
            else:
                hotspot (1465, 410, 43, 43):
                    action Function(addFoundDifference, id=8)

            if 9 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1424
                    ypos 430
                    action NullAction()
            else:
                hotspot (1424, 430, 28, 22):
                    action Function(addFoundDifference, id=9)

            if 10 in found_differences:
                imagebutton:
                    idle "images/chapter2/part1/find_differences/circle.png"
                    xpos 1365
                    ypos 475
                    action NullAction()
            else:
                hotspot (1365, 475, 44, 30):
                    action Function(addFoundDifference, id=10)

    if len(found_differences) > 6:
        imagebutton:
            idle "gui/arrows/arrow_right.png"
            hover "gui/arrows/arrow_right_hover.png"
            xpos 1800
            yalign .9
            action Jump("enigma_differences")
