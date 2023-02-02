import random   
jugador1=input('ingrese nombre jugador 1')
jugador2=input('ingrese nombre jugador 2')
tirar=input('tocar cualquier tecla para comenzar')
dado1=random.randrange(1,7)
dado2=random.randrange(1,7)
#proceso
suma=dado1+dado2
par=suma%2
print(jugador1,"sacó ",dado1,'\n// ,jugador2,"sacó ",dado2)
if par==0:
    j2=1
    print("ganó ",jugador2,"ya que ",suma," es par")
else:
    j1=1
    print("gano ",jugador1," ya que ", suma," es inpar")
