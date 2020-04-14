################################################################################
## Initialization
################################################################################

init offset = -1



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

        text what id "what"

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
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

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


## Quick Menu screen ###########################################################
## The quick menu is displayed in-game to provide easy access to the out-of-game menus.
################################################################################
screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0

            imagebutton:
                action Show('pause')
                idle "gui/icons/pause.png"
                hover "gui/icons/pause_border.png"

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
                if is_in_puzzle:
                    action NullAction()
                    hover "gui/icons/save.png"
                else:
                    action [Show(screen="save_menu"), FileTakeScreenshot()]
                    hover "gui/icons/save_border.png"
                idle "gui/icons/save.png"

            imagebutton:
                action ShowMenu('help')
                idle "gui/icons/help.png"
                hover "gui/icons/help_border.png"

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True
style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
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
screen main_menu():
    tag menu
    style_prefix "main_menu"
    add gui.main_menu_background

    python:
        if not _preferences.language:
            _preferences.language = "english"

    frame:
        pass

    use navigation

    if gui.show_name:
        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "Vanessa Mañas":
                style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True
    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")
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

        textbutton _("Gallery") action ShowMenu("gallery")

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


## Preferences screen ######################################################################
## The preferences screen allows the player to configure the game to better suit themselves.
############################################################################################
screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("English") action Language("english")
                    textbutton _("Spanish") action Language("spanish")
                    textbutton _("Catalan") action Language("catalan")

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_music:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675
################################################################################


## Help screen #################################################################
## A screen that gives information about key and mouse bindings. It uses other screens
## (keyboard_help, mouse_help) to display the actual help.
################################################################################
screen help():
    tag menu
    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 23

            hbox:
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
################################################################################


## Keyboard help screen ########################################################
## A screen that gives information about keyboard help.
################################################################################
screen keyboard_help():
    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")
################################################################################


## Mouse help screen ########################################################
## A screen that gives information about mouse help.
################################################################################
screen mouse_help():
    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")
################################################################################


## About screen ################################################################
## This screen gives credit and copyright information about the game and Ren'Py.
################################################################################
screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"

        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            text _("Work in progress ...")

            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

define gui.about = ""
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style about_label_text:
    size gui.label_text_size
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
