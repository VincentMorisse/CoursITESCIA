
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

def checkInputIsInt() :
    try:
        value = int(input('Saissisez votre nombre : '))
        return value
    except :
        print("La valeur rentrée n'est pas un int")
        checkInputIsInt()

if __name__ == "__main__":
    exo2()
