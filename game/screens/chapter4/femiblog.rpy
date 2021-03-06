
## This script is for Femiblog in chapter 4.


init -1 python:
    def checkIfEcoIsSeen():
        global game_state
        if not game_state.eco_is_seen:
            game_state.eco_is_seen = True

screen femiblog:

    fixed:
        align .5, .5
        image "images/chapter4/femiblog/femiblog.png":
            align 0.99, 0

        image "images/chapter4/femiblog/nav_tab_selected.png":
            align .062, 0

        text _("FEMIBLOG"):
            align .062, 0.002
            size 30
            color "#000000"

        imagebutton:
            idle "images/chapter4/femiblog/nav_tab_idle.png"
            align .262, 0
            action [Hide("femiblog"), Show(screen="feminet")]

        text _("FEMINET"):
            align .242, 0.002
            size 30
            color "#455a64"

        image "images/chapter4/femiblog/nav_back_disabled.png":
            align .053, .04

        fixed:
            xysize 1400, 40
            align .3, .043
            text _("www.femiblog.cat/home"):
                size 25
                color "#000000"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_section_idle.png"
            hover "images/chapter4/femiblog/femiblog_section_hover.png"
            align .913, .215
            action [Hide("femiblog"), SetVariable("femiblog_post_active", True), Show(
            screen="post",
            title=_("{i}Feministing{/i}"),
            content_0=_("Internet i les xarxes socials han permès organitzar i promoure protestes. Per una banda, és una eina empoderadora perquè permet conscienciar a les persones, realitzar una gestió comunitària, i una major accessibilitat i rapidesa, però d’altra banda, és perjudicial perquè es poden donar casos de {i}trolling{/i} (publicacions amb missatges incendiaris pensats per provocar odi), {i}doxxing{/i} (publicar dades personals per incitar a la intimidació i l’assetjament), {i}amenaces de violació i mort{/i}, i {i}pornografia venjativa{/i} (publicació de fotos o vídeos íntims d’una persona a Internet sense el seu coneixement ni consentiment)."),
            content_1=_("No obstant això, hem decidit retre homenatge amb aquest blog a les germanes Jessica i Vanessa Valentí, creadores del blog {i}Feministing{/i} (2004), en el qual reunien un ampli ventall de veus femenines. Aquest blog incloïa articles d’actualitat i anàlisi en profunditat i posterior secció de comentaris, i fòrums de discussió. En aquest sentit, va contribuir a la visibilitat dels assumptes feministes."),
            image_0="images/chapter4/femiblog/feministing.png",
            x_0=300, y_0=200,
            path=_("feministing"))]

        text _("{i}Feministing{/i}"):
            align .913, .215
            size 35
            color "#ffffff"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_section_idle.png"
            hover "images/chapter4/femiblog/femiblog_section_hover.png"
            align .913, .295
            action [Hide("femiblog"), SetVariable("femiblog_post_active", True), Show(
            screen="post",
            title=_("{i}#EverydaySexism{/i}"),
            content_0=_("Les dones del món comparteixen les seves experiències del sexisme. Dones de totes les edats, classes, races. Es preté legitimar la sensació d’agreujament de les dones. Es mostra l’omnipresència del sexisme i la normalització social de les seves formes menors, que acostumen a considerar-se trivials, que permet prosperar a la misoginia subjacent en els casos més greus d’abús i opressió. Segons Laura Bates, la lluita contra el sexisme actualment no és assumpte solament d’homes, sinó de persones contra prejudicis."),
            image_0="images/chapter4/femiblog/everyday_sexism.jpg",
            image_1="images/chapter4/femiblog/girls.jpg",
            x_0=400, y_0=600, x_1=400, y_1=400,
            path=_("everyday-sexism"))]

        text _("{i}#EverydaySexism{/i}"):
            align .913, .295
            size 35
            color "#ffffff"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_section_idle.png"
            hover "images/chapter4/femiblog/femiblog_section_hover.png"
            align .913, .375
            action [Hide("femiblog"), SetVariable("femiblog_post_active", True), Show(
            screen="post",
            title=_("{i}#BringBackOurGirls{/i}"),
            content_0=_("L’any 2014, l’exèrcit armat del grup yihadista Boko Haram va segrestar més dues-centes nenes a Chibock, Nigèria. Activistes pels drets humans a Nigèria en conjunt amb familiars de les nenes segrestades han dut a terme la campanya {i}#BringBackOurGirls{/i}, un moviment que busca pressionar el govern per a què incrementi els esforços en el rescat de les menors en cautiveri. Aquest grup terrorista ha estat motivat per l’oposició al dret de la dona a l’educació. Avui dia, encara hi ha nenes desaparegudes que no han tornat amb les seves famílies."),
            image_0="images/chapter4/femiblog/bring_back_our_girls.png",
            image_1="images/chapter4/femiblog/bbog_education.jpg",
            x_0=600, y_0=400, x_1=600, y_1=400,
            path=_("bring-back-our-girls"))]

        text _("{i}#BringBackOurGirls{/i}"):
            align .913, .375
            size 35
            color "#ffffff"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_section_idle.png"
            hover "images/chapter4/femiblog/femiblog_section_hover.png"
            align .913, .455
            action [Hide("femiblog"), SetVariable("femiblog_post_active", True), Show(
            screen="post",
            title=_("{i}The Hunting Ground{/i}"),
            content_0=_("{i}The Hunting Ground{/i} (2015) és un documental sobre les experiències de dones i persones d’altres gèneres quan informaren de violència sexual en els campus universitaris. La resposta de les autoritats acadèmiques i la policia va consistir en culpar a aquelles persones que havien informat o en demanar que consideressin el futur del perpetrador."),
            image_0="images/chapter4/femiblog/hunting.jpg",
            x_0=400, y_0=600,
            path=_("the-hunting-ground"))]

        text _("{i}The Hunting Ground{/i}"):
            align .913, .455
            size 35
            color "#ffffff"

        if not game_state.eco_is_seen:
            imagebutton:
                align .913, .85
                idle "images/chapter4/femiblog/eco_friendly.png"
                hover "images/chapter4/femiblog/eco_friendly_hover.png"
                action [Function(GiveGlossaryItemToPlayer,12), Function(ShowItems), Function(checkIfEcoIsSeen)]
        else:
            image "images/chapter4/femiblog/eco_friendly.png":
                align .913, .85

        text _("Recolza la causa"):
            size 50
            align .85, .6
            xsize 170
            color "#ffffff"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_article_1_idle.png"
            hover "images/chapter4/femiblog/femiblog_article_1_hover.png"
            align .231, .3
            action [Hide("femiblog"), SetVariable("femiblog_post_active", True), Show(
                screen="post",
                title=_("Malala Yousafzai i l’educació global"),
                content_0=_("Malala Yousafzai és una activista pakistaní defensora del dret a l’educació de les nenes i les dones. Li encantava anar a l’escola i aprendre conjuntament amb el seu pare, professor, i les seves companyes. No obstant això, tot canvià quan els talibans van prendre el control del seu poble. Els extremistes radicals varen prohibir a les nenes assistir a l’escola, però ella, incapaç d’acceptar el destí imposat, començà a parlar sobre el dret a l’educació per diferents llocs del país, malgrat els perills que suposava.\n\nVa seguir promovent els seus ideals com a bloguera per la BBC. A més a més, va donar un discurs públic per recuperar els drets revocats a les nenes. A partir d’aquell moment, es convertí en objectiu dels talibans. En aquell mateix any, un assaltant talibà la va disparar en el costat esquerre del seu cap quan viatjava en l’autobús escolar. Dues nenes més varen ser ferides també. Tot i la gravetat de les seves ferides, fou traslladada en helicòpter a l’hospital i allà li salvaren la vida.\n\nDesprés d’operacions vàries i rehabilitació, els terroristes la tornaren a amenaçar, però no la van acoquinar. Es va traslladar amb la seva família al Regne Unit. Amb ajuda del seu pare, va poder veure materialitzat el seu somni amb la fundació Malala ({i}Malala Fund{/i}), l’objectiu de la qual era donar oportunitats a totes les nenes per assolir el futur que desitjaven. Així, Malala Yousafzai es convertí en la persona més jove en guanyar el premi Nobel de la Pau."),
                content_1=_("En relació a l’educació global de les nenes, un dels objectius de l’Organització de les Nacions Unides (ONU) és promoure la igualtat de gènere i l’autonomia de la dona. Els grups de pressió feministes recolzen aquests objectius, però consideren que estan excessivament centrats en els beneficis econòmics de l’aprenentatge. Insisteixen en què l’educació és tant un dret com un mitjà per formar futures dones i aportar confiança per assolir les seves aspiracions. També qüestionen la manera en què s’ensenya a les nenes, si els plans d’estudi haurien de ser més inclusius i quins estudis posteriors hi ha disponibles per satisfer les necessitats locals."),
                image_0="images/chapter4/femiblog/malala.jpg",
                image_1="images/chapter4/femiblog/malala_fund.png",
                x_0=800, y_0=500, x_1=300, y_1=200,
                path=_("malala-yousafzai-i-educacio-global"))]

        text _("Malala Yousafzai i l’educació global"):
            align .265, .461
            xysize 300, 100
            size 40
            color "#ffffff"
            text_align .5
            line_spacing -5

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_article_2_idle.png"
            hover "images/chapter4/femiblog/femiblog_article_2_hover.png"
            align .585, .3
            action [Hide("femiblog"), SetVariable("femiblog_post_active", True), Show(
            screen="post",
            title=_("El feminisme universal"),
            content_0=_("Què defineix a una persona feminista? Creure que el gènere està socialment condicionat, reconèixer el patriarcat, desafiar la misoginia, defensar l’autonomia corporal, i buscar la igualtat de gènere.\n\nEn {i}How to be a woman{/i} (2011), Caitlin Morán usa l’humor per presentar la idea del feminisme com una filosofia de sentit comú. Narra fets de la seva pròpia vida, des de com s’anomenaven les parts del cos en la seva família, fins la pressió per eliminar el pèl corporal, portar tacons a l’adolescència, o l’experiència d’un avortament en l’edat adulta. Manté que la vida de les dones del segle XXI està inextricablement lligada a les conquestes històriques del feminisme. Rebutja la idea de que el feminisme sigui solament per un subconjunt de dones i afirma que hi ha lloc inclús per a dones que viuen d’una manera tradicionalment no feminista."),
            content_1=_("En recerca d’un feminisme universal, es duu a terme la campanya {i}#HeForShe{/i}, la qual busca recolzament actiu dels homes en la prevenció de violència contra les dones. Insisteix en el dret de les dones i els homes a la igualtat, en què s’ha de posar fi a la percepció del feminisme com a motivació per l’odi als homes. I, estableix que el feminisme no és un assumpte de dones, sinó de drets humans i, per tant, també concerneix els homes; ells també mereixen ser alliberats dels estereotips de gènere."),
            image_0="images/chapter4/femiblog/caitlin.jpg",
            image_1="images/chapter4/femiblog/heforshe.png",
            x_0=400, y_0=600, x_1=300, y_1=200,
            path=_("el-feminisme-universal"))]

        text _("El feminisme universal"):
            align .57, .459
            size 40
            color "#ffffff"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_article_3_idle.png"
            hover "images/chapter4/femiblog/femiblog_article_3_hover.png"
            align .231, .845
            action [Hide("femiblog"), SetVariable("femiblog_post_active", True), Show(
            screen="post",
            title=_("Feminisme anticapitalista"),
            content_0=_("El capitalisme és un sistema econòmic erroni que produeix una gran desigualtat d’ingressos i reforça la subordinació de les dones. Les raons per a la bretxa salarial entre homes i dones poden ser voluntàries, com la mitja jornada, i involuntàries, com la discriminació per mandat social. Segons la teoria de la discriminació laboral, les dones eren considerades menys capaces que els homes, sobretot respecte de la maternitat al suposar tenir menys productivitat i compromís al veure’s interrompuda la seva dedicació, i per la falta de guarderies públiques que les obliga a treballar menys hores. L’educació té un paper rellevant, tot i haver menys dones que estudien carreres científiques i tecnològiques, que acostuma a encaminar cap a treballs millor remunerats.\n\nLaurie Penny, en {i}Meat Market: Female Flesh Under Capitalism{/i} (2011), ataca el feminisme liberal i el marxisme com a falses rutes cap a l’alliberació de les dones. Exposa com el capitalisme converteix els cossos de les dones en mercaderia i influeix en l’esfera domèstica, on es manté una divisió desigual de la feina entre homes i dones. La mercantilització capitalista es mostra en l’impost rosa, pel qual productes essencials per a dones són més cars que els mateixos per a homes. En aquest sentit, es produeix un desequilibri agreujat per la bretxa salarial de gènere i comporta menys poder adquisitiu per les dones."),
            content_1=_("De la mateixa manera, Kathi Weeks, en {i}The Problem with Work{/i} (2011), afirma que el moviment marxista i feminista han acceptat el treball remunerat com a mètode principal de la distribució d’ingressos. És per aquest motiu que proposa una sociedad {i}postlaboral{/i} en la qual totes les persones mantingudes per l’Estat produeixen per sí mateixes, resultant-ne un enriquiment cultural. El treball és una institució que pot i ha de ser qüestionada."),
            image_0="images/chapter4/femiblog/meat.jpg",
            image_1="images/chapter4/femiblog/problem.jpg",
            x_0=400, y_0=600, x_1=400, y_1=600,
            path=_("feminisme-anticapitalista"))]

        text _("Feminisme anticapitalista"):
            align .254, .85
            size 40
            color "#ffffff"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_article_4_idle.png"
            hover "images/chapter4/femiblog/femiblog_article_4_hover.png"
            align .585, .845
            action [Hide("femiblog"), SetVariable("femiblog_post_active", True), Show(
            screen="post",
            title=_("El sistema prostitucional i el mercat dels desitjos"),
            content_0=_("El capitalisme ha convertit la prostitució en un sistema prostitucional, és a dir, en un sistema com a conjunt estructurat i racionalment entrellaçat d’actors i interessos que han institucionalizat i institucionalitzen la subordinació de les dones i la seva permanent disponibilitat pels homes. No és un assumpte apolític ni segueix el mite de la lliure elecció, sinó que com a exemples de factors determinants hi ha la situació econòmica, l’activitat migratòria, el turisme sexual i/o el poder simbòlic.\n\nS’ha produït un increment de la trata de dones i de l’expansió de la {i}indústria del sexe femení{/i}, íntimament relacionada amb polítiques migratòries, la recent crisi econòmica mundial, la feminització de la pobresa i la transforamció de l’economia de mercat en societats de mercat, és a dir, res a veure amb la lliure elecció. El mercat prostitucional s’alimenta, fonamentalment, de la trata de dones, ja que hi ha implicació d’estratègies de captació i coacció.\n\nAquest resulta ser un mercat global que satisfà una demanda potencialment il·limitada amb dones pobres. Per alguns països pobres, és significativament més productiu prostituir les seves nenes que educar-les. Així ho feu saber el Banc Mundial a alguns d’aquests països més endeutats, aconsellant-los que paguessin el deute dedicant a les seves dones al negoci de l’{i}oci masculí{/i}, fet que reconeix desaparegut el dret de les dones pobres a no ser prostituïdes.\n\nLa prostitució i la gestació subrogada perpetuen la ideologia que sosté que el cos de les dones existeix per a la satisfacció i els objectius i desitjos d’altres. Si bé l’apropiació del cos, la sexualitat i la capacitat reproductiva de les dones no és cap novetat, sí ho és el fet de mercantilitzar la dissolució del vincle existent entre la gestació i la maternitat; les dones són éssers destinats a custodiar i parir allò que altres creen i desitgen. D’aquesta manera, la gestació comercial remet a ciutadania censitària, en la qual solament les persones amb capacitat econòmica suficient tenen garantida una descendència a demanda."),
            content_1=_("Finalment, Carol Leigh encunyà el concepte {i}treball sexual{/i}, amb el qual pretén retornar la dignitat que s’és negada a la paraula {i}prostituta{/i}. Gràcies a ella, s’està normalitzant el concepte de treball sexual com a activitat laboral legítima que ofereix oportunitats i independència econòmica. No obstant això, les persones voluntàriament dedicades segueixen estigmatitzades i no tenen els mateixos drets que en altres sectors."),
            image_1="images/chapter4/femiblog/atwood.jpg",
            x_1=400, y_1=600,
            path=_("el-sistema-prostitucional-i-el-mercat-dels-desitjos"))]

        text _("El sistema prostitucional i el mercat dels desitjos"):
            align .582, .875
            xysize 350, 100
            size 40
            color "#ffffff"
            text_align .5
            line_spacing -5

define femiblog_post_active = False
define femiblog_post_last_title = ""
define femiblog_post_last_content_0 = ""
define femiblog_post_last_content_1 = ""
define femiblog_post_last_image_0 = ""
define femiblog_post_last_image_1 = ""
define femiblog_post_last_xsize_0 = 1000
define femiblog_post_last_ysize_0 = 1000
define femiblog_post_last_xsize_1 = 1000
define femiblog_post_last_ysize_1 = 1000
define femiblog_post_last_path = "home"

screen post(title="", content_0="", content_1="", image_0="", image_1="", x_0=1000, y_0=1000, x_1=1000, y_1=1000, path="home"):
    default adj = ui.adjustment()
    python:
        global femiblog_post_last_path
        global femiblog_post_last_title
        global femiblog_post_last_image_0
        global femiblog_post_last_image_1
        global femiblog_post_last_xsize_0
        global femiblog_post_last_xsize_1
        global femiblog_post_last_ysize_0
        global femiblog_post_last_ysize_1
        global femiblog_post_last_content_0
        global femiblog_post_last_content_1

        femiblog_post_last_title = title
        femiblog_post_last_content_0 = content_0
        femiblog_post_last_content_1 = content_1
        femiblog_post_last_image_0 = image_0
        femiblog_post_last_image_1 = image_1
        femiblog_post_last_xsize_0 = x_0
        femiblog_post_last_ysize_0 = y_0
        femiblog_post_last_xsize_1 = x_1
        femiblog_post_last_ysize_1 = y_1
        femiblog_post_last_path = path

    fixed:
        align .5, .5
        image "images/chapter4/femiblog/femiblog_base.png":
            align 0.99, 0

        imagebutton:
            idle "images/chapter4/femiblog/nav_back.png"
            align .053, .04
            action [Hide(screen="post"), SetVariable("femiblog_post_active", False), Show(screen="femiblog")]

        image "images/chapter4/femiblog/nav_tab_selected.png":
            align .062, 0

        text _("FEMIBLOG"):
            align .062, 0.002
            size 30
            color "#000000"

        imagebutton:
            idle "images/chapter4/femiblog/nav_tab_idle.png"
            align .262, 0
            action [Hide("femiblog"), Show(screen="feminet")]

        text _("FEMINET"):
            align .242, 0.002
            size 30
            color "#455a64"

        fixed:
            xysize 1400, 40
            align .3, .043
            text _("www.femiblog.cat/"+str(_(path))):
                size 25
                color "#000000"

        text _(title):
            size 75
            font "fonts/impact.ttf"
            align .3, .1
            xysize 1000, 400

        viewport id "femiblog_vp":
            align .5, .65
            xysize 1270, 600
            draggable True
            mousewheel True
            yinitial 0
            yadjustment adj

            vbox:
                spacing 20
                xsize 1070

                if not image_0 == "":
                    image Frame(image_0, xysize=[x_0,y_0])

                if not content_0 == "":
                    text _(content_0):
                        align .5, .2
                        xysize 1070, 1000

                if not image_1 == "":
                    image Frame(image_1, xysize=[x_1,y_1])

                if not content_1 == "":
                    text _(content_1):
                        align .5, .2
                        xysize 1070, 1000

        vbar:
            value YScrollValue("femiblog_vp")
            align .97, .65
            ysize 600

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_section_idle.png"
            hover "images/chapter4/femiblog/femiblog_section_hover.png"
            selected_idle "images/chapter4/femiblog/femiblog_section_hover.png"
            selected_hover "images/chapter4/femiblog/femiblog_section_hover.png"
            align .913, .215
            selected title == "{i}Feministing{/i}"
            action [Hide("femiblog"),
                Function(adj.change, 0),
                Show(
                    screen="post",
                    title=_("{i}Feministing{/i}"),
                    content_0=_("Internet i les xarxes socials han permès organitzar i promoure protestes. Per una banda, és una eina empoderadora perquè permet conscienciar a les persones, realitzar una gestió comunitària, i una major accessibilitat i rapidesa, però d’altra banda, és perjudicial perquè es poden donar casos de {i}trolling{/i} (publicacions amb missatges incendiaris pensats per provocar odi), {i}doxxing{/i} (publicar dades personals per incitar a la intimidació i l’assetjament), {i}amenaces de violació i mort{/i}, i {i}pornografia venjativa{/i} (publicació de fotos o vídeos íntims d’una persona a Internet sense el seu coneixement ni consentiment)."),
                    content_1=_("No obstant això, hem decidit retre homenatge amb aquest blog a les germanes Jessica i Vanessa Valentí, creadores del blog {i}Feministing{/i} (2004), en el qual reunien un ampli ventall de veus femenines. Aquest blog incloïa articles d’actualitat i anàlisi en profunditat i posterior secció de comentaris, i fòrums de discussió. En aquest sentit, va contribuir a la visibilitat dels assumptes feministes."),
                    image_0="images/chapter4/femiblog/feministing.png",
                    x_0=300, y_0=200,
                    path=_("feministing"))]

        text _("{i}Feministing{/i}"):
            align .913, .215
            size 35
            color "#ffffff"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_section_idle.png"
            hover "images/chapter4/femiblog/femiblog_section_hover.png"
            selected_idle "images/chapter4/femiblog/femiblog_section_hover.png"
            selected_hover "images/chapter4/femiblog/femiblog_section_hover.png"
            align .913, .295
            selected title == "{i}#EverydaySexism{/i}"
            action [Hide("femiblog"),
                Function(adj.change, 0),
                Show(
                    screen="post",
                    title=_("{i}#EverydaySexism{/i}"),
                    content_0=_("Les dones del món comparteixen les seves experiències del sexisme. Dones de totes les edats, classes, races. Es preté legitimar la sensació d’agreujament de les dones. Es mostra l’omnipresència del sexisme i la normalització social de les seves formes menors, que acostumen a considerar-se trivials, que permet prosperar a la misoginia subjacent en els casos més greus d’abús i opressió. Segons Laura Bates, la lluita contra el sexisme actualment no és assumpte solament d’homes, sinó de persones contra prejudicis."),
                    image_0="images/chapter4/femiblog/everyday_sexism.jpg",
                    image_1="images/chapter4/femiblog/girls.jpg",
                    x_0=400, y_0=600, x_1=400, y_1=400,
                    path=_("everyday-sexism"))]

        text _("{i}#EverydaySexism{/i}"):
            align .913, .295
            size 35
            color "#ffffff"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_section_idle.png"
            hover "images/chapter4/femiblog/femiblog_section_hover.png"
            selected_idle "images/chapter4/femiblog/femiblog_section_hover.png"
            selected_hover "images/chapter4/femiblog/femiblog_section_hover.png"
            align .913, .375
            selected title == "{i}#BringBackOurGirls{/i}"
            action [Hide("femiblog"),
                Function(adj.change, 0),
                Show(
                    screen="post",
                    title=_("{i}#BringBackOurGirls{/i}"),
                    content_0=_("L’any 2014, l’exèrcit armat del grup yihadista Boko Haram va segrestar més dues-centes nenes a Chibock, Nigèria. Activistes pels drets humans a Nigèria en conjunt amb familiars de les nenes segrestades han dut a terme la campanya {i}#BringBackOurGirls{/i}, un moviment que busca pressionar el govern per a què incrementi els esforços en el rescat de les menors en cautiveri. Aquest grup terrorista ha estat motivat per l’oposició al dret de la dona a l’educació. Avui dia, encara hi ha nenes desaparegudes que no han tornat amb les seves famílies."),
                    image_0="images/chapter4/femiblog/bring_back_our_girls.png",
                    image_1="images/chapter4/femiblog/bbog_education.jpg",
                    x_0=600, y_0=400, x_1=600, y_1=400,
                    path=_("bring-back-our-girls"))]

        text _("{i}#BringBackOurGirls{/i}"):
            align .913, .375
            size 35
            color "#ffffff"

        imagebutton:
            idle "images/chapter4/femiblog/femiblog_section_idle.png"
            hover "images/chapter4/femiblog/femiblog_section_hover.png"
            selected_idle "images/chapter4/femiblog/femiblog_section_hover.png"
            selected_hover "images/chapter4/femiblog/femiblog_section_hover.png"
            align .913, .455
            selected title == "{i}The Hunting Ground{/i}"
            action [Hide("femiblog"),
                Function(adj.change, 0),
                Show(
                    screen="post",
                    title=_("{i}The Hunting Ground{/i}"),
                    content_0=_("{i}The Hunting Ground{/i} (2015) és un documental sobre les experiències de dones i persones d’altres gèneres quan informaren de violència sexual en els campus universitaris. La resposta de les autoritats acadèmiques i la policia va consistir en culpar a aquelles persones que havien informat o en demanar que consideressin el futur del perpetrador."),
                    image_0="images/chapter4/femiblog/hunting.jpg",
                    x_0=400, y_0=600,
                    path=_("the-hunting-house"))]

        text _("{i}The Hunting Ground{/i}"):
            align .913, .455
            size 35
            color "#ffffff"

        if not game_state.eco_is_seen:
            imagebutton:
                align .913, .85
                idle "images/chapter4/femiblog/eco_friendly.png"
                hover "images/chapter4/femiblog/eco_friendly_hover.png"
                action [Function(GiveGlossaryItemToPlayer,12), Function(ShowItems), Function(checkIfEcoIsSeen)]
        else:
            image "images/chapter4/femiblog/eco_friendly.png":
                align .913, .85

        text _("Recolza la causa"):
            size 50
            align .85, .6
            xsize 170
            color "#ffffff"
