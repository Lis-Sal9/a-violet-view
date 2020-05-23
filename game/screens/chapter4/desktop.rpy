
## This script is for femiblog screen.



label desktop_label:
    scene black
    $ renpy.choice_for_skipping()
    $ setIsInSpecialScreen(True)
    call screen desktop

    return


screen desktop:
    add "images/chapter4/desktop/desktop_bg.png"

    imagebutton:
        idle "images/chapter4/desktop/off_icon.png"
        hover "images/chapter4/desktop/off_icon_hover.png"
        align 0, 0
        action [Hide("desktop"), Jump("credits")]

    imagebutton:
        idle "images/chapter4/desktop/browser_icon.png"
        hover "images/chapter4/desktop/browser_icon_hover.png"
        selected_idle "images/chapter4/desktop/browser_icon_hover.png"
        selected_hover "images/chapter4/desktop/browser_icon_hover.png"
        align 0, .16
        action Show(screen="femiblog")

    imagebutton:
        idle "images/chapter4/desktop/ciberfeminism_icon.png"
        hover "images/chapter4/desktop/ciberfeminism_icon_hover.png"
        align 0, .4
        action [Function(init_all_functions), Show(screen="nonogram")]



    ########## Quick menu ####################################
    hbox:
        style_prefix "quick"
        xalign 0.5
        yalign 1.0
        spacing 5

        imagebutton:
            action Show('pause')
            idle "gui/icons/pause.png"
            hover "gui/icons/pause_border.png"

        imagebutton:
            action Rollback()
            idle "gui/icons/return.png"
            hover "gui/icons/return_border.png"

        imagebutton:
            action ShowMenu('glossary')
            hover "gui/icons/glossary_new_icon.png"
            if len(game_state.glossary_items_unread) > 0:
                idle "gui/icons/glossary_new_icon.png"
            else:
                idle "gui/icons/glossary_icon.png"

        imagebutton:
            action ShowMenu('gallery')
            hover "gui/icons/gallery_new_icon.png"
            if len(game_state.gallery_items_unread) > 0:
                idle "gui/icons/gallery_new_icon.png"
            else:
                idle "gui/icons/gallery_icon.png"

        imagebutton:
            if is_in_special_screen:
                action NullAction()
                hover "gui/icons/save.png"
            else:
                action [Show(screen="save_menu"), FileTakeScreenshot()]
                hover "gui/icons/save_border.png"
            idle "gui/icons/save.png"

        if renpy.variant("pc"):
            imagebutton:
                action ShowMenu('help')
                idle "gui/icons/help.png"
                hover "gui/icons/help_border.png"
    ##########################################################
