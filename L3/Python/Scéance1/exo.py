from math import *
import math

def checkInputIsInt() :
    try:
        value = int(input('Saissisez votre nombre : '))
        return value
    except :
        print("La valeur rentrée n'est pas un int")
        checkInputIsInt()

def exo1() :
    name = input('Saissisez votre nom: ')
    print('Bienvenue ' + name)

def exo2() :
    print("Exercice 2")
    print("Première valeur")
    valueOne = checkInputIsInt()
    print("Deuxième valeur")
    valueTwo = checkInputIsInt()
    somme= int(valueOne) + int(valueTwo)
    print("Leur somme est ", somme)

def exo3():
    print("Exercice 3")
    print("Première valeur")
    valueOne = int(checkInputIsInt())
    print("Deuxième valeur")
    valueTwo = int(checkInputIsInt())
    if valueOne > valueTwo:
        print("La première valeur (", valueOne ,") est la plus grande")
    elif valueOne < valueTwo :
        print("La deuxième valeur (", valueTwo ,") est la plus grande")
    else :
        print("Les deux valeurs sont égales")

def exo4():
    print("Exercice 4")
    print("Valeur dont vous voulez savoir si elle est pair ou impair:")
    value = int(checkInputIsInt())
    if value%2==1 :
        print("La valeur saisie est impair")
    else :
        print("La valeur saisie est pair")

def exo5():
    print("Exercice 5")
    print("Valeur votre age:")
    value = int(checkInputIsInt())
    if value >=18 :
        print("Vous êtes majeur")
    elif value<0 :
        print("tu n'es pas né t'es tu trompé dans ton age ?")
        exo5()
    else :
        print("Vous êtes mineur")

def exo6():
    print("Exercice 6")
    print("Première valeur")
    valueOne = int(checkInputIsInt())
    print("Deuxième valeur")
    valueTwo = int(checkInputIsInt())
    print("Troisième valeur")
    valueThree = int(checkInputIsInt())
    print("La valeur maximum est ", max([valueOne, valueTwo, valueThree]))
    
def exo7() :
    print("Exercice 7")
    for tempValue in range(1,101) :
        print(tempValue)

def exo8() :
    print("Exercice 8")
    value = int(checkInputIsInt())
    somme = 0
    for tempValue in range(0,value+1):
        somme = somme + tempValue
    print("La somme de tout les entiers jusqu'à",value," est ", somme)
    
def exo9():
    print("Exercice 9")
    print("Calculer la factorielle d'un nombre")
    value = int(checkInputIsInt())
    produit = 1
    for tempValue in range(1,value+1):
        produit = produit * tempValue
    print("La factorielle de ",value," est ", produit)

def exo10() :
    print("Exercice 10")
    print("Calculer le périmètre à partir d'un rayon")
    value = int(checkInputIsInt())
    peri = 2 * math.pi * value
    surface = value * value * math.pi
    print("Un cercle de rayon ", value," a un périmètre de", peri, " et une surface de ", surface)

def exo11() :
    print("Exercice 11")
    print("Afficher tout les diviseurs d'un nombre")
    value = int(checkInputIsInt())
    res = []
    for tempValue in range(1, value + 1):
        if value % tempValue == 0:
            res.append(tempValue)
    print("Les diviseurs de ",value,"sont",res)

def exo12() :
    print("Exercice 12")
    print("Affiche la table de multiplication d'un nombre")
    value = int(checkInputIsInt())
    for tempValue in range(0,11) :
        print(value,"x",tempValue,"=",value*tempValue)

def exo12v2() :
    print("Exercice 12v2")
    print("Affiche les tables de multiplication")
    for tempValue1 in range(0,11):
        print("Table de multiplication de", tempValue1)
        for tempValue2 in range(0,11) :
            print(tempValue1,"x",tempValue2,"=",tempValue1*tempValue2)

def exo13() :
    print("Exercice 13")
    print("Calcul le quotient et le reste de la division euclidienne")
    print("Première valeur")
    valueOne = int(checkInputIsInt())
    print("Deuxième valeur")
    valueTwo = int(checkInputIsInt())
    reste = max([valueOne,valueTwo]) % min([valueOne,valueTwo])
    quotient = max([valueOne,valueTwo]) // min([valueOne,valueTwo])
    print("Le quotient de cette division est ",quotient,"et le reste est",reste)

def exo14() :
    print("Exercice 14")
    print("Savoir si un nombre est un carré parfait")
    value = int(checkInputIsInt())
    if sqrt(value)%1==0 :
        print(value, " est un carré parfait")
    else :
        print(value, " n'est pas un carré parfait")

def exo15() :
    print("Exercice 15")
    print("Savoir si un nombre est premier")
    value = int(checkInputIsInt())
    res = []
    for tempValue in range(1, value + 1):
        if value % tempValue == 0:
            res.append(tempValue)
    
    if len(res) == 2 or res == [1] :
        print(value," est un nombre premier")
    else :
        print(value,"n'est pas un nombre premier")
        
def exo16() :
    print("Exercice 16")
    chaine = input("Saissisez votre chaine de caractère : ")
    for char in chaine :
        print(char)

if __name__ == "__main__":
    exo16()


