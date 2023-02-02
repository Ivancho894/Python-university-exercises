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
if super2==1:
    superp=superp+precioprenda2
if super3==1:
    superp=superp+precioprenda3
if super1==1 and super2==1 and super3==1:
    superp=superp*2
#PROMOCIONES
#Promo 3X2:
if prenda1==prenda2 and prenda2==prenda3:
    promo3x2=1
    if precioprenda1<=precioprenda2:
        if precioprenda1<=precioprenda3:
                promogratis=precioprenda1
        else:
                promogratis=precioprenda3
    elif  precioprenda2<=precioprenda3:
        promogratis=precioprenda2
    else:
        promogratis=precioprenda3                
else:   
         promo3x2=0
         promogratis=0
#Promocion 50% off
if promo3x2==0:
    if prenda1==prenda2:
        if precioprenda1<precioprenda2:
            promo50=precioprenda2/2
        else:
            promo50=precioprenda1/2
    if prenda2==prenda3:
        if precioprenda3<precioprenda2: 
            promo50=precioprenda2/2
        else:
            promo50=precioprenda3/2
    if prenda1==prenda3:
        if precioprenda1<precioprenda3:
            promo50=precioprenda3/2
        else:
            promo50=precioprenda1/2
else:
    promo50=0
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
print("------------------------------------\nTIENDA ELEGANCIA\nTipo de precios SuperPuntos\n",prenda[prenda1]," ",precioprenda1,"$\n",prenda[prenda2]," ",precioprenda2,"$\n",prenda[prenda3]," ",precioprenda3,"$\nTotal sin promo ",totalsinpromo,"$\nAhorro ",ahorro,"$\nTotal con promo ",total,"$\nForma de pago: ",pago[fpago],"(",fdepago,")\nMonto a pagar: ",totalfinal,"$\nUsted obtiene ",superp,"SuperPuntos\n------------------------------------")
