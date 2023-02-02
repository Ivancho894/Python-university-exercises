
__author__ = 'Cátedra de AED'
#Datos de lo que quiere comprar el usuario

pprendas=('una remera','una camisa','un pantalon','una falda','un vestido','un abrigo','un calzado')
prenda=('remera','camisa','pantalon','falda','vestido','abrigo','calzado')

#Prenda numero 1

prenda1=int(input('¿Cual es la primer prenda que desea? remera(0), camisa(1), pantalon(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
print('Eligió:',pprendas[prenda1])
precioprenda1=float(input('¿Cual es su valor?'))
print('Eligió: ',pprendas[prenda1])
super1=int(input('¿Participa de los SuperPuntos?Si(1) o no(0)'))

#Prenda numero 2

print('Recorda que comprando 3 prendas iguales recibis un 3x2 y dos iguales una al 50%\nUsted ha comprado: \n1. ',pprendas[prenda1],' ',precioprenda1,'$ ')
prenda2=int(input('¿Cual es la segunda prenda que desea? remera(0), camisa(1), pantalon(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
print('Eligió:',pprendas[prenda2])
precioprenda2=float(input('¿Cual es su valor?'))
print('Eligió: ',pprendas[prenda2])
super2=int(input('¿Participa de los SuperPuntos?Si(1) o no(0)'))

#Prenda numero 3

print('Usted ha comprado: ')
print('1. ',pprendas[prenda1],' ',precioprenda1,'$ \n2. ',pprendas[prenda2],' ',precioprenda2,'$\nrecorda que comprando 3 prendas iguales recibis un 3x2 y dos iguales una al 50%')
prenda3=int(input('¿Cual es la tercer prenda que desea? remera(0), camisa(1), pantalon(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
print('Eligió:',pprendas[prenda3])
precioprenda3=float(input('¿Cual es su valor?'))
print('Eligió: ',pprendas[prenda3])
super3=int(input('¿Participa de los SuperPuntos?Si(1) o no(0)'))
fpago=int(input('¿Desea pagar en efectivo(0) o con tarjeta de credito(1)'))
if fpago==1:
    cuotas=float(input('¿Con cuantas cuotas desea pagar?'))

#RPOCESOS
    
#TOTAL SIN PROMO

totalsinpromo=precioprenda1+precioprenda2+precioprenda3

#SUPERPUNTOS

superp=0
if super1==1:
    superp=precioprenda1
    s1="S"
else:
    s1=""
if super2==1:
    superp=superp+precioprenda2
    s2="S"
else:
    s2=""
if super3==1:
    superp=superp+precioprenda3
    s3="S"
else:
    s3=""
if super1==1 and super2==1 and super3==1:
    superp=superp*2

#PROMOCIONES
promogratis=0
promo50=0   
if prenda1==prenda2:
    if prenda3==prenda2:                        #Promo3x2
        if precioprenda1<=precioprenda2:
            if precioprenda1<=precioprenda3:
                promogratis=precioprenda1
            else:
                promogratis=precioprenda3
        elif  precioprenda2<=precioprenda3:
            promogratis=precioprenda2
        else:
            promogratis=precioprenda3
    elif precioprenda1<precioprenda2:           #Promo50% de descuento entre 1 y 2
        promo50=precioprenda2/2
    else:
        promo50=precioprenda1/2
elif prenda2==prenda3:                          #Promo50% de descuento entre 3 y 2
    if precioprenda3<precioprenda2:
        promo50=precioprenda2/2
    else:
        promo50=precioprenda3/2
elif prenda1==prenda3:                          #Promo50% de descuento entre 1 y 3
    if precioprenda1<precioprenda3:
        promo50=precioprenda3/2
    else:
        promo50=precioprenda1/2
 
        

#Detalles de la compra
    
total=precioprenda1+precioprenda2+precioprenda3-promo50-promogratis

#pago de la compra

pago=('contado', 'tarjeta')
if fpago==1:
    if cuotas==0:
        fdepago="0% de recargo"
        recargo=0
    elif cuotas<=3:
        fdepago="2% de recargo"
        recargo=total/100*2
        totalfinal=total+recargo
    elif cuotas>3:
        fdepago="5% de recargo"
        recargo=total/100*5
        totalfinal=total+recargo
else:
    fdepago="10% de descuento"
    descuento=total*10/100
    totalfinal=total-descuento

#Resultados finales
    
ahorro=promogratis+promo50
print("------------------------------------")
print("TIENDA ELEGANCIA")
print("Tipo de precios SuperPuntos")
print(prenda[prenda1]," ",precioprenda1,"$ ",s1)
print(prenda[prenda2]," ",precioprenda2,"$ ",s2)
print(prenda[prenda3]," ",precioprenda3,"$ ",s3)
print("Total sin promo ",totalsinpromo,"$")
print("Ahorro ",ahorro,"$")
print("Total con promo ",total,"$")
print("Forma de pago: ",pago[fpago],"(",fdepago,")")
print("Monto a pagar: ",totalfinal,"$")
print("Usted obtiene ",superp,"SuperPuntos")
print("------------------------------------")
