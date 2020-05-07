
## This is script for the female eunuch secret inside pizzey hostel room.


init python:
    def addEunuch():
        game_state.eunuch_is_found = True
        #GiveGlossaryItemToPlayer(13)
        #ShowItems()


screen the_female_eunuch():
    imagemap:
        idle "images/chapter2/part1/hostel/pizzey_hostel_room.png"
        ground "images/chapter2/part1/hostel/pizzey_hostel_room.png"
        hotspot (897, 664, 171, 18):
            clicked [Function(addEunuch), Hide("the_female_eunuch"), Hide("hover_eunuch")]
            hovered ShowTransient("hover_eunuch", img="images/chapter2/part1/hostel/pizzey_hostel_room_hover.png")
            unhovered Hide("hover_eunuch")


screen hover_eunuch(img):
    add img at truecenter
