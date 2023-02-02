from registrosestudiantes import *

def cargarvector(v):
    for posi in range(len(v)):
        nom=input('Ingrese nombre:')
        leg=int(input('Ingrese legajo de '+str(nom)+':'))
        prom=int(input('Ingrese promedio de '+str(nom)+':'))
        print("\n")
        v[posi]=estudiante(leg,nom,prom)

def ordenarporlegajo(v):
    for posi in range(len(v)-1):
        for posi2 in range(posi+1,len(v)):
            if v[posi].legajo>v[posi2].legajo:
                v[posi],v[posi2]=v[posi2],v[posi]
def listado(v,x):
    print("Ordenado por legajo")
    for posi in range(len(v)):
        if v[posi].promedio>=x:
            write(v[posi])
def mostrarvector(v):
    print('Datos del vector')
    for posi in range(len(v)):
        write(v[posi])
def cambiarpromedio(v):
    x=input("\nIngrese estudiantes a modificar promedio: ")
    nocambio=True
    for posi in range(len(v)):
        if v[posi].nombre==x:
            v[posi].promedio=7
            write(v[posi])
            nocambio=False
            break
    if nocambio:
        print("no existe")
def buscarporpromedio(v):
    x=int(input("Ingrese promedio a buscar: "))
    nofound=True
    for posi in range(len(v)):
        if v[posi].promedio==x:
            write(v[posi])
            nofound=False
            break
    if nofound:
        print("No existe el alumno con ese promedio")
def test():
    n=int(input("Ingrese cantidad de estudiantes: "))
    v=[None] * n
    cargarvector(v)
    mostrarvector(v)
    ordenarporlegajo(v)
    listado(v,8)
    cambiarpromedio(v)
    buscarporpromedio(v)







test()
