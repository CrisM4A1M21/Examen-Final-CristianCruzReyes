import random
import math


def crearArchivo():
    try:
        file = open("notas.txt", "a+")
    except OSError as error:
        print(error)
    finally:
        file.close()


def insertarDatos():
    try:
        lista = []
        tamanio = int(input("Ingrese el tamaño de la lista: "))
        for i in range(tamanio):
            lista.append(random.randint(0, 50))

        file = open("notas.txt", "w")
        for i in lista:
            file.write(str(i) + "\n")
    except ValueError as error:
        print(error)
    except OSError as error:
        print(error)
    finally:
        file.close()


def raizCuadrada():
    try:
        file = open("notas.txt", "r")
        lista = file.read()
        lista = lista.split("\n")
        lista.pop()
        file.close()
        file = open("notas.txt", "a+")
        for i in lista:
            raiz = math.sqrt(int(i))
            file.write(str(f"{raiz:.2f}") + "\n")
    except OSError as error:
        print(error)
    finally:
        file.close()
