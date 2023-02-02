x=int(input("ingrese el valor de x: "))
y=int(input("ingrese el valor de y: "))
if x>0 and y>0:
    print("El punto (",x,";",y,") esta en el primer cuadrante")
if x<0 and y>0:
    print("El punto (",x,";",y,") esta en el segundo cuadrante")
if x<0 and y<0:
    print("El punto (",x,";",y,") esta en el tercer cuadrante")
if x>0 and y<0:
    print("El punto (",x,";",y,") esta en el tercer cuadrante")
if x==0 and y==0:
    print("El punto (",x,";",y,") no esta en ningun cuadrante, esta en el eje")
