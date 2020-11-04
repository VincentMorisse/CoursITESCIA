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
    

if __name__ == "__main__":
    exo6()
