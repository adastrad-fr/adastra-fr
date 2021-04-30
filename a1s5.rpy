label a1s5:
scene bg black with slow_dissolve
"J'ai beaucoup rêvé la nuit précédant la première épreuve."
"Je ne me souviens pas de tout, mais dans les derniers moments de mon rêve, je suis dans la salle du trône, entouré d'une douzaine de loups que je suppose être les Triumvirats."
"Cato est assis sur le trône, surplombant la salle, son menton reposant sur son poing."
"Pendant ce temps, Amicus est au centre, faisant une sorte de breakdance."
"Il a l'air athlétique et est léger sur ses pieds avant de jeter sa cape et de faire le poirier."
"Puis il tourne sur sa tête pendant un moment alors que les loups autour de lui applaudissent."
"Même Cato applaudit à contrecœur."
"Pendant ce temps, Cassius a la patte à la bouche, réalisant qu'il a été battu, ses os de verre incapables de résister à des mouvements aussi incroyables."
"C'est à ce moment que je me réveille."
scene bg amicusroomdim with dissolve
"J'ouvre les yeux et je vois le contour sombre du plafond au-dessus de moi, les lumières s'allumant automatiquement d'une faible lueur jaune."
"J'entends le doux ronflement d'Amicus à côté de moi et je le regarde, voyant qu'il est à plat sur le dos, la bouche ouverte et étreignant l'un de ses nombreux oreillers contre sa poitrine."
"Je roule sur le dos, ressentant l'angoisse de la première épreuve à venir."
"Après un moment, je murmure au plafond."
m "\"Com, quelle heure est-il?\""
"Com murmure en retour."
com "\"Une heure et demie.\""
"Il me reste donc au moins trois heures avant de pouvoir me lever et me préparer."
"Je ferme les yeux pour essayer de dormir davantage."
"C'est difficile cependant, principalement parce que mon avenir pourrait être déterminé aujourd'hui."
"Amicus m'a dit que nous n'avions besoin que de gagner cette épreuve pour tout gagner."
"Parce que si nous gagnons demain, cela signifie que Cassius devra au moins participer à l'épreuve de combat, à moins qu'il ne perdre directement si nous gagnons aussi la deuxième épreuve."
"Et selon Amicus, Cassius n'a absolument aucune chance contre lui au {i} pugnu {/ i}, et il le sait."
"Bien qu'il puisse encore participer à la deuxième épreuve pour se sauver la face, il devra déclarer forfait pour la troisième, sinon il fera face à une humiliation pure et simple."
"Donc si nous gagnons demain, je suis presque assuré de rentrer chez moi ..."
"La pensée que tout ce fiasco pourrait être bientôt terminé me donne des sentiments mitigés."
"Même si je rentrerai chez moi dès que j'en aurai l'occasion, je ne peux m'empêcher de me sentir un peu triste à l'idée de quitter Amicus et le palais."
"Nous sommes de bons amis à ce stade, et la pensée que je pourrais juste être renvoyé sur Terre et ne plus jamais le revoir ..."
"Je soupire et j'écoute les ronflements périodiques du loup, le son est si doux et apaisant que plutôt que de me garder éveillé, il me berce jusqu'à m'endormir ..."
scene bg black with slow_dissolve
play loop"music/beyondthestars1.ogg" fadein 5.0
"Et encore une fois, je me retrouve flottant dans cette conscience large et vide qui semble déborder au-delà des limites de toute sorte d'individualité."
"Je ne panique pas cette fois."
"Je suis habitué à cette sensation, je sais que ce n'est qu'un rêve et que ça va passer."
"Je sens aussi cette autre présence au-dessus de moi, bien plus grande que moi."
"Elle me suit partout depuis que je suis monté sur ce vaisseau."
"Savoir que quelqu'un d'autre est là m'apaise davantage, et j'attends, me demandant s'il va me parler à nouveau."
"Il rompt finalement le silence."
"\"Je suis toujours curieux.\""
"J'essaie de répondre cette fois, je lui demande ce qui l'intéresse exactement, mais je n'ai pas de bouche avec laquelle parler."
"Il semble m'entendre cependant, et en réponse je sens un léger amusement mélangé avec ..."
"De la fascination?"
"\"Beaucoup, beaucoup de choses, mais encore une fois, j'ai peur de devoir rester bref.\""
"J'attends avec impatience."
"\"Penses-tu qu'Amicus serait capable d'accomplir ses devoirs en tant qu'empereur d'Adastra?\""
menu:
    "Oui":
        $ end_game1 += 1
        $ galaxias = True
        "\"Ah, comme c'est... intéressant.\""
    "Non":
        $ end_game2 += 1
        "..."
    "Je ne sais pas":
        $ end_game3 += 1
        "\"Je vois...peut être que tu as encore besoin de temps. Tu as encore beaucoup, beaucoup à apprendre.\""
stop loop fadeout 7.0
"La présence au-dessus de moi commence à se dissiper, et je m'efface aussi de la réalité."
with Pause(3)
scene bg bathroom with slow_dissolve
"Je me tiens maladroitement dans la salle de bain pendant qu'un autre loup se déplace activement autour de moi, faisant des commentaires courts et tronqués sur ma forme étrange et ma petite taille."
"C'est le premier loup que j'ai vu qui ne fasse pas partie de la famille impériale, alors j'essaie de ne pas le fixer du regard pendant qu'il tourne ma tête à gauche et à droite, en étalant une substance noire sur mon visage."
show ami at right with dissolve
"Pendant ce temps, Amicus se tient derrière nous, son visage montrant un mélange d'amusement et d'inquiétude."
"Je lève un sourcil vers lui à travers le miroir, mais il hausse les épaules en réponse."
"Vieux Loup" "\"Ne bougez pas votre ... visage, s'il vous plaît.\""
"Je regarde à nouveau droit devant moi, le laissant maculer mon visage avec ce maquillage noir, pendant que j'essaie toujours de ne pas le regarder."
"Il est voûté et tombant, portant une sorte de monocle avec des lumières clignotantes."
"La lentille ressort de temps en temps avec un bourdonnement mécanique alors qu'il examine son travail."
"Aussi, je suis en robe."
"Il n'y a pas moyen de tourner autour du pot; je porte une robe bleue moulante recouverte de motifs dorés complexes."
"C'est beau, sans aucun doute, mais je ne suis pas vraiment un amateur de robes, et je sens mon visage rougir d'embarras à chaque fois que je me regarde dans le miroir."
"Alors à la place, je me concentre, le regard fixé sur le mur ou Amicus."
m "\"Alors pourquoi {i} tu {/ i} n'est pas en train de t'habiller?\""
"Vieux Loup" "\"Ne parlez pas, s'il vous plaît.\""
show ami crossed talking with dis
a "\"Moi? Eh bien, je suis déjà habillé en empereur!\""
show ami happy eyes with dis
"Amicus déploie sa cape avec ses deux pattes."
"Je commence à rouler des yeux, mais je m'arrête avant que le vieux loup ne puisse à nouveau me crier dessus."
"Je me rends compte qu'il peint des rayures noires sur mon visage, et cela me rappelle immédiatement des rayures de tigre."
"Une fois que c'est fait, il fait de même pour les parties exposées de mes bras."
"Vieux Loup" "\"N'oubliez pas de ne pas toucher ou gratter votre visage. Aussi, gardez vos bras éloignés de votre corps à moins que vous ne vouliez abîmer le tissu avec ce maquillage.\""
"Le loup recule enfin, donnant un grognement d'approbation avant de se retourner et de fourrer son équipement dans son sac."
show ami eyes with dis
a "\"Merci.\""
"Vieux Loup" "\"De rien.\""
"Et avec ça, le vieux loup se précipite hors de la salle de bain, nous laissant seuls tous les deux."
"Je reste là un moment, me regardant dans le miroir, me sentant comme une attraction de cirque."
m "\"J'ai l'air ... horrible.\""
play music"music/memories.ogg" fadein 5.0
show ami surprised with dis
"Amicus tousse et se rapproche rapidement, posant une patte sur mon épaule."
show ami eyes with dis
a "\" Tu as l'air très bien, en fait. Très élégant.\""
"Je lève les yeux vers le loup et je le vois me sourire."
"Je ne sais pas s'il essaie juste de me faire me sentir mieux, mais là encore, je suppose que les loups n'ont vraiment aucune idée de ce que sont les normes de beauté humaine."
"Je regarde les rayures noires sur mon visage."
m "\"Est-ce que ce sont des rayures de tigre?\""
show ami surprised with dis
"Amicus hausse les sourcils."
a "\"Oui, en effet. Vous avez des tigres sur Terre?\""
m "\"Ouais ... est-ce qu'ils sont genre, d'accord avec ça, ce n'est pas offensant? Cela ressemble à une blague.\""
show ami embarrassed with dis
a "\"Offensant? Pourquoi ce serait offensant? Nous honorons Meera avec cette danse.\""
m "\"Si tu en es sûr ...\""
show ami happy eyes with dis
a "\"Bien sûr que j'en suis sûr! Et tu ne ressembles pas à une blague, tu ressembles à une tigresse hindo forte et belle.\""
"Je soupire à nouveau, tenant toujours maladroitement mes bras loin de la robe, me sentant raide."
m "\"Quand est ce que l'épreuve commence ?\""
show ami with dis
a "\"Eh bien, pour MOI dans une vingtaine de minutes, mais pour toi, dans une heure environ.\""
m "\"D'accord, il y a des choses auxquelles je dois m'attendre avant que ça ne commence?\""
a "\"Pas grand chose, les triumvirats regarderont l'épreuve par liaison vidéo, donc seul Cato sera là pour juger.\""
m "\"Oh.\""
a "\"Garde à l'esprit que tout sera retransmit en direct pour tout le reste d'Adastra, alors ...\""
"Amicus voit l'expression sur mon visage."
show ami embarrassed with dis
a "\"Euh ... peut-être que je n'aurais pas dû te dire ça?\""
m "\" TOUT Adastra? En direct !?\""
a "\"Ne t'inquiétes pas! Personne ne sera réellement présent, alors... fais semblant, j'imagine.\""
m "\"Pourquoi tu me l'a dit ?\""
show ami crossed serious with dis
a "\"Eh bien, j'avais prévu que tu regardes la première moitié de l'épreuve dans la salle à manger. Tu aurais découvert comment tout se passe jusqu'à ce que ce soit ton tour.\""
"Je déglutis bruyamment."
show ami embarrassed with dis
a "\"Je ne voulais pas te cacher ça, j'ai juste pensé que tu savais peut-être que ce serait le cas ... la lune entière prête une attention très particulière aux Épreuves.\""
"Il a raison, j'ai en quelque sorte supposé que ce serait le cas, mais maintenant que j'en ai la certitude ..."
"J'ai l'impression que je vais m'évanouir."
"Peut-être que j'aurai de la chance et que ça arrivera quand Meera mourra pendant la danse."
show ami eyes with dis
a "\"Écoute, tout ira bien. Nous allons gagner cette épreuve et avant que tu ne t'en rendes compte, je serai empereur et nos problèmes seront résolus.\""
"Encore une fois, l'idée que mon retour à la maison soit presque garantie dans l'heure qui suit ..."
"Cela me rappelle les pensées que j'avais eues la nuit dernière."
m "\"Alors, euh, quand je rentrerai sur Terre, ce sera la dernière fois que je te verrai?\""
show ami embarrassed with dis
"Les coins de la bouche d'Amicus se tordent en un froncement de sourcils, mais seulement pendant un moment avant qu'il ne sourit à nouveau."
show ami eyes with dis
a "\" Eh bien, je suppose que cela dépend de toi. Avec un accès illimité au moteur supraluminique, je pourrais peut-être faire des visites de temps en temps. Ça te plairais ?\""
"Je n'ai même pas besoin de réfléchir à ma réponse."
m "\"Ouais.\""
show ami happy with dis
"Le sourire d'Amicus s'élargit."
a "\"Moi aussi.\""
m "\"Ouais, je veux dire, tu es mon ami, et je voudrais entendre des nouvelles de ton empire.\""
show ami embarrassed with dis
"Mais alors le sourire d'Amicus faiblit, puis se transforme en froncement de sourcils."
m "\"Quoi?\""
"Le loup est silencieux pendant un moment, puis ses oreilles s'aplatissent."
a "\"Je euh ... j'ai oublié la raison pour laquelle tu es ici en premier lieu.\""
"Pendant a moment, je ne sais pas de quoi il parle ... Puis je réalise."
"Nous ne sommes même pas censés savoir que l'autre existe."
"Tout cela est contraire à la loi."
m "\"Oh ... alors je suppose que nous ne pourrons pas faire ça, hein?\""
"Amicus se mord la lèvre, puis secoue la tête."
show ami motivated with dis
a "\"Nous verrons cela plus tard, ne pensons plus à ça pour le moment. Nous avons une épreuve à gagner!\""
show ami with dis
"Amicus se tourne vers moi et, après un court moment d'hésitation, me prend dans une rapide étreinte, évitant soigneusement la poudre noire sur mes bras."
a "\"Nous parlerons plus après, autour d'un dîner de fête, d'accord?\""
"La confiance absolue et le réconfort dans la voix d'Amicus me calme un peu, et je parviens à esquisser un petit sourire."
m "\"Très bien ...\""
show ami eyes with dis
a "\"Bien! Et euh ... on célébrera ma victoire autrement après ça, si tu vois ce que je veux dire. \""
"J'avais presque oublié ça."
m "\"Amicus ...\""
show ami happy eyes with dis
a "\"Si tu en as envie, si tu en as envie ...\""
show ami with dis
"Amicus rit avant que ses oreilles ne se redressent, son com personnel lui parlant dans un petit bruit murmurant."
a "\"Très bien, c'est le signal. Dirige toi vers la salle à manger si tu souhaites regarder. Sinon, Com te dira quand partir pour la salle du trône, d'accord?\""
"Je hoche la tête, et Amicus me donne une dernière tape sur l'épaule avant de se retourner."
m "\"Euh, bonne chance. Je sais que tu vas réussir.\""
show ami eyes with dis
stop music fadeout 10.0
"Amicus me fait un signe de la main avant de passer la porte, me laissant seul dans l'attente."
scene bg amicusroom with dissolve
"Je me dirige vers le lit et m'assois, reposant soigneusement mes bras sur le côté. J'aurais souhaité qu'ils aient appliqué le maquillage juste avant la danse pour que je n'ai pas à marcher comme un épouvantail."
"Je me rends compte assez rapidement qu'être assis ici en silence ne fait que me rendre plus nerveux, alors je me lève lentement, me dirigeant vers le hall principal."
scene bg palace1 with dissolve
play loop"sfx/birds.ogg" fadein 3.0
"Comme d'habitude, les salles sont vides."
"Les seules personnes vivant ici sont les frères et sœurs impériaux, Cato et Neferu."
"Le vieux loup est la seule autre personne que j'ai vue au cours des deux dernières semaines et demie que je suis ici."
"Cela me fait penser que je veux toujours voir la ville avant de partir ... si je pars."
"Je bloque cette pensée de mon cerveau, en essayant de ne pas penser à ce qui pourrait arriver si ces épreuves se passent mal pour nous."
"Au lieu de cela, j'essaie de laisser le soleil éclatant et l'air frais du matin calmer mes nerfs."
scene bg diningroom with dissolve
stop loop fadeout 3.0
"Finalement, je me dirige vers la salle à manger et quand je regarde à l'intérieur, je vois Alex assis sur l'un des lits."
show ale u shocked with dissolve
play music"music/dawn.ogg" fadein 3.0
"Ses oreilles se redressent quand il me voit, les yeux s'écarquillant de surprise."
al "\"Oh! Bonjour, [mc] ... Comment vas-tu?\""
"Il regarde mon visage, puis mon costume."
"Je me sens devenir rouge et j'aurais désespérément souhaité rester dans la chambre d'Amicus."
"Je suis capable d'intérioriser mon embarras pour le moment."
"Je connais assez bien Alex, après tout."
m "\"Où est {i} ton {/ i} costume?\""
"À ce stade, je sens que je suis la seule personne à se déguiser."
"Je m'assois sur le lit du milieu, ne voulant pas être directement en face du chat pour ne pas qu'il me fixe."
show ale tilt u with dis
al "\"Euh, devrais-je en porter un?\""
"Je hausse les épaules."
m "\"Je ne sais pas, ils m'ont en mis un.\""
show ale serious u with dis
al "\"Évidemment ... Et de la poudre aussi.\""
"Je regarde Alex."
show ale smile e u with dis
al "\"Je veux dire, tu as l'air beau, c'est très audacieux.\""
m "\"Alors pourquoi diable n'es-tu pas habillé en Meera? On fait la même danse, non?\""
show ale tilt e u with dis
al "\"Eh bien, oui, bien que Cassius m'ait ordonné de ne porter que mes sous-vêtements. En fait, je pense que je préférerais ta situation.\""
m "\"Bien sûr.\""
show ale flustered e u with dis
al "\"Sérieusement! Tu penses que je veux que tout Adastra voie mon torse nu?\""
"Alex se prend dans ses bras en frissonnant."
show ale serious w u with dis
al "\"C'est tellement embarrassant.\""
"Je soupire et m'assois sur le lit, remarquant seulement maintenant que Cassius est à l'écran, jouant une sorte d'instrument de cuivre qui ressemble vaguement à la forme d'un cor d'harmonie."
"Mais ça ne sonne pas du tout comme un cor d'harmonie, cependant."
"Le volume est faible, mais je peux entendre le son rauque et grésillant qu'il produit."
"Ce n'est pas agréable à mon oreille, mais l'idée de ce qu'est la musique et la danse semble très différente de la Terre."
m "\"Eh bien, je préfèrerais être à moitié nu. Et si c'est mon introduction à la lune, pourquoi suis-je tout couvert comme ça? Je suis presque sûr qu'ils préfèreraient mieux voir à quoi je ressemble {i} réellement {/ i}.\""
"Mais comme je le dis, je me demande si c'est peut-être POURQUOI Amicus m'avait tellement couvert."
show ale smile u with dis
al "\"La robe est  très belle je t'assure ... c'est le maquillage qui me surprend. Je suppose que c'est très ... Loup-esque de faire quelque chose comme ça.\""
"Je regarde Alex en fronçant les sourcils."
m "\"Loup-esque? Est-ce que c'est offensant?\""
show ale sad e u with dis
al "\"Uhhhh ... peut-être juste un peu, mais pas pour les loups, donc tu n'as pas à t'inquiéter. Les Hindos ne parlent plus à Adastra.\""
m "\"Oh mon dieu ...\""
"Je veux enfouir mon visage dans mes mains, mais je ne peux pas avec tout le maquillage."
"En plus de ça, tout commence à me démanger."
m "\"C'est tellement stupide.\""
show ale smile u with dis
"Alex rit."
al "\"Ça l'est. Les loups sont tellement obsédés par le spectacle et le drame, c'est pourquoi les Épreuves sont utilisées à la place des élections ... ou même simplement du bon jugement d'un conseil.\""
"Alex montre l'un des écrans."
show ale u with dis
al "\"C'est un jour férié Adastran en ce moment donc tout le monde peut regarder ça.\""
"Cassius ayant terminé sa petite chanson, il se lève et s'incline."
"Le long du bord droit de l'écran, cinq petites boîtes apparaissent, chacune contenant les visages de trois loups assis solennellement côte à côte."
al "\"Bien que, d'une certaine manière, les gens jouent un rôle dans le choix de leur empereur ici, avec leurs triumvirats élus qui prennent la décision, mais alors je ne comprends pas pourquoi la chanson et la danse devraient s'appliquer.\""
m "\"Alors pourquoi Cassius et Amicus feraient-ils campagne s'ils devaient simplement être choisis dans le cadre de ces épreuves?\""
show ale tilt e u with dis
al "\"Eh bieeeen ... si la décision n'est pas claire, alors pourquoi ne pas choisir le loup qui a le plus de popularité auprès de votre peuple? Cela augmente les chances de réélection.\""
"Amicus apparaît soudain à l'écran, assis, un projecteur sur lui alors qu'il commence à souffler dans le même instrument."
"Encore une fois, ce son rauque et blattant qui me ferait grincer des dents s'il s'agissait d'un instrument humain lors d'un concert humain."
"Je ne sais pas s'il est meilleur que Cassius ou pas."
al "\"Et il est bon d'être populaire de manière général de toute façon. Un peuple heureux est généralement une société plus pacifique et plus facile à contrôler.\""
m "\"Alors ... Amicus est désavantagé?\""
al "\"A moins qu'il ne surpasse clairement Cassius.\""
"Je soupire, regardant les joues du loup gonfler à chaque fois qu'il souffle dans sa petite corne, ses yeux se croisent presque avec l'effort."
m "\"Je suppose que vous élisez vos fonctionnaires?\""
show ale smile w u with dis
al "\"Oui.\""
m "\"Il en va de même pour la plupart de ...\""
"Je me surprends presque à dire le nom de ma planète."
"Il est de plus en plus difficile de cacher ce secret à Alex, d'autant plus que notre relation est devenue plus décontractée."
m "\"... nos tribus.\""
"Au moins, je pense que c'est ce qu'ils sont sur la planète simienne."
"Je dois juste espérer qu'Alex ne pose pas trop de questions."
"Mais il continue comme s'il n'avait pas remarqué ma pause, comme il le fait toujours."
al "\"Quoi qu'il en soit, malgré la concurrence, je te considère toujours comme un ami et j'espère que tu ressens la même chose. Peut-être pourrons-nous bientôt déjeuner dans les jardins, quel que soit le résultat?\""
m "\"Ouais, faisons ça.\""
show ale u with dis
al "\"Merveilleux.\""
"Nous restons assis en silence pendant encore une dizaine de minutes, regardant Amicus finir son cor."
"Puis Cassius reprend les projecteurs pour commencer à \"chanter\"."
"C'est en fait juste un hurlement, la tête de Cass penchée en arrière, le museau levé vers le plafond, ressemblant à un loup sur Terre alors qu'il hurle vers la lune."
"Je pense qu'il dit des mots, mais je ne peux pas vraiment comprendre, surtout avec le ton étrange et aigu qu'il a."
"Pendant ce temps, une petite jauge apparaît dans l'écran du bas, une aiguille va et vient avec le pas du hurlement."
al "\"Ils veulent que cet indicateur reste au milieu. Cela représente un meilleur contrôle de leur chanson.\""
"C'est court, seulement quelques minutes avant que ce soit au tour d'Amicus, faisant à peu près la même chose que Cassius sauf que son hurlement est plus profond, plus grave..."
"- beaucoup mieux, je pense."
"J'aime aussi penser que l'aiguille reste au milieu plus souvent qu'elle ne l'avait fait pour Cassius, mais je n'en suis pas sûr."
"Vers la fin de la chanson d'Amicus, la voix de Com crépite doucement au-dessus de nos têtes."
stop music fadeout 5.0
show ale tilt u with dis
com "\"Alex, [mc], la danse commence dans cinq minutes. Veuillez vous diriger vers les portes de la salle du trône.\""
"Mon cœur saute un battement alors que nous nous levons tous les deux, Alex menant le chemin vers le hall."
scene bg palace1 with dis
"Je me demande s'il est nerveux aussi."
"Même s'il a l'air calme, sa queue se cogne d'avant en arrière pendant que nous marchons."
"Je n'essaye pas de lui parler, j'ai l'impression que nous sommes tous les deux un peu préoccupés par nos propres pensées en ce moment."
"Nous arrivons aux grandes portes doubles et attendons côte à côte."
"Les pattes d'Alex sont bien repliées devant lui, alors je fais de même."
"J'essaye de respirer uniformément."
"Je n'ai jamais été bon devant de grandes foules et, même si techniquement, il n'y a que Cato là-dedans, je ne peux pas oublier le fait que des millions de personnes vont nous regarder."
com "\"L'épreuve de danse commence dans cinq, quatre, trois, deux ...\""
play sound"sfx/dooropen.ogg"
scene bg throneroomdark with dissolve
"Les portes s'ouvrent et je me retrouve à regarder dans une salle du trône sombre, les fenêtres profondément teintées de sorte que seul un vague soupçon de soleil passe à travers."
"Je vois immédiatement Amicus juste devant moi, baigné d'un projecteur brillant."
"On peut dire la même chose de Cassius, à une dizaine de mètres à sa droite."
"Cato est assis sur le trône, comme dans mon rêve."
"J'ai aussi remarqué Virginia et Neferu assis l'un à côté de l'autre sur l'un des bancs."
"Cela seul me rend encore plus nerveux, mais ensuite une voix se fait entendre venant du plafond."
"Ce n'était pas celle de Com, mais quelqu'un d'autre, qui a l'air vieux et frêle."
"Loup""\"Présentation de l'animal de compagnie Alexios de la lune Omorfa, et l'animal de compagnie [mc], de la planète Simia.\""
"Amicus et Cassius tendent une patte, et Alex commence à marcher sur ses orteils, l'air léger et sophistiqué."
"Je fais rapidement de même, essayant d'imiter en quelque sorte sa démarche."
"Je n'avais jamais pratiqué mon entrée avec Amicus."
"Je commence à me demander si je suis encore plus mal préparé que je ne le pensais."
"Pas le temps de penser à ça maintenant."
"Je fais de mon mieux avec ma stupide marche cabré avant de m'arrêter devant Amicus, tendant une main pour se reposer dans sa grosse patte."
show ami eyes with dis
"Il me sourit de manière rassurante, et pour une raison quelconque, sa présence me rend un peu moins nerveux que je ne l'avais été en attendant seul le début de l'épreuve."
"Nous restons là tranquillement pendant un moment, mais ensuite cette vieille voix recommence, mais maintenant elle pousse un hurlement; haut, vacillant et faible."
"\"{i} Explorant ... adver ... viro ... {/ i}\""
"Il commence à réciter l'histoire dans le même hurlement, mais c'est difficile à entendre, et maintenant qu'il y a des mots-"
"Attends... je ne peux pas comprendre. Il parle..."
play loop"music/emorph.ogg" fadein 20.0
"Oh putain."
"Le Lingua ne traduit pas la chanson."
"Immédiatement, je commence à paniquer en voyant Amicus lever la patte."
show ami embarrassed with dis
"J'ai probablement un air d'horreur sur mon visage, parce que son sourire rassurant s'est transformé en un froncement de sourcils."
"Maladroitement, je lève la main pour toucher la patte du loup, essayant de rester calme."
"Je peux le faire."
"Bien sûr, j'ai attaché beaucoup de mouvements aux mots de la chanson, mais je me souviens de l'ordre des poses ... je pense."
"Pourtant, la bévue inattendue m'a énervé et je suis trébuchant, mes mouvements hésitants et définitivement peu élégants."
"Je suis tellement épuisé que je n'ai pas vraiment le temps de m'attarder sur le fait qu'Alex et Cassius font la danse en même temps."
"Sommes-nous en compétition pour l'attention de Cato et des triumvirats qui nous regardent?"
"J'essaye de rester concentré sur Amicus, en observant ses mouvements, en espérant que je pourrais me souvenir de suffisamment de ses signaux pour passer tous les mouvements correctement."
"Mon trouble doit également affecter Amicus, son front plissé de confusion, ses mouvements devenant également plus lents, plus hésitants."
"Merde."
"Je pense que je sens la sueur couler sur mon visage, transformant probablement mon maquillage rayé en un désordre strié."
"Plusieurs fois, je suis surpris en train de regarder Amicus, ne sachant pas quoi faire jusqu'à ce que je regarde Alex pour voir ce qu'il fait."
stop loop fadeout 10.0
"Le chat semble totalement dans son élément, étirant et allongeant son corps luxueusement en tandem avec Cassius."
"Le loup n'est pas mal lui-même, prenant clairement les devants dans la danse alors qu'il plonge et se balance avec le corps d'Alex."
"Pendant ce temps, je tâtonne avec Amicus, regardant la poudre sur mes bras en sueur s'étaler sur sa fourrure, laissant de longues taches noires sur sa poitrine et ses bras."
"Finalement, nous arrivons à la mort de Meera et au moins je sais quand cela est censé se produire parce que je vois Amicus tendre la main de façon spectaculaire pour moi."
"C'est le seul moment de toute la danse où je me sens confiant dans ce que je fais, et je mets tout dans mon évanouissement ... mais Alex aussi."
scene alexandcassius with slow_dissolve
play music"music/reveal2.ogg"
"Amicus est déjà à côté de moi pour me rattraper avant que je puisse commencer à tomber, mais Alex s'évanouit alors que Cassius est encore à quelques mètres de lui, mais l'autre loup glisse doucement à ses côtés pour l'attraper."
"Alex est allongé là dans les bras de Cassius, évasé de façon dramatique, semblant en quelque sorte serein et angoissé en même temps."
"Les projecteurs font presque briller la paire, et même moi j'ai l'impression qu'il y a une alchimie entre eux."
"Il y avait eu un petit mais certain espoir de mon côté qu'Alex pourrait nous aider ici, peut-être saboter la danse en notre faveur avec une chute ou a trébuchement, mais il semble qu'il a tout mis dans la performance."
"Cassius, malgré sa réputation d'être faible, a l'air fort et confiant, supportant facilement le poids d'Alex alors que le chat plonge plus loin vers le sol."
"En même temps, le hurlement du loup atteint un nouveau niveau, le point culminant de l'histoire."
"Et c'est là qu'Alex tourne la tête vers Cassius pour a baiser profond et passionné."
scene alexandcassiuskiss with slow_dissolve
"Même si Meera est censée être partie à ce stade, Alex tend la main pour caresser le visage de Cassius, l'attirant plus profondément."
"Pendant ce temps, leurs corps se pressent étroitement l'un contre l'autre, Cassius frottant très clairement ses hanches contre celles du chat, la patte qui ne soutient pas Alex monte sur sa cuisse-"
"... Avant de plonger sous les sous-vêtements d'Alex, en les poussant jusqu'à ce que la majeure partie de la cuisse du chat soit visible."
"Et ils... se tordent l'un contre l'autre comme ça, comme pris dans les affres de la passion, les mouvements de leurs museaux me disant qu'il se passe beaucoup de choses au-delà de ces lèvres."
"L'ensemble de l'acte m'étourdit, me faisant presque oublier le désastre que notre propre danse avait été."
"Cassius se retourne, portant Alex avec lui alors qu'il fait face à l'assemblée, sans jamais rompre le baiser, en fait leurs tâtonnements et frottements deviennent encore plus intenses."
"Il donne à tout le monde une belle vue de ce qui se passe."
"Si l'idée même de la danse est de capter l'attention et de rendre l'histoire et les sentiments crédibles -"
"... eh bien, je les crois."
"En fait, je crois qu'il se passe beaucoup plus de choses entre les deux que je ne le pensais au départ."
"Cela pourrait expliquer pourquoi Alex ne voudrait pas nuire aux chances de Cassius d'être empereur."
"Peut-être que mes espoirs qu'Alex nous aiderait étaient complètement naïfs."
"Et c'est à ce moment-là que je suis soudainement revenu à la réalité alors que j'entends Amicus grogner au-dessus de moi."
scene bg throneroomdark
show ami embarrassed
with dissolve
"J'étais tellement épris du baiser de Cassius et d'Alex que j'avais oublié le nôtre."
"Voir un aperçu de ce que je pourrais avoir à faire avec Amicus..."
"Je rougis, me raidissant, me préparant alors que le loup commence à se pencher vers moi, ses lèvres légèrement plissées."
"Je prépare mes propres lèvres, mais soudain, Amicus tourne légèrement la tête sur le côté, déposant le baiser sur ma joue à la place."
"C'est doux et éphémère, et avant que je le sache, Amicus s'est reculé avant de m'abaisser doucement vers le marbre froid en dessous."
hide ami with dissolve
stop music fadeout 10.0
"Je reconnais le mot Adastra dans le hurlement avant que tout ne se calme."
"J'entends Alex se lever à quelques mètres de là, alors je fais de même, Amicus se dépêchant rapidement pour m'aider dans ma robe."
"Ce n'est qu'alors que je vois les différents drones flotter au-dessus de nous, les lentilles attachées me faisant réaliser que ce sont des caméras."
"J'ai rapidement baissé la tête, ne voulant pas que les gens voient le maquillage taché et offensant sur mon visage."
"Amicus me tient près de lui, ne disant rien, heureusement."
"Cassius continue de regarder droit devant et je peux voir Alex nous regarder, l'air confus."
"Puis la voix de Com retentit-"
com "\"Les triumvirates ont pris leurs décisions.\""
com "\"Lupas: Cassius.\""
com "\"Ad Rotae: Cassius.\""
com "\"Lux: Cassius.\""
com "\"Gebii: Cassius.\""
com "\"Tricelli: Cassius.\""
com "\"Adastra?\""
"Les drones de la caméra pivotent pour se concentrer sur Cato."
"Il bouge sur son trône avant de grogner sa réponse."
ca "\"Cassius.\""
com "\"L'épreuve a été décidé. Cassius est le vainqueur.\""
"Il y a un moment de silence absolu, puis les fenêtres s'éclaircissent et les drones caméra dérivent paresseusement dans un compartiment du plafond."
scene bg throneroom with dissolve
"Je suis resté là, regardant les autres."
"Cato descend les marches du trône, en direction de Cassius."
"Pendant ce temps, Virginia chuchote à Neferu derrière un éventail qu'elle agite avec désinvolture."
"Cassius caresse la tête d'Alex, lui murmurant dans sa barbe."
show ami serious at left with dissolve
"Finalement, Amicus se tient maladroitement à mes côtés, ne me regardant même pas, ses pattes derrière son dos et ses yeux sur Cato."
"Je me rends soudain compte à quel point j'ai l'air stupide."
m "\"Je peux aller me changer?\""
"Je marmonne à Amicus, gardant ma voix basse comme tout le monde, comme si nous étions dans une bibliothèque, ou quelque chose comme ça."
show ami embarrassed with dis
a "\" Euh, bien sûr. Est-ce que tu veux-\""
"Je ne le laisse pas finir."
"Je marche aussi vite que possible vers les doubles portes, sachant que tout le monde a les yeux rivés sur mon dos alors que je m'arrête pour toucher le panneau noir."
play sound"sfx/dooropen.ogg"
scene bg palace1 with dissolve
play loop"sfx/birds.ogg" fadein 3.0
"Une fois que je suis dans le hall principal, je suis capable de respirer un peu plus facilement, commençant à sentir la colère monter à travers l'humiliation absolue."
"Je ne sais pas exactement contre quoi je suis en colère."
"Pas Amicus, même s'il aurait peut-être dû avoir une idée que les hurlements ne se traduisent pas."
"Pas Cato ou les triumvirats; ils avaient pris la bonne décision."
"J'avais été un désastre complet là-bas."
"Je suppose que je suis juste en colère contre tout ce système, que la responsabilité de rentrer à la maison repose sur moi autant que sur le gars qui m'a amené ici en premier lieu."
"Ce n'est pas juste."
"Donc je suppose que je suis en colère contre Amicus d'une certaine manière, mais la colère est beaucoup plus large que ça, je suis en colère contre toute la situation."
scene bg amicusroom with dissolve
stop loop fadeout 3.0
"Je vais directement dans la salle de bain, essayant grossièrement d'arracher la stupide robe."
scene bg bathroom with dissolve
"Elle est serré autour de mon cou et je passe la minute suivante à faire une danse maladroite, essayant de trouver les boutons dans le dos pour que je puisse la desserrer."
"Finalement, je l'arrache pour enfin me libérer, me sentant un peu coupable après avoir vu le beau tissu froissé sur le sol."
"Je me tiens là, respirant profondément, en sueur."
"Je me regarde dans le miroir et je suis un peu surpris de voir le maquillage encore presque intact sur mon visage."
"Ce qui me rappelle; je suis aussi énervé que la première fois que je sois présenté au public, ce soit dans un costume et un maquillage racistes."
play loop"sfx/showerloud.ogg" fadein 3.0
"Je rentre dans la douche, laissant l'eau chaude couler sur mon visage, me sentant un peu mieux maintenant que je suis seul avec mes pensées ... et hors de la robe moulante."
"Pourtant, mon humeur est un peu sombre."
"Je suppose que maintenant je peux réellement commencer à penser que je pourrais vivre ici pour toujours."
"Bien que mon esprit rejette l'idée au départ, je suppose que ce n'est pas le pire sort."
"Je vais au moins vivre dans un palais avec Amicus, et je sais qu'il prendra soin de moi."
"Au moins je pense qu'il le fera."
"Peut-être que tout ce truc d'animal de compagnie est temporaire, et s'il perd les épreuves, il me jettera avec les ordures, peut-être qu'il me tuera comme il l'avait mentionné une fois dans le vaisseau."
"Je chasse ces sombres pensées, je sais qu'il ne le fera pas."
"Il ne ferait pas ça, mais je ne peux pas me promettre que je serais capable de rester ami avec lui si les choses tournaient vraiment mal."
"Il m'avait dit que ce serait facile tant de fois."
stop loop fadeout 3.0
"Même si le Lingua n'avait pas foiré, je doute que nous aurions quand même gagné."
"Après une bonne demi-heure, je sors enfin de la douche."
play loop"sfx/showerfan.ogg" fadein 3.0
"Je me tiens devant les ventilateurs pendant un moment, appréciant la façon dont ils fouettent mes cheveux avant de prendre des sous-vêtements et de les attacher."
stop loop fadeout 3.0
"Je fais ça assez vite maintenant, je n'ai même pas à y penser."
"Enfin, j'ouvre la porte."
play sound"sfx/dooropen.ogg"
scene bg amicusroom with dissolve
"L'air frais qui se précipite est rafraîchissant après une douche aussi chaude, mais je tombe immédiatement sur Amicus s'éloignant de la porte, il était probablement en train de faire les cent pas."
"Il se retourne immédiatement au son de la porte, les yeux écarquillés."
play music"music/dawn.ogg" fadein 10.0
show ami surprised with dis
a "\"Hé! [mc], comment vas-tu?\""
m "\"Génial.\""
"Je me dirige vers la commode, ouvrant celle qui est pleine de robes d'enfants."
show ami embarrassed with dis
a "\"Vraiment?\""
"\"Oui.\""
"J'entends Amicus souffler derrière moi."
show ami disappointed with dis
a "\" S'il te plaît, je ne veux pas avoir affaire à ta mauvaise humeur maintenant. Je veux juste parler.\""
"Le fait qu'Amicus me dise d'arrêter de bouder ne fait que renforcer ma mauvaise humeur."
m "\"Tu sais, j'aurais adoré parler il y a une semaine de cette stupide épreuve. Imagine à quel point cela se serait mieux passé si j'avais MÉMORISÉ la danse plutôt que de simplement suivre tes signaux à toi et à la chanson.\""
"Je tire une robe de l'armoire."
m "\"Qui, au fait, n'est pas une chanson. Vous vous moquez toujours des Terriens et de nos manières primitives, mais au moins, nous avons des variétés de musique. Oh, et nous pouvons aussi chanter, pas ces hurlements effrayants qui donnent l'impression que vous êtes en train de mourir.\""
"Amicus fronce les sourciels, les oreilles à plat."
show ami embarrassed with dis
a "\"Tu es en colère.\""
m "\"Nooooon, qu'est-ce qui te fais penser ça?\""
show ami angry with dis
a "\" Arrête ça, [mc]. Je suis tout aussi contrarié et déçu que tu l'es... Ce sont les caméras qui t'ont dérangés ? Ou c'est Cato qui t'as rendu nerveux? Qu'est ce qu'il s'est passé?\""
"Je suis calme pendant un moment alors que je commence à nouer ma robe, puis soudainement Amicus tend la patte, saisit ma main droite et la rapproche de lui."
m "\"Quoi-\""
show ami surprised with dis
a "\"Qu'est-il arrivé à ta patte!?\""
"Je lève les yeux et vois le loup regarder la paume de ma main avec de grands yeux avant de la tourner dans un sens ou dans l'autre."
m "\"Quoi?\""
a "\"Ta peau c'est ... elle est frippée ! Tu fais une réaction à la poudre?\""
"Je le regarde, confus avant de retirer ma main pour regarder mes doigts plissés."
m "\"Non, j'étais juste trop longtemps sous la douche. Ma peau fait ça quand je suis mouillé pendant longtemps.\""
a "\"Je n'ai jamais remarqué cela auparavant.\""
m "\"Tu prends des douches courtes.\""
show ami embarrassed with dis
"Le loup fronce les sourcils, puis relève ma main pour regarder mes doigts avec fascination, alors même que j'essaye de la tirer en arrière."
"À ce moment-là, je sens que mon humeur est sur le point de prendre un virage dans l'une des deux directions suivantes: soit exploser sur Amicus de frustration et de colère à cause de tout ... soit simplement rire."
"Et je me surprends à prendre ce dernier, en gloussant au début avant de laisser échapper de grands éclats de rire."
"Amicus me lance un regard étrange, lâchant finalement ma main."
a "\"Tu es sûr que tu vas bien? Tu m'inquiètes.\""
"Je soupire en finissant de nouer ma robe de chambre avant de retomber sur le lit, les mains au-dessus de ma tête alors que je laisse l'air frais et agréable dériver du plafond pour recouvrir mon corps."
"Je sais que je vais avoir froid dans quelques minutes, mais pour l'instant ça fait du bien."
m "\"Tu te souviens comment tu as dit que le Lingua avait du mal à traduire certaines choses?\""
a "\"Oui, je-\""
show ami surprised with dis
"J'entends le loup faire une pause alors qu'il comprend ce qui ne va pas."
m "\"Je n'entendais rien d'autre que des lamentations latines dans ces hurlements. Je n'avais aucune idée de ce que je faisais.\""
show ami frustrated with dis
a "\"Oh dieux ...\""
"Il y a un gros bruit sourd et je sens le matelas s'incliner un peu sur le côté alors qu'Amicus s'assoit à côté de moi."
m "\"Ouais ...\""
a "\"[mc], je suis vraiment désolé. Je n'ai même pas envisagé cette possibilité!\""
m "\"C'est pas grave...Je ne pense qu'aucun de nous deux ne s'en serait douté.\""
a "\"Je veux dire, j'ai écouté la musique des chats auparavant, et je n'ai jamais eu de problèmes avec la traduction des paroles...\""
"Je hausse les épaules."
m "\"Je ne sais pas, le Lingua n'essaye t-il pas aussi de comprendre l'intention ? Peut-être que je suis censé entendre le \"vrai\" Langage quand vous chantez. Ça s'est aussi produit quand tu faisais ta chanson, même si je ne m'en étais pas rendu compte à ce moment-là.\""
show ami embarrassed with dis
a "\"Oh...tu m'as entendu chanté?\""
"Je peux entendre l'embarras dans la voix d'Amicus."
m "\"Ouais...Ça sonnait bien honnêtement. J'ai été un con quand je me suis plains à l'instant.\""
show ami crossed with dis
a "\"Je sais.\""
m "\"Mais quand même, je suis fatigué que tu regardes de haut la culture humaine.\""
show ami eyes with dis
a "\"Je sais.\""
m "\"Et je {i} savais {/ i} que le maquillage était offensant au fait. J'avais l'air d'un idiot devant tout Adastra.\""
show ami surprised with dis
a "\"Tu avais l'air bien!\""
"Je tourne la tête vers le loup."
m "\"Oh vraiment, tâtonner comme un idiot sans aucune idée de ce je faisais ça a l'air bien?\""
show ami embarrassed with dis
"Amicus reste silencieux cette fois."
"Je regarde le plafond."
m "\"J'imagine qu'au moins je suis bon dans mon rôle de stupide singe primitif, hein?\""
"Amicus soupire juste en se levant."
"Je le regarde se diriger lentement vers le canapé pour s'asseoir."
show ami crossed serious with dis
a "\"Je dois dire que même si tu es une personne très gentille et intelligente, tu es très frustrant lorsque tu es de mauvaise humeur.\""
m "\"Frustrant?\""
a "\"Tu deviens tellement ... sombre et autodestructeur. Tu me rappelles parfois Cassius.\""
"Je fais la grimace."
m "\"Depuis quand est-il autodestructeur? Il me semble assez sûr de lui.\""
a "\"Tu ne connais pas le vrai Cass. Il se déteste beaucoup.\""
m "\"Aussi, ne me compare pas à ton frère. Je ne veux vraiment pas penser à lui pour le moment.\""
show ami crossed with dis
a "\"Je dis juste que je te préfère dans un esprit plus léger. Cela te convient davantage.\""
m "\"Je vais y travailler.\""
"Un long silence passe et avec la façon dont Amicus se déplace, je peux dire qu'il veut me demander quelque chose."
m "\"Qu'est-ce qu'il y a?\""
show ami eyes with dis
a "\"Eh bien, euh, je suppose que cette petite fête est hors de question, maintenant?\""
m "\"Le dîner?\""
show ami embarrassed with dis
a "\"Euh ...\""
"Je m'assois soudainement, lui lançant un regard incrédule."
m "\"Sérieusement!?\""
show ami surprised with dis
a "\"Whoa, j'étais juste en train de plaisan-\""
m "\"Nous venons de perdre l'épreuve! Tu es à une épreuve de perdre le titre d'empereur et tu y penses sérieusement -\""
show ami frustrated with dis
a "\"Je m'amusais juste un peu.\""
m "\"Non, tu voulais une branlette.\""
show ami angry with dis
a "\"Ce n'est pas comme si J'AI BESOIN de toi pour le faire. Je peux faire le travail moi-même.\""
m "\"Alors fais-le.\""
a "\"Je le ferai.\""
"Amicus est assis là, sans croiser mon regard."
"Je soupire, me souvenant de ce que le loup avait dit sur l'amélioration de mon humeur."
"Je critique souvent Amicus pour ses crises de colère, lui rappelant que cela ne nous aidera pas de bouder."
"C'est un peu hypocrite que je ne me tienne pas aux mêmes normes."
m "\"Désolé, j'ai juste beaucoup de choses en tête.\""
show ami serious with dis
a "\"Ecoute, je sais que cela s'est passé très différemment de ce que nous avions prévu, mais je gagnerai certainement la prochaine épreuve. J'ai déjà débattu avec Cassius plusieurs fois.\""
m "\"Je dois faire quelque chose?\""
a "\" A part regarder? Non.\""
m "\"Quand est-ce que se déroulera l'épreuve?\""
a "\"Dans deux semaines.\""
m "\"Tu ferais mieux de gagner.\""
a "\"Je gagnerai.\""
"Je soupire à nouveau, réalisant que le nœud que j'ai eu dans l'estomac ces dernières semaines va rester là encore un moment."
m "\"Et je pourrais toujours ...\""
"Je fais un mouvement de va et vien en l'air."
m "\"... plus tard. Je ne suis tout simplement pas dans le bon état d'esprit pour le moment.\""
show ami with dis
a "\"Je comprends. Il était trop tôt pour ça... cependant, euh, peut-être que nous pourrions faire autre chose qui nous ferait nous sentir mieux tous les deux?\""
m "\"Quelque chose d'autre?\""
show ami embarrassed with dis
a "\"Oui, genre, je pourrais juste ... t'étreindre?\""
"La voix d'Amicus devient inhabituellement élevée au dernier mot."
m "\"M'étreindre.\""
"Je répète ses paroles."
m "\"Pourquoi tu voudrais faire ça?\""
show ami disappointed blush with dis
a "\"Eh bien, la camaraderie fait partie des devoirs de l'animal de compagnie, et s'étreindre, ou s'embrasser est souvent la façon dont elle s'exprime. Cela pourrait aussi te réconforter compte tenu du stress des dernières heures.\""
show ami embarrassed with dis
"Encore une fois, ce regard plein d'espoir et encore une fois je me sens vraiment mal pour lui."
"A quel point faut-il être seul pour vouloir juste câliner quelqu'un?"
"Mais en même temps, j'en ai envie."
"Je ne veux peut-être pas l'admettre, mais j'ai aussi été seul ces trois dernières semaines, émotionnellement et physiquement."
"De plus, j'ai vraiment aimé nos petits câlins, donc un câlin plus longs ..."
"Essayant de ne pas avoir l'air trop impatient moi-même, je soupire et me lève."
show ami surprised with dis
"Les oreilles d'Amicus se réveillent immédiatement de bonne surprise."
"Il se penche en arrière, les jambes jointes, attendant que je m'approche de lui."
show ami eyes with dis
a "\"Est-ce que tu-\""
show ami surprised with dis
"Je m'assois sur ses genoux, un peu maladroitement au début alors que je vacille, puis je m'arrête j'opte finalement pour me tourner sur le côté, les genoux relevés alors que j'appuie mon épaule contre sa poitrine."
"Amicus fait une pause, puis enroule ses bras autour de moi."
show ami eyes with dis
"Malgré le départ maladroit, je suis étonné de la façon dont je m'adapte à la courbe de son corps."
"Ses grands bras poilus m'enveloppent, et je sens les muscles se resserrer brièvement avant de me détendre."
"Son ventre moelleux coussine contre mon flanc, ce qui donne l'impression que je suis appuyé contre un grand matelat d'eau velu mais ferme."
"Sa poitrine est large et épaisse, soutenant confortablement ma tête alors qu'il écarte un peu ses fesses pour nous aider à mieux nous incliner."
"Puis il met ma tête sous son menton, et juste comme ça, je suis entouré de sa chaleur, le froid qui avait commencé à mordre ma peau nue se dissipant immédiatement."
"Je ressens un peu de frisson dans ma poitrine à la sensation d'avoir ce loup, si grand et puissant, me serrer dans ses bras et me câliner si doucement."
"Ce câlin est juste si ... sympa."
"Amicus me tient juste en silence pendant un moment, et je sens ses pattes bouger un peu, comme s'il pétrissait à travers la robe la peau de mon dos."
"Enfin, sa voix grave gronde dans sa poitrine et contre mon oreille."
show ami crossed with dis
a "\"Est-ce que ça va?\""
m "\"Ouais c'est ... très bien.\""
"Je rougis, embarrassé de voir à quel point j'apprécie ça."
"A l'origine, je voulais juste qu'il se sente mieux, mais il avait raison de me faire me sentir mieux."
"Amicus frotte son menton contre le haut de ma tête, et je l'entends inspirer."
a "\"Je suppose que ce n'est pas une chose normale à faire sur Terre?\""
m "\"Eh bien ... ça l'est si tu sors avec quelqu'un. Ce n'est pas une chose que l'on fait habituellement entre amis, cependant.\""
a "\"Ah.\""
"Amicus me patte un peu plus, faisant ces petits mouvements comme s'il essayait de me sentir le plus possible sans être évident à ce sujet."
a "\"Qu'est-ce que c'est \"sortir ensemble\" sur ta planète?\""
"Je hausse les épaules, même si c'est difficile à faire contre l'étreinte serrée du loup."
m "\"Eh bien ... tu proposes à quelqu'un que tu aimes un rendez-vous. En fait ça signifie simplement que tu aimes la personne et que tu veux en savoir plus sur elle et sortir avec t'aide à y arriver.\""
a "\"Ah, ça a l'air assez décontracté. Alors, comment peut-on initier ce ...sortir ensemble?\""
m "\"Je ne sais pas, demande-leur simplement ... donne-leur des fleurs si tu es vieux-jeu, mais c'est assez décontracté, honnêtement.\""
a "\"Mmmh.\""
m "\"Pourquoi es-tu si curieux?\""
"C'est au tour d'Amicus de hausser les épaules."
a "\"Je veux toujours faire attention à tes limites. C'est plus facile si je comprends mieux ta culture.\""
stop music fadeout 5.0
"Je m'appuie contre le loup, réalisant que même si je me suis complètement ridiculisé une demi-heure plus tôt, je me sens bien."
"J'espère en quelque sorte que ce n'est pas la dernière fois que nous faisons quelque chose comme ça."
"Connaissant Amicus, ce ne sera probablement pas le cas."

scene bg garden1 with fade
play loop"sfx/birds.ogg" fadein 3.0
"C'est quelques jours plus tard que je suis enfin capable de passer du temps avec Alex comme nous l'avions prévu."
"Cassius avait intensifié sa campagne au cours des derniers jours à mesure que ses chances de devenir empereur augmentaient."
"Amicus aussi après que ses chances aient diminuées."
"La différence étant qu'Alex se retrouvait souvent en voyage de campagne avec le loup blanc alors qu'Amicus me laissait toujours derrière."
"Je pense qu'Amicus a compris que je n'aime pas être devant autant de monde après tout l'incident de l'épreuve de danse."
"Pourtant, il me promet que QUAND il remportera la prochaine épreuve, nous irons en ville pour fêter ça."
"Pour l'instant, je suis heureux de rester dans les jardins avec Alex, appréciant un repas de midi tranquille pendant que nous parlons et sirotons notre thé."
show ale at right with dissolve
al "\"Honnêtement, ils devraient nous faire refaire la danse si ton Lingua ne traduisait pas.\""
m "\"Le tiens fonctionnait?\""
show ale tilt with dis
al "\"Eh bien, non, mais je savais que ce ne serait pas le cas. Les loups n'ont jamais l'intention de traduire leurs paroles sur le Lingua parce que cela ruine le hurlement, et ils considèrent que c'est le but du chant.\""
m "\"Hmm.\""
al "\"Je pourrais comprendre qu'Amicus oublie cela cependant. La plupart des loups ne voient jamais une autre espèce fraternelle en personne de toute leur vie.\""
m "\"Eh bien, c'est fini maintenant. Passons au débat qu'ils vont faire ensuite.\""
show ale smile with dis
al "\"Oh oui. Cassius s'est entraîné avec le meilleur rhéteur sur la lune; Marcus Manius.\""
"Je remarque qu'il met un peu l'accent sur le nom et je le regarde."
"Alex sirote délicatement son thé, regardant la fontaine paresseusement."
show ale with dis
al "\"Il a offert à Cassius de nombreux conseils pour convaincre les triumvirats. Des conseils très utiles. Amicus fait-il quelque chose de similaire?\""
"Je me rends compte alors qu'Alex m'offre des informations sur ce que Cassius fait pour se préparer à l'épreuve."
"... Enfin je pense que c'est ce qu'il fait."
"Que ce soit le cas ou non, j'essaie de retenir le nom du rhéteur, sachant que je devrais le répeter à Amicus plus tard."
m "\"Je ne suis pas vraiment sûr. Il ne m'a pas beaucoup parlé de ce qu'il faisait, mais j'espère que c'est quelque chose de similaire.\""
al "\"Eh bien, je lui recommande d'étudier les triumvirats et leurs villes, ne serait-ce que pour trouver le meilleur moyen de les convaincre lors du deuxième procès.\""
"Ouais, il m'offrait définitivement des informations."
"Le truc, c'est qu'après avoir vu la façon dont lui et Cassius ont interagi ... je me demande si je peux lui faire totalement confiance."
m "\"Tu sais, Cassius a dit quelque chose il y a une semaine quand je le servais. Tu sais qu'il a l'intention de se débarrasser des triumvirats?\""
show ale shocked e with dis
"Les yeux d'Alex s'écarquillent pendant a moment."
show ale smile e with dis
al "\"Oh vraiment? Hmm, je me demande pourquoi?\""
m "\"Quelque chose à propos du fait qu'il est plus facile de gouverner directement que par l'intermédiaire des élus?\""
show ale smile w with dis
al "\"Eh bien, c'est une réflexion radicale, n'est-ce pas?\""
m "\"C'est ce que Virginia a dit.\""
show ale with dis
al "\" Eh bien, elle a toujours été plutôt raisonnable. Honnêtement-\""
"Alex se penche, baissant la voix."
show ale tilt with dis
al "\"Je préférerais qu'elle devienne l'impératrice, mais malheureusement les loups ne permettent pas aux femmes d'occuper des postes de grande autorité, donc ses chances sur le trône sont nulles.\""
show ale shocked with dis
"Les yeux d'Alex s'écarquillent soudainement alors qu'il regarde par-dessus mon épaule."
"Je lève les sourcils, puis je regarde en arrière pour voir Neferu se diriger vers nous."
show ale embarrassed e with dis
"Je me retourne pour voir Alex regarder vers le sol, sa queue se fouettant avant de la tenir sur ses genoux."
show nef at left with dis
"Le chacal s'arrête pour se tenir devant nous."
"Sans un mot, il prend délicatement une des pattes d'Alex et s'incline pour l'embrasser."
"Alex pose son autre patte à sa bouche, rougissant furieusement."
"Pendant ce temps, Neferu me fait un signe de la tête."
n "\"Bonjour Alex et [mc]. Comment est votre déjeuner?\""
"Alex a toujours sa patte contre sa bouche, alors je réponds à sa place."
m "\" C'est bon. Comment tu va?\""
show nef smile a with dis
n "\"Splendide!\""
"Je remarque alors qu'il porte une bouteille dans sa patte, le verre brillant au soleil à chacun de ses mouvements."
n "\"Je faisais juste une promenade dans les jardins ce matin quand je suis tombé sur une araignée incroyablement grosse qui a grimpé sur le sol à mes pattes.\""
"Neferu passe sa patte devant lui, comme pour montrer où l'araignée a couru."
show nef sad with dis
n "\"Je ne peux pas m'empêcher de me demander si je suis en danger ici.\""
"Alex prend enfin la parole, grinçant avec la première syllabe."
al "\"N - non, elles sont plutôt inoffensives. Leur venin est sans danger.\""
show nef sidesmile f with dissolve
n "\"Ah, c'est un soulagement à entendre, Alex. Sur ma planète natale, je devais souvent secouer mes pagnes avant de les porter en cas de scorpions.\""
show ale smile e with dis
al "\"Oh vraiment? C'est terrifiant.\""
show nef smile eyes with dis
n "\"Ça l'est en effet, mais c'est à laquelle on s'habitue.\""
"Alex et Neferu se sourient pendant a moment, et je fronce les sourcils au chat, me demandant ce qu'il fait."
show nef smile a with dis
n "\"Oh oui! Je suis venu te donner ça.\""
"Neferu se penche et tend la bouteille en verre et maintenant je vois qu'elle est remplie d'un liquide couleur miel qui glisse paresseusement dans la bouteille."
show nef with dis
n "\"L'huile de graine de Baa que j'ai promis. Beaucoup mieux pour la fourrure que les huiles Adastranes qu'ils ont pour nous.\""
"Alex tend la main et prend la bouteille, rougissant à nouveau."
show ale with dis
al "\"Me-merci Neferu. Je vais l'utiliser demain à la première heure.\""
n "\"Et je te reverrai demain pour m'assurer que tu le feras!\""
show ale embarrassed with dis
"Le chacal fait un clin d'oeil et je crois entendre Alex faire un bruit étranglé dans sa gorge."
n "\"En attendant, souhaites-tu te promener avec moi?\""
show ale shocked with dis
al "\"Euh, oh, je-\""
"Neferu tend à nouveau ae patte."
show ale embarrassed with dis
"Alex tousse maladroitement avant de tendre la main pour le prendre."
show nef smile eyes a with dis
n "\"Merveilleux, tu es toujours de si bonne compagnie. Souhaites-tu également nous rejoindre, [mc]?\""
"Je repense à ce qui s'était passé dans les bains."
m "\"Non merci.\""
n "\"Dans ce cas, je te verrai dans le palais.\""
show ale smile e with dis
al "\"Ouais, à bientôt, [mc]!\""
hide nef
hide ale
with dissolve
"Neferu offre son bras au chat, et ils partent dans les jardins, disparaissant autour des nombreux buissons bordant les sentiers."
"Je les regarde, un peu confus, les intentions du chacal ne sont toujours pas claires pour moi."
"Je me rappelle aussi que je dois demander à Alex pourquoi diable il a révelé à Neferu le secret de mon intelligence."
"Le seul problème, c'est que je ne sais pas comment faire ça sans paraître suspect."
"Techniquement, il n'y a pas de raison pour laquelle c'est censé être un secret, et j'ai l'impression que le fait de le soulever ne fera que donner au chat une raison de creuser plus profondément."
"Alors que je réfléchis à tout ça, je remarque une forme dans les buissons, près de ceux derrière lesquels Alex et Neferu ont disparu."
"Ensuite, je vois un flash de rouge et peut-être un coude sortir."
m "\"Qu'est-ce que ... Amicus?\""
"Je crie dans sa direction et je vois le loup sauter, sortant soudain de derrière sa couverture."
show ami embarrassed with dissolve
a "\"Ou - oui, je regardais simplement les roses.\""
"Le loup marche vers moi, ses pattes derrière le dos."
"Je lève un sourcil vers lui."
m "\"Tu nous espionnais? Tu essayais d'éviter Neferu, ou un truc comme ça?\""
"Amicus m'ignore cette fois."
show ami eyes with dis
a "\"Comment s'est passée ta journée, [mc]?\""
m "\"Umm ... Okaaay.\""
"J'essaye de regarder du côté du loup ce qu'il cache derrière son dos, mais il se retourne en conséquence pour le garder obscurci."
m "\"Qu'est ce que tu fais?\""
a "\"Eh bieeeeen...\""
"Amicus prend une profonde inspiration et je commence à devenir nerveux."
"Puis il pli un genou à terre."
play music"music/my_heart_dances.ogg" fadein 3.0
show ami with dis
a "\"[mc], au cours des dernières semaines, j'ai énormément apprécié ta compagnie.\""
"Ma mâchoire tombe."
a "\"Et au cours des dernières semaines, je me suis rendu compte que nous partageons tellement de choses en commun en termes d'objectifs et de désirs.\""
"Amicus me donne un sourire timide."
m "\"Qu'est-ce que tu -\""
a "\"J'ai donc décidé de passer à l'étape suivante, pour que tu te sentes plus à l'aise et pour te montrer à quel point j'apprécie ta gentillesse et ta compréhension.\""
"Le loup balance soudain ses pattes vers son front, révélant ce qu'il cachait."
"C'est un bouquet de fleurs violettes, de lavande pour être exact, avec plusieurs petites fleurs blanches saupoudrées dans le mélange."
show ami motivated with dis
a "\"[mc], veux-tu sortir avec moi?\""
stop music
"Je regarde le loup, mon cerveau toujours en train d'essayer de comprendre la déclaration d'Amicus."
"Ma bouche est toujours ouverte et je fais quelques sons \"euh\" alors que j'essaye de former une phrase cohérente pour répondre dans mon esprit."
show ami smile eyes with dis
a "\" Ah, j'ai probablement foiré ça, hein? Eh bien, j'espère que le message est passé clairement? Qu'en penses-tu?\""
m "\"Je - je suis abasourdi.\""
show ami smile with dis
a "\"Et c'est ... une bonne chose?\""
m "\"Amicus, qu'est-ce que c'est que ça?\""
show ami embarrassed with dis
a "\"J'ai fait quelque chose de mal, pas vrai?\""
m "\"Eh bien, je veux dire ... tu sais ce que tu es en train de faire?\""
"Tout cela est fou, mais le comportement d'Amicus ne correspond pas vraiment à la proposition qu'il vient de faire."
a "\"Je viens de te demander de sortir avec moi?\""
m "\"Eh bien ... ouais, mais tu le penses vraiment?\""
a "\"Oui?\""
"Maintenant, le loup s'agite vraiment, tirant nerveusement sur sa cape alors qu'il abaisse le bouquet pour le suspendre mollement à ses côtés."
"J'ai une étrange sensation de papillons dans l'estomac qui ne semble pas disparaître."
"Je ne sais pas ce que cela signifie, mais j'essaye de l'ignorer."
"Le loup se dégonfle soudainement, l'air abattu."
show ami sad with dis
a "\"Je n'ai pas compris la signification de \"sortir ensemble\"?\""
"Je me racle la gorge, essayant de reprendre mes esprits."
m "\"Qu'est-ce que, euh, tu penses que sortir ensemble signifie?\""
show ami frustrated with dis
a "\"Eh bien, ce que tu m'as dit; c'est un statut relationnel qui te permet de te rapprocher, d'en apprendre davantage sur l'autre, tout en normalisant l'intimité physique.\""
"Eh bien, il semble avoir compris les grandes lignes."
"La partie avec laquelle j'ai du mal par contre ..."
m "\"Eh bien, les gens qui sortent ensemble ont aussi tendance à avoir ... je suppose des sentiments les uns pour les autres.\""
show ami emabrrassed with dis
a "\"Eh bien oui, j'ai des sentiments très amicaux pour toi, et je veux que tu sois plus à l'aise avec moi, surtout en ce qui concerne l'intimité physique. N'est-ce pas le but de sortir ensemble?\""
"Je soupire, réalisant que je ne l'avais pas assez bien expliqué, mais je n'avais pas réalisé qu'Amicus avait l'intention de faire ça non plus."
m "\"Eh bien, en général, les gens ne le font pas à moins qu'ils aient des sentiments...amoureux.\""
"Ma voix devient de plus en plus silencieuse au cours de la phrase jusqu'à ce qu'Amicus doive pousser ses oreilles en avant pour m'entendre."
a "\"Amoureux?\""
m "\"... Ouais.\""
show ami surprised with dis
a "\"Oh.\""
"Amicus se tient là un moment avant que l'intérieur de ses oreilles ne devienne rouge vif."
show ami disappointed blush with dis
stop loop
play music"music/trouble.ogg"
a "\"Tu avais dit que c'était décontracté!\""
"Le loup élève la voix, l'augmentation soudaine du volume me fait sursauter."
m "\"Eh bien! Je veux dire, tu n'as pas nécessairement besoin d'être {i} amoureux {/ i} pour sortir avec quelqu'un, mais l'intention est généralement de {i} trouver {/ i} l'amour ...\""
show ami frustrated with dis
a "\"Oh dieux, ton intention était juste de m'humilier après la danse?\""
m "\"De quoi tu parles? Comment j'étais censé savoir que tu plannifirais ça?\""
show ami serious crossed with dis
a "\"Je pense que le fait de poser ces questions l'a rendu assez évident.\""
m "\"Tu penses trop.\""
show ami angry with dis
a "\"Clairement.\""
"Le loup jette le bouquet sur le côté, le laissant atterrir sur le banc avant qu'il ne roule au sol."
stop music fadeout 5.0
"Amicus s'effondre sur le banc à côté de moi, ses oreilles toujours rouges."
"Je le laisse se morfondre pendant une minute ou deux, voulant le laisser se calmer de l'embarras initial."
"Puis je tends la main pour poser ae main sur sa large épaule."
m "\"Désolé, je ne voulais pas t'embarrasser. D'ailleurs, comment est-ce que tu étais censé le savoir? C'est un concept terrien.\""
"Amicus agite une patte."
play music"music/secondthoughts1.ogg" fadein 3.0
show ami serious with dis
a "\"C'est pas grave. Comme tu l'as dit, je suppose trop.\""
"Je me penche pour ramasser le bouquet, voyant à quel point les fleurs étaient en quelque sorte regroupées."
m "\"Tu as fais ça toi même?\""
a "\"Eh bien, oui. Le jardin a de nombreuses fleurs.\""
m "\"Ça sent comme toi.\""
show ami embarrassed with dis
a "\"Euh, oui.\""
m "\"Il est très beau.\""
show ami crossed serious with dis
a "\"Merci.\""
"Nous nous asseyons tranquillement pendant quelques minutes de plus alors que je fais semblant d'examiner toutes les fleurs du bouquet."
a "\"Alors ... C'est soit de l'amitié, soit de l'amour avec les humains? Pas d'intimité physique à moins que vous ne tombiez amoureux?\""
m "\"Qu'est ce que tu veux dire?\""
show ami embarrassed with dis
a "\"Comme ce concept de sortir ensemble que vous avez. Tu étais ok pour m'accorder des faveurs sexuelles. Ça veut dire que tu as également des sentiments amoureux pour moi?\""
"Je rougis."
m "\"Eh bien, pas exactement.\""
a "\"Mais tu as dis que sortir ensemble permettait plus d'intimité? Mais sortir ensemble, c'est aussi chercher l'amour?\""
"Je soupire et je mets le bouquet de côté."
m "\"Les choses changent, deviennent de plus en plus ... décontractées.\""
show ami crossed serious with dis
"Je dis le mot avec soin et Amicus renifle."
m "\"Mais je suppose que le terme que tu recherches peut-être est\"amis avec bénéfices\".\""
a "\"Bénéfices?\""
m "\"Des amis qui ont des relations sexuelles, en gros.\""
show ami surprised with dis
a "\"Ah, je vois. Nous n'avons rien fait, cependant.\""
m "\"Non. Mais je ne vais pas te faire sortir avec moi juste pour avoir une branlette.\""
show ami smile eyes with dis
a "\"Hehe ...\""
show ami sad with dis
"Amicus se gratte derrière la tête avant de détourner le regard à nouveau."
"Encore une fois, je me sens mal pour lui."
m "\"Écoute, si on était pas en plein milieu de cette -\""
"Je baisse la voix."
m "\"- cette aventure spatiale illégale, je pourrais dire oui.\""
show ami surprised with dis
a "\"Quoi, vraiment?\""
m "\"J'ai dit 'pourrais'.\""
show ami crossed with dis
a "\"Oh, vraiment?\""
m "\"Je pense que tu oublis un mot clé là.\""
a "\"Je crois que je comprend.\""
"Je me redeviens rouge, j'aurais aimé garder la bouche fermée."
a "\"Eh bien, peut-être que je pourrais dire oui aussi.\""
m "\"Eh bien, tu as déjà demandé.\""
a "\"Sans en connaître le sens complet.\""
"J'essaye de penser à autre chose pour changer de sujet, sachant que mon rougissement est clair comme le jour pour le loup et qu'il l'apprécie beaucoup."
m "\" Bref, Alexios m'a dit que Cassius s'entraînait sous la direction d'un rhéteur, euh ... Markus Malin, ou quelque chose comme ça?\""
show ami crossed serious with dis
"Amicus fronce soudain les sourcils."
a "\"Marcus Manius, vraiment?\""
m "\"Je pense que c'est ce qu'il a dit.\""
a "\"Merde.\""
"Le ton d'Amicus est celui de la crainte."
m "\"C'est mauvais?\""
a "\"C'est ... tout simplement surprenant. Il est le rhéteur adastran le plus célèbre qui soit.\""
m "\"Je dois m'inquiéter?\""
show ami smile eyes with dis
a "\"Non, en fait, maintenant que tu me l'as dit je suis en bien meilleure forme. J'ai maintenant une idée du style qu'il pourrait utiliser, ce qui me permettra de contrer plus facilement ses points.\""
m "\"Si tu en es sûr ...\""
show ami motivated with dis
a "\"Bien sûr! Maintenant, viens dans ma chambre pour m'aider à m'entraîner, juste pour être sûr que je gagnerai.\""
stop music fadeout 5.0
play loop"sfx/birds.ogg" fadein 3.0
scene bg garden2 with dissolve
"Nous nous levons et retournons au palais à travers les jardins, laissant le bouquet de fleurs sur le banc."
"Amicus semble avoir surmonté son embarras à propos de tout l'incident assez rapidement."
"C'est tout lui de pouvoir faire ça, en fait"
"En fait, nous rions et parlons aussi facilement que nous l'avons toujours fait, le loup me donnant un coup de coude toutes les quelques minutes pour ponctuer quelque chose qu'il dit, chacun me faisant trébucher."
scene bg palace1 with dissolve
show ami with dissolve
a "\"Quoi qu'il en soit, Cass a tendance à bégayer sur ses mots devant une foule nombreuse. Un rhéteur ne peut pas faire grand-chose à ce sujet!\""
stop loop fadeout 3.0
"Le loup tend une patte, la pressant contre le carré noir."
play sound"sfx/dooropen.ogg"
scene bg amicusroom with dissolve
a "\"D'ailleurs, qu'est-ce qu'il -\""
show cas surprised at right with dissolve
"Amicus et moi regardons avec surprise alors que Cassius nous regarde avec ce qui semble être encore plus de surprise."
"Puis ses yeux se rétrécissent."
show cas annoyed with dis
c "\"Excusez-moi.\""
"Il essaie de se déplacer autour de nous, mais Amicus lui bloque le chemin en grognant."
show ami angry teeth at left with dissolve
a "\"Qu'est-ce que tu fous ici, Cassius!\""
show cas scared with dis
"Amicus semble réserver ses hurlements réels uniquement pour Cassius, ça me fait sursauter quand je l'entends."
"Cassius se ressaisit rapidement malgré les grognements intimidants d'Amicus."
show cas talking with dis
c "\"Ce ne sont pas tes affaires.\""
a "\"Si tu es dans ma chambre, c'est mon affaire.\""
a "\"Qu'est ce que. Tu. As. FAIS!?\""
show cas surprised with dis
"Le loup commence à avancer sur Cassius, s'arrêtant à quelques pas."
show cas paw talking with dis
c "\"Laisse moi passer Amicus, sinon j'appelle Cato.\""
"Amicus regarde Cassius de près, puis recule finalement, croisant les bras."
show ami crossed serious with dis
a "\"Tu fouines pour trouver quelque chose qui pourrait te donner une chance pour l'épreuve? Je peux te dire tu ne trouveras rien.\""
c "\"Evidemment. Tu n'as rien à offrir pour m'aider à gagner.\""
show ami angry teeth with dis
a "\"Alors pourquoi venir ici?\""
"Cassius l'ignore, passant devant Amicus avant de passer à côté de moi."
"Il se retourne alors."
show cas smile with dis
c "\"Et tu sais, je ne devrais pas m'inquiéter après le pitoyable étalage que toi et ton 'animal de compagnie' avez fait.\""
"Il se tourne vers moi et je ne peux pas m'empêcher de froncer les sourcils."
c "\"Aussi stupide qu'il est laid.\""
"Je sais que Cassius essaie juste d'énerver Amicus."
"Il sait qu'il se soucie de moi."
"Mais alors que Cassius tend la patte pour me frotter le menton avec, je ne peux pas m'empêcher de la repousser en la frappant."
show cas surprised with dis
"Les yeux de Cassius s'écarquillent alors, et je vois sa patte reculer."
show cas angry with dis
"Je tressaille, mais immédiatement Amicus est là, tendant la main pour attraper Cassius par sa cape."
hide cas
hide ami
with dissolve
play loop"music/tensebackgroad.ogg" fadein 3.0
"Le plus petit des deux loups est éloigné de moi, mais Amicus ne s'arrête pas là."
"Alors que Cassius trébuche devant Amicus, le plus gros loup balance sa patte, frappant Cassius au nez."
play sound"sfx/thud.ogg"
"Cassius tombe immédiatement sur ses fesses et j'entends un autre son."
play sound"sfx/bonebreak.ogg"
"Amicus et moi fixons le plus petit loup alors qu'il est assis là, stupéfait, puis il se remet soudainement debout, une patte à l'arrière."
show cas furious blood at left with dissolve
c "\"Amicus, espèce de salaud! Lève-queue ! Avaleur de sabres!\""
"Je fais un pas en arrière alors que Cassius crache du sang de sa bouche."
show ami serious crossed at right with dis
"Amicus me tire à ses côtés, les yeux plissés, mais je peux sentir son cœur battre contre mon épaule."
c "\"Je vous jetterai tous les deux dans le donjon pour ça. Je le ferai EXECUTER quand je serai empereur!\""
stop loop fadeout 7.0
"Je vois des larmes commencer à couler des yeux de Cassius avant qu'il ne se retourne et ne trébuche hors de la pièce, sa queue pendait mollement sur le côté."
hide cas with dissolve
"Amicus et moi restons là pendant un long moment après son départ, le silence presque oppressant après le combat bruyant."
jump a1s6


play sound"music/tbc.ogg"
scene bg black with transition_fade
"À suivre..."
window hide
scene bg credits with dissolve
pause
stop sound fadeout 3.0
return

