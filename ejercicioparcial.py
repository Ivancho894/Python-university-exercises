from ejercicio_tipo_parcial import *
import random
def validar(x):
    while x<=0:
        x=int(input("ingrese un valor mayor a 0"))
    return x
def entre(x):
    while x<=0 or x>19:
        x=int(input("por favor ingrese un numero entre 0 y 19"))
    return x
def cargarv(v):
    for posi in range(len(v)):
        numip=int(input("Numero de identificacion del paquete:"))
        numip=validar(numip)
        des=input("Descripcion del paquete: ")
        tipo=int(input("Tipos de pasajes: "))
        tipo=entre(tipo)
        dias=int(input("Cantidad de dias: "))
        dias=validar(dias)
        impo=int(input("Importe: "))
        v[posi]=agencia(numip,des,tipo,dias,impo)
    return v
def aleatorio(v):
    for posi in range(len(v)):
        numip=random.randint(1000,100001)
        des=random.randint(0,12)
        tipo=random.randint(0,20)
        dias=random.randint(3,20)
        impo=random.randint(500,100001)
        v[posi]=agencia(numip,des,tipo,dias,impo)
def mostrarvector(v):
    print('Datos del vector')
    for posi in range(len(v)):
        write(v[posi])
def ordenarvector(v):
    for posi in range(len(v)-1):
        for posi1 in range(posi+1,len(v)):
            if v[posi].descripcion>v[posi1].descripcion:
                v[posi],v[posi1]=v[posi1],v[posi]
def cantidad(v):
    cant=[0]*20
    for posi in range(len(v)):
        cant[v[posi].tipodepa]=+1
    return cant
def item4(v,x,t):
    ban=False
    for posi in range(len(v)):
        if v[posi].numeroip==x and v[posi].importe:
            write(v[posi])
            ban=True
            break
def test():
    x=9
    while x!=0:
        print("0.Salir\n"
              "1.Cargado manual\n"
              "2.Cargado automatico")
        x=input()
        if x==1:
            n=int(input("Ingrese la cantidad de pasajes que desea ingresar: "))
            v=[None]*n
            cargarv(v)
            mostrarvector(v)
            print("Ordenado:")
            ordenarvector(v)
            mostrarvector(v)
        else:
            n=int(input("Ingrese la cantidad de pasajes que desea ingresar: "))
            v=[None]*n
            aleatorio(v)
            mostrarvector(v)
            ordenarvector(v)
            mostrarvector(v)
            cant=cantidad(v)
            print(cant)
test()

