import random


def numerosAleatorios():
    lista = []
    for i in range(10):
        lista.append(random.randint(0, 10))
    print("Elementos de la lista creada: \n{}".format(lista))
    return lista


def noRepetidos(lista):
    elimina = []
    contador = 0
    for i in range(10):
        for j in range(10):
            if lista[i] == lista[j]:
                contador = contador + 1
        if contador > 1:
            elimina.append(lista[i])
        contador = 0

    for i in elimina:
        lista.remove(i)

    return lista


def ordena(lista):
    lista_mayor_menor = lista.copy()
    lista_menor_mayor = lista.copy()
    lista_mayor_menor.sort()
    lista_mayor_menor.reverse()
    lista_menor_mayor.sort()
    print("Lista mayor a menor: {}".format(lista_mayor_menor))
    print("Lista menor a mayor: {}".format(lista_menor_mayor))


def mayorElemento(lista):
    maximo = max(lista)
    return maximo


lista = numerosAleatorios()
lista = noRepetidos(lista)
print("Elementos no repetidos de la lista: {}".format(lista))
ordena(lista)
print("Maximo valor de la lista: {}".format(mayorElemento(lista)))
