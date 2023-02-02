import pickle
import os
from registro import *
import random


def generador(n, fd):
    m = open(fd, 'wb')
    n=50
    for a in range(n):
        titulo = random.randint(0, 6)
        genero = random.randint(0, 5)
        idioma = random.randint(0, 4)
        pelicula = Pelicula(titulo, genero, idioma)
        pickle.dump(pelicula, m)
    m.close()


def generador_archivo_idioma(vector, fd, x):
    m = open(fd, 'wt')
    existen = False
    for a in range(len(vector)):
        if vector[a].idioma == x:
            linea = to_string(vector[a])
            m.write(linea + '\n')
            existen = True
    m.close()
    return existen
