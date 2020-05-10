
## This is script for Redstockings and WITCH protest.


label redstockings_witch_protest:
    "..."
    "[tmpSavePlayer] portava una estona de camí gaudint del paisatge quan, de sobte ..."
    user "Ostres, què raro, m'ha semblat veure una bruixa ... aix, aquest cansament ..."
    "Però el conductor del taxi no semblava pas sorprès ..."
    unknown_boy "No és el cansament. Són les militants de W.I.T.C.H., la Conspiració Terrorista Internacional de les Dones de l'Infern."
    user "Com? Qui ha dit que són?"
    scene black
    show witch_rally at truecenter
    unknown_boy "Després de la dissolució de NYRW, es crearen dues organitzacions, W.I.T.C.H. i les {i}Redstockings{/i}."
    unknown_boy "La primera és més radical que la segona, però el que pretenen és comú entre ambdues."
    unknown_boy "Tenen l'objectiu d'aturar l'opressió de les dones mitjançant la reclamació de la soberania sobre el propi cos i la promoció de canvis socials radicals."
    unknown_boy "Concretament, la tàctica de les {i}Redstockings{/i} consisteix en els anomenats {i}zaps{/i}, una mescla de protesta d'acció directa i teatre de carrer."
    unknown_boy "Tenen una forma peculiar de moure's i actuen de manera independent."
    unknown_boy "Si es fixa detalladament, avui l'activisme és pro avortament."
    unknown_boy "Miri, miri aquella fotografia. Veu que és bastant impactant?"
    "El conductor del taxi assenyalava amb el dit una pancarta del fons ..."
    hide witch_rally
    show gerri_santoro at truecenter
    user "Sí ..."
    unknown_boy "Aquesta imatge s'ha convertit en un catalitzador de la campanya per l'avortament legal."
    unknown_boy "Gerri Santoro, la dona de la fotografia, morí en un motel a causa d'un avortament autoinduït."
    user "Ostres ... em deixa sense paraules ..."
    "Per uns moments, al taxi es fa silenci ..."
    "... fins que [tmpSavePlayer] li formula una pregunta."
    user "Sembla que vostè en sap molt sobre aquest tema ... com és que ho coneix tant a fons?"
    hide gerri_santoro
    show witch_dancing at truecenter
    unknown_boy "Perquè la meva germana petita és una militant que, probablement, ara estigui circulant amb la moto vestida amb un barret de bruixa i una capa negres per la ciutat."
    hide witch_dancing
    scene now_building
    "La conversa s'estava posant d'allò més interessant, però el taxi s'acabava d'aturar. Havien arribat a la destinació."
    user "Moltes gràcies pel viatge i per la conversa."
    "I, amb la mateixa alegria que a les converses de cafè, [tmpSavePlayer] pagà i baixà del taxi."

    return
