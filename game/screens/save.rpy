
## The script for saving data.
##
## The save file has two params: saveName required and an optional string parameter. This parameter is serialized to JSON in this script.
define config.save_json_callbacks = [GetPlayerDataJson]

init -1 python:
    import json, time

    def FinishEnterSaveName():
        global saveName
        if not tmpSaveName:
            return
        if renpy.can_load(tmpSaveName):
            renpy.show_screen("confirm", message="This game already exists. Do you want overwrite it?", yes_action=[SetVariable("saveName", tmpSaveName), Function(SavePlayerData)], no_action=Show(screen="save_name_input", message="Please enter a save name.\nOnly numbers and letters allowed.", ok_action=Function(FinishEnterSaveName)))
        else:
            saveName = tmpSaveName
            SavePlayerData()
        return

    def SavePlayerData():
        config_save_params = {
            "player": player,
            "items_player": items_player,
            "saveName": saveName
        }
        json_obj = json.dumps(config_save_params)
        renpy.save(saveName, json_obj)
        renpy.notify(json_obj)
        return

    def OnSaveNameUpdate(value = ""):
        global tmpSaveName
        tmpSaveName = value

    def GetPlayerDataJson(data):
        data["player"] = player
        data["items_player"] = items_player
        data["saveName"] = saveName

    def LoadPlayerDataJson(extra_info):
        json_data = json.loads(x)
        player = json_data["player"]
        items_player = json_data["items_player"]
        saveName = json_data["saveName"]


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

        textbutton _("Save") action [If(saveName, true=[Hide("save_menu"), Function(SavePlayerData)], false=[Hide("save_menu"), Show(screen="save_name_input", message="Please enter a save name.\nOnly numbers and letters allowed.", ok_action=Function(FinishEnterSaveName))])]

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
