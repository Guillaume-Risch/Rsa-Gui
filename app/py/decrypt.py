import sys
import math
import random
import json
# import numpy as np

def genereTabs():
    tabReste = [ ]
    tabDiviseur = [ ]
    tabDividende = [ ]
    tabQuotient = [ ]
    return (tabReste,tabDiviseur,tabDividende,tabQuotient)


def genereAlphabet( ): #créé une matrice alphabet de type [ ['lettre',valeur] ] où la correspondance des valeurs et des les lettres sont celles de la table ASCII 
    alphabet = [                   #table ASCII 
        [' ',40], ['a',97],  ['0',60],
        ['A',65], ['b',98],  ['1',61],
        ['B',66], ['c',99],  ['2',62],
        ['C',67], ['d',100], ['3',63],
        ['D',68], ['e',101], ['4',64],
        ['E',69], ['f',102], ['5',65],
        ['F',70], ['g',103], ['6',66],
        ['G',71], ['h',104], ['7',67],
        ['H',72], ['i',105], ['8',68],
        ['I',73], ['j',106], ['9',69],
        ['J',74], ['k',107],
        ['K',75], ['l',108],
        ['L',76], ['m',109],
        ['M',77], ['n',110],
        ['N',78], ['o',111],
        ['O',79], ['p',112],
        ['P',80], ['q',113],
        ['Q',81], ['r',114],
        ['R',82], ['s',115],
        ['S',83], ['t',116],
        ['T',84], ['u',117],
        ['U',85], ['v',118],
        ['V',86], ['w',119],
        ['W',87], ['x',120],
        ['X',88], ['y',121],
        ['Y',89], ['z',122],
        ['Z',90],
        ['.',56], ['!',41],['\'',47],[',',54]]
    return alphabet


def pgcd(a,b,tabReste,tabDiviseur,tabDividende,tabQuotient): #permet de calculer le pgcd de deux nombres premiers a et b et ainsi de remplir les tableaux tabReste ... pour s'en servir dans la fonction Bezout
    if a !=0 and b != 0:
        if b > a :
            return pgcd(b,a,tabReste,tabDiviseur,tabDividende,tabQuotient) #si b > a on rappelle pgcd en inversant les deux valeurs 
        if a > b :
            
            reste : int = a%b
            tabReste.append(int(a%b))  #.append permet d'ajouter une valeur dans un tableau ici on y met le reste de la division entière de a/b
            tabDiviseur.append(int(b)) #on met le diviseur b dans tabDiviseur
            tabDividende.append(int(a)) #on met le dividende a dans tabDividende 
            tabQuotient.append(int(a//b)) #on met le quotient entier de la division de a/b
            if tabReste[len(tabReste)-1] == 1: #permet de savoir si on arrive au moment où le reste à la fin de la division euclidienne de a/b est égal à 1
                                               #pour vérifier la propriété pgcd(e,phi) = 1
                return (tabReste,tabDiviseur,tabDividende,tabQuotient, tabReste[len(tabReste)-1]) # 
            else:
                return pgcd(b,reste,tabReste,tabDiviseur,tabDividende,tabQuotient)


def est_premier(nombre):  
    for x in range(3, nombre): # on regarde si chaque x est un diviseur de nombre dans ce cas on renvoie faux, si on ne trouve pas de diviseur entre 3 et lui-même alors on renvoie faux 
        if nombre % x == 0 or nombre % 2 == 0: # nombre % x veut dire que le nombre a un diviseur qui n'est ni 1 ni lui-même et nombre % 2 == 0 pour éviter les cas où le nombre est pair
            return False
    return True



def genereTabPremier(nombre,tabNombrePremier): #genere un tableau contenant tout les entiers de 1 jusqu'à le nombre passé en paramètre
    for i in range (1,nombre):
        if est_premier(i): 
            tabNombrePremier.append(i)
    return tabNombrePremier

def Bezout(a,b,u,v,i,tabReste,tabDiviseur,tabDividende,tabQuotient): #permet de calculer les coefficients de Bezout de manière récursive grâce aux tableaux remplis par la fonction pgcd(a,b)
    if tabDividende[0] * u + tabDiviseur[0] * v == 1: #a == tabDividende[0] and b == tabDiviseur[0] and i == 0:
        return (u,v)
    elif tabDividende[0] * u  + tabDiviseur[0] * v == 1 and i == 0:
        return (1,-1)
    else:
        return Bezout(tabDividende[i-1],a,v,u+v*(-tabQuotient[i-1]),i-1,tabReste,tabDiviseur,tabDividende,tabQuotient) #appel à la fonction de manière récursive pour pouvoir remonter les étapes du pgcd et obtenier les coeffs de bezout
    
def is_space(char): #permet de savoir si le caracètre passé en paramètre est un espace 
    if char == " ":
        return True
    else: 
        return False

def findCharToInt(char,alphabet): # va chercher la valeur correspondante à la lettre dans la matrice alphabet 
    for i in range(0, len(alphabet)):
        if alphabet[i][0] == char: 
            return alphabet[i][1]
        elif is_space(char):
            return 32 #valeur des espaces dans l'ascii
        
        
def findIntToChar(nombre,alphabet): #va chercher la lettre en fonction de la valeur de nombre dans la matrice alphabet
    for i in range(0, len(alphabet)):
        if alphabet[i][1] == nombre: 
            return alphabet[i][0]

def findLastIndexNbrPrime (n,tabNombrePremier): # la fonction sert à trouver l'indice du dernier nombre premier plus petit que la partie entière de la racine de n                                                 
    racine_n : int = int(n**0.5) # sqrt(n) == n**0.5
    for i in range(0,len(tabNombrePremier)):
        if tabNombrePremier[i] > racine_n: # récuperer l'indice du dernier nombre premier avant la racine de la clé publique n
            return i-1
        elif tabNombrePremier[i] == racine_n:
            return i
        
def crackage (n,tabNombrePremier): #Permet de trouver le premier p ou n%p = 0 pour vérifier que : n = p*q <=> q = n/p 
    indice : int = findLastIndexNbrPrime(n,tabNombrePremier) #on cherche l'indice de la partie entière de la racine carré de n dans le tableau des nombres premiers car par exemple
                                                             #sqrt(16) = 4, 4*4 =16 mais 4*5 =20 cette racine peut-être considéré comme une limite dans la multiplication                                                           
    for i in range(indice, -1, -1): # parcours du tableau tabNombrePremier en partant de l'indice de la racine carré de n (clé publique) 
        if n%tabNombrePremier[i] == 0:
            return tabNombrePremier[i]
        
def chiffrage (mot,tabVal,alphabet,e,n): #récupère chaque lettre du mot à chiffrer, trouve la valeur correspondante à la lettre dans la matrice alphabet et met chaque valeur dans un tableau 
    for lettre in mot: 
        valLettre : int = findCharToInt(lettre,alphabet)
        lettrechiffree = valLettre**e%n
        tabVal.append(lettrechiffree)

def dechiffrage(tabVal,alphabet,d,n): #récupère chaque valeur du tableau contenant le chiffrage des lettres et renvoie le mot déchiffré
    motdechiffree : str =""
    for i in range(0,len(tabVal)):
        lettredechiffree = int(tabVal[i]**d%n)
        lettre = findIntToChar(lettredechiffree,alphabet)
        motdechiffree = motdechiffree + lettre
    return motdechiffree
    
def isKeyNegative(v,phi):
    d : int 
    if v < 0:  #si v est négatif alors d prend la valeur v + phi(n) car dans le cas où v < 0 le chiffrement est impossible avec juste d = v, mais le devient avec d = v + phi
        d = v + phi
    else:
        d = v
    return int(d) 



        
def initialisation(tabNombrePremier,tabReste,tabDiviseur,tabDividende,tabQuotient): # permet d'initialiser les valeurs p et q qui servent à créer la clé publique (n,e) où n = p*q et e est un nombre premier choisi aléatoirement  
    p : int = random.choice(tabNombrePremier) #on cherche un nombre premier aléatoirement dans tabNombrePremier et on l'affecte à p
    q : int = random.choice(tabNombrePremier) #on cherche un nombre premier aléatoirement dans tabNombrePremier et on l'affecte à q
    if p == q:                                #Dans le cas possible où p == q on tire un autre nombre aléatoirement dans tabNombrePremier (pas obligatoire)
        q = random.choice(tabNombrePremier) 
    n : int = p*q
    phi : int = (p-1)*(q-1)
    e : int = random.choice(tabNombrePremier)
    while e > phi:                            # e partie de la clé publique (n,e) doit être 0 < e < phi, ce bloc permet de gérer cette exception
        e = random.choice(tabNombrePremier)
    pgcd(e,phi,tabReste,tabDiviseur,tabDividende,tabQuotient)                              
    
    return (n,phi,e,p,q)
  
    


tabValChiffre = sys.argv[1]
tabValChiffre = tabValChiffre.replace('[', '')
tabValChiffre = tabValChiffre.replace(']', '')
tabValChiffre = tabValChiffre.split(',')

for i in range(0, len(tabValChiffre)) :
    tabValChiffre[i] = int(tabValChiffre[i])

n = int(sys.argv[2])
e = int(sys.argv[3])


tabNombrePremier = []
tabNombrePremier = genereTabPremier(1500, tabNombrePremier)

tabRestebis, tabDiviseurbis, tabDividendebis, tabQuotientbis = genereTabs()
alphabet = genereAlphabet()
pbis : int = crackage(n,tabNombrePremier) #permet d'obtenir le premier facteur de n = p*q (ça ne peut pas être p directement car la fonction renvoie le plus grand terme trouvé car on parcourt le tableau à l'inverse)
qbis : int = n/pbis                       #permet d'obtenir le deuxième facteur de n= p*q car n/p = q  

phibis : int = (pbis-1)*(qbis-1)
# tabReste,tabDiviseur,tabDividende,tabQuotient, tabReste[len(tabReste)-1]
tabRestebis, tabDiviseurbis, tabDividendebis, tabQuotientbis,z = pgcd(e,phibis,tabRestebis, tabDiviseurbis, tabDividendebis, tabQuotientbis)
ubis,vbis = Bezout(tabDividendebis[len(tabDividendebis)-1],tabDiviseurbis[len(tabDiviseurbis)-1],1,-1,len(tabDividendebis)-1,tabRestebis,tabDiviseurbis,tabDividendebis,tabQuotientbis)
dbis : int = isKeyNegative(vbis,phibis)
motdechiffrecrack : str = dechiffrage(tabValChiffre,alphabet,dbis,n)

json_dict = json.dumps(motdechiffrecrack)
print(json_dict)














