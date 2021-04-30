label a1s2:
play music "music/beyondthestars1.ogg"fadein 5.0
"Je fais un étrange rêve."
"Je suis dans un vide noir et malgré l'absence de toute chose, j'ai une sorte de but."
"Je ne sais pas ce que c'est, mais j'y suis poussé."
"Ce n'est pas un bon rêve, c'est presque un cauchemar."
"Toutefois, ce n'est pas le vide qui est effrayant."
"C'est le sentiment d'être observé par quelqu'un… ou quelque chose."
"C'est le sentiment de ne pas avoir mon mot à dire sur l'endroit où je vais."
"Aucun libre-arbitre…"
"…"
"\"Vous attisez ma curiosité\""
"Quoi ?"
"\"Je suis limité dans ce que je peux demander, mais je vais commencer par ceci —\""
"\"Qu'est-ce que la mort pour vous ?\""
menu:
    "L'Infini":
        $ end_game1 += 1
        "…"
        "Très intéressant…"
    "L'Oubli":
        "…"
        "Je vois…"
stop music fadeout 10.0
$ renpy.pause(5.0, hard=True)
"Quelque temps juste avant de me réveiller complètement, j'entends quelque chose bouger derrière moi suivi d'un marmonnement, puis d'un doux son coussiné qui s'estompe après quelques instants."
"Je me demande si l'un de mes colocataires vient d'arriver et… a regardé dans ma chambre pour une raison quelconque."
"En me déplaçant, je fronce les sourcils en voyant à quel point le lit sur lequel je m'allonge est étrangement ferme."
"Mon lit était plus moelleux que ça quand je suis entré dedans… et où sont les draps ?"
scene bg amicusroom with slow_dissolve
"J'ouvre les yeux et vois une surface rouge et veloutée devant moi."
"Puis je me retourne et vois un plafond inconnu avec un motif carré d'or au-dessus de moi."
"Oh oui…"
"Je regarde vers le lit où je m'attends à voir Amicus, mais il est vide."
"Je regarde à nouveau le plafond pendant un moment, laissant la soudaine réalisation que je suis toujours là me submerger."
"Je passe en revue tout ce qui s'est passé hier, le dernier espoir dont j'avais rêvé disparaissant de mon esprit."
"Je regarde à nouveau le lit d'Amicus, me demandant s'il est allé dans la salle de bain."
"J'écoute un moment, mais je n'entends rien venant de la porte en face du lit."
"Il y a un son étouffé de ce que je suppose être des oiseaux qui chantent derrière le rideau."
"Lentement, je glisse du canapé, sentant le marbre froid contre mes pieds nus quand ils touchent le sol."
"Je frissonne et décide d'apporter la couverture avec moi, l'enroulant autour de mes épaules."
"Je fais le tour du canapé et je me déplace sur le côté du grand rideau pour l'ouvrir légèrement."

scene adastranl with dissolve
play background "sfx/birds.ogg"fadein 3.0
"L'air qui provient de dehors est frais et me rappelle immédiatement le camping au bord d'un lac pendant les colonies de vacances."
"Ça me semble logique, car devant moi se dresse une immense étendue d'eau qui arrive jusqu'au bord du balcon."
"Il fait chaud, mais pas aussi humide que la nuit dernière."
"La lumière rose et orange peint les nuages ​​à l'horizon, et pendant un moment j'admire la vue la vue."
"Les collines et les montagnes de chaque côté du lac sont couvertes d'arbres luxuriants et verts."
"Tout comme la petite île un peu plus loin sur ma gauche."
"Au loin, de l'autre côté du lac je peux apercevoir une ville quelconque."
"Difficile à dire à quel point elle est grande car elle est vraiment loin, mais d'après ce que je peux voir, les bâtiments sont énormes et les structures plus petites qui s'effilent sur le côté semblent s'étirer loin derrière ces bâtiments."
"Les lumières tamisées des fenêtres scintillent au loin et je me demande si cette ville est pleine de loups comme Amicus et Cassius."
"Malgré ma situation, j'aimerais bien aller la visiter."
"Pendant que je regarde, je vois une petite forme ovale sombre descendre vers la ville, avec des lumières bleues et rouges clignotantes."
"Je souris et secoue un peu la tête."
"Je veux toujours retourner sur Terre, mais il faut dire que c'est indéniablement incroyable."
"Je laisse enfin le rideau se fermer et je retourne dans la pièce."
scene bg amicusroom with dissolve
stop background fadeout 3.0
"Alors, où est allé ce grand loup ?"
"Il aurait au moins pu me le dire avant de s'enfuir."
com "\"Bonjour, [mc].\""
"Je sursaute alors que la voix de l'ordinateur crépite au-dessus de ma tête."
"Je serre ma poitrine, respirant fort alors que la voix continue."
com "\"Amicus a un message pour vous.\""
"Il y a une pause, et—"
a "\"Heeey, [mc] ? Je vais à ma méditation matinale. C'est dans une pièce juste au bout du couloir et je serai de retour dans environ une heure. Pourquoi ne prends-tu pas le temps de te familiariser avec la pièce  ?\""
"Il y a une pause, et—"
a "\"Tu enregistres toujours, Com ?\""
com "\"Oui. Pour terminer l'enregistrement, dites «fin du message.\""
a "\"Oh, euh, à bientôt, [mc]. Fin du message… est-ce que c'est—\""
com "\"Pour terminer l'enregistrement, dites\"fin du message\".\""
a "\"Par les dieux, fin du message !\""
"J'entends Amicus recommencer à maudire l'IA avant que le message ne s'arrête."
"Je regarde un peu autour de la pièce, remarquant à quel point il y a peu de choses avec lesquelles se familiariser."
"Je pourrais regarder à l'intérieur de la commode, mais je suppose que c'est principalement rempli d'effets personnels d'Amicus et je doute qu'il veuille que je me familiarise avec ceux-ci."
"Je traverse la pièce jusqu'à arriver devant la porte de la salle de bain. Je me tiens devant elle pendant un moment avant d'étudier le panneau noir au milieu."
"C'est similaire à ce qu'Amicus utilisait pour ouvrir la porte dans le couloir."
"Je tends la main pour essayer de le pousser et au moment où mes doigts frôlent la surface, la porte glisse sur le côté si vite que je sursaute."
play sound "sfx/dooropen.ogg"
scene bg bathroom with slow_dissolve
"Les lumières à l'intérieur s'allument, éclairant lentement l'intérieur."
"Je mets ma tête à l'intérieur, puis j'entre rapidement, imaginant la porte coulissante se refermant soudainement et me coupant la tête."
"Elle reste ouverte jusqu'à ce que je sois à mi-chemin dans la pièce, puis elle se ferme automatiquement."
play sound "sfx/doorclose.ogg"
"Il y a un grand lavabo à ma gauche et un miroir encore plus grand au-dessus."
"Dans le coin, il y a un banc d'aspect marbre avec un trou dont je ne peux que supposer que ce sont les toilettes."
"Enfin, en face des toilettes, il y a une grande baignoire et ce que j'imagine être la douche."
"En fait, j'ai vraiment besoin de faire pipi, alors je me dirige vers le banc et fais mon affaire dans le trou, en espérant que ce n'est pas une blanchisserie et que je pisse sur les serviteurs en dessous."
"Dès que j'ai commencé, l'eau commence à couler sur les côtés de la cuvette, me laissant à peu près sûr qu'il s'agit bien d'un toilette."
"Je suppose que je devrais être plus confiant pour assumer des choses à propos de cet endroit."
"Tout est assez similaire à ce que j'avais sur Terre."
"Je me dirige vers l'évier et ouvre le robinet, puis je mets ma main sous celui-ci et l'eau commence à couler."
"Je suis tenté de prendre un verre, mais je remarque ensuite que l'eau est pétillante et savonneuse."
"N'ayant plus rien à faire dans la salle de bain, je me retourne vers la porte et retrouve le carré noir."
"Je le saisis, et juste comme avant que la porte ne s'ouvre -"
play sound "sfx/dooropen.ogg"
scene bg amicusroom with dissolve
show cas at center with dissolve
c "\"- s'il pense qu'il va s'en tirer.\""
"Cassius est tourné à l'opposé, les bras croisés alors que sa queue blanche et touffue bouge d'un côté à l'autre."
"Je me fige, le regardant, les yeux écarquillés."
"J'ai beaucoup de temps pour sauter sur le côté, peut-être me cacher dans la douche, mais je reste juste là comme un idiot alors que le loup se retourne, presque au ralenti."
show cas surprised at center with dis
"Il se fige comme je l'ai fait quand il me voit debout dans l'embrasure de la porte."
"Nous nous regardons pendant un moment, pendant un très long moment."
"Puis il hurle, me faisant sursauter sous le choc."
play music "music/trouble.ogg"
show cas scared at chase with dis
c "\"OH DIEUX ! EDAPOL ! QU'EST-CE QUE C'EST !?\""
"Le loup se balance d'avant en arrière, comme s'il s'attendait à ce que je tente de lui courir dessus."
c "\"CATO ! CATO ! À L'AIDE ! VIENS VITE !\""
hide cas scared with moveoutleft
"Finalement, la petite danse de terreur de Cassius se termine par un sprint à gauche, de manière à ce qu'il sorte de la pièce."
"Je reste là pendant un moment, écoutant ses cris s'estomper dans le couloir en écho tout en me demandant si je devrais me cacher ou quelque chose comme ça, peut-être retourner dans la salle de bain et essayer de la verrouiller…"
"Au lieu de cela, j'entends un autre de bruit sourd, quelqu'un qui court dans le couloir de l'autre côté."
show ami shocked u at center with moveinright
"Alors Amicus arrive en courant dans la pièce, glissant pour s'arrêter au milieu de celle-ci."
show ami surprised u with dis
"Il tourne en cercle, puis me repère et court vers moi."
a "\"Que s'est-il passé !?\""
m "\"Euh, Cassius est entré et m'a vu.\""
show ami angry u with dis
a "\"Tu l'as laissé te voir comme!?\""
m "\"Quo - Non ! Il vient juste d'entrer ! Où étais-tu !?\""
a "\"Je méditais ! J'ai laissé un message ! Où est-il allé ?\""
m "\"Cassius ? Il vient de s'enfuir.\""
show ami frustrated u with dis
a "\"Bon sang !\""
"Amicus se tient là, sa queue battant furieusement."
"Je le regarde fixement."
m "\"Si tu ne m'avais pas laissé ici, cela ne serait pas arrivé !\""
show ami angry u with dis
a "\"Cassius n'aurait même pas dû entrer ici !\""
"Amicus se détourne et commence à faire les cent pas."
m "\"Quu'est-ce que tu fais ?\""
a "\"Chut ! Je réfléchis.\""
"Je suis un peu vexé d'avoir été muselé, mais je reste silencieux, regardant le loup se promener."
"Ensuite, j'entends à nouveau des voix; celle de Cassius avec une autre voix plus profonde."
"Amicus se tourne vers moi."
show ami angry teeth u with dis
a "\"Tais-toi juste un instant pendant que j'essaie d'expliquer les choses, compris ?\""
"Je regarde Amicus."
"Ses oreilles s'aplatissent et son expression devient un peu plus désespérée."
show ami embarrassed u with dis
a "\"S'il te plaît ?\""
"Je ne dis toujours rien, mais lui fais un bref signe de tête."
show ami serious u with dis
"Amicus tend la main vers mon épaule, puis s'arrête et me tend sa patte à la place."
show ami serious u at twelve with moveinright
"Je la prends et il me tire doucement de la salle de bain pour me tenir à côté de lui au milieu de la pièce, face à la porte ouverte du couloir."
show ami u with dis
"Amicus montre un sourire confiant sur son visage, même si je peux sentir à quel point il est tendu à côté de moi."
"Du coin de pièce vient Cassius, mais il se cache derrière quelqu'un d'autre; un autre loup."
show cas scared at one
show cat at four
with dissolve
stop music fadeout 5.0
"Ils s'arrêtent tous les deux dans l'embrasure de la porte alors que le plus grand loup nous prend à partie Amicus et moi."
show cas furious with dis
c "\"Amicus ! Qu'est-ce que c'est que ça !? Éloigne-toi !\""
"Amicus place doucement sa patte autour de mes épaules, m'attirant contre son torse massif."
"Les yeux de Cassius s'écarquillent à cela, bien que le loup à côté de lui semble n'avoir aucune réaction."
"Encore une fois, cela pourrait être simplement parce que je ne peux pas voir ses yeux."
show cas annoyed with dis
c "\"Que fais-tu, Amicus ?\""
"Amicus s'éclaircit la gorge."
show ami talking u with dis
a "\"Cassius, Cato—\""
"Il fait un signe de tête à chacun d'eux à son tour."
play music "music/memories.ogg"fadein 5.0
a "\"Ceci est mon animal de compagnie, [mc]\""
show cas surprised
show cat surprised
with dis
"La bouche de Cassius s'ouvre."
"L'autre loup, Cato, semble être un peu choqué face à ça."
"Le silence s'éternise."
"Puis Cato sort de son choc."
show cat bow with dis
ca "\"Est-ce là ce que tu faisais ces deux derniers jours, Amicus ?\""
"Le bras d'Amicus se resserre un peu autour de mes épaules, me rapprochant de lui."
show ami serious u with dis
a "\"Oui.\""
ca "\"Et c'est pourquoi tu as pris le vaisseau de ton père ?\""
"Une légère pause."
show ami embarrassed u with dis
a "\"O — oui.\""
"Cassius en perd son souffle."
show cas furious with dis
c "\"Il ne peut pas faire ça !\""
"Il jette un coup d'œil à Cato."
show cas surprised with dis
c "\"Pas vrai ?\""
"Le plus grand loup est calme, et même si je ne peux pas voir ses yeux, j'ai le sentiment qu'il me regarde de près."
"Cassius retourne son regard sur Amicus."
show cas angry with dis
c "\"D'où vient cette chose ?\""
show ami serious u with dis
"Amicus me caresse le bras."
a "\"Cette PERSONNE… est venue de loin.\""
show cat frown with dis
ca "\"Est-ce un Enfant ?\""
a "\"Oui.\""
show cas surprised with dis
c "\"Quoi !? Il ne peut pas simplement prendre l'Enfant de quelqu'un d'autre… n'est-ce pas ?\""
"Encore une fois, Cassius regarde Cato."
"Et encore une fois, Cato est calme, puis il soupire enfin."
show cat talking with dis
ca "\"Nous en discuterons pendant le petit-déjeuner, Amicus. Habillez-vous et amène la créature avec toi… à moins qu'il ne soit une menace ?\""
show ami crossed u with dis
a "\"Bien sûr que non.\""
ca "\"Alors, nous continuerons la conversation là-bas.\""
hide cat with dis
"Sur ce, Cato tourne les talons et sort de la pièce, laissant Cassius le regarder avec une bouche béante."
"Il se retourne vers nous en grognant."
show cas angry with dis
c "\"Je ne sais pas ce que tu prévois avec cette {i} chose {/ i}, Amicus, mais je te connais, ça va être incroyablement stupide.\""
"Il prend une seconde de plus pour me regarder avec un dégoût indéniable."
c "\"Tu aurais pu revenir avec une créature qui ne soit pas aussi moche que ça, tu le sais —\""
show ami crossed serious with dis
a "\"Pars, Cassius. Et ne viens plus fouiner dans ma chambre à l'avenir, c'est compris ?\""
hide cas with dissolve
"Cassius ne répond pas et s'éloigne tout simplement, regardant par-dessus son épaule juste avant de partir."
c "\"Et attends-toi à recevoir une punition de Cato pour avoir volé le vaisseau de père… C'est absolument scandaleux.\""
"Je regarde la queue de Cassius disparaitre derrière la porte."
"Amicus laisse échapper un énorme soupir et je sens sa poitrine se dégonfler contre mon épaule."
show ami frustrated u with dis
a "\"Bontée divine.\""
"Je soupire aussi."
m "\"Tu n'as VRAIMENT pas réfléchi à tout ça, psa vrai ?\""
"Je m'éloigne lentement sous le bras lourd du loup."
show ami crossed serious u with dis
a "\"Comme je l'ai dit, j'ai commis de nombreuses erreurs. Je suis juste fatigué de mentir maintenant.\""
stop music fadeout 10.0
m "\"Tu leur as quand même dit que j'étais un Enfant.\""
show ami surprised u with dis
"Amicus porte brusquement une patte à sa bouche, touchant les coussinets de ses doigts à ses lèvres."
"Ce n'est peut-être pas un geste de silence que je connais, mais je sais ce que cela signifie."
"Amicus écoute, les oreilles droites et les yeux levés vers le plafond."
"Finalement, il me regarde en chuchotant."
show ami embarrassed u with dis
a "\"C'est… quelque chose que je ne pourrais jamais leur révéler, et il serait préférable que tu ne le mentionnes plus… s'il te plaît.\""
"Son comportement soudainement sérieux refroidit clairement l'ambiance de la pièce, alors je soupire à nouveau et m'assois sur le bord de son lit."
"Amicus se tient maladroitement au milieu de la pièce pendant un moment, puis se dirige rapidement vers la porte ouverte, plaçant sa patte sur le carré tactile pour la fermer."
hide ami with dissolve
play sound "sfx/doorclose.ogg"
"Il revient vers moi, me parlant toujours à voix basse."
show ami crossed serious u with dissolve
a "\"Eh bien, si nous allons te faire passer pour un animal de compagnie, je devrais probablement te familiariser avec tes nouveaux devoirs.\""
m "\"Mes devoirs ?\""
"J'arque un sourcil en entendant cela de la part d'Amicus."
"Le loup soupire."
a "\"Je comprends ta frustration, mais nous devons faire correctement les choses si nous voulons qu'elles se passent aussi bien que possible. Tu n'as {i} pas {/ i} à faire quoi que ce soit, mais cela t'aidera à mieux t'intégrer.\""
"Je roule les yeux au ciel et je me penche en arrière, supportant mon poids avec mes mains tout en regardant Amicus."
m "\"Très bien… que dois-je faire ?\""
show ami crossed u with dis
a "\"Eh bien, quand je prends ma douche…\""
show ami embarrassed u with dis
a "\"… tu devrais m'aider à me laver.\""
play music "music/dawn.ogg"fadein 10.0
m "\"T'aider à te laver ?\""
a "\"… Oui. Tu savonnerais ma fourrure, par exemple.\""
"Nous nous regardons pendant un moment."
a "\"Euh, c'est quelque chose que les autres ne verraient pas, donc je suppose que ce n'est pas nécessaire… à moins que tu ne le veuilles.\""
m "\"Non.\""
show ami disappointed u with dis
a "\"Eh bien, d'accord alors. Ce n'est pas un problème.\""
"Amicus est clairement offensé."
m "\"Ecoute, je ne vais quand même pas te savonner le corps nu.\""
show ami disappointed eyes u with dis
a "\"Ouais, tu me l'as clairement dit.\""
show ami crossed serious u with dis
a "\"De toute façon, je préfère honnêtement sauter la douche aujourd'hui, mais passer tout ce temps dans le vaisseau spatial m'a laissé plutôt négligé.\""
"Amicus se tourne vers la salle de bain et ouvre la porte."
play sound "sfx/dooropen.ogg"
a "\"Tu devras au moins entrer dans la salle de bain pendant que je prends une douche au cas où Cassius déciderait de faire irruption à nouveau. Tu pourras regarder le mur ou quelque chose comme ça.\""
scene bg bathroom with dissolve
"Amicus entre dans la salle de bain et je me sens sourire en le suivant à l'intérieur, la porte se refermant doucement derrière moi."
play sound "sfx/doorclose.ogg"
"Amicus me remarque mon sourire narquois."
show ami crossed serious u with dis
a "Quoi ?\""
"Je hausse les épaules."
m "\"Rien, ça m'amuse juste un peu que tu le prennes aussi mal.\""
a "\"Je ne vois pas de quoi tu parles.\""
show ami crossed u with dis
"Amicus ajuste ses sous-vêtements, puis ils tombent soudainement et je détourne rapidement le regard."
hide ami with dissolve
a "\"Heh, je suppose que votre peuple est plutôt pudique.\""
"Du coin de l'œil, je peux dire qu'Amicus me retourne le sourire narquois de tout à l'heure."
m "\"Autour des autres au moins… et vous ne vous promenez pas nus non plus, vous ne préferez pas plutôt la modestie aussi ?\""
a "\"Tout dépend de l'heure et du lieu.\""
"Amicus entre dans la douche et pendant les dix minutes suivantes, je m'assois sur le comptoir pendant que la pièce se remplit de vapeur."
play loop "sfx/showerfan.ogg" fadein 4.0
"Une fois que l'eau s'est arrêtée, un ventilateur bruyant se met en marche et je jette un coup d'œil pour voir Amicus les bras écartés, sa fourrure allant et venant."
"Il remarque que je regarde par-dessus puis détourne à nouveau le regard."
a "\"Tu sais —\""
"Il doit presque crier pour que je l'entende avec le bruit du ventilateur."
a "\"Tu aurais pu te laver en même temps si tu avais pris ta douche avec moi, mais tu n'auras pas le temps avec le petit déjeuner qui vient. Tu devras le faire après.\""
stop loop fadeout 3.0
"Je hausse les épaules et j'attends qu'Amicus sorte et attrape des sous-vêtements propres suspendus à un crochet, qu'il passe la minute suivante à nouer."
show ami happy eyes u with dis
a "\"D'accord, les couilles sont cachées. Tu peux regarder maintenant.\""
show ami u with dis
a "\"En fait, est-ce que tu en as d'ailleurs ? Je ne veux pas faire de supposition pour ce genre de chose.\""
#play sound "sfx/dooropen.ogg"
#"J'ouvre la porte et je sors de la salle de bains."
# Consistency ?
m "\"Je suppose que tu ne le sauras jamais.\""
show ami eyes u with dis
a "\"Héhé…\""
scene bg amicusroom with dissolve
"Amicus passe une autre minute dans la salle de bain à ouvrir un tiroir sous l'évier et à fouiller dedans."
a "\"La prochaine chose que tu es censé faire en tant qu'animal de compagnie, c'est de récupérer la brosse et les huiles d'ici.\""
"Il soulève une brosse et quelques bouteilles en verre avec des liquides colorés à l'intérieur avant de venir se placer devant moi."
show ami serious u with dissolve
"Il soupire."
a "\"Je sais que tu n'en as pas envie, et je me rends compte maintenant que je te répugne, mais je ne peux pas atteindre chaque partie de ma fourrure, et ce serait étrange si j'appelais un drone quand j'ai un animal de compagnie…\""
"Je pense faire une autre remarque acerbe, mais l'expression sur son visage m'arrête là."
"Je suppose que je suis un peu grincheux en ce moment."
"En plus, qu'est-ce que je vais faire d'autre pendant que je suis ici ?"
"Rester assis sur le canapé toute la journée? "
"Je me lève et prends la brosse d'Amicus et je vois un sourire surpris sur son visage."
show ami eyes u with dis
a "\"Merci, [mc].\""
"Il me montre comment appliquer l'un des liquides, un liquide de couleur miel, sur la brosse."
show ami u with dis
a "\"C'est un traitement pour ma fourrure. Il la garde douce et volumineuse. Ici, il te suffit de prendre la brosse et de l'appliquer sur ma fourrure.\""
"Il me tend la brosse puis se tient dos à moi."
"Je commence lentement et passe la brosse à travers la fourrure entre ses oreilles et le long de son large dos, regardant les poils légèrement ébouriffés s'aligner et se déposer en douceur."
"Cela accentue la visibilité de ses omoplates et des muscles épais et réguliers de son dos."
"J'hésite au début, mais je deviens plus confiant à chaque coup de brosse."
"En fait, c'est un peu reposant, c'est jusqu'à ce que je frôle le côté gauche de son cou, ce qui lui coupe le souffle."
show ami surprised u with dis
"Je recule rapidement."
"Je suis désolé ! J'ai brossé trop fort ?\""
show ami eyes u with dis
"Amicus rit."
a "\"Heh, non, c'est juste là où tu m'as frappé plus tôt.\""
m "\"Oh…\""
"Je regarde de plus près et je vois qu'il y a une sorte  de bosse sous la fourrure."
"Je continue alors de brosser doucement le pelage en prenant soin de l'éviter et me dirige ensuite vers le devant d'Amicus."
"Amicus, quant à lui, garde les yeux fermés avec un sourire sur son visage, prenant un certain plaisir à se faire servir."
m "\"Je suis désolé par rapport à ça, d'ailleurs. J'avais vraiment peur quand je l'ai fait.\""
show ami u with dis
a "\"Ne t'en fais pas. Je l'ai mérité pour t'avoir si mal attaché.\""
"Amicus me fait un clin d'œil."
"Je sens mon visage devenir un peu chaud alors que je me concentre sur le brossage de la fourrure de ses biceps."
m "\"Et tu sais, tu ne me répugnes pas du tout. J'étais juste très con plus tôt. Tu es… agréable à regarder.\""
a "\"Eh bien, je suppose que je l'étais aussi. Je n'aurais pas dû me moquer de ta sensibilité. Tous les extraterrestres ont leurs propres cultures, mais cela ne signifie pas qu'elles sont moins valeureuses.\""
"Le ton d'Amicus semble étrangement répété, comme s'il citait quelque chose."
a "\"Et merci aussi, [mc]. Tu m'as l'air aussi agréable à regarder.\""
# You look good => tu n'es pas mal (autre traduction possible > *>>>"Tu es agréable à regarder"<<<* ?)
"Il est peut-être juste en train de retourner le compliment, mais c'est agréable d'entendre cela  après ce que Cassius a dit."
"Mais je ne mentais certainement pas, et maintenant que je suis si proche de lui, je dois admettre qu'il est plutôt beau."
"Son visage est expressif et charmant et il y a juste un air généralement amical en lui."
"Et… enfin, il y a son corps."
"Il est large et masculin, tout comme un humain costaud, et je ne peux vraiment pas nier que c'est plutôt attrayant… en quelque sorte."
"Je commence à brosser le devant du loup, sentant sa poitrine et son estomac se soulever contre la brosse au rythme de sa respiration."
"Je sculpte la fourrure plus claire autour de ses pectoraux pour mieux les faire ressortir puisqu'il semble que c'est comme ça qu'il la gardait plus tôt."
"Je ne peux pas lui en vouloir."
"Puis je me déplace vers son ventre, déplaçant la brosse sur cette forme épaisse et légèrement arrondie."
"Les muscles sont moins définis ici, mais je peux toujours sentir la force sous tout cela."
"En frôlant la partie inférieure de son abdomen, je remarque que son pagne est étonamment bombé…"
show ami shocked blush u at jumping with dis
a "\"Très bien ! Merci, [mc], ça devrait aller !\""
hide ami with dissolve
"Il me prend la brosse des mains et se détourne, me laissant avec la forte suspicion qu'il ajuste son pagne, bien qu'il couvre cela en faisant semblant de jouer avec l'une des bouteilles."
"Finalement, il se retourne, l'air un peu embarrassé."
show ami embarrassed u with dis
a "\"Euh, tends tes pattes, s'il te plaît ?\""
"Je tends les mains et il penche la bouteille contenant un liquide violacé qu'il tient dans la main."
"Plusieurs gouttes tombent dans ma main."
"Immédiatement, mon nez est rempli de ce parfum de lavande que je sentais sur Amicus depuis que je l'ai rencontré pour la première fois."
a "\"Frottes-tes pattes ensemble puis tapote simplement mon corps, mes aisselles et le long de mon cou également.\""
"Je peux dire qu'Amicus est toujours embarrassé, alors je le fais rapidement, ne voulant pas m'attarder et causer au loup d'autres… problèmes."
"Peut-être que ça fait vraiment du bien d'être brossé comme ça ?"
m "\"C'est du parfum ?\""
show ami u with dis
a "\"Oui, il garde la plupart des odeurs musquées cachées.\""
m "\"Je vois.\""
a "\"Utilises-tu du parfum ?\""
m "\"Eh bien, je suppose que je met quelque chose comme ça sur mes aisselles.\""
show ami eyes u with dis
a "\"N'hésite pas à l'utiliser alors !\""
"Je décide de ne pas lui dire que les parfums de lavande sont principalement destinés aux femmes sur Terre… en plus, ça sent bon."
hide ami with dissolve
"Une fois parfumé, Amicus passe à l'habillage, me montrant comment draper sa cape sur ses épaules."
show ami with dissolve
a "\"Très bien ! Sachant que tu n'as que la paire de vêtements avec laquelle tu es venu, je ferai donc venir un drone tailleur plus tard dans la journée pour voir si nous ne pouvons pas te fabriquer plus de vêtements similaires.\""
m "\"Oh, d'accord.\""
a "\"Maintenant, allons à la salle à manger avant que nous ne soyons en retard.\""
show ami embarrassed with dis
"Amicus s'arrête, fronçant les sourcils."
a "\"Maintenant… je sais que tu n'aimeras pas ça, mais tu vas devoir feindre une certaine ignorance devant les autres.\""
"Je lève un sourcil."
m "\"Comment ?\""
a "\"Eh bien, tu vas devoir te faire passer pour… un simple d'esprit ?\""
"Les sentiments antagonistes qui s'étaient estompés au cours des dernières minutes recommencent à ressurgir."
m "\"Et comment je peux faire ça ?\""
"Amicus hausse les épaules."
a "\"Je ne sais pas, aies le regard vide, des marmonnements incohérents, fais comme si tu ne pouvais pas comprendre des choses plus complexes. Le but est de donner l'impression que tu es un enfant typique.\""
"Je n'aime pas ça, mais si je peux ne pas m'impliquer dans les histoires des ces extraterrestres, alors…"
m "\"Très bien.\""
show ami eyes with dis
"Amicus laisse échapper un souffle, clairement soulagé."
a "\"Merci, [mc]. Ce ne sera peut être pas toujours le cas, mais pour l'instant, nous devons faire profil bas. Laisse-moi juste parler.\""
m "\"Compris.\""
show ami motivated with dis
stop music fadeout 5.0
a "Super ! Maintenant, hâtons-nous dans la salle à manger. Je ne veux pas rendre Cato plus en colère qu'il ne l'est déjà.\""
scene bg palace1 with dissolve
play loop "sfx/birds.ogg"fadein 10.0
"Sur ces mots, je suis Amicus dans le couloir."
m "\"Alors qui est Cato ?\""
show ami crossed with dis
a "\"Le loup que tu as vu avec mon frère. Il était le conseiller de mon père et actuellement l'empereur par intérim. J'ai mentionné plus tôt qu'il choisirait entre moi et mon frère.\""
a "\"C'est pourquoi je fais de mon mieux pour le garder de bonne humeur, ou du moins, ne pas le mettre de mauvaise humeur. Je ne pense pas qu'il puisse être de bonne humeur.\""
"Je garde alors en tête de me faire bien voir par Cato."
"Pendant ce temps, la lumière du soleil pénètre par les fenêtres ouvertes, et je peux à nouveau entendre les oiseaux appeler de l'extérieur."
m "\"Des oiseaux.\""
a "\"Tu disais ?\""
m "\"Je peux entendre des oiseaux. Je suis juste surpris qu'ils chantent de la même manière que sur Terre.\""
a "\"Ah, oui, tu ne le sais pas; toute vie a la même origine et se développe à peu près de la même manière. Il est tout à fait naturel que la vie ici ressemble à celle de votre lune… planète, je veux dire.\""
m "\"Oh.\""
show ami thinking with dis
a "\"Eh bien, toute la vie de ce côté de l'univers, au moins. Il y en aura peut-être un autre, mais nous devrons reprendre cette conversation plus tard. Pour l'instant—\""
stop loop fadeout 5.0
scene bg diningroom with dissolve
play music "music/lute.ogg"fadein 5.0
"Je suis Amicus dans un coin et me retrouve debout dans une grande pièce spacieuse."
"Les premières choses que je remarque sont les grands écrans sur chaque mur de la pièce, affichant des images colorées d'étoiles, de galaxies et de vaisseaux spatiaux."
"Au milieu de la pièce se trouvent ce qui semble être des lits de banquet autour d'une table."
"Dans ces lits se trouvent les deux loups que j'ai vus plus tôt."
show cas at seven
show cat behind cas at twelve
with dissolve
"Cato est assis et se penche vers Cassius qui est luxueusement drapé sur l'un des lits."
"Cato parle à Cassius tandis que l'autre loup a une expression amère typique."
"Une créature est assise par terre devant le lit de Cassius, une créature que je n'ai jamais vue auparavant."
show ale at three with dissolve
"Ce n'est certainement pas un loup, c'est plus félin."
"Cassius a sa patte posée sur sa tête, la grattant paresseusement pendant qu'il écoute ce que Cato dit."
show cas surprised with dis
"Il nous voit et s'arrête brusquement, puis se lève."
"Cato arrête de parler et il nous regarde."
show cas annoyed with dis
c "\"Vous êtes en retard.\""
show ami at zero behind ale with dissolve
a "\"Et bonjour à toi, Cass. Et à vous Cato, Alexios.\""
"Amicus se tourne vers Cato et la petite créature féline, s'inclinant devant eux deux."
show cat bow with dis
ca "\"Bonjour.\""
show ale smile with dis
al "\"Bonjour, Amicus.\""
"Le chat, Alexios, fait un signe de tête à Amicus avec un sourire."
"En même temps, je vois Cassius tirer sur le collier doré autour de son cou."
show ale tilt with dis
"Ce n'est pas beaucoup, mais Alexios laisse immédiatement tomber le sourire de son visage, baissant les yeux."
hide ale with dissolve
c "\"Combien de fois dois-je te dire de ne pas le saluer, Amicus ?\""
"Amicus semble ignorer Cassius, marchant vers le lit vide tout en me tirant avec lui."
"Il me murmure à l'oreille."
show ami crossed behind cas with dis
a "\"Assieds-toi devant le lit, fais comme Alex.\""
show ale tilt at three with dissolve
"Je regarde le chat et vois ses oreilles se dresser dans notre direction, bien qu'il continue d'éviter de nous regarder."
"Il est à genoux, alors je fais de même, je commence à me sentir un peu mal à l'aise dans cette posture."
hide ale with dissolve
"Amicus, quant à lui, s'étend sur le lit, un coude dans les coussins alors qu'il élève son corps."
show cat with dis
ca "\"Com, envoyez le petit-déjeuner.\""
com "\"Oui, Cato.\""
"Quelques secondes plus tard, de véritables soucoupes volantes lévitent dans la pièce depuis une autre salle."
"J'ai un moment pour voir une sorte de dispositif noir sur le dessous des assiettes avant qu'elles ne viennent doucement se poser sur la table."
"Je cligne des yeux, mais je ne dis rien, décidant de ne poser aucune question."
"Je décide plutôt de me concentrer sur la nourriture."
"Je peux au moins identifier quelques-unes des portions, l'une d'elles étant ce qui ressemble à du pain."
"Ensuite, il y a une assiette d'une substance étrange, blanche et friable, se trouvant à côté d'un bol qui semble contenir des olives."
"Il y a une bouteille en verre remplie d'un liquide rouge, probablement du vin."
"Enfin, au milieu, à côté de quelques serviettes de table, se trouve une volaille rôtie, dorée et fumante."
"En fait, ça sent vraiment très bon et, étant donné que je n'ai pas mangé de vraie nourriture depuis hier, je sens que j'ai l'eau à la bouche."
"Pourtant, j'ai assez de bon sens pour savoir que je ne peux probablement pas me contenter d'attaquer le banquet comme ça. Je garde alors un œil sur le chat, attendant de voir ce qu'il fera ensuite."
show ale at three with dis
"Il attrape quatre petites assiettes de la grande pile et les pose devant lui."
"Puis il commence à attraper quelques tranches de pain qu'il pose sur l'une des assiettes."
hide ale with dissolve
"Je regarde Amicus et il hoche la tête."
"Alors je fais de même, attrapant quatre assiettes et les posant devant moi sur la table, commençant à attraper les portions de nourriture séparées pour les mettre dans leur propre assiette."
"Pendant ce temps, Cato se penche juste pour attraper le sien pendant que Cassius se racle la gorge."
show cas paw with dis
c "\"Alors… Amicus. Qu'est-ce que c'est ?\""
"Je lève les yeux et je trouve immédiatement les yeux de Cassius enfoncés dans les miens."
"Je décide de détourner le regard et j'attrape le couteau au manche en bois qu'Alexios vient de poser, en l'utilisant pour étendre la substance blanche sur les tranches de pain."
"Je me plisse le nez en voyant à quel point c'est puant et je me rends compte que c'est probablement un type de fromage."
show ami with dis
a "\"Il s'appelle [mc]. C'est mon animal de compagnie.\""
c "\"Non, Amicus. Qu'est-ce que c'est. Ce n'est pas l'un de nos Enfants. Appartient-il à un Frère ou une Sœur ?\""
"J'écoute à moitié la conversation pendant que je vois Alexios tendre ses pattes nues et retirer juste un morceau de viande de la volaille."
"J'hésite, j'aurais voulu avoir de quoi me laver les mains, mais je le fais quand même, la température de la viande me faisant grimacer."
"La tentation de juste fourrer le morceau dans ma bouche est si forte, mais j'arrive à résister et à le déposer dans l'assiette."
"Enfin, je prends une poignée d'olives et les mets dans leur propre assiette."
"À ce stade, je peux voir qu'Alexios aligne ses assiettes devant Cassius sur le lit."
"Prudemment, je fais la même chose pour Amicus, même si je perds une olive dans le processus."
"Je le regarde rouler sur le sol, mais décide de l'ignorer, et Amicus me tapote simplement la tête avec un\"merci\"."
a "\"Non… il vient d'une civilisation dont l'ascension a échoué.\""
show cas surprised
show cat surprised
with dis
stop music fadeout 5.0
"Je regarde Alexios commencer à remplir un gobelet avec le liquide rouge, mais je lève les yeux lorsque je réalise qu'il y a un silence complet."
"Cassius et Cato regardent tous les deux Amicus."
"Je le regarde et vois qu'il a l'air plutôt calme, même si je peux le voir se jouer nerveusement avec ses griffes.."
c "\"T — Tu es sérieux ?\""
show ami crossed talking with dis
a "\"Oui.\""
c "\"Po — Pourquoi !? C'est un barbare !\""
a "\"Parce que j'ai décidé que les enfants abandonnés méritaient de rétablir un contact régulier. Si nous voulons nous unir face aux Khemians, nous devons aussi nous unir —\""
"Je commence à remplir le gobelet d'Amicus alors que je sens ses yeux sur moi."
show ami crossed with dis
a "\"- que nous soyons des Enfants ou non. Avoir un animal de compagnie comme celui-ci montrera mes intentions aux Khemians.\""
show cas angry with dis
"Cassius se moque bruyamment, mettant une olive dans sa bouche et la mâchant vigoureusement."
c "\"Une habile manœuvre de ta part, Amicus, mais tu as quand même volé le vaisseau de père pour y arriver. Utiliser l'hyperespace sans l'autorisation de l'empereur est une violation de la loi, n'est-ce pas, Cato ?\""
"Je donne le gobelet à Amicus, me demandant silencieusement si le loup va être jeté en prison dès mon premier jour ici."
"Que m'arriverait-il alors ?"
"Pourtant, Amicus a l'air calme et quand il voit mes yeux écarquillés, il fait un clin d'œil."
show cat talking with dis
ca "\"C'est possible, mais il n'y a pas d'empereur, Cassius ?\""
"Cato se couche enfin, ses petites assiettes remplies de nourriture."
"Il tourne la tête vers Amicus."
ca "\"Es-tu en train de dire que tu as piloté le vaisseau jusqu'aux confins de notre empire ? Les commandes vocales ne fonctionnent que pour l'empereur, si je ne me trompe pas.\""
a "\"C'est exact. J'ai appris à naviguer seul sur le vaisseau. J'ai également pu communiquer avec leur peuple, négocier ET signer un, euh, contrat avec eux.\""
"C'est là que je commence à entendre la voix d'Amicus faiblir."
"Je crois en fait maintenant qu'il ne ment pas souvent, car il est clair qu'il est si mauvais dans ce domaine."
"Je copie Alexios et retourne à ma position à genoux à côté du lit, puis passe à une position en tailleur lorsque mes genoux me font trop mal."
"Cato observe la scène silencieusement depuis son lit, et je me sens à nouveau décontenancé par le sentiment qu'il pourrait me regarder."
show cat bow with dis
ca "\"Fascinant.\""
"Cassius retrousse ses lèvres."
show cas furious with dis
c "\"Fascinant !? Il a utilisé l'hyperespace ! Il va s'en tirer parce que père est mort ? Qu'est-ce que cela fait de toutes les autres lois ?\""
c "\"Un mendiant peut-il maintenant voler au marché parce qu'il n'y a aucune autorité pour lui dire de ne pas le faire ? Un enfant peut-il se rebeller contre l'empire parce qu'il n'y a pas d'empereur pour leur dire…\""
show cat with dis
ca "\"Du calme, Cassius. Tu connais les circonstances aussi bien que moi.\""
show cas disappointed with dis
"Cassius ferme la bouche avec un soupir, reportant son attention sur sa nourriture qu'il commence à picorer."
"La conversation semble s'arrêter là, et je me demande si Amicus est tiré d'affaire."
"Alors que Cassius semblait indigné, j'ai le sentiment qu'Amicus n'était pas vraiment en danger."
"Je suppose qu'être le fils de l'empereur a ses avantages."
play music "music/lute.ogg" fadein 5.0
a "\"Peux-tu me donner un peu plus d'{i}azur{/ i}, [mc] ?\""
"Je regarde la table pendant un moment avec confusion."
m "\"Euh… qu'est-ce que c'est ?\""
"J'essaye de garder ma voix basse, mais c'est à ce moment-là que Cassius hurle soudainement, frappant une patte contre sa tête."
show cas angry with dis
c "\"Ô dieux ! Il ne parle pas la Langue ?\""
"Je regarde Cassius et Amicus avec confusion."
show ami crossed serious with dis
a "\"Bien sûr que non, ils ont été abandonnés.\""
ca "\"La plupart des abandonnés parlent encore la Langue… à quelle distance se trouve son étoile d'origine ?\""
a "\"Environ cinquante mille années-lumière.\""
c "\"Je m'en fiche ! Fais-le taire. La dernière chose dont j'ai besoin est un mal de tête causé par le Lingua traduisant manuellement tout ce qu'il dit. C'est cruel.\""
"Je ne sais pas s'il définit le mal de tête cruel, ou moi… probablement moi."
show cas with dis
c "\"Télécharge sa langue sur le Nexus avant que tu ne le laisse encore sortir, Amicus.\""
"Je décide que je n'aime vraiment pas Cassius."
"Il parle de moi comme si je n'étais qu'une propriété…"
show ami crossed with dis
"Puis je sens la patte d'Amicus sur mon épaule pendant un moment, la pressant doucement avant de l'enlever."
"Le sujet de la conversation passe alors à des choses que je ne comprends pas vraiment, principalement la politique et les Khemians, quoi que cela puisse être."
"Malgré leur dispute arrivée plus tôt, Amicus et Cassius sont assez animés dans leur conversation."
"Amicus n'arrête pas de me coller des assiettes vides sur le visage, indiquant que je devrais les remplir."
"Il est clair que je ne vais pas manger pendant que les Loups le font, et je sens mon irritation grandir."
"Je ne suis pas un serviteur, je n'étais pas d'accord avec ça, et même si cela est censé m'aider à me fondre dans la masse, je ne peux pas m'empêcher de penser qu'Amicus aurait pu me mettre dans une meilleure position que ça."
c "\"Virginia m'a envoyé une lettre hier soir disant qu'elle ramènerait un Khemian demain. Il a été piégé ici après l'épuisement de carburant de son moteur supraluminique.\""
show ami surprised with dis
a "\"Oh ? Il n'a pas pu revenir sur le vaisseau de secours ?\""
show cas paw talking with dis
c "\"Il était sur Ancoris à l'époque, il lui a donc fallu plusieurs mois pour revenir à Adastra. Il sera notre invité jusqu'à l'arrivée du prochain vaisseau.\""
c "\"Je pense que ce sera assez intéressant d'en voir un en personne. Qui peut se vanter d'avoir rencontré deux Frères et Sœurs ?\""
"Cassius se penche et commence à caresser la fourrure d'Alexios."
show cas with dis
show ale smile e at three with dissolve
"Le chat vert et gris ferme les yeux, souriant et ronronnant."
"Je regarde ça pendant un moment, puis je me fige en sentant la patte d'Amicus sur ma tête."
show ami eyes with dis
"Il commence à gratter doucement mon cuir chevelu avec ses griffes émoussées, ébouriffant mes cheveux."
"En fait, ça fait vraiment du bien, mais sachant ce qu'il fait me met encore une fois en colère."
"Il sait déjà que je ne veux pas faire ça, qu'il m'a amené ici contre ma propre volonté."
"Maintenant, il me caresse en public comme si j'étais son animal de compagnie ?"
"Eh bien… je dirais que c'est logique, je suppose qu'il rempli son rôle m'aider à me fondre dans sa société, tout comme je remplis le miens."
"Mais ça ne veut pas dire que je ne déteste pas ça, et puis son autre patte me met son gobelet vide sous le nez."
show ami happy eyes with dis
a "\"Plus de vin, s'il te plaît.\""
"Je laisse le gobelet pendre en l'air pendant un moment, puis le prends et vais chercher la lourde bouteille de vin d'une manière robotique, me mettant à genoux pour mieux le verser dans le gobelet vide."
"Je le remplis pendant qu'Amicus continue de me caresser."
show ami with dis
a "\"Je parie que peu de gens se permettent de se vanter d'avoir rencontré une espèce abandonnée, tu ne crois pas ?\""
show cas annoyed with dis
"Cassius regarde fixement Amicus, et je regarde fixement le vin."
"J'essaie de me rappeler que c'est juste pour m'aider à rentrer chez moi…"
"… Ou peut-être qu'il m'exhibe simplement parce qu'il aime mettre en rogne Cassius."
"Je me mets à genoux pour faire face au loup et lui rend son gobelet, remarquant à quel point il est plein, le vin glissant presque sur le bord."
"Amicus tend sa patte pour prendre le gobelet."
"Mes doigts tremblent, puis je sens le gobelet glisser hors de ma main. Je ne peux que le regarder tomber au ralenti sur le côté du lit."
"Le vin rouge jaillit dans les airs, éclaboussant le devant de la fourrure claire d'Amicus."
stop music
play sound "sfx/winespill.ogg"
show cas surprised
show cat surprised
show ale shocked
show ami shocked at jumping
with dis
"Le loup perd son souffle, s'asseyant soudainement alors que le vin coule le long de sa poitrine, mouillant son ventre et son pantalon."
show ami embarrassed with dis
a "\"Merde !\""
show ale tilt
show cas smile eyes
with dis
"Pendant ce temps, Cassius éclate de rire derrière moi, reniflant d'une manière très énervante."
play music "music/trouble.ogg"
c "\"Hahahahaha ! Il y a peut-être une raison pour laquelle si peu de gens se sont aventurés à les rencontrer, Amicus.\""
"Je vois Alex me regarder, mais quand nos regards se croisent, il baisse les yeux."
hide ale with dis
"Amicus me tend la main pour prendre l'une des serviettes, tout en me regardant."
"J'essaye d'empêcher un rictus d'apparaître sur mon visage, mais je pense que j'échoue."
show ami surprised with dis
"Il fait une pause, me regardant avec étonnement alors que je suppose qu'il se rend compte que je l'ai fait exprès."
"Il n'a pas l'air en colère cependant, et attrape plutôt la serviette commençant à tapoter sa poitrine, la fourrure tachée toujours d'une couleur sombre et brune."
show cas paw talking with dis
c "\"Que fais-tu, Amicus ?\""
"Cassius a fini de rire et je le vois nous regarder."
show ami disappointed with dis
a "\"Que veux-tu dire par \"que fais-tu\" ? Je nettoie ce bazar.\""
"Amicus grogne en direction de Cassius, en continuant de se nettoyer."
show cas paw annoyed with dis
c "\"Seigneur, tu ne sais vraiment pas comment t'y prendre. Punis-le.\""
"Cassius mime paresseusement une gifle dans les airs."
"Je regarde alors Amicus, et lui aussi me regarde."
show ami embarrassed with dis
a "\"Qu — N — Non, je ne peux pas faire ça.\""
c "\"Pourquoi pas ?\""
a "\"C'est… dans le contrat; pas de punitions physiques, comme pour Alexios.\""
show cas surprised with dis
c "\"Quoi !?\""
a "\"Tu m'as bien entendu.\""
show cas angry with dis
c "\"Alexios est un Frère ! Ta créature à peine un Enfant.\""
show ami angry with dis
a "\"IL est à moi et ce n'est pas à toi de décider pour lui.\""
show cas paw talking with dis
c "\"Les espèces inférieures ne peuvent apprendre que par la punition, Amicus !\""
"Il me regarde."
c "\"Toi, créature, debout. Je vais te frapper à sa place.\""
show cas scared
show ami angry teeth
with vpunch
a "\"CASSIUS !\""
"Je sursaute, tout comme Cassius, les oreilles sifflant alors que la voix profonde d'Amicus résonne en moi."
show cat with dis
"Pendant ce temps, Cato reste assis sur son lit, écoutant… ou peut-être pas."
a "\"Laisse moi mettre les choses au clair tout de suite. JAMAIS tu ne poseras la moindre patte sur lui, ou lui ordonneras quoi que ce soit !\""
show cas annoyed with dis
"Cassius, se remettant du choc, lève un sourcil à Amicus."
c "\"Et si je le fais, mon frère ?\""
"La fourrure d'Amicus redevient normale tandis qu'il hausse les épaules."
show ami crossed serious with dis
a "\"Alors je te frapperai.\""
show cas scared with dis
c "\"Qu-Tu… Tu ne peux pas faire ça, nous ne sommes plus des louveteaux !\""
show ami crossed with dis
a "\"Et si tu l'appelles à nouveau \"créature\", je ferai de même.\""
"Cassius semble s'étouffer pendant un moment."
c "\"Mais quelle mouche t'a donc piqué, Amicus !?\""
"Son regard se tourne vers le loup plus âgé."
c "\"Cato !\""
show cat talking with dis
ca "\"Oui, Cassius ?\""
show cas furious with dis
c "\"Eh bien FAITES quelque chose! Il ne peut pas me menacer comme ça !\""
show cat with dis
ca "\"Amicus, sois gentil avec ton frère.\""
show cas sad with dis
"Les oreilles de Cassius devinrent rouge vif et il s'effondre sur le lit, regardant fixement sa nourriture restante."
stop music fadeout 5.0
ca "\"Quoi qu'il en soit, si vous avez fini tous les deux, partez étudier. Ne sois pas en retard cette fois, Amicus. Ton tuteur s'est plaint à nouveau la semaine dernière.\""
show ami frustrated with dis
a "\"C'est aujourd'hui ?\""
ca "\"Tu sais, tu devrais faire plus attention. Après avoir vu ce que tu as accompli, je vais commencer à me pencher vers les Épreuves pour prendre ma décision.\""
show ami surprised
show cas surprised
with dis
"La pièce devient soudainement très silencieuse."
ca "\"Et Cassius, j'ai besoin de te parler un moment avant que tu partes.\""
hide cas
hide cat
with dissolve
"Amicus se lève et je fais de même."
show ami serious at center with moveinright
"Le loup jette un coup d'œil à Cassius et Cato, mais ils sont en pleine conversation."
"Il se retourne vers moi."
a "\"J'ai oublié que c'est ma journée d'étude, donc je serai parti un petit moment. Je vais demander à Alexios de te montrer le palais et te donner quelque chose à faire pendant mon absence.\""
"Je me sens tendu à l'idée de me retrouver sans la seule personne que je connaisse ici."
m "\"Sérieusement ?\""
a "\"Écoute, tu n'as rien à faire, je vais le préciser à tout le monde, mais je pense que tu préfèrerais peut-être faire {i} quelque chose {/ i} plutôt que de rester assis dans ma chambre toute la journée.\""
"Il semble penser que ce sont les tâches qui me dérangent plutôt que du fait de me laisser seul."
m "\"Très bien.\""
show ami embarrassed with dis
"Amicus fronce les sourcils et je ne peux pas m'empêcher de me sentir un peu mal."
"Il semble essayer de rendre les choses aussi faciles que possible pour moi."
m "\"Et… désolé.\""
"Je fais un geste vers son torse encore taché."
show ami crossed with dis
a "\"Ne t'inquiète pas. Oui, le vin n'est pas facile à faire partir de la fourrure, mais je sais pourquoi tu l'as fait, et je l'ai mérité.\""
c "\"Ugh, est-ce que ça-il parle encore avec sa langue ?\""
a "\"La ferme, Cassius.\""
c "\"Quoi !?\""
a "\"Alexios.\""
"Amicus fait un geste vers le petit chat qui empile actuellement la vaisselle sale les unes sur les autres."
show ami with dis
a "\"Pourrais-tu montrer à [mc] le palais et les tâches à accomplir ? Il ne connaît presque rien.\""
show ale smile at one with dissolve
al "\"Je serais heureux de le faire, Amicus !\""
show cas paw annoyed at eleven with dissolve
show ale tilt with dis
c "\"Donc toi tu peux donner des ordres à {i} mon {/ i} animal de compagnie ?\""
"Cato, debout près de la porte et clairement impatient de partir, soupire."
ca "\"Assez. Essaie d'être raisonnable Cassius. Maintenant, partez tous les deux étudier… et va te laver rapidement, Amicus\""
hide cas
hide ale
with dissolve
show ami serious with dis
"Amicus grogne et commence à tourner les talons, avant de se retourner vers moi et de poser une patte sur mon épaule."
show ami with dis
a "\"Je serai de retour ce soir…\""
"Le grand loup s'arrête, comme s'il voulait en dire plus, mais me laisse avec un simple…"
show ami eyes with dis
a "\"À plus tard.\""
hide ami with dissolve
"Et avec ça, il me fait un petit signe de la main et un autre clin d'œil avant de suivre Cassius et Cato à travers l'arche."
"Juste au moment où Amicus part, Cassius fait une pause pour me donner un regard amer… là encore, la plupart de ses expressions sont plutôt acerbes et cela me met toujours autant mal à l'aise."
"Alors je reste seul avec le chat."
"Je ressens un étrange sentiment de solitude en voyant Amicus partir comme ça."
"C'est comme si ma mère venait de me déposer à l'école maternelle, ou quelque chose comme ça."
"Il est le seul à me traiter comme une vraie personne… du moins, qui me traite le plus comme tel."
"J'entends quelqu'un se racler la gorge derrière moi."
play music "music/dawn.ogg"fadein 10.0
show ale with dissolve
al "\"Bonjour.\""
"Le petit chat me sourit agréablement, ses pattes bien serrées devant lui."
"Je dis qu'il est petit, mais il a vraiment à peu près la même taille que moi."
"C'est juste étrange de voir un autre extraterrestre de ma taille alors que je dois toujours regarder les Loups."
m "\"Euh, salut.\""
"Je vois l'œil gauche d'Alexios se contracter et il lève une patte sur sa tête."
show ale smile w with dis
al "\"Oh là là. Cette journée s'annonce intéressante.\""
m "\"… Quelque chose ne va pa ?\""
"Plus de contractions."
show ale talking e with dis
al "\"Juste mon Lingua. Cela prendra un certain temps pour apprendre votre langue, mais cela s'améliorera au fur et à mesure que tu parles… alors si cela ne te dérange pas, j'aimerais en savoir plus sur toi. Je suis très curieux.\""
m "\"Euhhh…\""
"Amicus m'a dit de faire l'idiot, alors j'essaie de trouver comment je pourrais faire ça."
"Je feinte un regard lointain."
m "\"Loin, par là-haut…\""
show ale shocked w with dis
"Alexios cligne des yeux, puis rit."
show ale smile with dis
al "\"Oh.\""
"Nous restons tous les deux là maladroitement pendant un moment avant qu'il ne fasse un geste vers la table."
show ale with dis
al "\"Eh bien, prends place, veux-tu ? Nous mangeons leurs restes lorsqu'ils ont fini.\""
show ale at right with moveinright
"Le chat se déplace pour s'asseoir sur le lit de Cato, cherchant sa propre petite assiette."
"Je me rappelle à quel point j'ai faim, alors je fais rapidement de même, choisissant de m'asseoir sur le lit de Cassius puisque celui d'Amicus est couvert de vin."
show ale talking with dis
al "\"Cette nourriture sera-t-elle faite pour votre estomac ?\""
m "\"Je pense que oui. Cela ressemble en fait à certaines des choses que je mange là d'où je viens. Enfin, ce sont essentiellement des olives, du pain et de la viande.\""
"Je montre chacun des plats."
"Alexios remet sa patte contre sa tête."
show ale smile w with dis
al "\"Oh dis donc, tant de mots, et en phrases complètes aussi !\""
"Je me fige."
m "\"Oh euh… eh bien, je ne sais pas vraiment ce qu'est cette nourriture, je devine juste…\""
show ale w with dis
al "\"Non, je veux dire, ce sont vos mots. Tant d’entre eux et dans des phrases complètes et complexes.\""
"Putain, je ne suis pas bon pour ça."
al "\"Je suppose que les Loups avaient déjà beaucoup amélioré votre intelligence avant d'abandonner votre ascension.\""
m "\"Oh, peut-être…\""
"Je me demande si j'ai déjà ruiné notre plan, mais Alexios ne semble pas alarmé, juste curieux, alors je reporte mon attention sur la nourriture."
"Il ne reste plus grand-chose sur la table."
"Cato avait mangé la viande si bien qu'il ne restait que les os de la volaille."
"A côté se trouvent quatre tranches de pain et le bol d'olives."
"Alexios se concentre sur la volaille, y travaillant avec ses griffes jusqu'à ce qu'elle se sépare en deux avec un fort son de déchirement."
"Il m'en tend une moitié."
show ale with dis
al "\"Tu devrais pouvoir y trouver un peu de viande.\""
"Je le lui prends, essayant de ne pas montrer ma déception."
"Puis il met deux tranches de pain sur une assiette et la fait glisser vers moi avant de prendre les deux autres."
al "\"Assure-toi d'utiliser le fromage. Le pain est un peu fade sans ça.\""
"Je retire quelques fines lanières de viande de l'os et je goûte."
"C'est bon, vraiment, vraiment bon et je fouille rapidement les os pour en avoir plus, mais il n'y a pas grand-chose."
show ale smile with dis
al "\"Tu as encore faim ?\""
"Je lève les yeux et vois Alexios ramasser délicatement sa propre moitié d'oiseau."
m "\"Ouais… je n'ai pas mangé depuis quelques jours.\""
show ale shocked with dis
al "\"Oh vraiment ? Pourquoi ?\""
m "\"Le… voyage ici a été un peu difficile. Je dirais que j'ai mangé sur le vaisseau, mais ce n'était pas très copieux.\""
show ale tilt with dis
al "\"Oh, comme la bouillie de protéines qu'ils ont ? Ouais, ce truc est assez horrible. Je peux comprendre pourquoi tu as faim. Eh bien, tu n'as plus à t'inquiéter.\""
m "\"Pourquoi ça ?\""
show ale smile with dis
al "\"Nous dînons avec nos maîtres dans leurs chambres. Amicus se sert toujours de très grosses portions et me donne aussi un peu de nourriture car Cassius n'en prend pas beaucoup\""
"Alexios étend lentement du fromage sur son pain."
al "\"Il prendra bien soin de toi à cet égard.\""
"La mention d'Amicus me fait me sentir un peu seul."
"En fait, quelque chose que j'ai remarqué, c'est que tout le palais semble être vide."
m "\"Alors… où est passé tout le monde ?\""
"Alexios mâche pensivement son pain."
show ale tilt with dis
al "\"Hm ?\""
"J'essaie de trouver un moyen de formuler les choses bêtement, puis j'abandonne car je décide qu'il sait déjà que je suis capable de former des \"phrases complexes\"."
m "\"Ce palais ne semble pas accueillir beaucoup de monde.\""
al "\"Oh ! Tattendais-tu à trouver d’autres personnes ici ?\""
m "\"Eh bien, des domestiques, des gardes ou des responsables par exemple ?\""
show ale talking e with dis
al "\"La plupart des besoins dans le palais sont couverts par l'intelligence artificielle et les drones. Il en va de même pour la défense du palais.\""
al "\"Je suppose que cela peut être différent d'où tu viens, mais les Drères et Sœurs ont appris il y a longtemps que moins il y a de Sapiens dans un endroit qui doit être sécurisé, mieux c'est. Nous sommes une exception bien entendu.\""
"Le pain a un véritable goût de craie, alors je décide d'étaler un peu de fromage dessus malgré l'odeur."
"À ma grande surprise, c'est salé, crémeux et pas mal du tout."
"L'odeur {i} est {/ i} difficile à ignorer, cependant."
m "\"Alors… quel est l'intérêt d'avoir un animal de compagnie ?\""
show ale tilt w with dis
al "\"Amicus ne te l'a pas dit ?\""
m "\"Eh bien, il l'a fait. Il m'a mentionné le statut par exemple. Y a-t-il une autre raison ? Pourquoi devons-nous faire des choses pour eux s'ils ont des robots qui peuvent le faire à leur place ?\""
show ale talking w with dis
al "\"Le statut est la raison principale, oui. Notre devoir est d'être à leurs côtés lors d'apparitions publiques ou lors de réunions officielles. De toute évidence, avoir un Sapiens artificiel faisant la même chose n'est pas du tout impressionnant.\""
al "\"Nous n'avons vraiment rien à faire de manuel dans le palais, mais Cassius aime l'idée qu'un Sapiens soit son serviteur. Il dit que cela lui rappelle le bon vieux temps.\""
m "\"Je vois. Amicus m'a dit que je n'avais vraiment rien à faire pour lui… sauf brosser sa fourrure.\""
show ale smile w with dis
al "\"Ah oui, Amicus est très méticuleux à ce sujet.\""
m "\"Tu le connais bien ?\""
show ale w with dis
al "\"Assez bien. Je suis ici depuis quelques mois maintenant, donc j'ai eu ma juste part d'interactions avec lui, même si Cassius n'aime pas ça.\""
m "\"Je vois… que penses-tu de lui ?\""
show ale smile e with dis
al "\"Je pense que tu as beaucoup de chance d'avoir un maître comme Amicus.\""
m "\"Pourquoi ça ?\""
show ale e with dis
al "\"Eh bien, Amicus est très… gentil. Parfois, il essaie d'être tout à fait officiel et affirmé, et il aime me taquiner, mais il se présente comme plus ouvert, qu'il en ait l'intention ou non.\""
show ale smile e with dis
al "\"Comparé à Cassius, bien sûr.\""
"Je réfléchis un instant."
m "\"Tu n'aimes pas être l'animal de compagnie de Cassius ?\""
"Il y a une pause, bien qu'Alexios continue de sourire."
al "\"Cassius est très… précis sur la façon dont il veut qu'on lui parle et ainsi de suite, mais c'est une grande qualité pour un futur empereur, c'est sûr.\""
show ale e with dis
al "\"Mais dans une conversation informelle, il est beaucoup plus facile de parler à quelqu'un comme Amicus.\""
"Je prends une gorgée de vin et pour autant que je sache, c'est similaire aux rares fois où je l'ai bu sur Terre."
m "\"Il a été vraiment gentil avec moi.\""
"Au moins après tout ce kidnapping."
al "\"C'est une personne très gentille. Il a juste tendance à… ne pas penser à tout.\""
show ale tilt e with dis
"Les yeux d'Alexios se tournent pour regarder derrière moi avant qu'il ne se reconcentre sur mon visage."
show ale smile e with dis
al "\"Comprends bien que normalement nous ne devrions pas parler aussi franchement de nos maîtres. Ceci est juste une conversation entre animaux de compagnie.\""
m "\"Oh… Oui, je comprends.\""
"Il y a un moment de silence qui dure juste assez longtemps pour être mal à l'aise."
show ale w with dis
al "\"Oui, je me doutais que tu le ferais… Je dois dire que tu es extrêmement perspicace, presque au même niveau qu'un Frère ou une Sœur.\""
"Je grimace intérieurement alors qu'Alexios souligne à nouveau mon intelligence."
"Il ne m'a fallu que 10 minutes pour échouer dans mon seul et unique travail."
"Alexios me sourit à nouveau."
show ale smile with dis
al "\"Ah, n'étais-je pas censé le savoir ?\""
"Apparemment, il est aussi perspicace."
m "\"Euh…\""
show ale with dis
al "\"Ne t'inquiète pas. Comme je l'ai dit, c'est entre les animaux de compagnie—\""
"Alexios se penche de manière conspirative."
show ale tilt with dis
al "\"Je ne fais pas que raconter tout ce que je sais à mon maître. Je suis simplement son serviteur, pas un espion.\""
show ale with dis
"Il se penche à nouveau."
al "\"Bien qu'il souhaiterait peut-être que je le sois, mais honnêtement, c'est vraiment agréable de pouvoir parler à quelqu'un d'autre que mes supérieurs. Amicus a été le seul à me traiter comme un égal, mais Cassius garde généralement notre contact minimal.\""
"Je mets le dernier morceau de pain dans ma bouche et dès que je le fais, Alexios se redresse."
al "\"Com, nous avons terminé.\""
com "\"Oui, Alexios.\""
"Je regarde avec fascination les plats léviter de la table et flotter à travers l'arche par laquelle ils sont passés à l'origine."
al "\"Tu veux sortir ? Comme je l'ai dit, il n'y a pas grand chose à faire, mais les jardins nécessitent une touche plus intelligente pour les garder présentables.\""
m "\"Oui, bien sûr.\""
"Je dégage les miettes de mon jean et me lève."
"J'ai toujours faim, mais le peu que j'ai mangé m'aura au moins un peu calé l'estomac."
stop music fadeout 5.0
scene bg palace1 with dissolve
"Je suis tranquillement Alexios à travers les couloirs, et j'apprécie véritablement l'architecture du palais pour la première fois."
"Nous entrons dans le hall principal et Alexios se tient dans la lumière du soleil qui pénètre à travers les arcades."
show ale smile with dissolve
al "\"Ahh, les matinées ne sont-elles pas magnifiques ici? C'est le meilleur moment pour travailler dans les jardins. Je dirais que nous avons trois bonnes heures avant qu'il ne fasse trop chaud.\""
"Nous commençons à marcher dans les jardins quand quelque chose me vient à l'esprit."
m "\"Attends, tu viens de dire que nous avons trois heures ?\""
show ale tilt e with dis
al "\"Oui ?\""
m "\"Eh bien… combien de temps dure une heure ici ?\""
play loop "sfx/fountain.ogg"fadein 5.0
scene bg garden1 with dissolve
show ale w with dis
al "\"Autant de temps que chez toi.\""
m "\"Oh, donc nous utilisons les mêmes durées ici ?\""
"Cela ne me semblait pas possible."
"Alexios pense, frottant l'endroit au-dessus de son sourcil gauche."
show ale tilt w with dissolve
al "\"Ah, eh bien, le Lingua est un appareil compliqué. C'est de la technologie parentale que nous ne comprenons pas, mais ce que nous savons, c'est qu'elle traduit la langue d'une manière qui offre la meilleure compréhension possible pour l'hôte.\""
"Alexios s'accroupit près d'un pilier, examinant le lierre qui pousse autour de sa surface."
show ale w with dis
al "\"J'ai utilisé une mesure du temps spécifique aux loups et à leur langue, et le Lingua l'a simplement traduite en une mesure que tu dois mieux de comprendre.\""
"Le petit chat rit."
show ale smile w with dis
al "\"C'est quelque chose que j'ai renoncé à comprendre moi-même. Ce n'est pas parfait et peut créer des situations vraiment déroutantes. Surtout lorsqu'il s'agit de certains mots et chiffres.\""
m "\"Oh.\""
"Je vois Alexios isoler une petite fleur blanche qui pousse à la base du pilier avant de la cueillir et de la mettre sur le côté."
"Je commence à me demander si je devrais peut-être apprendre la Langue."
"Le lingua est impressionnant et tout, mais cela ne me semble pas être très précis."
show ale smile w with dis
"Alexios sourit."
al "\"N'y pense pas trop.\""
show ale w with dis
al "\"Essaye simplement de te rappeler que cela ne veut pas dire que tout {i} est {/ i} pareil. Il y a 19 heures dans une journée sur Adastra, ce qui, j'imagine, est au moins quelque peu différent par rapport à votre propre planète.\""
show ale with dis
al "\"Quoi qu'il en soit, ce que je fais en ce moment, c'est arracher quelques mauvaises herbes. Les drones font un bon travail d'arrosage et de lutte antiparasitaire, mais ils manquent souvent de petites mauvaises herbes comme celles-ci.\""
"Je m'accroupis au pilier à côté d'Alexios, cherchant dans le lierre des herbes à arracher à la base."
m "\"Alors… il y a 19 heures dans une journée ici ?\""
al "\"Oui.\""
m "\"C'est un peu plus court que chez nous.\""
al "\"Oh je comprends cela. Il y a 30 heures dans une journée d'où je viens. Cependant, on s'y habitue après quelques semaines. Je préfère ça, à vrai dire.\""
hide ale with dissolve
"Je reporte mon attention sur le pilier et je me retrouve soudain à fixer du regard une chose étrange ressemblant à un crabe collée à la pierre."
"Au début, je me demande si c'est une sorte de sculpture, car elle est si grande."
"Mais en regardant de plus près, ça bouge et je me rends compte que c'est une énorme araignée vivante."
"L'instant d'après, j'effectue une roulade comme dans un film d'action avant de me remettre sur pieds afin de m'éloigner du pilier."
scene bg garden1 with vpunch
m "\"OH MON DIEU !\""
show ale shocked with dis
al "\"Qu'est-ce qu'il y a !?\""
m "\"Une sorte… d'araignée !\""
"Je me tiens à une bonne dizaine de mètres du pilier maintenant, mais je peux toujours voir l'énorme araignée, ses pattes épaisses déployées sur la largeur d'une horloge."
"Je frissonne."
m "\"Eugh !\""
show ale smile w with dis
al "\"Ah… hahaha. Oh je vois.\""
"Je le regarde."
m "\"En quoi c'est drôle !?\""
al "\"Je suis désolé. Elles {i} sont {/ i} très surprenantes lorsqu'on les voit pour la première fois.\""
"Alexios s'approche de l'araignée et commence à agiter les bras pour la faire partir."
"Même d'ici, je peux voir ses yeux noirs perçants."
"Elle ne bouge pas du tout, choisissant de rester immobile sur son pilier."
al "\"Les arachnides et insectes adastrans sont d'une taille inquiétante par rapport à ceux de ma lune d'origine.\""
"Je regarde autour de moi, me sentant soudainement en danger, imaginant des guêpes géantes descendant du ciel."
show ale serious w with dis
"Alexios commence à avoir l'air plus frustré alors que l'araignée refuse d'être intimidée par ses mouvements de bras efféminés."
al "\"Rien dans les jardins n'est dangereux, et elles sont nécessaires pour équilibrer l'écosystème. Le venin de cette créature est bien trop faible pour causer beaucoup plus qu'une simple bosse urticaire, et il faut qu'elle morde.\""
"Alexios donne un autre coup faible à l'araignée et cette dernière en profite pour attacher son bras si vite qu'elle devient floue avant de s'arrêter sur son visage."
show ale shocked w with dis
"Pendant un moment, nous restons tous les deux là sous le choc alors qu'il s'accroche à lui tel un facehugger."
"Puis-"
show ale vshocked w at jumping with dis
al "\"PAR GALEN ! ENLÈVE-LÀ !\""
show ale vshocked w at my_shake with dis
"Il danse sur place pendant un moment et je ne peux que regarder la scène avec horreur."
"Finalement, il secoue la tête fort et l'araignée saute sur le sol avant de se faufiler dans quelques buissons."
"Alexios reprend son souffle pendant un moment, tout tremblant."
"Malgré moi, je dois rire d'étonnement de ce que je viens de voir."
show ale embarrassed e with dis
al "\"Po - Pourquoi est-ce que tu ris ?\""
m "\"Désolé, c'était juste… tellement surprenant, et tu étais si sûr de toi jusqu'à ce que—\""
"Je rigole encore."
al "\"Eh bien, cela m'a surpris !\""
"Il frissonne en se frottant les épaules."
show ale flustered e at center with dis
al "\"Honnêtement, il n'y a rien à craindre d'elles en temps normal, mais quand elles sont sur toi... Et puis avec la façon dont elles se déplacent —\""
"Il frissonne à nouveau."
show ale serious w with dis
al "\"Et toi tu es resté là à regardé, sans rien faire !\""
m "\"Qu'est-ce que j'aurais bien pu faire ? Si ça m'était arrivé, j'aurais sauté dans l'étang.\""
"Alexios soupire et je vois sa fourrure recommencer à s'aplatir."
show ale smile w with dis
"Puis il rit aussi."
al "\"Eh bien… j'étais sur le point de le faire.\""
show ale w with dis
al "\"Quoi qu'il en soit, retournons au travail. Si tu vois une autre araignée… contourne-la.\""
stop loop fadeout 5.0
hide ale with dissolve
play music "music/secondthoughts1.ogg"
"Pendant l'heure suivante, nous passons de pilier en pilier, nettoyant les mauvaises herbes."
"Je suis beaucoup plus vigilant maintenant, je vérifie chaque pilier pour ne pas me retrouver en tête à tête avec une araignée avant de me mettre au travail."
"Heureusement, je n'en trouve pas d'autre."
"Au bout d'un moment, nous nous installons enfin sur un banc sous des arbres et Com fait flotter quelques plateaux de minuscules pâtisseries qui me rappellent des quiches."
"Viennent ensuite des verres de boissons fraîches, vertes et au goût de légumes."
"C'est délicieux."
m "\"Alors, je peux te demander d'où tu viens ?\""
show ale smile with dissolve
al "\"De très loin. Encore plus loin que chez toi.\""
m "\"Qu'est-ce qui t'a amené ici ?\""
show ale tilt with dis
"Le chat soupire et s'arrête avec une pâtisserie à mi-chemin de sa bouche."
al "\"C'est un peu compliqué, mais j'étais ici comme une sorte d'ambassadeur. Je suis arrivé juste au moment où l'épuisement du carburant supraluminique s'est produit.\""
m "\"Comment ça ?\""
"Alexios hausse les épaules."
al "\"Eh bien, pour telle raison, les Romanus ont cessé de fournir aux Loups de l'énergie pour leurs moteurs lorsque l'empereur est mort. Ils sont liés à leur étoile en ce moment, ils ne peuvent donc pas me ramener sur ma planète.\""
show ale with dis
al "\"La situation entre les Loups et leurs parents est préoccupante, et nous ne savons pas combien de temps les Loups passeront sans pouvoir emprunter l'hyperespace, alors mon peuple a envoyé son propre vaisseau pour récupérer tout le monde sur Adastra, mais je l'ai, euh, raté.\""
m "\"Tu l'as manqué ?\""
"Alexios fronce les sourcils, l'air de nouveau embarrassé."
show ale tilt e with dis
al "\"Eh bien… j'ai trop dormi et j'ai raté le départ.\""
m "\"Wow, vraiment ?\""
al "\"Je veux dire, ça arrive aux meilleurs d'entre nous, non ?\""
m "\"J'imagine oui… pourquoi ils ne t'ont pas attendu ? C'est un peu foireux qu'ils partent sans toi.\""
al "\"Lorsque tu utilises l'hyperespace, le temps est important. Tout fonctionne selon un horaire spécifique, donc si tu le manques, tu le manques. Et ils ne vont certainement pas en envoyer un autre pour une seule personne.\""
m "\"Wow, tu n'avais pas de réveil ou quelqu'un pour te réveiller ?\""
show ale sad e with dis
al "\"Crois-moi, ce fut une série de nombreux événements malheureux qui ont conduit à cela, le principal étant que même si je me suis réveillé avec suffisamment de temps pour atteindre le spatioport, je me suis perdu dans le terrible système de transport public d'Adastra City.\""
al "\"Je courais de plate-forme en plate-forme, et les Loups tout autour de moi essayaient de me toucher parce qu'ils n'avaient jamais vu de chat auparavant, et je pouvais à peine lire les panneaux parce que… eh bien, pour mon espèce, l'eau monte vite aux yeux quand nous sommes stressés, alors…\""
m "\"Oh, tu pleurais.\""
show ale embarrassed e with dis
al "\"… Tu sais ce que c'est ?\""
m "\"Oui, mon espèce le fait aussi.\""
"Il détourne le regard et je peux voir l'intérieur de ses oreilles devenir rouge."
al "\"Ah, je ne le savais pas. C'est un trait commun entre nous et les Loups, mais je n'en connais pas beaucoup d'autres qui le font, à part les Khemians.\""
show ale serious e with dis
al "\"Quoi qu'il en soit, j'ai finalement décidé de profiter de ma situation pour continuer mon travail et construire une relation avec la famille impériale. Alors, je suis devenu l'animal de compagnie de Cassius.\""
"La situation d'Alexios ne semble pas si différente de la mienne, même si les raisons pour lesquelles nous sommes arrivés ici étaient très différentes."
m "\"Quand est-ce que le prochain vaisseau arrive ?\""
show ale tilt with dis
"Alexios hausse les épaules."
al "\"Des années. Au moins un par décennie, mais parfois plus. J'espère que ce sera pour dans quelques années par contre.\""
m "\"Je suis désolé d'entendre ça.\""
show ale smile with dis
al "\"Heh, ce n'est pas la pire vie, et les Loups me traitent assez bien. Nous avons une relation spéciale.\""
m "\"… Avec Cassius ?\""
al "\"Entre nous et les Loups. Contrairement aux autres Frères et Sœurs, nos parents sont originaires de la même galaxie. Bien que nos points de vue soient très différents, ça crée bien des liens.\""
"Alexios frôle ses pattes ensemble."
show ale with dis
al "\"As-tu terminé ?\""
m "\"Ouais.\""
stop music fadeout 10.0
play loop "sfx/fountain.ogg"fadein 10.0
al "\"Com, nous avons terminé.\""
"Et avec ça, les assiettes et les verres s'envolent."
"Je commence à m'habituer à tout ça."
al "\"Mais… [mc], c'est ça ?\""
m "\"Oui.\""
show ale smile with dis
al "\"Haha, je suis désolé. Je suppose que nous avons sauté les présentations. tu me connais déjà sous le nom d'Alexios, mais tu peux m'appeler Alex.\""
m "\"Enchanté Alex.\""
show ale talking w with dis
al "\"Enchanté [mc]. Alors, maintenant que tu as fini de te faire passer pour un imbécile, dis-moi d'où tu viens. Parle-moi de toi.\""
"Je prends une pause pour réfléchir."
"Bien qu'il ait été vraiment gentil avec moi jusqu'à présent, je sais que je ne peux pas tout révéler à Alex, alors je me contente d'être vague comme lui."
m "\"Eh bien, je viens de loin, mais de moins loin que toi. Je suis un primate.\""
show ale w with dis
al "\"Je vois. Es-tu une important parmi ton peuple ?\""
m "\"Non, je ne suis qu'un étudiant.\""
al "\"Oh… sais-tu pourquoi Amicus t'a choisi, alors ?\""
m "\"… Je pense qu'il m'a choisi au hasard. Je suis juste arrivé à l'endroit où l'ascension aurait dû se produire.\""
show ale shocked w with dis
"Alexios cligne des yeux, puis rit."
show ale smile w with dis
al "\"C'est tout Amicus, ça.\""
m "\"Ouais, c'est vrai que ça lui ressemble.\""
show ale with dis
al "\"Mais je suppose qu'il est logique de choisir quelqu'un de la plèbe s'il veut unir à nouveau les enfants abandonnés.\""
m "\"Ah oui ?\""
"Je pense que s'éloigner de la conversation est une bonne tactique pour le moment."
al "\"Ouais, il ne t'a pas expliqué cela ?\""
m "\"Euh, peut-être un peu. Il ne m'a pas dit grand-chose.\""
show ale smile with dis
al "\"Hehe, ne le prends pas personnellement. Amicus n'anticipe pas souvent.\""
show ale talking with dis
al "\"En ce moment, les Loups sont dans une posture assez délicate. Encore une fois, c'est entre toi et moi, mais ils ont pris du retard par rapport aux autres Frères et Sœurs en termes d'expansion et de ressources.\""
al "\"La raison principale étant qu'ils n'élèvent pas leurs Enfants à des niveaux d'intelligence similaires à eux.\""
m "\"Niveaux d'intelligence ? Je pensais qu'ils diffusaient juste leur culture ?\""
"Alex me regarde."
show ale tilt with dis
al "\"Tu ne le sais pas ? Je suppose que tu as été abandonné mais… tu devrais savoir que ton intelligence, l'intelligence de chaque enfant, a été élevée par un frère ou une sœur.\""
m "\"Oh… non, je suppose que nous avons perdu cette information.\""
show ale serious with dis
al "\"Eh bien, ce n'est pas tout. Ces enfants sont en quelque sorte des serviteurs sous contrat. En échange d'avoir leur intelligence… \"élevée\", ils doivent servir l'empire jusqu'à ce que la dette soit remboursée.\""
"Ça ne m'a pas vraiment l'air équitable."
m "\"Oh. Et depuis combien de temps ça dure ?\""
show ale smile with dis
al "\"Hé, eh bien, disons simplement que les premiers Enfants des Loups élevés avec succès n'ont pas tout à fait fini de rembourser leur dette.\""
m "\"Ça ressemble à… de l'esclavage ?\""
"Alex me regarde."
show ale serious with dis
al "\"N'est-ce pas ?\""
"C'est assez déroutant pour moi."
m "\"Mais, s'ils ont tous ces robots et tout, pourquoi ont-ils besoin de Sapiens pour être leurs esclaves ?\""
al "\"Les Sapiens artificiels avancés sont offerts par les parents. Nous ne pouvons pas les construire. Nous sommes un peu gâtés ici dans le palais, mais pas tellement à l'extérieur.\""
al "\"Et même alors, la sapience artificielle n'est pas parfaite et ne le sera probablement jamais. Les machines pensantes effectives n'existent pas. C'est pourquoi il est important d'élever les Enfants au même niveau d'intelligence qu'un Frère ou une Sœur; les bonnes idées peuvent venir de n'importe où.\""
m "\"Je suppose que votre peuple ne fait pas pareil que les Loups ?\""
al "\"Non, nous élevons nos enfants autant que nous le pouvons. Cette pratique est unique aux Loups. Ils sont considérés par les autres Frères et Sœurs assez… durement envers leurs propres Enfants et réfractaires aux droits des Sapiens en général.\""
m "\"Je vois.\""
"Je commence à voir les Loups et même Amicus sous un tout nouveau jour."
"Comme s'il lisais dans mes pensées, Alex continue."
show ale with dis
al "\"Mais les choses changent. Qu'Amicus t'ai choisit comme son animal de compagnie montre qu'il te voit comme un égal… mais il y a Cassius.\""
show ale serious with dis
"Alex bat de la queue sur le banc entre nous."
al "\"Il préfère que les choses restent comme elles sont… ou même régressent. C'est pourquoi il a lancé un défi de taille à Amicus. Il y a beaucoup de loups qui ne sont pas convaincus du changement suggéré par Amicus, et l'alliance proposée entre les Loups et les Khemians ne fait qu'augmenter le doute.\""
m "\"Les Khemians?\""
al "\"C'est une autre espèce fraternelle, la plus puissante de la galaxie, en fait. Mais cela inquiète beaucoup de gens ici. Il n'y a pas eu de guerre entre Frères et Sœurs depuis plus de cent ans, mais la dernière a eu lieu entre les Khemians et les Loups.\""
al "\"Tu peux imaginer quel genre de problèmes cela pourrait créer. Cassius donc, qui veut que les Loups restent indépendants et contrôlent totalement leurs Enfants, est plutôt populaire.\""
show ale  with dis
al "\"Tu te demandes peut-être pourquoi je te dis cela, mais je veux que tu comprennes l'empire dans lequel tu es. Cela facilitera ton… adaptation.\""
"En effet, je me demandais pourquoi il me disait tout cela."
"Y'a-t-il une autre raison qu'il ne me dit pas ?"
"Je le regarde."
m "\"Tu veux que Cassius devienne empereur ?\""
show ale smile with dis
al "\"J'aime que nous puissions discuter de nombreuses choses, et être Frère ou Sœur me permet d'avoir plus de liberté que la plupart des autres, mais c'est une chose sur laquelle je devrais probablement me taire.\""
"Cela ne fait que me dérouter davantage, mais il ne semble pas qu'il soit du côté de Cassius."
"Peut-être qu'Amicus et moi pourrions en faire un allié ?"
m "\"Eh bien, je pense que je préférerais choisir Amicus si son plan était de traiter les autres Sapiens de la même manière.\""
"D'après ce que je peux voir, cela semble plaire à Alex."
show ale with dis
al "\"Eh bien, nous le saurons après les Épreuves.\""
"L'humeur d'Alex s'éclaircit soudainement."
show ale smile with dis
al "\"J'ai vraiment apprécié passer du temps ensemble aujourd'hui. Comme je l'ai dit, c'est tellement agréable de pouvoir parler à quelqu'un qui n'est pas mon supérieur. J'espère que nous pourrons le faire souvent pendant que tu es ici.\""
m "\"Ouais, bien sûr.\""
show ale with dis
al "\"Merveilleux.\""
"Alex lève une patte pour regarder le soleil… Vita."
al "\"Nous devrions nous remettre à travailler. Il commence à faire trop chaud ici.\""
stop loop fadeout 3.0
"Pendant les prochaines heures, nous travaillons autour du jardin avant de finalement nous déplacer à l'intérieur pour nous promener un peu dans le palais."
scene bg palace1 with dissolve
"Il me montre des portes menant vers la salle du trône et le bain commun, mais nous n'entrons jamais à l'intérieur et il me dit que je ne devrais le faire que quand je suis avec Amicus."
scene bg diningroom with dissolve
"Finalement, nous retournons dans la salle à manger où Alexios nous propose de regarder les écrans jusqu'au retour de nos maîtres."
"Il dit que cela me familiarisera mieux avec la culture lupine."
"Il me faut un moment pour me rendre compte que je regarde une sorte de film mettant en vedette des loups similaires à Amicus."
"Ils jouent des scénarios sur le voyage dans l'espace et la recherche de plus de Sapiens."
"Les espèces intelligentes qu'ils trouvent sont des loups masqués… Je suppose qu'ils n'ont pas vraiment d'images de synthèse car chaque effet semble faits main."
"C'est long, ennuyeux et le jeu d'acteur est trop exagéré, comme dans un film muet."
"Finalement, après ce qui semble être trois bonnes heures, Alex me dit qu'Amicus reviendra bientôt et que je ferais bien de ranger sa chambre avant qu'il ne rentre."
"Je suis soulagé de couper court au film, et Alex et moi nous séparons pour aller dans nos salles respectives."

scene bg palace1night with dissolve
play loop "sfx/crickets.ogg"fadein 3.0
"Je suis surpris de voir qu'il fait déjà noir dehors."
"Même avec la journée plus courte, je suppose que regarder sans réfléchir des loups surjouer avec d'autres loups masqués a fait passer le temps plus rapidement que je ne le pensais."
"Sur mon chemin à travers les salles de marbre, je m'arrête de temps en temps pour regarder les grandes peintures murales représentant tout, des loups nageant aux loups se battant à l'épée face à d'autres canidés."
"Dans le hall principal se trouve la plus grande fresque murale, représentant cinq loups."
"Les dessins sont plats et manquent de toute sorte de perspective, ce qui donne aux museaux un aspect un peu de travers."
"Deux plus grands loups surgissent au-dessus des trois autres; l'un est blanc avec une forme féminine tandis que le plus grand des deux est noir et tient sa patte contre sa poitrine."
"Autour de sa tête se trouve une couronne."
"Des trois plus petits loups, l'un est également clairement féminin tandis que l'autre est blanc."
"Je me demande si ce pourrait être Cassius et Virginia, ce qui voudrait dire qu'Amicus est le dernier loup."
"Il est plus maigre, et je me demande si cela pourrait être lui enfant ou adolescent."
"Une couronne lumineuse flotte au-dessus de sa tête."
unk "\"Ahem.\""
"Je sursaute alors que quelqu'un s'éclaircit la gorge très fort à côté de moi."
show cat with dissolve
"Je me retourne et me surprends à regarder Cato, le conseiller."
"Il me regarde de haut en bas pendant un moment… du moins c'est ce que je pense qu'il fait."
"Tout est silencieux."
"J'ouvre la bouche pour répondre, puis je me souviens de ce qu'Amicus m'a dit."
"Je laisse mes yeux flous et ma bouche s'ouvrir un peu."
m "\"Euhhhh…\""
"Les oreilles de Cato tremblent au son que je fais puis s'éclaircit à nouveau la gorge."
show cat bow with dis
ca "\"Bonjour… [mc], n'est-ce pas ? Comment se passe ta première journée au palais ?\""
"Je me demande si je devrais continuer à faire des bruits démontrant ma supériorité intellectuelle ou si je devrais au moins répondre à la question."
"Je suis techniquement un Sapiens, donc je suppose que ce n'est pas grave si je comprends en quelque sorte."
m "\"Euhhh… bien.\""
"Le côté gauche du visage cicatrisé de Cato se contracte alors qu'il en attend plus, mais je ne lui donne rien."
show cat talking with dis
ca "\"Bien, bien… J'espère qu'Alexios t'a fait visiter le palais ? La vie est un peu étouffante derrière ces murs, mais j'espère qu'avec le temps, nous pourrons t'emmener en ville.\""
"Je croise un peu les yeux."
m "\"Oh… j'aime ça…\""
show cat smile with dis
ca "\"Heh, oui. Alors… d'où viens-tu, exactement ?\""
"Il y a quelque chose derrière les mots de ce loup, quelque chose qui est plus que de la curiosité pour le coup."
m "\"Euh, grosse planète rocheuse à côté étoile…\""
"Cato attend et encore une fois je ne dis rien de plus."
show cat frown with dis
ca "\"Avez-vous un nom pour la planète ?\""
m "\"Oui…. Grosse planète rocheuse.\""
"Cato masse le côté gauche de son front, l'air un peu agacé."
ca "\"Grosse planète rocheuse ?\""
m "\"Avec de l'eau…\""
"Cato me regarde fixement."
ca "\"Alors… Grosse planète rocheuse avec de l'eau ?\""
"Je hoche la tête bêtement."
hide cat with dissolve
"Cato soupire bruyamment et s'éloigne, ne prenant même pas la peine de mettre fin à la conversation."
ca "\"Merveilleux… maintenant j'ai mal à la tête.\""
"Et avec ça, il disparaît dans un couloir."
"Je décide que j'ai fait un bon travail car Cato semble penser que je suis un énorme idiot."
stop loop fadeout 3.0
"Je me dirige rapidement vers la chambre d'Amicus, heureux de ne rencontrer personne d'autre."

scene bg amicusroom with dissolve
"Il n'y a pas grand chose à faire; la chambre d'Amicus est impeccable, donc après avoir déambulé et lissé les couvertures du lit, je choisi de m'asseoir sur le canapé et d'attendre."
"Malgré le fait que je ne sois debout que depuis dix heures probablement, je suis épuisé."
"Peut-être que je n'aurai aucun problème à m'adapter aux journées plus courtes."
"Alors que je commence à somnoler, il y a un bruit de cliquetis soudain vers la porte."
"Je sursaute et je vois Amicus entrer, rouler dans un plateau avec plusieurs assiettes dessus, remplies de nourriture."
"Il me sourit et j'ai un sentiment de soulagement en le voyant."
show ami happy with dissolve
a "Bonsoir ! Désolé, je suppose qu'Alex ne t'a pas dit que les drones plaçaient le plateau devant la porte à la quinzième heure. Il s'est bien occupé de toi ?\""
m "\"Ouais, il était gentil.\""
"Amicus fait rouler le chariot vers le canapé, puis se laisse tomber dessus à côté de moi, faisant trembler le tout."
show ami with dis
with vpunch
play music "music/memories.ogg"fadein 5.0
a "\"Uggghhhh, c'était une longue journée.\""
m "\"Ça va ?\""
"Amicus ouvre un œil."
a "\"Bof. J'ai dû revoir les maths aujourd'hui, j'ai l'impression que ma tête va exploser. Cela n'a pas aidé que Balbus me frappe la tête avec son bâton quand je me trompais\""
m "\"Wow, ça n'a pas l'air facile.\""
show ami happy eyes with dis
a "\"Ne t'inquiète pas, ce n'est rien comparé à celui que tu m'as donné.\""
"Amicus a un sourire narquois, et je ne peux pas m'empêcher de sourire à ses taquineries."
"Il semble être devenu plus à l'aise avec moi avec la façon dont il est détendu."
m "\"Je suis désolé.\""
show ami with dis
a "\"Ne le sois pas et arrête de t'excuser pour ça. Maintenant lavons-nous les pattes et mangeons. Je n'ai rien avalé depuis le petit-déjeuner.\""
hide ami with dissolve
"Nous allons tous les deux dans la salle de bain pour nous rincer les pattes et les mains dans l'évier avant de remplir nos assiettes avec de la nourriture."
"C'est plus ou moins la même chose avec le pain, la viande et les olives, mais il y a aussi une bonne quantité d'autres légumes et de fruits que j'ai du mal à identifier."
"Amicus me montre comment combiner les fruits et le fromage sur le pain et je commence vraiment à aimer cette pâte… tant que j'ignore son odeur."
"Comparé au petit-déjeuner, Amicus mange vraiment beaucoup."
"Il finit probablement par manger environ trois fois plus que moi."
"Pendant tout ce temps, il me parle de son instructeur effrayant et comment il le punit bien plus que Cassius."
m "\"Ben alors, il donne généralement les bonnes réponses ?\""
show ami embarrassed with dis
a "\"Eh bien… oui, mais il devrait m'aider à comprendre plutôt que de me tirer les oreilles. Ça n'aide en rien, à moins qu'il n'ait l'information dans son bâton et qu'il ne la grave dans mon cerveau d'une certaine manière.\""
m "\"Ne t'inquiète pas; Je déteste aussi les maths.\""
a "\"Eh bien, je suis meilleur dans d'autres domaines comme la littérature et l'histoire. Ha ! Cassius est incapable de se souvenir des batailles.\""
show ami motivated with dis
"Amicus contracte un biceps."
a "\"Et il peut oublier la lutte. Il ne pourrait jamais me battre en plein combat.\""
m "\"Ouais, je ne pense pas non plus.\""
show ami with dis
a "\"Alors oui, il peut avoir les maths et tout ce qu'il veut. Les Épreuves ne portent pas là dessus.\""
m "\"Quels sont ces Épreuves dont vous n'arrêtez pas de parler ?\""
"Amicus prend une grande gorgée de vin, reprenant sa respiration quand il retire enfin le gobelet de sa bouche."
show ami crossed with dis
a "\"C'est ce que Cato envisage d'utiliser pour décider du prochain empereur. Essentiellement trois épreuves; musique et danse, rhétorique et enfin combat.\""
m "\"Et celui qui les gagne devient empereur ?\""
a "\"Eh bien, celui qui gagne deux épreuves sur trois. Le combat est le dernier, de sorte que si l'un de nous gagne les deux premiers, il n'y ai pas de match nul.\""
a "\"J'espère vraiment que Cato me choisira dans les prochains jours maintenant qu'il t'a vu. Mais si les épreuves ont lieu, tu n'as pas à t'inquiéter.\""
"Amicus me sourit avec confiance."
m "\"Je ne m'inquiète pas ?\""
show ami crossed serious with dis
a "\"Je suis meilleur que Cassius dans au moins deux de ces choses, peut-être même dans la musique et la danse.\""
m "\"Tu sais, je te croirais bien, mais une chose que je sais de toi, c'est comment, euh… tu peux être trop confiant quand il s'agit de certaines choses.\""
show ami embarrassed with dis
a "\"Pourquoi dis-tu cela ?\""
m "\"Toute notre expérience sur le vaisseau, peut-être ?\""
show ami crossed serious with dis
a "\"C'est… différent. Je faisais quelque chose que je ne comprenais pas vraiment. Je comprends mes études… à part les mathématiques.\""
"Amicus se penche enfin en arrière, une patte sur le ventre."
show ami with dis
a "\"Quoi qu'il en soit, comment s'est passée ta journée ? Alex t'a-t-il fait visiter ?\""
"Amicus commence à attraper la nourriture restante pour la mettre de côté dans sa propre assiette."
m "\"Ouais. J'ai réalisé qu'il n'y avait pas grand chose à faire.\""
a "\"Ah, oui, ce n'était pas une journée terrible. Demain je n'ai pas cours, alors nous pourrions faire quelque chose de plus amusant.\""
m "\"Comme quoi ?\""
show ami smile with dis
a "\"Oh, je ne sais pas. Aller nager, aux bains, ou parler. Tu me dis. Peut-être que nous pourrons éventuellement aller en ville aussi.\""
m "\"La ville dehors ?\""
show ami with dis
a "\"Eh bien, tout est dehors.\""
m "\"Je parle plutôt de celle que je peux voir de l'autre côté du lac.\""
a "\"Oui, celle-là. Adastra City, la capitale de notre empire.\""
m "\"Oh… elle m'a l'air petite pour une capitale, non ? Enfin, ça a l'air vraiment bien, mais ça ressemble à une ville de taille moyenne.\""
"Amicus fronce les sourcils."
show ami embarrassed with dis
a "\"Je pense que c'est assez grand. Quelle est la taille des villes sur Terre ?\""
"Je hausse les épaules."
m "\"Je ne sais pas, assez gros ? Des millions de personnes, parfois.\""
"Amicus lève un sourcil."
show ami thinking with dis
a "\"Des millions ?\""
m "\"Euh, ouais.\""
"Je me demande si le Lingua traduit tout correctement."
m "\"Pourquoi ? Combien de personnes habitent Adastra ?\""
a "\"La ville ? Un peu plus de cinq millions. Sur la planète, il y a 80 millions de loups.\""
m "\"Oh.\""
a "\"Combien y a-t-il d'humains ?\""
m "\"Environ sept milliards.\""
show ami shocked with dis
"Amicus s'étouffe."
a "\"Quoi !?\""
m "\"Ça fait beaucoup ?\""
show ami surprised with dis
a "\"C'est absurde ! N'avez-vous pas mis en place des mesures de contrôle des naissances ?\""
m "\"Eh bien, pas dans la plupart des pays.\""
"Amicus secoue la tête."
show ami crossed serious with dis
a "\"Eh bien, vous êtes sans Parents, donc je suppose que cela a du sens que votre espèce soit si… malavisée ?\""
"Amicus semble essayer très fort de choisir le dernier mot même s'il est toujours très condescendant."
"Il semble cependant remarquer mon agacement."
a "\"Eh bien, votre espèce se porte-t-elle bien ? Votre planète est-elle capable de subvenir aux besoins d'une telle population ?\""
m "\"… En quelque sorte. Je dirais qu'il y a des problèmes.\""
"Amicus se caresse le menton."
a "\"Eh bien, je suppose que lorsque je deviendrai empereur, je pourrais interroger notre Parent sur votre espèce. Tout cela est un vrai mystère, mais il est clair que nous avons dû négliger votre peuple d’une certaine manière\""
show ami crossed with dis
"Il me sourit."
a "\"Peut-être que nous pourrions même vous ramener sous notre protection !\""
m "\"Whoa, attends une seconde.\""
"Des images de vaisseaux spatiaux romains descendant des cieux pour asservir la race humaine tout cela à cause de moi me traversent l'esprit."
m "\"Tu sais, Alex m'a dit ce que vous faites aux autres Sapiens. Cela ne ressemble pas à quelque chose dont les humains voudraient faire partie.\""
show ami embarrassed with dis
a "\"De quoi t'a-t-il parlé ?\""
m "\"À propos de l'esclavage.\""
a "\"L'esclavage ?\""
m "\"Ce que vous faites à vos Enfants.\""
a "\"Eh bien… c'est un mot dur pour ça.\""
m "\"Non, c'est le mot juste. Les humains sont passés par les 'serviteurs sous contrat' sur Terre, et cela ne s'est jamais bien passé pour les 'serviteurs'.\""
"Les oreilles d'Amicus descendent un peu."
m "\"Et aussi malavisés que soient les humains, nous avons au moins aboli l'esclavage.\""
"Je remarque que les oreilles d'Amicus deviennent rouges."
"Peut-être qu'il ne s'attendait pas qu'un humain lui enseigne l'éthique."
a "\"Ah, eh bien, je - je veux vraiment changer un peu les choses quand je deviendrai empereur.\""
m "\"Un peu ?\""
show ami sad with dis
a "\"Enfin, le changement ne doit pas être trop abrupt; il doit être progressif.\""
m "\"Hm.\""
show ami angry with dis
"Amicus agite sa queue avec agacement vers moi."
a "\"Écoute, je suis d'accord avec toi. Nous essayons de changer la façon dont nous traitons nos enfants depuis des générations. Mon grand-père et mon père ont tous deux travaillé dans ce sens.\""
m "\"Eh bien, même si c'est clairement dégoûtant et définitivement injuste, je pense que la manière dont vous gérez leur intelligence est encore pire.\""
show ami embarrassed with dis
a "\"De quoi parles-tu ?\""
"La grimace sur le visage d'Amicus me dit qu'il connaît peut-être déjà la réponse."
m "\"La façon dont vous avez limité l'intelligence des enfants que vous étiez censé élever.\""
"Amicus est silencieux pendant un moment."
"Je peux dire que tout cela le met très mal à l'aise."
"Je me demande à nouveau comment j'en suis arrivé à ce point; assis sur un canapé à débattre d'éthique avec un futur loup empereur."
"Il croisa enfin les bras et souffla."
show ami crossed serious with dis
a "\"Encore une fois, je suis d'accord avec toi sur tout cela. Je n'aime pas la façon dont nous avons traité nos Enfants. En fin de compte, je sens vraiment que devenir un empire plus compatissant et uni mènera à un meilleur résultat pour tout le monde.\""
a "\"Cela se fera en petites étapes, mais comprends bien que c'est quelque chose que je veux réparer.\""
a "\"Et arrête de dire \"vous\" comme si {i} je {/ i} l'avais fait. J'y suis né.\""
"J'en viens à réaliser à quel point Amicus est un livre ouvert, donc je ne doute plus de ses paroles."
m "\"Eh bien, tant que Cassius ne devient pas empereur.\""
"Amicus souffle du nez."
a "\"Comme si c'était possible.\""
m "\"Eh bien, s'il le DEVIENT, il me semble qu'il veuille inverser tout cela.\""
a "\"Et je te dis qu'il n'y a aucune chance qu'il le soit… Attendez, que t'a dit Alex ?\""
m "\"Ce fut une courte conversation. Je lui ai posé des questions sur l'empire.\""
"Je ne l'ai pas fait, mais je ne veux pas causer d'ennuis à Alex au cas où il ne serait pas censé me le dire."
m "\"Cassius semble être une personne terrible en passant, et je ne parle pas seulement de sa personnalité. Il veut garder les gens asservis.\""
show ami embarrassed with dis
a "\"C'est… compliqué. Il est juste très traditionnaliste, mais là encore, il ne peut pas devenir empereur.\""
"Je soupire face à l'excès de confiance du loup, mais il connaît son frère bien mieux que moi."
m "\"Eh bien, je suis au moins content d'être derrière le bon loup pour rentrer à la maison.\""
show ami crossed with dis
a "\"Le bon loup ?\""
m "\"Ouais, je ne peux pas m'imaginer être l'animal de compagnie de ton frère.\""
"Amicus jette un coup d'œil à l'assiette qu'il avait remplie de la nourriture."
a "\"En parlant de ça, je vais apporter ça à Alex dans le jardin. Tu veux m'accompagner ?\""
"Je passe une main dans mes cheveux, gras à cause du manque de douche pendant deux jours."
m "\"Pourrais-je plutôt utiliser la douche en ton absence ? Je me sens un peu sale.\""
a "\"Oh oui, bien sûr. Euh, entre et ça démarre. Il y a un écran sur le mur qui contrôle la température. Il possède un spectre de couleurs sur lequel tu peux faire glisser le doigt—\""
m "\"Je vais me débrouiller.\""
show ami eyes with dis
a "\"Ah, c'est vrai. Eh bien, je devrais être de retour lorsque tu auras terminé.\""
hide ami with dissolve
stop music fadeout 10.0
"Et avec ça, Amicus met en équilibre son assiette de nourriture dans ses pattes alors qu'il sort de la pièce, me laissant aller dans la salle de bain."
scene bg bathroom with dissolve
"J'utilise à nouveau rapidement les toilettes, soudainement heureux de ne pas avoir à utiliser des toilettes \"publiques\" comme celles dont j'avais vu des dessins dans mes livres d'histoire romaine."
"La douche est assez facile à comprendre, et l'eau est immédiatement chaude et agréable, donc je n'ai pas à me soucier de la température."
"Il y a plusieurs bouteilles de savon en verre, alors je choisis celle qui a l'odeur la plus agréable et je me lave rapidement."
"Quand j'ai fini, je prends une serviette sur le mur et je me sèche avant de l'enrouler autour de ma taille."
"Je pense à remettre mes vêtements, mais l'idée de rentrer dans mes sous-vêtements sales me fait hésiter."
scene bg amicusroom with dissolve
"Au lieu de cela, j'ouvre la porte et je suis accueilli à la vue d'Amicus assis sur le bord du lit, regardant sur le côté, une patte sur ses genoux tenant une brosse."
"Sa tête tourne dans ma direction avant qu'il ne détourne immédiatement les yeux."
play music "music/starship.ogg"fadein 10.0
show ami shocked with dissolve
a "\"Désolé ! Pardon ! Je ne voulais pas voir, je pensais que tu serais habillé —\""
m "\"Hé, ça va. J'ai la serviette.\""
show ami surprised with dis
"Lentement, Amicus tourne son regard vers moi, les yeux dérivant sur mon torse avant de se relever immédiatement."
a "\"Oh ! Euh, je pensais que tu détestais toute sorte de nudité ?\""
m "\"Pas vraiment, juste les… organes génitaux. Et ce n'est pas que je déteste ça. C'est juste… plus privé.\""
a "\"Ah…\""
"Amicus semble me regarder et je commence à me sentir un peu gêné."
m "\"Est-ce que tout va bien ?\""
show ami sad with dis
"Amicus détourne de nouveau le regard."
a "\"Désolé, je - je n'ai simplement pas l'habitude de te voir comme ça. Je n'ai vu que des humains avec des vêtements, alors j'ai en quelque sorte imaginé que tu étais toujours comme ça.\""
m "\"Eh bien… mes vêtements sont sales alors j'allais te demander si tu en avais des propres, au moins jusqu'à ce que tu puisses me faire d'autres vêtements ?\""
show ami surprised with dis
a "\"Oh, bien sûr ! Com ! Envoie-nous des robes du stockage… des robes pour enfants, s'il te plaît.\""
com "\"Oui, Amicus.\""
m "\"Merci.\""
show ami eyes with dis
a "\"Je t'en prie.\""
"Je reste là maladroitement pendant encore quelques secondes jusqu'à ce qu'Amicus semble revenir à la réalité à nouveau."
show ami surprised with dis
"Il lève la brosse."
show ami with dis
a "\"En tout cas, j'ai pensé que tu aimerais peut-être que je m'occupe de ton pelage aussi ? Je pense que c'est la moindre des choses après ce que tu as fait pour moi.\""
m "\"Oh, eh bien, ce n'est que sur ma tête.\""
show ami happy eyes with dis
a "\"C'est d'autant plus simple pour moi.\""
"Amicus sourit."
m "\"Eh bien… d'accord.\""
show ami with dis
"Je vais vers le lit et je m'assois dos au loup."
"Amicus ajuste son siège pour me faire face plus directement, puis commence à passer doucement la brosse dans mes cheveux."
"Nous restons assis en silence pendant un moment, et je commence à apprécier la sensation du brossage, en particulier la façon dont les poils fermes caressent mon cuir chevelu, me donnant des frissons du haut au bas mon cou."
show ami talking with dis
a "\"Désolé d'avoir autant parlé tout à l'heure. Je… je n'ai pas l'habitude de pouvoir parler à quelqu'un. Le palais est un peu impersonnel, donc avoir une conversation amicale avec quelqu'un d'autre que Com est un peu une nouveauté.\""
show ami eyes with dis
"Amicus rit."
a "\"C'est probablement pourquoi j'avais tant de mal à me concentrer sur mes études aujourd'hui; J'étais tellement excitée de rentrer à la maison et de te parler.\""
"Entendre ça me fait me sentir un peu mal pour le loup."
"Je suppose qu'être le futur empereur ne vous permet pas d'avoir beaucoup d'amis, et être dans un palais aussi vide semble définitivement impersonnel."
"Je suppose que c'est pourquoi Alex m'a dit exactement la même chose."
m "\"Tout va bien. Et je ne voulais pas être trop dur tout à l'heure. Je sais que ce n'est pas ta faute.\""
show ami with dis
a "\"Non, je pense que nous sommes sur la même longueur d'onde là dessus. Raison de plus pour s'unir contre Cassius, n'est-ce pas ? Oh !\""
"Comme s'il avait oublié quelque chose, l'autre patte d'Amicus vient autour de moi et sur sa paume je vois deux raisins violets."
show ami happy with dis
a "\"J'ai réussi à en arracher quelques-uns de la boucle d'oreille d'Alexios. Il n'était pas trop content de ça, haha ! Tu en veux un ?\""
m "\"Sérieusement ?\""
"J'en prends un, plus parce que je suis gentil avec Amicus qu'autre chose, mais quand je mords dedans, je ne peux pas m'empêcher de remarquer à quel point c'est juteux et sucré."
show ami eyes with dis
"Amicus me parle avec le raisin dans sa bouche."
a "\"Mmmh, je ne sais pas pourquoi, mais sa boucle d'oreille en raisin a toujours le meilleur goût. Au fait, si cela ne te dérange pas, j'ai invité Alex à notre sortie de demain.\""
show ami with dis
a "\"Cassius va être absent pour faire quelques discours et va laisser Alex au palais pour une fois.\""
m "\"Bien sûr que non. Nous nous entendons très bien.\""
"Je penche la tête en arrière, permettant au loup de continuer le brossage."
a "\"Votre fourrure… des cheveux, c'est comme ça que vous l'appelez ? Ce n'est pas comme la fourrure d'un loup, mais c'est plutôt joli.\""
"Je souris."
m "\"Merci, Amicus.\""
a "\"Si tu le souhaites, je peux le faire pour toi tous les jours. Je pense que c'est normal.\""
"Je dois admettre que j'aime vraiment ça, alors j'accepte."
m "\"Oui, bien sûr. C'est vraiment agréable.\""
"J'entends des bruits sourds et j'imagine que c'est la queue d'Amicus qui remue contre le lit."
m "\"Donc, mes devoirs sont de te laver, de brosser ta fourrure et de te faire sentir bon ?\""
a "\"Eh bien, cela et m'accompagner à des réunions importantes et des sorties publiques, mais tout ce que tu fais pendant celles-ci est de rester là et d'avoir l'air civilisé.\""
m "\"Ouais, c'est ce que tu n'arrêtes pas de me dire. Tout cela semble assez simple.\""
show ami embarrassed with dis
a "\"Bien que… il y a une chose que tu peux faire pour moi avant d'aller me coucher.\""
m "\"Quoi ?\""
a "\"Eh bien, un - un massage complet du corps.\""
"Je le regarde par-dessus mon épaule."
a "\"Ouuuu, nous pouvons simplement nous en tenir aux autres tâches.\""
"Je ris et les oreilles d'Amicus remontent."
show ami eyes with dis
"Il continue de brosser mes cheveux pendant un moment encore avant de finalement mettre le peigne de côté."
show ami with dis
a "\"Voilà, ça a l'air beaucoup mieux maintenant !\""
"Je passe doucement une main sur mes cheveux, et je dois admettre qu'ils sont plus doux que jamais."
show ami eyes with dis
stop music fadeout 5.0
a "\"Mais de toute façon, [mc], j'attends avec impatience ces mois à venir avec toi, même si nous avons pris un mauvais… départ.\""
"Je repense au loup, à son sourire sincère mais hésitant."
"C'est définitivement un homme de contradictions; moitié téméraire, moitié prévenant."
"Je ne sais pas trop quoi penser de lui, mais à ce stade, je sens que je peux au moins lui faire confiance, et cela en dit long après ce qu'il m'a fait subir."
"Je souris en retour."
m "\"Ouais, moi aussi.\""
scene bg black with transition_fade
jump a1s3
