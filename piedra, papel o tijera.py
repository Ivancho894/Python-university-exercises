import random
valores=('piedra','papel','tijera')
num=int(input("Piedra(0), papel(1) o tijera(2)?"))
usuario=valores[num]
print('usuario elige: ',usuario)
pc=random.choice(valores)
print('la pc eligió: ',pc)
