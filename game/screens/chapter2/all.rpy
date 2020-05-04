
## Script for the chapter 2.
## This chapter explains the feminism between 1945-1990.


label chapter_2:
    ##  ######################
    scene black

    if not game_state.crosswords_done:
        #crossword is not done
        $ renpy.call_in_new_context("crosswords_label")
    else:
        #crossword is done
        "Ja has fet les encreuades de {i}The Dinner Party{/i}. Vols tornar-les a fer?"
        menu:
            "Sí":
                $ renpy.call_in_new_context("crosswords_label")
            "No":
                "D'acord. Continues amb la mateixa història com si l'haguessis fet."

    return
