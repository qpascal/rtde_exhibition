# RTDE EXHIBITION

Robotic cell programming with real-time piloting and synchronized simulation

## Addendums to the RTDE Instructions

- Section formattings  
- Include detailed steps to the Ubuntu Pro token and explanation
- Notify every "test" command and the expected output
- Include troubleshooting and version control commands in a separate section (ua version/systemctl status + Ctrl C)
- Included sudo apt updates/upgrades
- Add sudo and -y to ua enable, add sudo to docker build/run
- Add install of cmake and pip ?
- Remove su USER
- Add net-tools

## File management

- Main file is the RoboDK executed file, from which the RTDE custom library takes its commands and gives back data
- RTDE control and further Python logic not directly related to RoboDK rendering act as dependencies for the main file
- Convenience files can be written to setup the simulation (coordinates/3D models, etc.)

## Object dimensions

- A single block is 6.7 x 2.2 x 1.5mm
- The jenga game has 18 stacks of 3 aligned blocks 
- Box has 7mm thick walls and roof, has 2mm thick back panel and doesn't reach the floor leaving a 3mm gap between the bottom stack and the box limit

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