from registroEstudiante import *

def cargarVector(vec):
    for i in range(len(vec)):
        leg= int(input('Ingrese legajo: '))
        nom= input('Ingrese nombre: ')
        prom= int(input('Ingrese promedio:'))
        vec[i]=Estudiante(leg,nom,prom)

def mostrarVector(vec):
    print('Datos del vector')
    print('-----------------')
    for i in range(len(vec)):
        write(vec[i])

def ordenarPorLegajo(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1,n):
            if vec[i].legajo > vec[j].legajo:
                vec[i],vec[j] = vec[j],vec[i]

def listado(vec, x):
    for i in range(len(vec)):
        if vec[i].promedio >= x:
            write(vec[i])

def cambiarPromedio(vec,nom):
    ban = False
    for i in range(len(vec)):
        if vec[i].nombre == nom:
            vec[i].promedio = 7
            write(vec[i])
            ban=True
    if ban==False:
        print('Alumno no existe')

def buscarPrimerPromedio(vec,p):
    ban = False
    for i in range(len(vec)):
        if vec[i].promedio == p:
            write(vec[i])
            ban=True
            break
    if ban==False:
        print('Alumno no existe')

def test():

    n= int(input('Ingrese cantidad de estudiantes: '))
    v= [None] * n
    cargarVector(v)
    mostrarVector(v)
    # Ordenamos el vector de menor a mayor por el campo legajo
    ordenarPorLegajo(v)
    # Alumnos con promedio >= x, ordenado de menor a mayor por legajo
    listado(v, 8)
    # Cambiar promedio
    nom= input('Ingrese el nombre de los alumnos a los que se debe cambiar el promedio: ')
    cambiarPromedio(v,nom)
    # Primer alumno con promedio p
    p=input('Ingrese promedio del alumno a buscar: ')
    buscarPrimerPromedio(v,p)

test()
