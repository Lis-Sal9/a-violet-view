
## Preferences screen ######################################################################
## The preferences screen allows the player to configure the game to better suit themselves.
############################################################################################
init -100 python:
    LANGUAGES = ["catalan", "english", "spanish"]
    def init_language():
        if _preferences.language is None or _preferences.language is "None":
            _preferences.language = LANGUAGES[0]
            return 0
        else:
            return LANGUAGES.index(_preferences.language)
            
init -10 python:
    current_lang = init_language()
    def getCurrentLangShort():
        if _preferences.language == "english":
            return "EN"
        elif _preferences.language == "spanish":
            return "ES"
        elif _preferences.language == "catalan":
            return "CA"


default show_bar_music_volume = False
default show_bar_text_speed = False

screen preferences(from_main_menu = False):
    tag menu
    add "images/preferences/preferences_bg.png"

    fixed:
        align .5, .5

        text _("Preferències"):
            color "#ecc6ad"
            font "fonts/my_font.otf"
            size 115
            align .47, .08

        imagebutton:
            idle "gui/arrows/return_hover_blue.png"
            hover "gui/arrows/return_brown.png"
            align .03, .94
            action [Return(), SetVariable("show_bar_music_volume", False), SetVariable("show_bar_text_speed", False)]

        if renpy.variant("pc"):
            text _("Visualització"):
                color "#f6f69f"
                size 24
                align .475, .922

            imagebutton:
                if _preferences.fullscreen:
                    idle "images/preferences/preferences_fullscreen.png"
                    hover "images/preferences/preferences_fullscreen.png"
                else:
                    idle "images/preferences/preferences_fullscreen_hover.png"
                    hover "images/preferences/preferences_fullscreen.png"
                align .458, .94
                action Preference("display", "fullscreen")


            imagebutton:
                if not _preferences.fullscreen:
                    idle "images/preferences/preferences_window.png"
                    hover "images/preferences/preferences_window.png"
                else:
                    idle "images/preferences/preferences_window_hover.png"
                    hover "images/preferences/preferences_window.png"
                align .504, .94
                action Preference("display", "window")


        text _("Idioma"):
            color "#f6f69f"
            size 24
            align .31, .817

        if from_main_menu:
            imagebutton:
                idle "images/preferences/preferences_language.png"
                hover "images/preferences/preferences_language_hover.png"
                align .351, .817
                action [Language(LANGUAGES[(current_lang + 1) % 3]), SetVariable("current_lang", (current_lang + 1) % 3)]

        $ curr_lang_short = getCurrentLangShort()
        text curr_lang_short:
            color "#2f2929"
            font "fonts/digital_dreams.ttf"
            size 35
            align .395, .875

        python:
            dial_musicvolume = (_preferences.volumes["music"] * 300) - 150

        text _("Música"):
            color "#f6f69f"
            size 24
            align .313, .85

        imagebutton:
            idle "images/preferences/preferences_music.png"
            hover "images/preferences/preferences_music_hover.png"
            xpos 605
            ypos 970
            anchor .5, .5
            action [SetVariable("show_bar_music_volume", (not show_bar_music_volume)), SetVariable("show_bar_text_speed", False)]
            at transform:
                linear 0 rotate dial_musicvolume


        python:
            val_textspeed = (preferences.text_cps - 1) * 1.5
            if val_textspeed < 0:
                val_textspeed = 300
            val_textspeed = val_textspeed - 150

        text _("Text"):
            color "#f6f69f"
            size 24
            align .64, .85

        imagebutton:
            idle "images/preferences/preferences_music.png"
            hover "images/preferences/preferences_music_hover.png"
            xpos 1227
            ypos 970
            anchor .5, .5
            action [SetVariable("show_bar_text_speed", (not show_bar_text_speed)), SetVariable("show_bar_music_volume", False)]
            at transform:
                linear 0 rotate val_textspeed

        hbox:
            style_prefix "custom_slider"
            box_wrap True

            if show_bar_music_volume:
                vbox:
                    bar:
                        value Preference("music volume")
                        anchor 0.5, 0.5
                        pos 605, 1020

            if show_bar_text_speed:
                vbox:
                    bar:
                        value Preference("text speed")
                        anchor 0.5, 0.5
                        pos 1227, 1020


style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style slider_slider:
    xsize 300
    ysize 20
    base_bar Frame("images/preferences/preferences_bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "images/preferences/preferences_thumb.png"

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 300
################################################################################
