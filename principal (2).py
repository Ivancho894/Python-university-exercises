from archivo import *
from registro import *


def validar(inf, sup, mensaje):
    n = int(input(str(mensaje)))
    if sup is None:
        while n <= 0:
            n = int(input('Igresaste un numero menor o igual a 0, ingresa otro'))
        return n
    else:
        while inf > n or sup < n:
            n = int(input('Ingresaste un numero menor a ' + str(inf) + ' o superior a ' + str(sup)))
    return n


def add_in_order(v, add):
    n = len(v)
    izq, der = 0, n - 1
    pos = n
    while izq <= der:
        c = (der + izq) // 2
        if v[c].titulo == add.titulo:
            pos = c
            break
        elif v[c].titulo < add.titulo:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    v[pos:pos] = [add]
    return v


def generar_vector(fd):
    v = []
    m = open(fd, 'rb')
    size = os.path.getsize(fd)
    while m.tell() < size:
        x = pickle.load(m)
        v = add_in_order(v, x)
    m.close()
    return v


def mostrar_vector(vector):
    for a in range(len(vector)):
        write(vector[a])


def vector_peliculas_genero(vector, n, g):
    pelis= []
    completo = False
    aux = 0
    for a in range(len(vector)):
        if vector[a].genero == g:
            aux += 1
            pelis.append(vector[a])
            if aux == n:
                completo = True
                break
    return completo, pelis


def generar_matriz():
    mat = [[0] * 6 for a in range(5)]
    return mat


def cargar_matriz(vector, mat):
    for a in range(len(vector)):
        mat[vector[a].idioma][vector[a].genero] += 1


def total_fila(mat):
    fila = validar(1, 5, 'Ingrese el idioma que desea buscar (1-Español, 2-Ingles, 3-Frances, 4-Portugues, 5-Otros)')
    fila -= 1
    total = 0
    for a in range(6):
        total += mat[fila][a]
    return total, fila


def mostrar_matriz(mat):
    for posi in range(len(mat)):
        for pos in range(len(mat[0])):
            if mat[posi][pos] != 0:
                print('Idioma:', leng[posi], ', Genero:', gen[pos], ':', mat[posi][pos])


def buscar_titulo(v, x):
    n = len(v)
    izq, der = 0, n - 1
    while izq <= der:
        c = (der + izq) // 2
        if v[c].titulo == x:
            return c
        elif v[c].titulo < x:
            izq = c + 1
        else:
            der = c - 1
    return -1


def menu():
    print('-' * 60)
    print('Opciones: ')
    print('\t 0) Salir')
    print('\t 1) Generar y mostrar vector')
    print('\t 2) Lista de n peliculas de g genero')
    print('\t 3) Determinar la cantidad de peliculas por genero y por idioma (Matriz)')
    print('\t 4) A partir de la Matriz determinar la cantidad de peliculas de idioma i')
    print('\t 5) Buscar una pelicula con el titulo x')
    print('\t 6) Generar archivo con peliculas de idioma x')
    print('-' * 60)
    print(' ')
    opcion = validar(0, 6, 'Opcion: ')
    print('-' * 60)
    return opcion


def test():
    fd = 'peliculas.dat'
    print('----------')
    print('Bienvenido')
    print('----------')
    print(' ')
    cant_peliculas = validar(0, None, 'Ingrese la cantidad de peliculas que desea cargar: ')
    generador(cant_peliculas, fd)
    vector_peliculas = []
    op = menu()
    cargado = False
    carada_matriz = False
    while op != 0:
        if op == 1:
            vector_peliculas = generar_vector(fd)
            mostrar_vector(vector_peliculas)
            cargado = True

        elif op == 2:
            if not cargado:
                vector_peliculas = generar_vector(fd)
            n = validar(0, None, 'Ingrese la cantidad de peliculas que desea cargar')
            g = validar(1, 6,
                        'Ingrese el genero que desea buscar (1-Infantil, 2-Comedia, 3-Romantico, 4-Drama, 5-Ciencia Ficcion, 6-Otros)')
            g -= 1
            completo, vector_genero = vector_peliculas_genero(vector_peliculas, n, g)
            if not completo:
                print('No hay suficientes peliculas')
            mostrar_vector(vector_genero)
        elif op == 3:
            if not cargado:
                vector_peliculas = generar_vector(fd)
            mat = generar_matriz()
            cargar_matriz(vector_peliculas, mat)
            mostrar_matriz(mat)
            carada_matriz = True
        elif op == 4:
            if carada_matriz:
                a, i = total_fila(mat)
                print(leng[i], ': ', a)
            else:
                if not cargado:
                    vector_peliculas = generar_vector(fd)
                mat = generar_matriz()
                cargar_matriz(vector_peliculas, mat)
                a, i = total_fila(mat)
                print(leng[i], ': ', a)

        elif op == 5:
            if not cargado:
                vector_peliculas = generar_vector(fd)
            x = validar(1, 7,
                        'Ingrese el titulo: (1-Capitan America, 2-El Hombre Araña, 3-Iron Man, 4-Los Ilusionistas, 5-Star Wars, 6-Titanic, 7-Volver al Futuro)')
            pos = buscar_titulo(vector_peliculas, x - 1)
            if pos == -1:
                print('No existe pelicula con ese titulo')
            else:
                print('Se encontro la siguiente pelicula:')
                write(vector_peliculas[pos])
        elif op == 6:
            if not cargado:
                vector_peliculas = generar_vector(fd)
            x = validar(1, 5,
                        'Ingrese el idioma que desea buscar (1-Español, 2-Ingles, 3-Frances, 4-Portugues, 5-Otros)')
            x -= 1
            fd2 = 'PeliculasIdioma' + str(leng[x]) + '.txt'
            res = generador_archivo_idioma(vector_peliculas, fd2, x)
            if res:
                print('Archivo Generado con Exito !')
            else:
                print('No existen peliculas con ese Idioma')
        elif op == 0:
            print("Chau")
            pass
        op = menu()


test()
