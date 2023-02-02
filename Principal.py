import random
from Registros import *




def title(titulo, color, cant_iguales, espacio):

    espacio = '{:>'+ str(espacio) +'}'
    #Colores
    rojo = "\033[91m"
    negrita = '\033[1m'
    azul = '\033[94m'
    fin = '\033[0m'
    if color == "r":
        print(rojo + negrita + "=" * cant_iguales)
        print(espacio.format(str(titulo.upper())))
        print("=" * cant_iguales + fin)
    if color == "a":
        print(azul + negrita + "=" * cant_iguales)
        print(espacio.format(str(titulo.upper())))
        print("=" * cant_iguales + fin)


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


def mostrarv(v):
    for posi in range(len(v)):
        write(v[posi])
        print("-"*170)


def ordenar(vector, cat):
    for posi in range(len(vector) - 1):
        for posi2 in range(posi + 1, len(vector)):
            if vector[posi].__dict__[cat] > vector[posi2].__dict__[cat]:
                vector[posi], vector[posi2] = vector[posi2], vector[posi]
def uno(v):
    vector = []
    for posi in range(len(v)):
        if v[posi].estado == "Nuevo":
            vector.append(v[posi])
    ordenar(v, "precio")
    for posi in range(len(vector)):
        write(vector[posi])


def dos(v):
    conteo = [0]*5
    for i in range(len(v)):
        if v[i].estado == 'Usado':

            conteo[v[i].calificacion-1] += v[i].cantidad_disponible
    for i in range(5):
        print("Articulos con " + str(i+1) + " puntos:", conteo[i])

def tres(v):
    pass
    mat = [["Provincia","*","**","***","****","*****"]]
    for i in range(len(v)):
        existe = False
        for pos in range(len(mat)):
            if mat[pos][0] == v[i].ubicacion_geografica:
                existe = True
                mat[pos][v[i].calificacion] += v[i].cantidad_disponible
        if not existe:
            mat.append([v[i].ubicacion_geografica, 0, 0, 0, 0, 0])
            mat[-1][v[i].calificacion] += v[i].cantidad_disponible
    #imprimir
    txt = "{:^100}".format("Se muestran unicamente las provincias que tengan articulos disponibles!")
    title(txt, "r", 120, 110)
    for posi in range(len(mat)):
        print('{:<40}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(mat[posi][0],mat[posi][1], mat[posi][2], mat[posi][3], mat[posi][4], mat[posi][5]))
    return mat


def cuatro(v):
    provincia_elegida = input("Ingrese el nombre de provicia cuya cantidad de articulos desee conocer: ")
    provincia_elegida = provincia_elegida.title()
    provincias = ["Buenos Aires", "Catamarca", "Chaco", "Chubut", "Cordoba", "Corrientes", "Entre Rios", "Formosa",
                  "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquen", "Rio Negro", "Salta", "San Juan",
                  "San Luis", "Santa Cruz", "Santa Fe", "Santiago Del Estero",
                  "Tierra Del Fuego", "Tucuman"]
    while provincia_elegida not in provincias:
        provincia_elegida = input("INVALIDO! Ingrese una provicia valida: ")
    mat = []
    hay_una = False
    for i in range(len(v)):
        existe = False
        if v[i].ubicacion_geografica == provincia_elegida:
            hay_una = True
            for pos in range(len(mat)):
                if mat[pos][0] == v[i].ubicacion_geografica:
                    existe = True
                    mat[pos][1] += v[i].cantidad_disponible
            if not existe:
                mat.append([v[i].ubicacion_geografica, v[i].cantidad_disponible])
    if hay_una:
        for posi in range(len(mat)):
            print("Cantidad disponible en "+str(mat[posi][0]) + ":", mat[posi][1])
    else:
        print("No hay articulos en la provincia buscada.")


def cinco(v):
    total = 0
    cant = 0
    for posi in range(len(v)):
        if v[posi].estado == "Usado":
            cant += 1
            total += v[posi].precio
            write(v[posi])
    promedio = round(total / cant, 2)

    print("\nPromedio del precio de los usados: $" + str(promedio))


def seis(v):
    primero = True
    numeroideal = 0
    for posi in range(len(v)):
        if v[posi].estado == "Nuevo":
            if v[posi].calificacion > 1:
                if primero:
                    primero = False
                    ideal = v[posi].precio
                    numeroideal = posi
                elif v[posi].precio < ideal:
                    ideal = v[posi].precio
                    numeroideal = posi

    write(v[numeroideal])


def siete(v):
    busqueda = int(input("Ingrese codigo a buscar:"))
    izq,der = 0, len(v)
    encontrado = False
    while izq <= der and not encontrado:
        c = (izq + der) // 2
        if v[c].codigo == busqueda:
            cant = validador("Cuantos articulos desea comprar ", 0, None)
            while cant > v[c].cantidad_disponible:
                print("La cantidad que solicito es mayor que la disponible.")
                cant = validador("Ingrese otra cantidad ", 0, None)

            print("Desea realizar la compra:\n"
                  "1- Aceptar\n"
                  "2- Rechazar")

            op = validador('Ingrese una opcion', 1, 2)
            if op == "1":
                print("Su compra del articulo con codigo", busqueda, "por $" + str(v[posi].precio) + " precio unitario y una cantidad de " + str(cant) + " articulos",
                      "fue realizada con exito.")
                v[c].cant_disponible -= 1
            else:
                print("Su compra a sido rechazada.")
            encontrado = True
        elif busqueda < v[c].codigo:
            der = c - 1
        elif busqueda > v[c].codigo:
            izq = c + 1
    if not encontrado:
        print("No existe el codigo ingresado.")






    '''for posi in range(len(v)):
        if v[posi].codigo == busqueda:
            write(v[posi])
            band = True
            cant = validador("Cuantos articulos desea comprar ", 0, None)
            while cant > v[posi].cantidad_disponible:
                print("La cantidad que solicito es mayor que la disponible.")
                cant = validador("Ingrese otra cantidad ", 0, None)

            print("Desea realizar la compra:\n"
                  "1- Aceptar\n"
                  "2- Rechazar")
            op = input("Ingrese una opcion: ")
            while op != "1" and op != "2":
                op = input("INVALIDO! Ingrese una opcion correcta: ")
            if op == "1":
                print("Su compra del articulo con codigo", busqueda, "por $" + str(v[posi].precio) + " precio unitario y una cantidad de " + str(cant) + " articulos",
                      "fue realizada con exito.")
            else:
                print("Su compra a sido rechazada.")
    if not band:
        print("No existe el codigo ingresado.")'''


def menu(v):
    menu = 0
    bandera = False
    while menu != 8 and not bandera:
        c = "\033[36m"
        f = '\033[0m'
        print(
            c + "1)" + f + "Nuevo por precio\n" +
            c + "2)" + f + "Usados por calificación\n" +
            c + "3)" + f + "Distribución geográfica\n" +
            c + "4)" + f + "Total provincial\n" +
            c + "5)" + f + "Precio promedio de usados\n" +
            c + "6)" + f + "Compra ideal\n" +
            c + "7)" + f + "Comprar\n" +
            c + "8)" + f + "Salir\n"
        )
        menu = validador("Ingrese una opcion del menu ", 1, 8)

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
        if menu == 8:
            title("Gracias por usar Mercado Libre!", "a", 70, 50)
            return False
        print(c + "\n1)" + f + " Continuar con la busqueda realizada")
        print(c + "2)" + f + " Realizar otra busqueda\n")
        opcion = validador("Ingrese una opcion ", 1, 2)
        if opcion == 2:
            return True

def tres(v):
    primero=True
    for posi in range(len(v)):
        if primero:
            men=v[posi].precio
        if men>v[posi].precio:
            men=v[posi].precio
        if primero:
            maxi=v[posi].precio
            primero=False
        if maxi<v[posi].precio:
            maxi=v[posi].precio
    print('El rango es entre: ',men,'y',maxi)
    minimo=validador('Ingrese el minimo que desea gastar:',men,maxi-1)
    maximo=validador('Ingrese el maximo que desee gastar',minimo+1,maxi)
    for posi in range(len(v)):
        if v[posi].precio > minimo and v[posi].precio < maximo:
            write(v[posi])

def principal():
    men = True
    while men != False:
        n = validador("Ingrese cantidad de registros ", 0, None)
        v = [None] * n
        generador(v)
        '''ordenar(v, "codigo")
        mostrarv(v)
        men = menu(v)'''
        tres(v)

principal()
