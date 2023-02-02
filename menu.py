from laclase import *
from tp3 import *

def nuevo_por_precio(v,n):
    for posi in range(len(v)-1):
        for posi2 in range(posi+1,len(v)):
            if v[posi].precio > v[posi2].precio:
                v[posi],v[posi2]=v[posi2],v[posi]
    for posi in range(n):
            if v[posi].estado==1:
                write(v[posi])

def menu(v,n):

    print(
        "1)    Nuevo por precio\n"
        "2)    Usados por calificación\n"
        "3)    Distribución geográfica:\n"
        "4)    Total provincial:\n"
        "5)    Precio promedio de usados:\n"
        "6)    Compra ideal:\n"
        "7)    Comprar:\n"
    )
    menu=int(input())
    if menu==1:
        nuevo_por_precio(v,n)



