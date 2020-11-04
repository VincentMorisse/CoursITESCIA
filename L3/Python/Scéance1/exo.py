from ast import Param
from itertools import combinations
from math import *
import math
import re
import itertools

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

def exo17() :
    print("Exercice 17")
    chaine = input("Saissisez votre chaine de caractère : ")
    temp = []
    for char1 in chaine :
        if char1 not in temp :
            temp.append(char1)
            somme = 0
            for char2 in chaine :
                if char2 ==char1 :
                    somme +=1
            print("Le caractère :",char1," figure ", somme," fois dans votre chaine de caractère")

def exo18() :
    print("Exercice 18")
    chaine = input("Saissisez votre chaine de caractère : ")
    tempValue = 0
    for char in chaine :
        if char == "a" :
            print("La lettre a se trouve à la position :", tempValue)
        tempValue +=1

def exo19() :
    print("Exercice 19")
    list = ["laptop", "iphone", "tablet"]
    for word in list :
        print(word, "contient ", len(word), " caractère(s)")

def exo20() :
    print("Exercice 20")
    print("Inversser le premier et dernier caractère d'une liste")
    chaine = input("Saissisez votre chaine de caractère : ")
    newchaine = chaine[len(chaine)-1] + chaine[1:len(chaine)-1] +chaine[0]
    print(newchaine)

def exo21() :
    print("Exercice 21")
    print("Compter le nombre de voyelle")
    chaine = input("Saissisez votre chaine de caractère : ")
    voyelle = ["a","e","i","o","u","y"]
    compt= 0
    for char in chaine :
        if char in voyelle :
            compt +=1
    print("Il y a ",compt,"voyelle dans ce mot")

def exo22() :
    print("Exercice 22")
    print("Afficher le premier mot d'une phrase")
    chaine = input("Saissisez votre chaine de caractère : ")
    words = chaine.split()
    print(words[0])

def exo23() :
    print("Exercice 23")
    print("Afficher l'extension d'un fichier")
    chaine = input("Saissisez votre chaine de caractère : ")
    temp = len(chaine)-1
    while temp > 0  and chaine[temp]!="." :
        temp-=1
    print(chaine[temp:len(chaine)])

def exo24():
    print("Exercice 24")
    print("Savoir si un mot est un palindrome")
    chaine = input("Saissisez votre chaine de caractère : ")
    palin = True
    temp = 0
    while palin == True and temp < len(chaine)//2 :
        if chaine[temp] != chaine[len(chaine)-temp-1] :
            palin = False
        temp+=1
    if palin == True :
        print(chaine, " est un palindrome")
    else :
        print(chaine, " n'est pas un palindrome")

def exo24v2():
    print("Exercice 24v2")
    print("Savoir si un mot est un palindrome")
    chaine = input("Saissisez votre chaine de caractère : ")
    if chaine == chaine[::-1]:
        print(chaine, " est un palindrome")
    else :
        print(chaine, "n'est pas un palindrome")

def exo25():
    print("Exercice 25")
    print("Renvoyer l'inverse d'un mot")
    chaine = input("Saissisez votre chaine de caractère : ")
    print(chaine[::-1])

def exo26():
    print("Exercice 26")
    print("Renvoyer tout les mots commençant par a")
    chaine = input("Saissisez votre chaine de caractère : ")
    words = chaine.split()
    for word in words :
        if word[0]== "a" :
            print(word)

def exo27():
    print("Exercice 27")
    print("Renvoyer le mot le plus long")
    chaine = input("Saissisez votre chaine de caractère : ")
    words = chaine.split()
    temp = 0
    lenmax = 0
    longestword = 0
    for word in words :
        if len(word) > lenmax :
            lenmax = len(word)
            longestword = temp
        temp +=1
    print("Le mot le plus long est ", words[longestword])
        
def exo28(param):
    print("Exercice 28")
    print("Test si liste est vide")
    if len(param) == 0 :
        print("La liste ou chaine est vide")
    else :
        print("La liste ou chaine n'est pas vide")

def exo29(param):
    print("Exercice 29")
    print("Supprimer les doublon d'une liste")
    newListe = list(set(param))
    print(newListe)

def exo30(param1, param2) :
    print("Exercice 30")
    print("Chercher valeur commune de deux liste")
    for temp1 in param1 :
        if temp1 in param2 :
            print(temp1, "est un valeur commune au deux liste")

def exo31(param) :
    print("Exercice 31")
    print("Séparer valeur pair et impair")
    pair =[]
    impair = []
    for temp in param :
        if temp%2 ==0 :
            pair.append(temp)
        else :
            impair.append(temp)
    print("Valeur pair :", pair)
    print("Valeur impair :", impair)

def exo32(param):
    print("Exercice 32")
    print("Afficher toutes les combinaisons possible d'une liste")
    all_combi = []
    for temp in range(len(param) +1):
        combi= itertools.combinations(param, temp)
        combi_list = list(combi)
        all_combi += combi_list
    print(all_combi)
    

def exo33(param):
    print("Exercice 33")
    print("Afficher un caractre sur deux")
    temp = 0
    tempChaine = ""
    for carac in param :
        if temp%2 ==0 :
            tempChaine += carac
        temp +=1
    print(tempChaine)

def exo34(param) :
    print("Exercice 34")
    print("Récupérer les valeur d'un liste supérieur à une certaine valeur")
    newListe = []
    for note in param :
        if note > 10:
            newListe.append(note)
    print(newListe)

def exo35(phrase) :
    print("Exercice 35")
    print("Compter les occurence de mot dans une liste en utilisant un dictionnaire")
    param = phrase.split()
    dico = {}
    for word in param :
        if word not in dico :
            dico[word] = 1
        else :
            dico[word] += 1
    print(dico)

def exo36(param) :
    print("Exercice 36")
    print("Supprimer les doubles espaces")
    temp = re.sub(' +', ' ', param)
    print(temp)

def exo37(param11, param22) :
    print("Exercice 37")
    print("Mettre les mots commun de deux liste dans un ensemble")
    param1 = param11.split()
    param2 = param22.split()
    ensemble = set()
    for word in param1 :
        if word in param2 :
           ensemble.add(word)
    
    print(ensemble)

def exo38() :
    print("Exercice 38")
    print("Inversé premier et dernier mot")
    chaine = input('Saisir une phrase : ')
    words = chaine.split()
    tmp = words[-1]
    words[-1] = words[0]
    words[0] = tmp
    print(" ".join(words))

def exo39() :
    print("Exercice 39")
    print("Compter le nombre de mot")
    chaine = input('Saisir une phrase : ') 
    words = chaine.split()
    print(len(words))

def exo41(liste, div) :
    print("Exercice 41")
    print("Compter le nombre d'élément de la liste divisible par val")
    tmp = 0
    for temp in liste :
        if temp%div == 0 :
            tmp +=1
    print(tmp)

def exo42(liste, val) :
    print("Exercice 42")
    print("Compter le nombre d'apparition d'un nombre dans une liste")
    tmp = 0
    for temp in liste :
        if temp == val :
            tmp +=1
    print(tmp)

def exo43(chaine) :
    print("Exercice 43")
    print("Insérer un * entre chaque carac d'une phrase")
    res =""
    for temp in range(0,len(chaine)) :
        if temp != len(chaine) -1 :
            res += chaine[temp] + "*"
        else :
            res += chaine[temp]
    print(res)

def exo44(liste) :
    print("Exercice 44")
    print("Passer en uppercase")
    res = []
    for tmp in liste :
        res.append(tmp.upper())
    print(res)

def exo45(chaine) :
    print("Exercice 45")
    print("Calculer lower et uper case")
    uper =0
    lower =0
    for char in chaine :
        if char.isupper() :
            uper +=1
        if char.islower() :
            lower +=1
    print("Il y a ", uper," maj et ", lower,"minuscule")

def exo46(val) :
    if val == 0 :
        print("0")
    else :
        tmp = []
        while val > 0 :
            tmp.append(val % 10)
            val = val // 10
        print(tmp)

def exo47(param11, param22) :
    print("Exercice 37")
    print("Mettre les mots commun de deux liste dans un ensemble")
    param1 = param11.split()
    param2 = param22.split()
    ensemble = []
    for word in param1 :
        if word in param2 :
           ensemble.append(word)
    print(ensemble)

if __name__ == "__main__":
    exo32([1,2,3,4]);




