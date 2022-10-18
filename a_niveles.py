#Carpeta 1niveles

#Creo las funciones de los distintos niveles del juego. Para ello utilizo la libreria import random, la cual me ayuda a generar un numero random comprendido entre el minimo y el maximo de cada nivel.

import random


def nivel_simple():
    num = random.randint(0, 100)
    return num


def nivel_intermedio():
    num = random.randint(0, 1000)
    return num


def nivel_avanzado():
    num = random.randint(0, 1000000)
    return num


def nivel_experto():
    num = random.randint(0, 1000000000000)
    return num
