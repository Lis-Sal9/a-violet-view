
## Glossary screen #############################################################
## This screen shows the achievements of the user until that moment.
################################################################################
screen glossary():
    variant "touch"
    tag menu

    default adj = ui.adjustment()
    $ all_glossary_elements = GetGlossaryElementsByLanguage()

    fixed:
        xalign .5 yalign .5
        add "images/glossary/glossary.png"

        imagebutton:
            idle "images/glossary/glossary_return.png"
            hover "images/glossary/glossary_return_hover.png"
            align .05, .1
            yoffset -45
            action Return()

        text _("Glossary"):
            color '#ffffff'
            size 100
            xalign 0.085
            yalign 0.8
            at transform:
                rotate -10

        vbox:
            xsize 450
            xalign 0.5
            xoffset -50
            yanchor 0
            ypos 80
            spacing 10
            at transform:
                rotate 2

            imagebutton:
                idle Frame("gui/arrows/arrow_top.png")
                hover Frame("gui/arrows/arrow_top_hover.png")
                action Function(adj.change, 0)
                xalign 0.5
                xysize 60, 110

            vpgrid:
                cols 1
                xysize 450, 400
                spacing 15
                draggable True
                pagekeys True
                mousewheel True
                yinitial 0
                yadjustment adj
                side_yfill True

                for i in range(0, len(all_glossary_elements)):
                    fixed:
                        xysize 450, 40
                        if i not in game_state.glossary_items:
                            image "images/glossary/trunk.png":
                                align 0.5, 0.5
                        else:
                            hbox:
                                align 0.5, 0.5
                                spacing 0

                                text all_glossary_elements.get(i)["name"]:
                                    size 25
                                    yalign 0.5

                                if i in game_state.glossary_items_unread:
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
                idle Frame("gui/arrows/arrow_bottom.png")
                hover Frame("gui/arrows/arrow_bottom_hover.png")
                action Function(adj.change, adj.get_range())
                xalign 0.5
                xysize 60, 110
################################################################################
