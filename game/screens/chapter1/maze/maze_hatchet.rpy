
## This script defines the hatchet (objects panel) on maze.



label maze_hatchet:
    image venus = "images/chapter1/maze/maze_hatchet/venus.jpg"
    image detention = "images/chapter1/maze/maze_hatchet/detention.jpg"

    scene black

    mary_richardson "Sí, serà avui. Per la mort de la nostra estimada Emily i per la detenció de la senyora Pankhurst."
    edith_garrud "Està bé, però jo no puc acompanyar-te aquest cop."
    mary_richardson "No pateixis, ho faré sola."
    show venus at truecenter
    "I així fou com Mary va irrompre hores més tard en la {i}National Gallery{/i} amb una destral i danyà el quadre de {i}La Venus del espejo{/i}, de Velázquez."
    mary_richardson "Heu destruït a la senyora Pankhurst, la persona més maca de la història moderna !!!"
    mary_richardson "I jo us destrosso a la dona més bella de la història de la mitologia !!!"
    "Cridà a ple pulmó als policies que se li apropaven per detenir-la ... "
    hide venus with fade
    show detention at truecenter
    "Així, Mary fou detinguda i condemnada a sis mesos de presó, el màxim establert per llei pel delicte de destrucció d'una obra d'art."
    hide detention with fade

    user "Jajaja, quines idees que tenen aquestes dones ..."
    "Rient i fent que no amb el cap, [tmpSavePlayer] va continuar el seu trajecte ..."

    call screen maze
    return
