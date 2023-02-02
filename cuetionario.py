print('Determinacion del mayor de una sucesion (variante: may inicializada en 0)...')
n = int(input('Ingrese n: '))

may = 0
for i in range(1, n+1):
    num = int(input('Numero: '))
    if num > may:
        may = num

print('El mayor es:', may)
