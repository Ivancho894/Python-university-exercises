import random
from registros import *


def mayorque0(x):
    while x <= 0:
        x = int(input("Ingrese un numero mayor a 0: "))
    return x


def generador(v):
    for posi in range(len(v)):
        cp = random.randint(0, 100000)
        p = random.randint(0, 10000)
        ug = random.randint(1, 23)
        e = random.randint(0, 1)
        cd = random.randint(0, 100)
        pde = random.randint(1, 5)
        v[posi] = resultado(cp, p, ug, e, cd, pde)
""""hacer una tabla por ubicacio, tiene que mostrar la cantidad de articulos disponibles por puntuacipon"""
def mostrarv(v):
    for posi in range(len(v)):
        write(v[posi])

def uno(v):
    vector = []
    for posi in range(len(v)):
        if v[posi].estado == 1:
            vector.append(v[posi])
    for posi in range(len(vector) - 1):
        for posi2 in range(posi + 1, len(vector)):
            if vector[posi].precio > vector[posi2].precio:
                vector[posi], vector[posi2] = vector[posi2], vector[posi]
    for posi in range(len(vector)):
        write(vector[posi])


def dos(v):
    a = [0] * 5
    for posi in range(len(v)):
        if v[posi].estado == 0:

            a = [0] * 23
            for posi in range(len(v)):
                a[v[posi].ubicacion_geografica] += 1
            a[v[posi].calificacion - 1] += 1
    print("Usados por calificacion:\nVendedores con 1 punto: ", a[0], "\nVendedores con 2 puntos: ", a[1],
          "\nVendedores con 3 puntos: ", a[2], "\nVendedores con 4 puntos: ", a[3], "\nVendedores con 5 puntos: ", a[4])

def tres(v):
    provincias = [0] * 23
    calificacionezs = [0]

    for posi in range(len(v)):
        provincias[v[posi].ubicacion_geografica - 1] += 1

def cuatro(v):
    pass

def cinco(v):
    total = 0
    cant = 0
    for posi in range(len(v)):
        if v[posi].estado == 0:
            cant += 1
            total += v[posi].precio
            write(v[posi])
    promedio = round(total / cant, 2)

    print("\nPromedio del precio de los usados: $"+str(promedio))


def seis(v):
    primero = True
    numeroideal=0
    for posi in range(len(v)):
        if v[posi].estado == 1:
            if v[posi].calificacion > 1:
                if primero:
                    primero = False
                    ideal = v[posi].precio
                    numeroideal=posi
                elif v[posi].precio < ideal:
                    ideal = v[posi].precio
                    numeroideal=posi

    write(v[numeroideal])

def siete(v):
    band = False
    busqueda = int(input("Ingrese codigo a buscar:"))
    for posi in range(len(v)):
        if v[posi].codigo == busqueda:
            write(v[posi])
            band = True
            cant = int(input("Cuantos articulos desea comprar: "))
            cant = mayorque0(cant)
            while cant > v[posi].cantidad_disponible:
                print("La cantidad que solicito es mayor que la disponible.")
                cant = int(input("Cuantos articulos desea comprar: "))
                cant = mayorque0(cant)

            print("Desea realizar la compra:\n"
                  "1- Aceptar\n"
                  "2- Rechazar")
            op = input("Ingrese una opcion: ")
            while op != "1" and op != "2":
                op = input("INVALIDO! Ingrese una opcion correcta: ")
            if op == "1":
                print("Su compra del articulo con codigo", busqueda,"por $" + str(v[posi].precio), "fue realizada con exito." )
            else:
                print("Su compra a sido rechazada.")
    if not band:
        print("No existe el codigo ingresado.")



def menu(v):
    print(
        "1) Nuevo por precio\n"
        "2) Usados por calificación\n"
        "3) Distribución geográfica:\n"
        "4) Total provincial:\n"
        "5) Precio promedio de usados:\n"
        "6) Compra ideal:\n"
        "7) Comprar:\n"
    )
    menu = int(input())
    if menu == 1:
        uno(v)
    if menu == 2:
        dos(v)
    if menu == 3:
        tres(v)
    if menu == 4:
        cuatro(v)
    if menu == 5:
        cinco(v)
    if menu == 6:
        seis(v)
    if menu == 7:
        siete(v)

def principal():

    n = 0
    while n != -1:
        n = int(input("\nIngrese un numero mayor a 0 de cantidad de registros: "))
        n = mayorque0(n)
        v = [None] * n
        generador(v)
        mostrarv(v)
        menu(v)


principal()
