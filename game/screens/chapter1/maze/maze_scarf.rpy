
## This script defines the scarf (objects panel) on maze.



label maze_scarf:
    image empson = "images/chapter1/maze/maze_scarf/empson.png"
    image funeral = "images/chapter1/maze/maze_scarf/funeral.jpg"
    image tombstone = "images/chapter1/maze/maze_scarf/tombstone.jpg"
    image tragedy = "images/chapter1/maze/maze_scarf/tragedy.jpg"

    scene black

    show empson at truecenter
    show emily_davison at left
    emily_davison "Sí, és el millor moment. Vull interrompre el Derby de l'hipòdrom Epsom per donar a conèixer la nostra causa."
    show mary_richardson at right
    mary_richardson "Però no creus que és molt arriscat? Hi ha molta gent aquí i tots estan pendents de la carrera dels cavalls ..."
    emily_davison "Justament per això, perquè ens hem de fer notar. Hem d'aconseguir repercussió social per a la nostra causa."
    hide emily_davison
    hide mary_richardson
    "Així, Emily va endinsar-se enmig de la multitud i Mary la va perdre de vista."
    "De sobte, es va escoltar un soroll estrany i la multitud es començà a agitar ..."
    hide empson with fade
    show tragedy at truecenter
    "Mary va córrer cap allà i va presenciar l'escena."
    "Emily va ser copejada pel cavall Anmer, el cavall del Rei George V, patint lesions fatals. A la mà, duïa una espècie de mocador amb la bandera sufragista."
    "Aquest fet va causar una forta commoció."
    hide tragedy with fade
    show funeral at truecenter
    "Dies més tard, es va produïr un dels moments més emblemàtics del moviment sufragista."
    "Cinquanta mil persones varen recórrer la processó organitzada per retre homenatge a Emily."
    hide funeral with fade
    show tombstone at truecenter
    "En la seva làpida quedà escrit 'Deeds, not words', lema de la WSPU."
    hide tombstone with fade

    user "Ufff ... m'ha entrat una brosseta a l'ull ..."
    user "És molt bonic l'homenatge que li varen fer, però quin terrorífic final per ella ..."
    user "En aquest moviment, hi ha molt de patiment ..."
    "Amb el cos trist, [tmpSavePlayer] va seguir caminant, però amb el cap en aquella noia i el cavall ..."

    call maze_label
    return
