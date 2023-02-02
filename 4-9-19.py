from registros import *
import random

def mayorque0(x):
    while x<=0:
        x=int(input("Ingrese un numero mayor a 0:"))
    return x
def generador(v):
    nombres=('Ivan','Mauro','Gonza','Mati','Tomas','Lucho','Gaston')
    for posi in range(len(v)):
        nombre=random.choice(nombres)
        documento=random.randint(4000000,5000000)
        monto=random.randint(1234,12345)
        codigo=random.randint(0,9)
        v[posi]=alquiler(nombre,documento,monto,codigo)
def mostrar(v):
    for posi in range(len(v)):
        write(v[posi])
def uno(v):
    for posi in range(len(v)):
        if v[posi].codigo>9 or v[posi].codigo<0:
            write(v[posi])
            v[posi].codigo=int(input("ingreseun numero entre 0 y el 9"))
def dos(v):
    x=int(input("Ingrese un monto"))
    mayorque0(x)
    cantidad=0
    for posi in range(len(v)):
        if v[posi].monto>=x:
            cantidad+=1
    print("La cantidad de cabañas con un monto mayor a",x,"son: ",cantidad)
def tres(v):
    a=[0]*10
    for posi in range(len(v)):
        a[v[posi].codigo]+=v[posi].monto
    print("Monto para categoria 0: ",a[0])
    print("Monto para categoria 1: ",a[1])
    print("Monto para categoria 2: ",a[2])
    print("Monto para categoria 3: ",a[3])
    print("Monto para categoria 4: ",a[4])
    print("Monto para categoria 5: ",a[5])
    print("Monto para categoria 6: ",a[6])
    print("Monto para categoria 7: ",a[7])
    print("Monto para categoria 8: ",a[8])
    print("Monto para categoria 9: ",a[9])
def cuatro(v):
    for posi in range(len(v)):
        for posi2 in range(len(v)):
            if v[posi2].documento>v[posi].documento:
                v[posi],v[posi2]=v[posi2],v[posi]
    print("Ordenado por dni:")
    mostrar(v)
def cinco(v):
    l=[]
    primero=True
    for posi in range(len(v)):
        if primero:
            menor=v[posi].monto
            l.append(posi)
            primero=False
        elif v[posi].monto<menor:
            menor=v[posi].monto
    print("menor/es")
    print(menor)
    write(v[l[0]])
def menu(v):
    print("1.Comprobrar codigo de cabaña")
    print("2.Determinar cantidad de cabañas con un precio superior a x")
    print("3.Determinar y mostrar el monto de un tipo de cabaña")
    print("4.Mostrar datos en orden de mayor a menor por dni")
    print("5.Mostrar alquileres con el menor monto")
    m=int(input())
    if m==1:
        uno(v)
    if m==2:
        dos(v)
    if m==3:
        tres(v)
    if m==4:
        cuatro(v)
    if m==5:
        cinco(v)
def test():
    m=None
    while m!=0:
        n=int(input("Ingrese la cantidad de alquileres: "))
        n=mayorque0(n)
        v=[None]*n
        generador(v)
        mostrar(v)
        m=menu(v)
test()
