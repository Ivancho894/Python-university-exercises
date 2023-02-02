import random
dado1=random.randrange(0,7)
dado2=random.randrange(0,7)
dado3=random.randrange(0,7)
puntos=0
premio=0
#puntos por 1
if dado1==1:
    puntos=puntos+1
elif dado2==1:
    puntos=puntos+1
elif dado3==1:
    puntos=puntos+1
#puntos por 3
if dado1==3:
    puntos=puntos+2
elif dado2==3:
    puntos=puntos+2
elif dado3==3:
    puntos=puntos+2
#puntos por 5
if dado1==5:
    puntos=puntos+4
elif dado2==5:
    puntos=puntos+4
elif dado3==5:
    puntos=puntos+4
#si saca par
par1=dado1%2
par2=dado2%2
par3=dado3%2
par=par1+par2+par3
if par==0:
    premio=1
#proceso
puntos1=puntos
print("En el primer lanzamiento el jugador sacó:\nDado nro1: ",dado1,"\nDado nro2: ",dado2,"\nDado nro3: ",dado3,"\nEn total sumó: ",puntos)
#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
empezar=input("Presione enter para comenzar")
dado1=random.randrange(0,7)
dado2=random.randrange(0,7)
dado3=random.randrange(0,7)
#puntos por 1
if dado1==1:
    puntos=puntos+1
elif dado2==1:
    puntos=puntos+1
elif dado3==1:
    puntos=puntos+1
#puntos por 3
if dado1==3:
    puntos=puntos+2
elif dado2==3:
    puntos=puntos+2
elif dado3==3:
    puntos=puntos+2
#puntos por 5
if dado1==5:
    puntos=puntos+4
elif dado2==5:
    puntos=puntos+4
elif dado3==5:
    puntos=puntos+4
#si saca par
par1=dado1%2
par2=dado2%2
par3=dado3%2
par=par1+par2+par3
if par==0:
    premio=1
#proceso
puntos2=puntos
print("En el segundo lanzamiento el jugador sacó:\nDado nro1: ",dado1,"\nDado nro2: ",dado2,"\nDado nro3: ",dado3,"\nEn total sumó: ",puntos)
#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
empezar=input("Presione enter para comenzar")
dado1=random.randrange(0,7)
dado2=random.randrange(0,7)
dado3=random.randrange(0,7)
#puntos por 1
if dado1==1:
    puntos=puntos+1
elif dado2==1:
    puntos=puntos+1
elif dado3==1:
    puntos=puntos+1
#puntos por 3
if dado1==3:
    puntos=puntos+2
elif dado2==3:
    puntos=puntos+2
elif dado3==3:
    puntos=puntos+2
#puntos por 5
if dado1==5:
    puntos=puntos+4
elif dado2==5:
    puntos=puntos+4
elif dado3==5:
    puntos=puntos+4
#si saca par
par1=dado1%2
par2=dado2%2
par3=dado3%2
par=par1+par2+par3
if par==0:
    premio=1
#proceso
puntos3=puntos
total=puntos1+puntos2+puntos3
print("En el tercer lanzamiento el jugador sacó:\nDado nro1: ",dado1,"\nDado nro2: ",dado2,"\nDado nro3: ",dado3,"\nEn total sumó: ",puntos)
print("el total de puntos que saco es:", total)
