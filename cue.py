# asuma que la variable descripcion es una variable global 
# correctamente definida como una tupla de esta forma:
descripcion = 'Piedra', 'Papel', 'Tijera'

humano = int(input('Ingrese 1 - Piedra, 2 - Papel o 3 - Tijera: '))
print('Usted eligio:', descripcion[humano])
