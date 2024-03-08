# RTDE EXHIBITION

Robotic cell programming with real-time piloting and synchronized simulation

## Predefined positions

Home position : position de départ du code fonctionnel
Start/Stop position : position de rangement du robot

Tower position : position d'approche en fonction de la tour

Interface place position : position de placement de la pièce d'interface de préhension
Interface pick position : position de récupération de la pièce d'interface de préhension
Side start position : position d'approche des blocs d'un côté donné
Max Push position : position maximale de poussée de chaque bloc
Pickup position : position d'approche du bloc à demi sorti

Place position : position d'approche du dépôt des blocs retirés ----> variable avec niveau de Z
## Functions

connection/deconnexion : fonctions de connection au robot
moveJ(matrice,vitesse,acceleration,asynchrone,move/servo) : mouvements MoveJ/ServoJ
moveL(matrice,vitesse,acceleration,asynchrone,move/servo) : mouvements MoveL/ServoL

getDataFromRobot : données prélevées (avec modes)
getData : tranfert des données du RTDE à RoboDK
renderData : afficher données nécessaires (valeurs de force/position) ----> matplotlib

getBlockPosition : 
getBlockState : stade de gestion du bloc (sur la tour/récupéré)