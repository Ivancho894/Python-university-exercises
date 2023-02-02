import pickle
import random
from regggistros import *
from datetime import date


def validar(texto, inf, sup):
    # funcion para numero mayor que:
    if sup == None:
        num = int(input(str(texto) + " (numero mayor que " + str(inf) + "): "))
        while num <= inf:
            num = int(input("INVALIDO! " + str(texto) + " (numero mayor que " + str(inf) + "): "))
    # funcion para numero entre
    else:
        num = int(input(str(texto) + "(numero entre " + str(inf) + " y " + str(sup) + "): "))
        while num < inf or num > sup:
            num = int(input("INVALIDO! " + str(texto) + " (numero entre " + str(inf) + " y " + str(sup) + "): "))
    return num


def menu():
    print("1. Comprar")
    print("2. Mis compras")
    print("3. Rango de precios")
    print("4. Agregar favorito")
    print("5. Actualizar favorito")
    print("6. Salir")
    opcion = validar("Ingresar opción: ", 1, 6)
    return opcion


def add_in_order_bin(v, articulo):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der)//2
        if v[c].codigo == articulo.codigo:
            pos = c
            break
        if v[c].codigo < articulo.codigo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [articulo]


def generador():
    n = validar("Ingrese cantidad de registros ", 0, None)
    v = []
    for i in range(n):
        cp = random.randint(0, 100000)
        p = random.randint(0, 10000)
        provincias = ["Buenos Aires", "Catamarca", "Chaco", "Chubut", "Cordoba", "Corrientes", "Entre Rios", "Formosa",
                      "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquen", "Rio Negro", "Salta",
                      "San Juan",
                      "San Luis", "Santa Cruz", "Santa Fe", "Santiago Del Estero",
                      "Tierra Del Fuego", "Tucuman"]
        ug = random.choice(provincias)
        estados = ["Nuevo", "Usado"]
        e = random.choice(estados)
        cd = random.randint(1, 100)
        pde = random.randint(1, 5)
        articulo = resultado(cp, p, ug, e, cd, pde)
        add_in_order_bin(v, articulo)
    return v


def ordenar(vector, cat):
    for posi in range(len(vector) - 1):
        for posi2 in range(posi + 1, len(vector)):
            if vector[posi].__dict__[cat] > vector[posi2].__dict__[cat]:
                vector[posi], vector[posi2] = vector[posi2], vector[posi]


def mostrarv(v):
    for posi in range(len(v)):
        write(v[posi])
        print("-" * 170)


def busqueda_binaria(v, codigo):
    n = len(v)
    izq, der = 0, n-1
    posi = -1
    while izq <= der:
        c = (izq + der)//2
        if v[c].codigo == codigo:
            posi = c
        if v[c].codigo < codigo:
            izq = c + 1
        else:
            der = c - 1
    return posi



def tres(v):
    primero = True
    n = len(v)
    for i in range(n):
        if primero:
            men = v[i].precio
        if men > v[i].precio:
            men = v[i].precio
        if primero:
            maxi = v[i].precio
            primero = False
        if maxi < v[i].precio:
            maxi = v[i].precio
    print('El rango es entre: ', men, 'y', maxi)
    minimo = validar('Ingrese el minimo que desea gastar:', men, maxi - 1)
    maximo = validar('Ingrese el maximo que desee gastar', minimo + 1, maxi)
    for i in range(n):
        if v[i].precio >= minimo and v[i].precio <= maximo:
            write(v[i])
            print("-" * 170)
def cinco(v,fav):
    codigo = int(input("Ingresar codigo a buscar: "))
    posi = busqueda_binaria(v, codigo)
    if posi==-1:
        op=validar('El codigo ingresado no se encontro.\n1.Volver al menu.\n2.Volver a buscar el codigo.\n',1,2)
        if op==2:
            fav=cinco(v,fav)
            return fav
        else:
            if fav:
                print("-"*170)
                print('Lista de favoritos:')
                mostrarv(fav)
            return fav
    else:
        verificacion=busqueda_binaria(fav,codigo)
        if verificacion==-1:
            print("-"*170)
            add_in_order_bin(fav, v[posi])
            print('Publicacion guardada en favoritos:')
            write(v[posi])
        else :
            op=validar('El codigo ingresado ya existe.\n1.Volver al menu.\n2.Volver a buscar el codigo.\n',1,2)
            if op==1:
                if fav:
                    print("-"*170)
                    print('Lista de favoritos:')
                    mostrarv(fav)
                return fav
            else:
                fav=cinco(v,fav)
                return fav
    op=validar('1.Volver al menu.\n2.Ingresar otro favorito.\n',1,2)
    if op == 2:
        fav=cinco(v,fav)
        return fav
    else:
        if fav:
            print("-"*170)
            print('Lista de favoritos:')
            mostrarv(fav)
        return fav


def cuaatro(v, fav):
    codigo = int(input("Ingresar codigo para agregar a favoritos: "))
    posi = busqueda_binaria(v, codigo)
    while posi == -1:
        op=validar('El codigo ingresado no se encontro.\n1. Volver al menu.\n2. Agregar otro articulo.\n',1,2)
        if op == 1:
            if not fav: #Esto comprueba si la lista de favoritos esta vacia
                print("-"*170)
                print("La lista de favoritos esta vacia")
                print("-"*170)
            else:
                print("-"*170)
                mostrarv(fav)
            return
        else:
            cuatro(v, fav)
    verificacion = busqueda_binaria(fav, codigo)
    if verificacion == -1:
        print("Publicacion guardada en favoritos: ")
        write(v[posi])
        add_in_order_bin(fav, v[posi])
        print("-"*170)
    else:
        print("El codigo ya existe en favoritos.\n")
    op=validar('1. Volver al menu.\n2. Agregar otro articulo.\n',1,2)
    if op == 1:
        if not fav: #Esto comprueba si la lista de favoritos esta vacia
            print("-"*170)
            print("La lista de favoritos esta vacia")
        else:
            print("-"*170)
            print("Listado de favoritos agregados: ")
            mostrarv(fav)
        return
    else:
        cuatro(v, fav)

def principal():
    fav=[]
    v = generador()
    ordenar(v, "codigo")
    mostrarv(v)

    op = -1
    while op != 6:

        if op == 1:
            codigo = int(input("Ingresar codigo a buscar: "))
            posi = busqueda_binaria(v, codigo)
            if posi == -1:
                print("El articulo buscado no existe")
            else:
                #valido que haya esa cantidad
                disponible = v[posi].cantidad_disponible
                cant = validar("Ingrese la cantidad de articulos que desea adquirir", 0, disponible)
                print("Desea confirmar la compra de", cant, "articulos?")
                print("1.Aceptar")
                print("2.Rechazar")
                confirm = validar("Ingresar opción seleccionada", 1, 2)
                if confirm == 2:
                    break
                else:
                    v[posi].cantidad_disponible -= cant
                    #Consultar al usuario si desea envío a domicilio (costo 10% de la compra) o retira en sucursal
                    print("Como desea recibir el articulo?")
                    print("1. Envío a domicilio (10% del costo de la compra)")
                    print("2. Retirar en sucursal")
                    retiro = validar("Ingresar opción seleccionada", 1, 2)
                    monto = v[posi].precio*cant
                    envio = 0
                    if retiro == 1:
                        envio = monto*10/100
                        monto += envio
                    fd = "miscompras.dat"
                    m = open(fd, "wb")
                    hoy = date.today()
                    if envio:
                        artic = compras(codigo, cant, v[posi].precio, envio, monto, hoy)
                        pickle.dump(artic, m)
                    else:
                        artic = compras(codigo, cant, v[posi].precio, envio, monto, hoy)
                        pickle.dump(artic, m)
                    m.close()
        elif op == 2:
            m = open("miscompras.dat", "rb")
            fechai = pickle.load(m)
            fechas = int(input("Seleccione un rango de fechas desde el" + str(fechai.fecha) + " hasta hoy."))
            for i in range(fechai,):
                i = pickle.load(m)
                write2(i)
            m.close()
        elif op == 3:
            tres(v)
        elif op == 4:
            fav=cinco(v,fav)
        else:
            pass

        op = menu()

    print("BYE BYE")


principal()
