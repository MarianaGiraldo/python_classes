import random


def ask() :
    return int(input("Desea crear la lista de números manualmente (1) o generarla aleatoriament(2)? (1/2):  "))

def getRandomList() :
    return random.sample(range(1, 100), 20)

def numList() :
    #Pregunta si se desea crear manualmente o generarla
    question = ask()
    #initializa list
    list = []
    #Verifica si son respuestas validas
    if (question == 1  or question == 2):
        #Verifica si se desea generar de forma manual
        if (question == 1) :
            #Inizializa la posición inicial y el limite de tamaño de la lista
            i = 1
            limit = 8
            while (i <= limit):
                #Agrega los numeros
                list.append(int(input(f"Ingrese un numero para la posición {i} de la lista: ")))
                #Aumenta el valor de la posición
                i += 1
                #Verifica si llegó al límite
                if (i > limit):
                    #Pregunta si se desan agregar más elementos
                    addNumber = (input("¿Desea añadir otro número a la lista? (Y/n) ")).lower()
                    #Aumenta el límite
                    if (addNumber == "y"):
                        limit += 1
        #Si la respuesta es 2, se genera la lista aleatoria
        else:
            list = getRandomList()
        print("Lista creada.")
        #Imprime lista
        print(list)
        #Verifica si hay duplicados
        if len(list) == len(set(list)):
            #No hay duplicados
            return False
        else:
            #Si hay duplicados
            return True
    else:
        print("Opción incorrecta")
        numList()

if numList():
    print("Hay elementos duplicados en la lista")
else:
    print("No hay elementos duplicados en la lista")