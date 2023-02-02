def valores_entre(a,b,mensaje):
    valor = int(input(mensaje))
    while (valor < a or valor > b):
        print ('Error! El valor ingresado debe estar entre [',a,'-',b,']')
        valor = int(input(mensaje))
    return valor
def mayor_que(a, mensaje):
    valor = int(input(mensaje))
    while (valor <= a):
        print ('Error!')
        valor = int(input(mensaje))
    return valor

    fila1 = "{:<20} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format('Genero', 'Infantil', 'Comedia', 'Romantico', 'Drama','Ciencia Ficcion', 'Otros')
    print ('-' * 82)
    print (fila1)
    print ('-' * 82)
    print (' ')
    for a in range(len(mat)):
        fila = a
        pasa = total_fila(mat, fila)
        if (pasa > 0):
            pub = ""
            pub += '{:<21}'.format(leng[a])
            for b in range(6):
                pub += '{:<13}'.format(mat[fila][b])
            pub += ("\n")
            print(pub)
    print ('-' * 82)
