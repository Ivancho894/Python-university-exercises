from regi import *
import random
import pickle
import os

def generador():
    nombres=['Ivan','Juan','Marcela','Gabriel','Paula','Cecilia','Mauro','Gonzalo']
    n=int(input('Numero de registros'))
    v=[]*n
    for posi in range(n):
        id=random.randint(0,100)
        titulo=random.choice(nombres)
        importe=random.randint(0,10000)
        tipo=random.randint(0,9)
        pais=random.randint(0,19)
        add_in_order(v,cine(id,titulo,importe,tipo,pais))
    return v

def add_in_order(v,add):
    n=len(v)
    izq,der=0,n-1
    posi=n
    while izq<=der:
        c=(izq+der)//2
        if v[c].titulo==add.titulo:
            posi=c
            break
        elif v[c].titulo<add.titulo:
            izq=c+1
        else:
            der=c-1
    if izq>der:
        posi=izq
    v[posi:posi]=[add]
def mos(v):
    for posi in range(len(v)):
        write(v[posi])
def archivo(v):
    m=open('cac.dat','wb')
    x=int(input('dsfsd'))
    for posi in range(len(v)):
        if v[posi].pais!=10 and v[posi].importe>x:
            pickle.dump(v[posi],m)
    m.close()
    m=open('cac.dat','rb')
    size=os.path.getsize('cac.dat')
    while m.tell()<size:
        x=pickle.load(m)
        write(x)
    m.close()
def v(v):
    mat=[[0]*10 for a in range(20)]
    for posi in range(len(v)):
        mat[v[posi].pais][v[posi].tipo]+=1
    for posi in range(len(mat)):
        for posis in range(len(mat[0])):
            if mat[posi][posis]!=0:
                print('Pais:',posi,'Tipo de peli:',posis,mat[posi][posis])
v=generador()
mos(v)
v(v)
