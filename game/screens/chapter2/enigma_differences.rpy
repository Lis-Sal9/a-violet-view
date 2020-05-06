
# This script is for one of the enigmas of chapter 2.
##
### The player has to find, minimum, seven differences between two images to collect two gifts: a gallery item and a journal.



label enigma_differences:
    scene black

    # If player finds seven differences minimum
    "[tmpSavePlayer] ha resolt correctament l'enigma de les diferències, així que s'apropa al mostrador."
    unknown_girl "Molt bé! Ho ha aconseguit!"
    unknown_girl "Tingui, aquí té el nostre petit obsequi."

    if game_state.witch_is_seen:
        unknown_girl "És el nou número de la revista {i}Our Bodies, Our Selves{/i}."
        unknown_girl "No sé si la coneix, però és una revista que pretén exhibir el tracte sexista i condescendent per part dels metges cap a les dones."
        user "No, no la coneixia. Moltes gràcies per la informació."
    else:
        unknown_girl "És el nou número de la revista sobre feminisme indi, {i}Manushi{/i}."
        user "Moltes gràcies. Molt amable."

    "Així, [tmpSavePlayer] decidí marxar de la sala amb la revista en mà. Ja tenia un entreteniment més pel viatge."

    ## If player finds all differences
    # GiveGalleryItemToPlayer(1)

    return
