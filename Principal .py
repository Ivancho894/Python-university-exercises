import pickle
import random
from regggistros import *
from datetime import timedelta, datetime
import os

def title(titulo, color, tamaño):
    class c(object):
        rojo = "\033[91m"
        azul = '\033[94m'
        grande = [170, 90]
        mediano = [90, 50]
    espacio = '{:>'+ str(c.__dict__[tamaño][1]) +'}'
    negrita = '\033[1m'
    fin = '\033[0m'

    print(c.__dict__[color] + negrita + "=" * c.__dict__[tamaño][0])
    print(espacio.format(str(titulo.upper())))
    print("=" * c.__dict__[tamaño][0] + fin)


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
    title("Menu", "rojo", "mediano")
    print("1. Comprar")
    print("2. Mis compras")
    print("3. Rango de precios")
    print("4. Agregar favorito")
    print("5. Actualizar favorito")
    print("6. Salir")
    opcion = validar("Ingresar opción: ", 1, 6)
    return opcion


def bin(v, codigo, articulo):
    n = len(v)
    pos = -1
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der)//2
        if v[c].codigo == codigo:
            pos = c
            break
        if v[c].codigo < codigo:
            izq = c + 1
        else:
            der = c - 1
    if articulo != None:
        if izq > der:
            pos = izq
        v[pos:pos] = [articulo]
    else:
        return pos


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
        bin(v, articulo.codigo, articulo)
    return v


def mostrarv(v):
    for posi in range(len(v)):
        write(v[posi])
        print("-" * 170)


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
    minimo = validar('Ingrese el minimo que desea gastar:', men, maxi)
    maximo = validar('Ingrese el maximo que desee gastar', minimo, maxi)
    for i in range(n):
        if v[i].precio >= minimo and v[i].precio <= maximo:
            write(v[i])
            print("-" * 170)


def generar_y_mostrar_archivo_txt(fd, res):
    m = open(fd, "w+t")
    m.write("-" * 47 + "\n")
    m.write("Compra #" + str(res.codigo) + " - " + str(res.fecha.day) + "/" + str(res.fecha.month) + "/" + str(res.fecha.year) + "\n")
    m.write("Resumen de compra\n")
    m.write("Articulo: " + str(res.codigo) + "  $" + str(res.cantidad * res.precio) + " (" + str(res.cantidad) + " x $" + str(
        res.precio) + ")\n")
    if res.envio == 0:
        m.write("Retira en sucursal\n")
    else:
        m.write("Cargo de envío $" + str(res.envio) + "\n")
    m.write("Tu pago $" + str(res.monto) + "\n")
    m.write("-" * 47 + "\n")
    #Apunto al inicio del archivo el puntero para leerlo
    m.seek(0)
    todo = m.read()
    print(todo)
    m.close()


def generar_archivo_bin(fd, articulo):
    m = open(fd, "ab")
    pickle.dump(articulo, m)
    m.close()


def mostrar_archivo(fd,desde,hasta):
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    hay = False
    while m.tell() < t:
        a = pickle.load(m)
        if desde <= a.fecha and a.fecha <= hasta:
            hay = True
            write2(a)
    if not hay:
        print("En ese rango de fechas no realizó ninguna compra.")
    m.close()


def buscar_en_archivo(codigo, fd):
    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    while m.tell() < t:
        art = pickle.load(m)
        if art.codigo == codigo:
            return 1
    return -1


def cuatro(v,fav):
    codigo = int(input("Ingresar codigo a buscar: "))
    posi = bin(v, codigo, None)
    if posi==-1:
        op=validar('El codigo ingresado no se encontro.\n1.Volver al menu.\n2.Volver a buscar el codigo.\n',1,2)
        if op==2:
            fav=cuatro(v,fav)
            return fav
        else:
            if fav:
                print("-"*170)
                print('Lista de favoritos:')
                mostrarv(fav)
            return fav
    else:
        verificacion= bin(fav,codigo, None)
        if verificacion==-1:
            print("-"*170)
            bin(fav,v[posi].codigo, v[posi])
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
                fav=cuatro(v,fav)
                return fav
    op=validar('1.Volver al menu.\n2.Ingresar otro favorito.\n',1,2)
    if op == 2:
        fav=cuatro(v,fav)
        return fav
    else:
        if fav:
            print("-"*170)
            print('Lista de favoritos:')
            mostrarv(fav)
        return fav


def cinco(fav):
    dat = True
    fd = 'favoritos.dat'
    if os.path.exists(fd):
        if fav:
            #El archivo existe
            m = open(fd, 'a+b')
            for i in range(len(fav)):
                existe = buscar_en_archivo(fav[i].codigo,fd)
                if existe == -1:
                    pickle.dump(fav[i], m)
            print("Se actualizo la lista de favoritos con exito.")
        else:
            print("\nNo se agregaron articulos a la lista.")
    else:
        if fav:
            #El archivo no existe, lo creo
            m = open(fd, 'a+b')
            for i in range(len(fav)):
                pickle.dump(fav[i], m)
            m.close()
            print("\nSe actualizo la lista de favoritos con exito.")
        else:
            dat = False
            print("\nNo hay nuevos favoritos para actualizar.")
    if dat:
        m = open(fd, 'rb')
        t = os.path.getsize(fd)
        print('Se recuperaron estos articulos desde el archivo', fd, ':')
        while m.tell() < t:
            art = pickle.load(m)
            write(art)
        m.close()
    else:
        print("No se han guardado favoritos con anterioridad.")
    print("-"*170)


def uno(v):
    codigo = int(input("Ingresar codigo a buscar: "))
    posi = bin(v, codigo, None)
    if posi == -1:
        print("El articulo buscado no existe")
    else:
        # valido que haya esa cantidad
        disponible = v[posi].cantidad_disponible
        if disponible == 0:
            print("No quedan articulos disponibles de dicho producto, vuelva a intentar más tarde.")
        else:
            cant = validar("Ingrese la cantidad de articulos que desea adquirir", 0, disponible)
            print("Desea confirmar la compra de", cant, "articulos?")
            print("1.Aceptar")
            print("2.Rechazar")
            confirm = validar("Ingresar opción seleccionada", 1, 2)
            if confirm == 2:
                print("Se rechazó correctamente")
            else:
                v[posi].cantidad_disponible -= cant
                # Consultar al usuario si desea envío a domicilio (costo 10% de la compra) o retira en sucursal
                print("Como desea recibir el articulo?")
                print("1. Envío a domicilio (10% del costo de la compra)")
                print("2. Retirar en sucursal")
                retiro = validar("Ingresar opción seleccionada", 1, 2)
                monto = v[posi].precio * cant
                envio = 0
                if retiro == 1:
                    envio = monto * 10 / 100
                    monto += envio
                hoy = datetime.now()
                fecha_aleatoria = hoy + timedelta(days=random.randint(-3570, 0))
                artic = compras(codigo, cant, v[posi].precio, envio, monto, fecha_aleatoria)
                generar_archivo_bin("miscompras.dat", artic)
                # Ticket
                generar_y_mostrar_archivo_txt("compras.txt", artic)


def dos():
    if not os.path.exists("miscompras.dat"):
        print("No se ha registrado ninguna compra.")
    else:
        m = open("miscompras.dat", "rb")
        hoy = datetime.today()
        print("Seleccione un rango de fechas desde el " + str(1) + "/" + str(1) + "/" + str(2010) + " hasta hoy:")
        print("DESDE: ")
        desde_año = validar("Ingresar año", 2010, hoy.year)
        # Valido que cada input no pueda ser mayor a la fecha actual
        if desde_año == hoy.year:
            desde_mes = validar("Ingresar mes", 1, hoy.month)
        else:
            desde_mes = validar("Ingresar mes", 1, 12)
        if desde_año == hoy.year and desde_mes == hoy.month:
            desde_día = validar("Ingresar día", 1, hoy.day)
        else:
            desde_día = validar("Ingresar día", 1, 30)
        desde = datetime(desde_año, desde_mes, desde_día)
        print("HASTA:")
        hasta_año = validar("Ingresar año", desde.year, hoy.year)
        # En cada if valido que la fecha final del rango no pueda ser menor que la principal del rango.
        # A la vez valido que no pueda superar la fecha actual.
        if desde.year == hasta_año:
            if hasta_año == hoy.year:
                hasta_mes = validar("Ingresar mes", desde.month, hoy.month)
            else:
                hasta_mes = validar("Ingresar mes", desde.month, 12)
        else:
            if hasta_año == hoy.year:
                hasta_mes = validar("Ingresar mes", 1, hoy.month)
            else:
                hasta_mes = validar("Ingresar mes", 1, 12)
        if desde.year == hasta_año and desde.month == hasta_mes:
            if hasta_mes == hoy.month and desde_año == hoy.year:
                hasta_dia = validar("Ingresar día", desde.day, hoy.day)
            else:
                hasta_dia = validar("Ingresar día", desde.day, 30)
        else:
            if hasta_mes == hoy.month and hasta_año == hoy.year:
                hasta_dia = validar("Ingresar día", 1, hoy.day)
            else:
                hasta_dia = validar("Ingresar día", 1, 30)
        hasta = datetime(hasta_año, hasta_mes, hasta_dia)
        mostrar_archivo("miscompras.dat", desde, hasta)
        m.close()


def principal():
    title("Mercado Libre", 'azul', "grande")
    v = generador()
    mostrarv(v)
    fav = []
    op = -1
    while op != 6:
        if op == 1:
            title("Comprar", "azul", "mediano")
            uno(v)
            print()
        elif op == 2:
            title("Mis Compras", "azul", "mediano")
            dos()
            print()
        elif op == 3:
            title("Rango De Precios", "azul", "mediano")
            tres(v)
            print()
        elif op == 4:
            title("Agregar Favorito", "azul", "mediano")
            fav=cuatro(v, fav)
            print()
        elif op == 5:
            title("Actualizar Favorito", "azul", "mediano")
            cinco(fav)
            print()
        print()
        op = menu()
    title("¡Gracias por utilizar MERCADO LIBRE!", "azul", "grande")


principal()
