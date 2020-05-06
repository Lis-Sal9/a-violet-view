
## Script for the train scene.
## To change the chapter ...


init python:
    CHAPTERS = ["P", "1", "2", "3", "E"]

    def setChapter(chapter_completed):
        global game_state
        if chapter_completed not in game_state.chapters_completed:
            game_state.chapters_completed.append(chapter_completed)


# Train background
label train(chapter_completed):
    $ renpy.choice_for_skipping()
    $ setChapter(chapter_completed)

    image bg_train = "images/train/train_bg.png"
    image img_train = "images/train/train_img.png"

    transform moving:
        rotate 2
        yalign 0.60 xpos 2500
        linear 15.0 xpos -3000 yalign 0.72

    stop music fadeout 0.5
    scene bg_train
    play music "audio/sound/train.mp3" fadein 0.5
    show img_train at moving
    call screen hold_screen(15)
    stop music fadeout 0.5

    if len(game_state.chapters_completed) < 3:
        call screen library

    return
