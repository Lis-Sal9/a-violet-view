﻿################################################################################
## Initialization
################################################################################

init offset = -1

init -10 python:
    is_in_special_screen = False

    def setIsInSpecialScreen(value):
        global is_in_special_screen
        is_in_special_screen = value


################################################################################
## Styles
################################################################################
style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################

## Say screen ##################################################################
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
################################################################################
screen say(who, what):
    style_prefix "say"
    key "K_ESCAPE" action MainMenu()

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what:
            id "what"
            line_spacing -16

        ####### Quick menu ##################
        hbox:
            style_prefix "quick"
            xalign 0.82
            yalign 0.15
            spacing 5

            imagebutton:
                action Show('pause')
                idle "gui/icons/pause.png"
                hover "gui/icons/pause_border.png"

            if not is_in_special_screen:
                imagebutton:
                    action Rollback()
                    idle "gui/icons/return.png"
                    hover "gui/icons/return_border.png"

            imagebutton:
                action Skip() alternate Skip(fast=True, confirm=True)
                idle "gui/icons/skip_action.png"
                hover "gui/icons/skip_action_border.png"

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
        ##############################################################

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor 0.5
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.6
    yalign gui.name_yalign

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
################################################################################


## Input screen ################################################################
## This screen is used to display renpy.input. The prompt parameter is used to pass a text prompt in.
## This screen must create an input displayable with id "input" to accept the various input parameters.
################################################################################
screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
################################################################################


## Choice screen ###############################################################
## This screen is used to display the in-game choices presented by the menu statement.
## The one parameter, items, is a list of objects, each with caption and action fields.
################################################################################
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    imagebutton:
        idle "gui/arrows/return_white.png"
        hover "gui/arrows/return_hover_blue.png"
        align .03, .9
        action Rollback()

define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
################################################################################


## Pause menu ##############################################################
## This menu appears on quick menu to pause the game. The user can choose diferent options:
## continue for return to game, load for initializate another game, preferences for access to
## volume, language and display options, and exit for return to main menu.
################################################################################
screen pause():
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png" as panel
    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        textbutton _("Continue") action Hide("pause")

        textbutton _("Load") action [Hide("pause"), ShowMenu("load")]

        textbutton _("Preferences") action [Hide("pause"), ShowMenu("preferences")]

        textbutton _("Exit") action [Hide("pause"), MainMenu()]
###############################################################################


## Confirm screen ##############################################################
## The confirm screen is called when Ren'Py wants to ask the player a yes or no question.
################################################################################
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action [Hide("confirm"), yes_action]
                textbutton _("No") action [Hide("confirm"), no_action]

    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    color "#ffffff"
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
################################################################################



################################################################################
## Main and Game Menu Screens
################################################################################

## Main Menu screen ############################################################
## Used to display the main menu when Ren'Py starts.
################################################################################
init -2 python:
    def GetCover():
        if _preferences.language == "english":
            return "en"
        elif _preferences.language == "spanish":
            return "es"
        elif _preferences.language == "catalan":
            return "ca"

screen hover_main_menu(img):
    add img at truecenter

screen main_menu():
    python:
        lang = GetCover()

    tag menu

    imagemap:
        idle "images/cover/desktop/full_" + str(lang) + ".png"
        ground "images/cover/desktop/full_" + str(lang) + ".png"

        # Start
        hotspot (1594, 90, 225, 225):
            clicked [Hide("hover_main_menu"), Show(screen="name_input", message="Please, enter your name.", ok_action=Function(FinishEnterName))]
            hovered ShowTransient("hover_main_menu", img="images/cover/desktop/hover/full_hover_start_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")

        # Load
        hotspot (1310, 375, 232, 246):
            clicked [Hide("hover_main_menu"), ShowMenu("load")]
            hovered ShowTransient("hover_main_menu", img="images/cover/desktop/hover/full_hover_load_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")

        # Preferences
        hotspot (1004, 288, 211, 234):
            clicked [Hide("hover_main_menu"), ShowMenu("preferences", True)]
            hovered ShowTransient("hover_main_menu", img="images/cover/desktop/hover/full_hover_preferences_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")

        # About
        hotspot (1624, 645, 219, 223):
            clicked [Hide("hover_main_menu"), ShowMenu("about")]
            hovered ShowTransient("hover_main_menu", img="images/cover/desktop/hover/full_hover_about_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")
        # Help
        hotspot (1184, 732, 226, 241):
            clicked [Hide("hover_main_menu"), ShowMenu("help")]
            hovered ShowTransient("hover_main_menu", img="images/cover/desktop/hover/full_hover_help_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")

        # Exit
        hotspot (819, 786, 200, 196):
            clicked Quit(confirm=not main_menu)
            hovered ShowTransient("hover_main_menu", img="images/cover/desktop/hover/full_hover_exit_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")


################################################################################


## Game Menu screen ############################################################
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation. The
## scroll parameter can be None, or one of "viewport" or "vpgrid".
################################################################################
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    key "K_ESCAPE" action MainMenu()

    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title xpos 300

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
################################################################################


## Navigation screen ###########################################################
## This screen is included in the main and game menus, and provides navigation to
## other menus, and to start the game.
################################################################################
init -1 python:
    def FinishEnterName():
        if not tmpSavePlayer: return
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Show(screen="name_input", message="Please, enter your name.", ok_action=Function(FinishEnterName))

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):
            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
########################################################################################


## Name input screen ###########################################################
## Ask for player name on a modal ##############################################
screen name_input(message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action ok_action

    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" length 20 allow "ABCÇDEFGHIJKLMNÑOPQRSTUVWXYZabcçdefghijklmnñopqrstuvwxyz" changed OnSavePlayerUpdate

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action
            textbutton _("Cancel") action Hide("name_input")
################################################################################



## Help screen #################################################################
## A screen that gives information about key and mouse bindings. It uses other screens
## (keyboard_help, mouse_help) to display the actual help.
################################################################################
screen help():
    tag menu

    fixed:
        xalign .5 yalign .5
        add "images/keymap.png"

        imagebutton:
            idle "images/glossary/glossary_return.png"
            hover "images/glossary/glossary_return_hover.png"
            align .04, .1
            yoffset -45
            action Return()

        text _("Mapa de controls"):
            color '#3c291c'
            font "fonts/my_font.otf"
            size 160
            xalign 0.5
            yalign 0.03

        text _("Avançar / Seleccionar / Arrossegar"):
            xalign 0.43
            yalign 0.25

        text _("Avançar / Seleccionar / Arrossegar"):
            xalign 0.95
            yalign 0.78

        text _("Desplaçar-se"):
            xalign 0.4
            yalign 0.42

        text _("Sortir (des de diàlegs)"):
            xalign 0.75
            yalign 0.64



## About screen ################################################################
## This screen gives credit and copyright information about the game and Ren'Py.
################################################################################
screen about():
    tag menu

    image "images/about_me.png"

    text _("Sobre mi"):
        color '#000000'
        font "fonts/my_font.otf"
        size 160
        xalign 0.51
        yalign 0.04

    text _("Sobre mi"):
        color '#a00f42'
        font "fonts/my_font.otf"
        size 160
        xalign 0.5
        yalign 0.03

    imagebutton:
        idle "images/glossary/glossary_return.png"
        hover "images/glossary/glossary_return_hover.png"
        align .05, .95
        action Return()

    viewport:
        align .77, .5
        xysize 1270, 580
        scrollbars "vertical"
        draggable True
        mousewheel True

        text _("Ara em sento sola i tinc por. Por perquè quan em miro al mirall, solament veig algú a qui no he estimat com es mereix. A qui no m’havia pres la molèstia de preguntar-li què la fa realment feliç, i si està contenta amb sí mateixa. Ara, em sento sola amb mi mateixa i no sé com he d’actuar, què he de fer o, inclús, què he de sentir i com. La culpa m’ha ennuvolat el pensament i el sentiment, inclús el plaer de ser tocada per algú altre.\nDes de llavors, els dies són grisos per a mi. Però avui he decidit llevar-me amb la millor versió de mi. Forta, lliure i rebel. Sense retre comptes a ningú més que a mi mateixa. Avui, vull agrair a les meves companyes del grup, perquè amb sororitat m’han demostrat que m’estava perdent la fantàstica oportunitat d’estimar-me. De conèixer-me, de no jutjar-me i de confiar en mi. Juntes, totes nosaltres, podem lluitar agafades de la mà per denunciar el patriarcat, la misogínia, la desigualtat sexual i la violència masclista en totes les seves formes. Aquest videojoc és un homenatge a totes vosaltres, les meves companyes de vida.\n\n                         {i}No es neix dona, s'arriba a ser-ho.{/i} - Simone de Beauvoir"):
            color '#3b0f52'
            size 41

################################################################################



################################################################################
## Additional screens
################################################################################

## Notify screen ###############################################################
## The notify screen is used to show the player a message.
################################################################################
screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
################################################################################
