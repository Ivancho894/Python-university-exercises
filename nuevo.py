import random
import pickle
import os.path
import os
from registros import *
def validador(texto, inf, sup):
    # funcion para numero mayor que:
    if sup == None:
        num = int(input(str(texto) + "(numero mayor que " + str(inf) + "):"))
        while num <= inf:
            num = int(input("INVALIDO! " + str(texto) + "(numero mayor que " + str(inf) + "):"))
    # funcion para numero entre
    else:
        num = int(input(str(texto) + "(numero entre " + str(inf) + " y " + str(sup) + "):"))
        while num < inf or num > sup:
            num = int(input("INVALIDO! " + str(texto) + " (numero entre " + str(inf) + " y " + str(sup) + "):"))
    return num
def generador(v):
    for posi in range(len(v)):
        cp = random.randint(0, 100000)
        p = random.randint(0, 10000)
        provincias = ["Buenos Aires", "Catamarca", "Chaco", "Chubut", "Cordoba", "Corrientes", "Entre Rios", "Formosa",
                  "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquen", "Rio Negro", "Salta", "San Juan",
                  "San Luis", "Santa Cruz", "Santa Fe", "Santiago Del Estero",
                  "Tierra Del Fuego", "Tucuman"]
        ug = provincias[random.randrange(len(provincias))]
        estados = ["Nuevo", "Usado"]
        e = estados[random.randrange(len(estados))]
        cd = random.randint(1, 100)
        pde = random.randint(1, 5)
        v[posi] = resultado(cp, p, ug, e, cd, pde)
def tres(v):
    primero=True
    for posi in range(len(v)):
        if primero:
            men=v[posi].precio
        if men>v[posi].precio:
            men=v[posi].precio
        if primero:
            max=v[posi].precio
            primero=False
        if max<v[posi].precio:
            max=v[posi].precio
    print('El rango es entre: ',men,'y',max)
    minimo=validador('Ingrese el minimo que desea gastar:',min,max-1)
    maximo=validador('Ingrese el maximo que desee gastar',minimo+1,max)
    for posi in range(len(v)):
        if v[posi].precio > minimo and v[posi].precio < maximo:
            write(producto)







def principal():
    men = True
    while men != False:
        n = validador("Ingrese cantidad de registros ", 0, None)
        v = [None] * n
        generador(v)
        tres(v)
principal()
