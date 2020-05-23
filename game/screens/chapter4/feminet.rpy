
## This script is for Feminet in chapter 4.


init -10 python:
    chimamanda_movie = ""

    def publishArticle(id):
        global game_state
        game_state.published_article = id

    def initVideo():
        global chimamanda_movie
        if _preferences.language == "english":
            chimamanda_movie = Movie(play="video/chimamanda_en.mkv")
        elif _preferences.language == "spanish":
            chimamanda_movie = Movie(play="video/chimamanda_es.mkv")
        elif _preferences.language == "catalan":
            chimamanda_movie = Movie(play="video/chimamanda_ca.mkv")



screen feminet:

    fixed:
        align .5, .5
        image "images/chapter4/feminet/social_base.png":
            align 0.99, 0

        imagebutton:
            idle "images/chapter4/femiblog/nav_tab_idle.png"
            align .062, 0
            action [Hide("feminet"), Show(screen="femiblog")]

        text _("FEMIBLOG"):
            align .062, 0.002
            size 30
            color "#455a64"

        image "images/chapter4/femiblog/nav_tab_selected.png":
            align .262, 0

        text _("FEMINET"):
            align .242, 0.002
            size 30
            color "#000000"

        image "images/chapter4/femiblog/nav_back_disabled.png":
            align .053, .04

        text _("www.femi.net/[tmpSavePlayer]"):
            align .093, .043
            size 25
            color "#000000"

        fixed:
            align .58, .13
            xysize 1000, 100
            text _("@[tmpSavePlayer]"):
                size 75
                color "#ffffff"

        imagebutton:
            idle "images/chapter4/feminet/social_plume.png"
            hover "images/chapter4/feminet/social_plume_hover.png"
            align .821, .14
            action Show(screen="post_message")


    viewport id "vp":
        align .58, .75
        xysize 960, 700
        draggable True
        mousewheel True
        yinitial 0

        vbox:
            spacing 40
            xsize 950

            hbox:
                spacing 20
                image Frame("images/chapter4/feminet/social_user_avatar.png", xysize=[60,60])

                text _("@chimangoadichie_fan"):
                    size 50
                    color "#ffffff"

            text _("{i}Tothom hauria de ser feminista{/i} (2012), de Chimamanda Ngozi Adichie."):
                size 30
                color "#ffffff"
                xsize 930

            imagebutton:
                idle Frame("images/chapter4/feminet/social_video.png", xysize=[900, 500])
                hover Frame("images/chapter4/feminet/social_video_hover.png", xysize=[900, 500])
                action Function(initVideo)

            hbox:
                spacing 20
                image Frame("images/chapter4/feminet/social_user_avatar.png", xysize=[60,60])

                text _("@sonyareneetaylor_fan"):
                    size 50
                    color "#ffffff"

            text _("Com a feminista negra queer, Sonya Renee Taylor vesteix aquest cosset negre sobre els seus 104 kg per proclamar el seu poder i atractiu. L’empoderament i l’autoestima davant el terrorisme corporal contra les persones marginades ha de ser denunciat! {i}The Body Is Not An Apology{/i}!"):
                size 30
                color "#ffffff"
                xsize 930

            image Frame("images/chapter4/feminet/sonya_renee_taylor.jpg", xysize=[450, 300])

            hbox:
                spacing 20
                image Frame("images/chapter4/feminet/social_user_avatar.png", xysize=[60,60])

                text _("@niunamenos_help"):
                    size 50
                    color "#ffffff"

            text _("La violència contra les dones no és una simple qüestió d’homes individuals, sinó d’estructures de poder més àmplies que normalitzen el menyspreu d’homes cap a dones, i els assassinats són el cas més extrem. Protesta contra el feminicidi i la inacció policial al respecte. Ja n’hi ha prou d’assassinar a les persones pel seu gènere!! Nos queremos vivas, libres y sin miedo!! Ni una menos!!"):
                size 30
                color "#ffffff"
                xsize 930

            hbox:
                spacing 20
                image Frame("images/chapter4/feminet/niunamenos_1.jpg", xysize=[450, 300])
                image Frame("images/chapter4/feminet/niunamenos_2.jpg", xysize=[450, 300])



    vbar:
        value YScrollValue("vp")
        align .97, .75
        ysize 750



screen post_message:
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png" as panel
    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 50
            xysize 1500, 820

        text _("Què vols publicar?"):
            color "#ffffff"

        hbox:
            align .5, .5
            spacing 30
            xysize 1500, 640

            fixed:
                xysize 480, 500
                spacing 20

                imagebutton:
                    idle "images/chapter4/feminet/social_post_select_border.png"
                    hover "images/chapter4/feminet/social_post_select_border_hover.png"
                    action [Function(publishArticle, id=1), Hide("post_message")]

                vbox:
                    xysize 470, 490
                    xalign .5
                    xoffset 5
                    yoffset 5
                    spacing 15

                    text _("La meva roba no és el meu consentiment"):
                        size 30
                        color "#ffffff"
                        bold True

                    text _("La {i}SlutWalk{/i} és una marxa de protesta contra la culpabilització de les víctimes de violència sexual. Fan referència al concepte {i}slut{/i} ({i}puta{/i}) per defensar el dret de les dones a la llibertat sexual sense ser jutjades. Les persones participants mostren símbols prosexe, organitzen tallers i parlen de les seves experiències com a supervivents."):
                        size 25
                        color "#ffffff"

                    image Frame("images/chapter4/feminet/slutwalk.jpg", xysize=[450, 250])

            fixed:
                xysize 480, 500
                spacing 20

                imagebutton:
                    idle "images/chapter4/feminet/social_post_select_border.png"
                    hover "images/chapter4/feminet/social_post_select_border_hover.png"
                    action [Function(publishArticle, id=2), Hide("post_message")]

                vbox:
                    xysize 470, 490
                    xalign .5
                    xoffset 5
                    yoffset 5
                    spacing 15

                    text _("#MeToo"):
                        size 30
                        color "#ffffff"
                        bold True

                    text _("Tarana Burke fundà el moviment #MeToo de supervivents desfavorides de la violència sexual. No obstant això, es va fer viral amb el cas contra Harvey Weinstein. L’efecte social causat s’ha traduït en implicacions en la societat, la legislació i la vida. Per exemple, hi ha major defensa de la igualtat en les arts escèniques, s’ha prescindit d’hostesses en l’automobilisme, i s’han creat lleis per no subvencionar mitjans de comunicació que incloguin publicitat amb continguts per adults."):
                        size 25
                        color "#ffffff"

                    image Frame("images/chapter4/feminet/metoo.jpg", xysize=[390, 200])

            fixed:
                xysize 480, 500
                spacing 20

                imagebutton:
                    idle "images/chapter4/feminet/social_post_select_border.png"
                    hover "images/chapter4/feminet/social_post_select_border_hover.png"
                    action [Function(publishArticle, id=3), Hide("post_message")]

                vbox:
                    xysize 470, 490
                    xalign .5
                    xoffset 5
                    yoffset 5
                    spacing 15

                    text _("Hollaback!"):
                        size 30
                        color "#ffffff"
                        bold True

                    text _("Hollaback! (2005) és una plataforma amb la missió d’acabar amb l’assetjament en espais públics en totes les seves formes, en la qual es permet a dones assetjades sexualment denunciar públicament els incidents amb el relat i la foto dels seus assetjadors. Treballem plegats per comprendre el problema, tenir discussions públiques i desenvolupar estratègies innovadores que es tradueixin en entorns segurs i acollidors per tothom. Tots mereixem ser qui som, estem on estem."):
                        size 25
                        color "#ffffff"

                    image Frame("images/chapter4/feminet/hollaback!.png", xysize=[400, 150])

        hbox:
            align .99, .9
            textbutton _("Cancel·lar") action Hide("post_message")
