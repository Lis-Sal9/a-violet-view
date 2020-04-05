
## Script for the glossary section.
## The player can achieve some items according to his selected path.

define current_glossary_index = -1


init -10 python:
    def GetGlossaryElementsByLanguage():
        if _preferences.language == "catalan":
            return glossary_dict_ca.copy()
        elif _preferences.language == "english":
            return glossary_dict_en.copy()
        elif _preferences.language == "spanish":
            return glossary_dict_es.copy()


init python:
    # Function for show the content of item
    def ShowItemContent(i):
        item_content = GetGlossaryElementsByLanguage().get(i)["content"]
        renpy.show_screen("glossary_content", item_content)
    glossary_unread_items = []

    def HasUnreadGlossayItems():
        return len(glossary_unread_items) > 0

    def MarkGlossaryItemAsRead(item):
        global glossary_unread_items
        if item in glossary_unread_items:
            glossary_unread_items.remove(item)

    def GiveGlossaryItemToPlayer(item):
        global items_player
        global glossary_unread_items
        if item not in items_player:
            items_player.append(item)
            glossary_unread_items.append(item)


# Screen to add the content of item on text element ############################
screen glossary_content(content):
    fixed:
        xysize 400, 600
        align 0.5, 0.5
        offset 490, -30
        at transform:
            rotate -3
        text content:
            xsize 400
            ymaximum 600
            align 0.5, 0
            size 15
            line_spacing 10
################################################################################


## Glossary screen #############################################################
## This screen shows the achievements of the user until that moment.
################################################################################
screen glossary():
    tag menu
    default adj = ui.adjustment()
    $ all_glossary_elements = GetGlossaryElementsByLanguage()

    frame:
        xalign .5 yalign .5
        add "images/glossary/glossary.png"

        textbutton _("Return"):
            xpos gui.navigation_xpos
            yalign .1
            yoffset -45
            action Return()

        $ title = At(Text(_("Glossary"), color='#ffffff', size=65), Transform(rotate=-10, xpos=gui.navigation_xpos + 70, ypos=570))
        text (title)

        vbox:
            xsize 450
            xalign 0.5
            xoffset -50
            yanchor 0
            ypos 100
            spacing 10
            at transform:
                rotate 2

            imagebutton:
                idle "images/glossary/arrow_top.png"
                hover "images/glossary/arrow_top_hover.png"
                action Function(adj.change, 0)
                xalign 0.5

            vpgrid:
                cols 1
                xysize 450, 500
                spacing 15
                draggable False
                pagekeys True
                mousewheel True
                yinitial 0
                yadjustment adj
                side_yfill True

                for i in range(0, len(all_glossary_elements)):
                    fixed:
                        xysize 450, 40
                        if i not in items_player:
                            image "images/glossary/trunk.png":
                                align 0.5, 0.5
                        else:
                            hbox:
                                align 0.5, 0.5
                                spacing 0

                                text all_glossary_elements.get(i)["name"]:
                                    size 17
                                    yalign 0.5

                                if i in glossary_unread_items:
                                    image "images/glossary/glossary_item_new.png":
                                        yalign 0.5

                            imagebutton:
                                idle "images/glossary/list_item_idle.png"
                                hover "images/glossary/list_item_hover.png"
                                selected_idle "images/glossary/list_item_hover.png"
                                selected_hover "images/glossary/list_item_hover.png"
                                align 0.5, 0.5
                                xysize 450, 40
                                action [SetVariable("current_glossary_index", i), SelectedIf(current_glossary_index == i), Function(ShowItemContent, i), Function(MarkGlossaryItemAsRead, i)]

            imagebutton:
                idle "images/glossary/arrow_bottom.png"
                hover "images/glossary/arrow_bottom_hover.png"
                xalign 0.5
                action Function(adj.change, adj.get_range())
################################################################################
