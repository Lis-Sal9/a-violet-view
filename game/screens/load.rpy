
## The script for loading data.
##
## In this script, there are a modal for loading slots and the screen for load to see all slots.

init -1 python:
    def DeleteSlot(slot):
        renpy.unlink_save(slot)

    def LoadSlot(slot, extra_info):
        renpy.load(slot)
        LoadPlayerDataJson(extra_info)


## Load pause menu #############################################################
## This submenu allows to choose different options: load the selected game, remove
## the selected game, and cancel the operation.
################################################################################
screen load_pause(slot, extra_info):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png" as panel
    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        textbutton _("Load") action [Function(LoadSlot, slot, extra_info), Hide("load_pause")]

        textbutton _("Remove Game") action [Function(DeleteSlot, slot), Hide("load_pause")]

        textbutton _("Cancel") action Hide("load_pause")
################################################################################


## Load screen #################################################################
## This screen is responsible for letting the player load the game with file_slots.
################################################################################
screen load():
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    tag menu
    add "images/load/load.png"

    image "images/load/load_cinema.png":
        align .5, .5

    text _("Carregar partida"):
        size 160
        font "fonts/my_font.otf"
        align .5, .05

    imagebutton:
        idle "gui/arrows/return.png"
        hover "gui/arrows/return_hover_blue.png"
        align .03, .94
        action Return()

    ## The grid of file slots.
    grid gui.file_slot_cols gui.file_slot_rows:
        style_prefix "slot"
        xalign 0.49
        yalign 0.48
        spacing 15

        $ current_page = float(page_name_value.get_page()) - 1
        $ num_items_per_page = gui.file_slot_cols * gui.file_slot_rows
        $ current_offset = current_page * num_items_per_page
        $ saved_games = renpy.list_saved_games()
        $ saved_games = filter(lambda x: ('reload' not in x[0]) and ('quick' not in x[0]) and ('auto' not in x[0]), saved_games)
        $ saved_games.sort(key = lambda x: x[-1], reverse = True)
        $ saved_games_len = len(saved_games)
        $ num_filled_slots = 0
        $ num_empty_slots = num_items_per_page

        ## Calculate the number of empty slots and filled slots.
        $ i = 0
        if saved_games_len > 0:
            for i in range(saved_games_len):
                $ num_filled_slots = num_filled_slots + 1
                $ i = i + 1

            if saved_games_len <= current_offset:
                $ num_filled_slots = 0
                $ num_empty_slots = num_items_per_page
            elif saved_games_len - current_offset >= num_items_per_page:
                $ num_filled_slots = num_items_per_page
                $ num_empty_slots = 0
            else:
                $ num_filled_slots = saved_games_len % num_items_per_page
                $ num_empty_slots = num_items_per_page - num_filled_slots

        ## Fill the slots with its screenshot
        $ j = 0
        if num_filled_slots > 0:
            for j in range(num_filled_slots):
                $ position = int(j + current_offset)
                $ saved_slot = saved_games[position]
                $ saved_slot_name = saved_slot[0]
                $ saved_slot_name_display = saved_slot_name.encode("utf-8")
                $ saved_slot_extra_info = saved_slot[1]
                $ saved_slot_displayable = saved_slot[2]
                $ slot_screenshot = renpy.slot_screenshot(saved_slot_name)

                button:
                    action Show("load_pause", slot=saved_slot_name_display, extra_info=saved_slot_extra_info)
                    xysize 430, 262
                    yoffset 30
                    xoffset 4
                    has vbox
                    add Frame(slot_screenshot) xalign 0.5
                    text saved_slot_name:
                        style "slot_name_text"
                        yoffset 2

                $ j = j + 1

        ## Fill the empty slots
        $ k = 0
        if num_empty_slots > 0:
            for k in range(num_empty_slots):
                $ k = k + 1
                imagebutton:
                    idle Frame("gui/button/slot_idle_background.png")
                    xalign 0.5
                    yoffset 28
                    xysize 430, 330
                    action NullAction()

    ## Buttons to access other pages.
    hbox:
        style_prefix "page"
        xalign 0.5
        yalign 0.98
        spacing gui.page_spacing

        textbutton _("<"):
            xysize 50, 50
            action FilePagePrevious()

        ## TODO: The maximum number of slots depends on number of choice scenes.
        for page in range(1, 11):
            textbutton "[page]":
                xysize 50, 50
                action FilePage(page)

        textbutton _(">"):
            xysize 50, 50
            action FilePageNext(max=10)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
############################################################################################
