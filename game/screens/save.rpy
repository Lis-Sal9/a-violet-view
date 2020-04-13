
## The script for saving data.
##
## The save file has two params: saveName required and an optional string parameter. This parameter is serialized to JSON in this script.

init -1 python:
    import json, time

    def FinishEnterSaveName():
        global game_state
        if not tmpSaveName:
            return
        if renpy.can_load(tmpSaveName):
            renpy.show_screen("confirm", message="This game already exists. Do you want overwrite it?", yes_action=[SetVariable("game_state.save_name", tmpSaveName), Function(SavePlayerData)], no_action=Show(screen="save_name_input", message="Please enter a save name.\nOnly numbers and letters allowed.", ok_action=Function(FinishEnterSaveName)))
        else:
            game_state.save_name = tmpSaveName
            game_state.player = tmpSavePlayer
            SavePlayerData()
        return

    def SavePlayerData():
        json_obj = json.dumps(game_state.__dict__)
        renpy.save(game_state.save_name, json_obj)
        renpy.notify(_("Saved successfully."))
        return

    def OnSaveNameUpdate(value = ""):
        global tmpSaveName
        tmpSaveName = value

    def OnSavePlayerUpdate(value = ""):
        global tmpSavePlayer
        tmpSavePlayer = value

    def LoadPlayerDataJson(extra_info):
        global game_state
        game_state = json.loads(extra_info)


## Save menu screen ############################################################
## Ask player for save, and save name
################################################################################
screen save_menu():
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png" as panel
    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        textbutton _("Save") action [If(game_state.save_name, true=[Hide("save_menu"), Function(SavePlayerData)], false=[Hide("save_menu"), Show(screen="save_name_input", message="Please enter a save name.\nOnly numbers and letters allowed.", ok_action=Function(FinishEnterSaveName))])]

        textbutton _("Save as") action [Hide("save_menu"), Show(screen="save_name_input", message="Please enter a save name.\nOnly numbers and letters allowed.", ok_action=Function(FinishEnterSaveName))]

        textbutton _("Cancel") action Hide("save_menu")
################################################################################


## SaveName input screen #######################################################
## Ask for save slot name
################################################################################
screen save_name_input(message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Hide("save_name_input"), ok_action]

    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" length 20 allow "ABCÇDEFGHIJKLMNÑOPQRSTUVWXYZabcçdefghijklmnñopqrstuvwxyz0123456789" changed OnSaveNameUpdate

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action [Hide("save_name_input"), ok_action]
            textbutton _("Cancel") action Hide("save_name_input")
################################################################################
