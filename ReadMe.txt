## Prérequis 

- Avoir une version de python installé sur sa machine 
https://www.python.org/

- Pour connaitre sa version de python utiliser la commande python --version
https://docs.python.org/3/using/cmdline.html#generic-options 

## Lancer le code python sans Ihm:

electron.app\CodePython\Rsa.py

## Lancer l'application electron avec l'Ihm:

electron.app\my-electron-app\out\electron-quick-start-win32-x64\electron-quick-start.exe

## Fonctionnement de l'application: 

- Cliquez sur le cadenas au menu pour démarrer 
- Dans la zone textuel rentrer le message à chiffrer et cliquer sur le bouton chiffrer 
  les accents ne sont pas pris en compte veiller à ne pas en utiliser
- Pour déchiffrer cliquer sur le bouton changer de mode copier le le message chiffrer precedement 
  et coller le dans la zone textuel Message à déchiffrer veiller a ne pas laisser d'espace a la fin de la saisie 
  Répeter le processus pour partie commune de la clé  et partie publique de la clé et cliquer sur Dechiffrer 

- Liste des caracteres pris en compte
	
 ' ' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
 'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'
 '0' '1' '2' '3' '4' '5' '6' '7' '8' '9' '.' '!' '\' ','