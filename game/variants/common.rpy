################################################################################
## Mobile Variants
################################################################################

default mobile_icon_size = 80


################################################################################
## Styles
################################################################################
style pref_vbox:
    variant "medium"
    xsize 675

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900

################################################################################



##### Screens ##################################################################

## Main Menu screen ############################################################
## Used to display the main menu when Ren'Py starts.
################################################################################
screen main_menu():
    variant "touch"

    python:
        if not _preferences.language:
            _preferences.language = "catalan"

        lang = GetCover()

    tag menu

    imagemap:
        idle "images/cover/mobile/mobile_" + str(lang) + ".png"
        ground "images/cover/mobile/mobile_" + str(lang) + ".png"

        # Start
        hotspot (1544, 142, 261, 265):
            clicked [Hide("hover_main_menu"), Show(screen="name_input", message="Please, enter your name.", ok_action=Function(FinishEnterName))]
            hovered ShowTransient("hover_main_menu", img="images/cover/mobile/hover/mobile_hover_start_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")

        # Load
        hotspot (1031, 726, 271, 281):
            clicked [Hide("hover_main_menu"), ShowMenu("load")]
            hovered ShowTransient("hover_main_menu", img="images/cover/mobile/hover/mobile_hover_load_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")

        # Preferences
        hotspot (1112, 354, 241, 240):
            clicked [Hide("hover_main_menu"), ShowMenu("preferences")]
            hovered ShowTransient("hover_main_menu", img="images/cover/mobile/hover/mobile_hover_preferences_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")

        # About
        hotspot (1505, 606, 247, 242):
            clicked [Hide("hover_main_menu"), ShowMenu("about")]
            hovered ShowTransient("hover_main_menu", img="images/cover/mobile/hover/mobile_hover_about_" + str(lang) + ".png")
            unhovered Hide("hover_main_menu")


################################################################################


## Say screen ##################################################################
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
################################################################################
screen say(who, what):
    variant "touch"
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
            line_spacing -10

        ####### Quick menu ##################
        hbox:
            style_prefix "quick"
            xalign 0.9
            yalign 0.10
            spacing 5

            imagebutton:
                action Show('pause')
                xysize mobile_icon_size, mobile_icon_size
                idle Frame("gui/icons/pause.png")
                hover Frame("gui/icons/pause_border.png")

            imagebutton:
                action Rollback()
                xysize mobile_icon_size, mobile_icon_size
                idle Frame("gui/icons/return.png")
                hover Frame("gui/icons/return_border.png")

            imagebutton:
                action Skip() alternate Skip(fast=True, confirm=True)
                xysize mobile_icon_size, mobile_icon_size
                idle Frame("gui/icons/skip_action.png")
                hover Frame("gui/icons/skip_action_border.png")

            imagebutton:
                action ShowMenu('glossary')
                xysize mobile_icon_size, mobile_icon_size
                hover Frame("gui/icons/glossary_new_icon.png")
                if len(game_state.glossary_items_unread) > 0:
                    idle Frame("gui/icons/glossary_new_icon.png")
                else:
                    idle Frame("gui/icons/glossary_icon.png")

            imagebutton:
                action ShowMenu('gallery')
                xysize mobile_icon_size, mobile_icon_size
                hover Frame("gui/icons/gallery_new_icon.png")
                if len(game_state.gallery_items_unread) > 0:
                    idle Frame("gui/icons/gallery_new_icon.png")
                else:
                    idle Frame("gui/icons/gallery_icon.png")

            imagebutton:
                if is_in_special_screen:
                    action NullAction()
                    hover Frame("gui/icons/save.png")
                else:
                    action [Show(screen="save_menu"), FileTakeScreenshot()]
                    hover Frame("gui/icons/save_border.png")
                    xysize mobile_icon_size, mobile_icon_size
                idle Frame("gui/icons/save.png")

        ##############################################################

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

init python:
    config.character_id_prefixes.append('namebox')
################################################################################



################################################################################
## GUI
################################################################################
init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    if renpy.variant("small"):

        ## Font sizes.
        gui.text_size = 45
        gui.name_text_size = 47
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Adjust the location of the textbox.
        gui.textbox_height = 360
        gui.text_xpos = -85
        gui.name_ypos = -70
        gui.name_yalign = 0.9
        gui.dialogue_ypos = 125

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## File button layout.
        gui.file_slot_cols = 4
        gui.file_slot_rows = 1

        ## NVL-mode.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
