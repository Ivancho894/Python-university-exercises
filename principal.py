from registro import *
import random
import os
import pickle


def generador():
    nombres=['Ivan','Juan','Marcela','Gabriel','Paula','Cecilia','Mauro','Gonzalo']
    n=int(input('Ingrese la cantidad de registros que desea crear'))
    v=[]*n
    for posi in range(n):
        dni=random.randint(0,100)
        nombre=random.choice(nombres)
        importe=random.randint(1000,2000)
        tipo=random.randint(0,4)
        trabajo=random.randint(0,14)
        add_in_order(v,profesionales(dni,nombre,importe,tipo,trabajo))
    return v
def mostrar(v):
    for posi in range(len(v)):
        write(v[posi])
def add_in_order(v,add):
    n=len(v)
    izq,der=0,n-1
    posi=n
    while izq<=der:
        c=(izq+der)//2
        if v[c].dni==add.dni:
            posi=c
            break
        elif v[c].dni<add.dni:
            izq=c+1
        else:
            der=c-1
    if izq>der:
        posi=izq
    v[posi:posi]=[add]
def tres(v):
    m=open('profecionales.dat','wb')
    x=int(input('Ingrese el valor minimo a haber pagado'))
    for posi in range(len(v)):
        if v[posi].trabajo==3 or v[posi].trabajo==4 or v[posi].trabajo==5 and v[posi].importe>x:
            pickle.dump(v[posi],m)
    m.close()
def cuatro():
    m=open('profecionales.dat','rb')
    size=os.path.getsize('profecionales.dat')
    while m.tell()<size:
        x=pickle.load(m)
        write(x)
    m.close()
def cinco(v):
    seubico=False
    nom=input('Ingrese nombre a buscar')
    for posi in range(len(v)):
        if v[posi].nombre==nom:
            seubico=True
            break
    if seubico:
        print('Se encontro el nombre buscado:')
        write(v[posi])
    else:
        print('No se encontro el nombre buscado')
def seis(v):
    mat=[[0]*5 for df in range(15)]
    for posi in range(len(v)):
        mat[v[posi].trabajo][v[posi].tipo]+=1
    for posi in range(len(mat)):
        for posis in range(len(mat[0])):
            if mat[posi][posis]!=0:
                print('Tipo de afiliacion:',posi,'Tipo de trabajo:',posis,'Cantidad:',mat[posi][posis])



def menu():
    op=9
    while op!=0:
        print('1,2,3,4,5 o 6')
        op=int(input())
        if op==1:
            v=generador()
        if op==2:
            mostrar(v)
        if op==3:
            tres(v)
        if op==4:
            cuatro()
        if op==5:
            cinco(v)
        if op==6:
            seis(v)



def principal():
    v=menu()

principal()




