#datos de lo que quiere comprar el usuario
pprendas=('una remera','una camisa','un pantalon','una falda','un vestido','un abrigo','un calzado')
prenda=('remera','camisa','pantalon','falda','vestido','abrigo','calzado')
prendas=('remeras','camisas','pantalones','faldas','vestidos','abrigos','calzados')
superpuntos=(0,100)
#prenda numero 1
prenda1=int(input('¿Cual es la primer prenda que desea? remera(0), camisa(1), pantalon(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
print('Eligió:',pprendas[prenda1])
precioprenda1=float(input('¿Cual es su valor?'))
print('Eligió: ',pprendas[prenda1])
super1=int(input('¿Participa de los SuperPuntos?Si(0) o no(1)'))
#prenda numero 2
print('Recorda que comprando 3 prendas iguales recibis un 3x2 y dos iguales una al 50%\nUsted ha comprado: \n1. ',pprendas[prenda1],' ',precioprenda1,'$ ')
prenda2=int(input('¿Cual es la segunda prenda que desea? remera(0), camisa(1), pantalon(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
print('Eligió:',pprendas[prenda2])
precioprenda2=float(input('¿Cual es su valor?'))
print('Eligió: ',pprendas[prenda2])
super2=int(input('¿Participa de los SuperPuntos?Si(0) o no(1)'))
#prenda numero 3
print('Usted ha comprado: ')
print('1. ',pprendas[prenda1],' ',precioprenda1,'$ \n2. ',pprendas[prenda2],' ',precioprenda2,'$\nrecorda que comprando 3 prendas iguales recibis un 3x2 y dos iguales una al 50%')
prenda3=int(input('¿Cual es la tercer prenda que desea? remera(0), camisa(1), pantalon(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
print('Eligió:',pprendas[prenda3])
precioprenda3=float(input('¿Cual es su valor?'))
print('Eligió: ',pprendas[prenda3])
super3=int(input('¿Participa de los SuperPuntos?Si(0) o no(1)'))
#SUPERPUNTOS
superp=0
if super1==0:
    superp=precioprenda1
if super2==0:
    superp=superp+precioprenda2
if super3==0:
    superp=superp+precioprenda3
if super1==0 and super2==0 and super3==0:
    superp=superp*2
pp1=precioprenda1
pp2=precioprenda2
pp3=precioprenda3
#promociones:
#promo 3X2
if prenda1==prenda2 and prenda2==prenda3:
        promo3x2=1
        if precioprenda1<precioprenda2 and precioprenda1<precioprenda3:
                precioprenda1=0
                promogratis=1
        if precioprenda2<precioprenda1 and precioprenda2<precioprenda3:
                precioprenda2=0
                promogratis=2
        if precioprenda3<precioprenda2 and precioprenda3<precioprenda1:
                  precioprenda3=0
                  promogratis=3
else:   
         promo3x2=0
         promogratis=0
         promocion3x2='La promocion de 3x2 no esta incluida en tu compra'
#promocion 50% off
if promo3x2==0:
    if prenda1==prenda2:
        if precioprenda1<precioprenda2:
            promo50=2
            promocion1=precioprenda2*50//100
            precioprenda2=precioprenda2-promocion1
        else:
            promo50=1
            promocion1=precioprenda1*50//100
            precioprenda1=precioprenda1-promocion1
    if prenda2==prenda3:
        if precioprenda3<precioprenda2: 
            promo50=2
            promocion1=precioprenda2*50//100
            precioprenda2=precioprenda2-promocion1
        else:
            promo50=3
            promocion1=precioprenda3*50//100
            precioprenda3=precioprenda3-promocion1
    if prenda1==prenda3:
        if precioprenda1<precioprenda3:
            promo50=3
            promocion1=precioprenda3*50//100
            precioprenda3=precioprenda3-promocion1
        else:
            promo50=1
            promocion1=precioprenda1*50//100
            precioprenda1=precioprenda1-promocion1         
else:
         promo50=0
descuento1=' '
descuento2=' '
descuento3=' '
descutotal="tubo un descuento del 100% por la compra de 3"
descu50="tubo un descuento del 50% por la compra de 2"
if promogratis==1:
         descuento1="tu",prenda[prenda1],descutotal,prendas[prenda1]
if promogratis==2:
         descuento2="Tu",prenda[prenda2] ,descutotal,prendas[prenda2],"iguales."
if promogratis==3:
         descuento3='Tu',prenda[prenda3],descutotal,prendas[prenda3],'iguales.'
if promo50==1:
         descuento1='Tu',prenda[prenda1],descu50,prendas[prenda1],'iguales.'
if promo50==2:
         descuento2='Tu',prenda[prenda2],descu50,prendas[prenda2],'iguales.'   
if promo50==3:
         descuento3='Tu',prenda[prenda3],descu50,prendas[prenda3],'iguales.'
        
#Detalles de la compra

total=precioprenda1+precioprenda2+precioprenda3
print ('Usted ha comprado: \n1.',pprendas[prenda1],' ',precioprenda1,'$ ',descuento1,'\n2.',pprendas[prenda2],' ',precioprenda2,'$ ',descuento2,'\n3.',pprendas[prenda3],' ',precioprenda3,'$ ',descuento3,"\nTotal: ",total,"$")

#pago de la compra

pago=('contado', 'tarjeta')
fpago=int(input('¿Desea pagar en efectivo(0) o con tarjeta de credito(1)'))
if fpago==1:
    cuotas=float(input('¿Con cuantas cuotas desea pagar?'))
    if cuotas==0:
        fdepago="0% de recargo"
        recargo=0
        totalfinal=total+recargo
    if cuotas<=3:
        fdepago="2% de recargo"
        recargo=total//100*2
        totalfinal=total+recargo
    if cuotas>3:
        fdepago="5% de recargo"
        recargo=total//100*5
        totalfinal=total+recargo
else:
    fdepago="10% de descuento"
    descuento=total*10//100
    totalfinal=total-descuento

#resultados
totalsinpromo=pp1+pp2+pp3
ahorro=totalsinpromo-total

print("------------------------------------\nTIENDA ELEGANCIA\nTipo de precios SuperPuntos\n",prenda[prenda1]," ",pp1,"$\n",prenda[prenda2]," ",pp2,"$\n",prenda[prenda3]," ",pp3,"$\nTotal sin promo ",totalsinpromo,"$\nAhorro ",ahorro,"$\nTotal con promo ",total,"$\nForma de pago: ",pago[fpago],"(",fdepago,")\nMonto a pagar: ",totalfinal,"$\n","Usted obtiene ",superp,"SuperPuntos\n------------------------------------")

       
    
    
         
 

