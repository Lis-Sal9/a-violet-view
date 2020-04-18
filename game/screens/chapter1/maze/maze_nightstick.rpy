
## This script defines the nightstick (objects panel) on maze.



label maze_nightstick:
    image arrest_pankhurst = "images/chapter1/maze/maze_nightstick/emmeline.jpg"
    image fight_0 = "images/chapter1/maze/maze_nightstick/fight.jpg"
    image fight_1 = "images/chapter1/maze/maze_nightstick/fight_1.jpg"
    image fight_2 = "images/chapter1/maze/maze_nightstick/fight_2.jpg"
    image rosa_mary_wheelchair = "images/chapter1/maze/maze_nightstick/rosa_mary.jpg"
    image parliament = "images/chapter1/maze/maze_nightstick/parliament.jpg"
    image paint = "images/chapter1/maze/maze_nightstick/paint.jpg"

    scene black
    user "Una porra ... això em comença a fer por de veritat ..."

    show parliament at truecenter
    emmeline_pankhurst "Noies, hem de seguir lluitant per a què el govern liberal estudiï el Projecte de Llei de Conciliació."
    "{i}Votes for Women !!!!!{/i} - varen cridar totes les noies alhora."
    "La líder de la WSPU va convocar una reunió de trobada a Caxton Hall a la Cambra dels Comuns."
    hide parliament with fade
    "Aquell dia, ocorregué una tragèdia. El famós {i}Divendres Negre{/i}."
    show fight_1 at truecenter
    "Aproximadament, unes 300 dones es reuniren davant del Parlament, però el què ocorregué no s'ho esperaven pas."
    hide fight_1 with fade
    show fight_0 at truecenter
    "Varen ser atacades brutalment per un grup de policies, i d'altres homes que passaven per allà."
    hide fight_0 with fade
    show fight_2 at truecenter
    "Moltes varen ser ferides, colpejades, agredides sexualment ..."
    hide fight_2 with fade
    show arrest_pankhurst at truecenter
    "... arrestades ... fins i tot, algunes varen perdre la vida."
    hide arrest_pankhurst with fade
    "Els testimonis de dones que quedaren són esgarrifadors ..."
    show rosa_mary_wheelchair at truecenter
    rosa_mary_billinghurst "Al principi, la policia em va fer caure de la cadira de rodes a terra violentament."
    rosa_mary_billinghurst "Vaig aconseguir tornar a seure-hi, però novament van intentar empènyer-me, amb els braços girats al meu darrere i un dels dits doblegats cap a l'esquena."
    rosa_mary_billinghurst "Era una posició molt dolorosa. Fou una gran agonia. "
    hide rosa_mary_wheelchair with fade
    "I, la resposta oficial del govern a aquell tracte va ser culpar aquelles dones per incitar a tothom que ho desitgés a sumar-se a la protesta."
    show paint at truecenter
    "A partir d'aquell moment, les dones que formaven part de la WSPU varen decidir que havia arribat el moment de radicalitzar-se."
    hide paint with fade

    user "És que ... no m'estranya pas, després del tracte que tenen amb les dones, com esperava el govern que es prenguessin aquest fet?"
    user "És indignant ..."
    "[tmpSavePlayer] estava en plena ebullició, però va tractar de calmar-se. Inspira, expira, inspira, expira ... i va seguir caminant."

    call screen maze
    return
