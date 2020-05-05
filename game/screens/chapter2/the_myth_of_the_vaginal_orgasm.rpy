
## This is script for the female eunuch secret inside pizzey hostel room.


init python:
    def addVaginalOrgasm():
        game_state.vaginal_orgasm_is_found = True
        #GiveGlossaryItemToPlayer(13)
        #ShowItems()


screen the_myth_of_the_vaginal_orgasm():
    imagemap:
        idle "images/chapter2/hostel/amazonas_hostel.png"
        ground "images/chapter2/hostel/amazonas_hostel.png"
        hotspot (1587, 696, 314, 60):
            clicked [Function(addEunuch), Hide("the_myth_of_the_vaginal_orgasm"), Hide("hover_vaginal_orgasm")]
            hovered ShowTransient("hover_vaginal_orgasm", img="images/chapter2/hostel/amazonas_hostel_hover.png")
            unhovered Hide("hover_vaginal_orgasm")


screen hover_vaginal_orgasm(img):
    add img at truecenter
