
## Script for the train scene.
## To change the chapter ...


# Train background
label train:

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

    if game_state.chapter == 0:
        call chapter_1

    return