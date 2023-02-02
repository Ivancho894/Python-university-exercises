__author__ = 'Facundo Gomez e Ivan Serralta'
__fecha__ = '28 de Abril de 2019'
__objetivo__ = 'Desarrollar un programa que permita simular la emisión de un ticket de una tienda de indumentaria.'
__version__ = '1'
#Datos de lo que quiere comprar el usuario

prenda=('remera','camisa','pantalón','falda','vestido','abrigo','calzado')

#Prenda numero 1

prenda1=int(input('¿Cuál es la primer prenda que desea? remera(0), camisa(1), pantalón(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
precioprenda1=float(input('¿Cuál es su valor?'))
super1=int(input('¿Participa de los SuperPuntos?Si(1) o no(0)'))

#Prenda numero 2

prenda2=int(input('¿Cuál es la segunda prenda que desea? remera(0), camisa(1), pantalón(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
precioprenda2=float(input('¿Cuál es su valor?'))
super2=int(input('¿Participa de los SuperPuntos?Si(1) o no(0)'))

#Prenda numero 3

prenda3=int(input('¿Cuál es la tercer prenda que desea? remera(0), camisa(1), pantalón(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
precioprenda3=float(input('¿cuál es su valor?'))
super3=int(input('¿Participa de los SuperPuntos?Si(1) o no(0)'))

#Forma de pago
fpago=int(input('¿Desea pagar en efectivo(0) o con tarjeta de crédito(1)'))
if fpago==1:
    cuotas=float(input('¿Con cuántas cuotas desea pagar?'))

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
    if cuotas<=3:
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
print(prenda[prenda1]," $","{0:.2f}".format(precioprenda1)," ",s1)
print(prenda[prenda2]," $","{0:.2f}".format(precioprenda2)," ",s2)
print(prenda[prenda3]," $","{0:.2f}".format(precioprenda3)," ",s3)
print("Total sin promo $","{0:.2f}".format(totalsinpromo))
print("Ahorro $","{0:.2f}".format(ahorro))
print("Total con promo $","{0:.2f}".format(total))
print("Forma de pago: ",pago[fpago],"(",fdepago,")")
print("Monto a pagar: $","{0:.2f}".format(totalfinal))
print("Usted obtiene ",int(superp),"SuperPuntos")
print("------------------------------------")
