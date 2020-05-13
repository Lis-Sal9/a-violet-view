
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
            game_state.find_differences_done = True
            renpy.notify(_("Ha aconseguit l'obsequi!"))

    def checkTenDifferences():
        if len(found_differences) == 10:
            GiveGalleryItemToPlayer(1)
            renpy.end_interaction("")



label find_differences_label:
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)
    $ found_differences = []

    if game_state.witch_is_seen:
        call screen find_differences_obos
    else:
        call screen find_differences_manushi

    $ setIsInSpecialScreen(False)
    return



screen find_differences_obos:
    imagemap:
        idle "images/chapter2/part1/find_differences/our_bodies_our_selves_big.png"
        ground "images/chapter2/part1/find_differences/our_bodies_our_selves_big.png"

        if 1 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 987, 845
        else:
            hotspot (987, 845, 25, 55):
                action Function(addFoundDifference, id=1)

        if 2 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1245, 895
        else:
            hotspot (1245, 895, 16, 24):
                action Function(addFoundDifference, id=2)

        if 3 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1170, 790
        else:
            hotspot (1170, 790, 40, 35):
                action Function(addFoundDifference, id=3)

        if 4 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1230, 740
        else:
            hotspot (1230, 740, 45, 45):
                action Function(addFoundDifference, id=4)

        if 5 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1433, 634
        else:
            hotspot (1433, 634, 35, 30):
                action Function(addFoundDifference, id=5)

        if 6 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1385, 485
        else:
            hotspot (1385, 485, 35, 35):
                action Function(addFoundDifference, id=6)

        if 7 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1537, 605
        else:
            hotspot (1537, 605, 50, 45):
                action Function(addFoundDifference, id=7)

        if 8 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1165, 345
        else:
            hotspot (1165, 345, 45, 45):
                action Function(addFoundDifference, id=8)

        if 9 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1397, 259
        else:
            hotspot (1397, 259, 35, 40):
                action Function(addFoundDifference, id=9)

        if 10 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1660, 950
        else:
            hotspot (1660, 950, 45, 45):
                action Function(addFoundDifference, id=10)

    imagebutton:
        idle "gui/arrows/return_white.png"
        hover "gui/arrows/return_hover_blue.png"
        align .03, .9
        action Rollback()

    if len(found_differences) > 6:
        imagebutton:
            idle "gui/arrows/arrow_right.png"
            hover "gui/arrows/arrow_right_hover.png"
            xpos 1800
            yalign .9
            action Return("")



screen find_differences_manushi:
    imagemap:
        idle "images/chapter2/part1/find_differences/manushi_big.png"
        ground "images/chapter2/part1/find_differences/manushi_big.png"

        if 1 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1120, 298
        else:
            hotspot (1120, 298, 30, 25):
                action Function(addFoundDifference, id=1)

        if 2 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1605, 295
        else:
            hotspot (1605, 295, 30, 25):
                action Function(addFoundDifference, id=2)

        if 3 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1329, 221
        else:
            hotspot (1329, 221, 30, 30):
                action Function(addFoundDifference, id=3)

        if 4 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1200, 575
        else:
            hotspot (1200, 575, 50, 40):
                action Function(addFoundDifference, id=4)

        if 5 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1300, 825
        else:
            hotspot (1300, 825, 45, 45):
                action Function(addFoundDifference, id=5)

        if 6 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1490, 840
        else:
            hotspot (1490, 840, 45, 35):
                action Function(addFoundDifference, id=6)

        if 7 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1380, 795
        else:
            hotspot (1380, 795, 50, 55):
                action Function(addFoundDifference, id=7)

        if 8 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1450, 475
        else:
            hotspot (1445, 475, 50, 50):
                action Function(addFoundDifference, id=8)

        if 9 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1405, 490
        else:
            hotspot (1405, 490, 30, 25):
                action Function(addFoundDifference, id=9)

        if 10 in found_differences:
            image "images/chapter2/part1/find_differences/circle.png":
                pos 1340, 545
        else:
            hotspot (1340, 545, 50, 35):
                action Function(addFoundDifference, id=10)

    imagebutton:
        idle "gui/arrows/return_white.png"
        hover "gui/arrows/return_hover_blue.png"
        align .03, .9
        action Rollback()

    if len(found_differences) > 6:
        imagebutton:
            idle "gui/arrows/arrow_right.png"
            hover "gui/arrows/arrow_right_hover.png"
            xpos 1800
            yalign .9
            action Return("")
