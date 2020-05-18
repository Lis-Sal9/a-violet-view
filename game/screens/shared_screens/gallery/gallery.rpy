
##### Gallery section
##
## This script is for gallery section. In this one, the user can see the women portraits, unlocked or locked until that moment.


init -10 python:
    def GetGalleryElementsByLanguage():
        if _preferences.language == "catalan":
            return gallery_dict_ca.copy()
        elif _preferences.language == "english":
            return gallery_dict_ca.copy()
        elif _preferences.language == "spanish":
            return gallery_dict_ca.copy()

    def ShowBiography(i):
        item = GetGalleryElementsByLanguage().get(i)
        renpy.show_screen("gallery_item_details", item)

    def HasUnreadGalleryItems():
        return len(game_state.gallery_items_unread) > 0

    def MarkGalleryItemAsRead(item):
        global game_state
        if item in game_state.gallery_items_unread:
            game_state.gallery_items_unread.remove(item)

    def GiveGalleryItemToPlayer(item):
        global game_state
        if item not in game_state.gallery_items:
            game_state.gallery_items.append(item)
            game_state.gallery_items_unread.append(item)

    def ShowBiographies():
        renpy.notify(_("You receive new gallery items."))


## Gallery screen ##############################################################
## This screen shows the women portraits which user has unlock until that moment.
screen gallery():
    tag menu
    $ all_gallery_elements = GetGalleryElementsByLanguage()

    fixed:
        xalign .5 yalign .5
        add "images/gallery/gallery_bg.png"

        imagebutton:
            idle "images/gallery/gallery_return.png"
            hover "images/gallery/gallery_return_hover.png"
            align .05, .9
            action Return()

        text _("Dones rellevants"):
            color '#f1dde0'
            font "fonts/my_font.otf"
            size 100
            align .3, .05

        hbox:
            align .5, .5
            xysize 1900, 900

            for i in range(0, len(all_gallery_elements)):
                fixed:
                    xysize 5, 100
                    if i == 0:
                        yoffset -20
                    elif i == 1:
                        yoffset 360
                        xoffset -20
                    elif i == 2:
                        yoffset 100
                        xoffset -40
                    elif i == 3:
                        yoffset 370
                        xoffset -30
                    elif i == 4:
                        yoffset -30
                        xoffset 15
                    elif i == 5:
                        yoffset 400

                    imagebutton:
                        yalign .1
                        if i not in game_state.gallery_items:
                            idle "images/gallery/gallery_empty_" + str(i) + ".png"
                            action NullAction()
                        else:
                            idle "images/gallery/gallery_full_" + str(i) + ".png"
                            hover "images/gallery/gallery_full_hover_" + str(i) + ".png"
                            selected_idle "images/gallery/gallery_full_hover_" + str(i) + ".png"
                            selected_hover "images/gallery/gallery_full_hover_" + str(i) + ".png"
                            action [Function(ShowBiography, i), Function(MarkGalleryItemAsRead, i)]


screen gallery_item_details(item):
    $ item_name = item["name"].replace(" ", "_")
    $ item_name = item_name.lower()

    imagebutton:
        xysize 1920, 1080
        idle Solid("0004")
        action NullAction()

    image "images/gallery/biography.png":
        align 0.5, 0.5
        zoom 1.15

    fixed:
        align .5, .5
        xysize 1000, 800

        imagebutton:
            idle "gui/arrows/arrow_left.png"
            hover "gui/arrows/arrow_left_hover.png"
            align 0, 0.05
            action Hide("gallery_item_details")


        add "images/gallery/women/" + item_name + ".png":
            yalign .35
            xoffset 10
            yoffset 20

        text item["content"]:
            size 25
            xysize 600, 600
            align .99, .35
            xoffset 20
            line_spacing 0
