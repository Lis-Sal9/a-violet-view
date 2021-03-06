
screen gallery_item_details(item):
    variant "touch"

    $ item_name = item["name"].replace(" ", "_")
    $ item_name = item_name.lower()

    imagebutton:
        xysize 1920, 1080
        idle Solid("0004")
        action NullAction()

    image "images/gallery/biography.png":
        align 0.5, 0.5
        zoom 1.15

    fixed:
        align .5, .5
        xysize 1000, 800

        imagebutton:
            idle Frame("gui/arrows/arrow_left.png")
            hover Frame("gui/arrows/arrow_left_hover.png")
            align 0, 0.05
            xysize 110, 60
            action Hide("gallery_item_details")


        add "images/gallery/women/" + item_name + ".png":
            yalign .35
            xoffset 10
            yoffset 20

        text item["content"]:
            size 27
            xysize 600, 600
            align .99, .35
            xoffset 20
            yoffset -10
            line_spacing 0
