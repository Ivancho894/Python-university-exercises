#datos de lo que quiere comprar el usuario
pprendas=('una remera','una camisa','un pantalon','una falda','un vestido','un abrigo','un calzado')
prendas=('remeras','camisas','pantalones','faldas','vestidos','abrigos','calzado')
superpuntos=(0,100)
#prenda numero 1
print('recorda que comprando 3 prendas iguales recibis un 3x2 y dos iguales una al 50%')
prenda1=int(input('¿Cual es la primer prenda que desea? remera(0), camisa(1), pantalon(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
if prenda1>=7:
				 print('No ingresaste un numero del 1 al 7')
print('Eligió:',pprendas[prenda1])
precioprenda1=float(input('¿Cual es su valor?'))
print('Eligió: ',pprendas[prenda1])
super1=int(input('¿Participa de los SuperPuntos?Si(0) o no(1)'))
#prenda numero 2
print('Recorda que comprando 3 prendas iguales recibis un 3x2 y dos iguales una al 50%\nUsted ha comprado: \n1. ',pprendas[prenda1],' ',precioprenda1,'$ ')
prenda2=int(input('¿Cual es la segunda prenda que desea? remera(0), camisa(1), pantalon(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
if prenda2>7:
				 print('No ingresaste un numero del 1 al 7')
print('Eligió:',pprendas[prenda2])
precioprenda2=float(input('¿Cual es su valor?'))
print('Eligió: ',pprendas[prenda2])
super2=int(input('¿Participa de los SuperPuntos?Si(0) o no(1)'))
#prenda numero 3
print('Usted ha comprado: ')
print('1. ',pprendas[prenda1],' ',precioprenda1,'$ \n2. ',pprendas[prenda2],' ',precioprenda2,'$\nrecorda que comprando 3 prendas iguales recibis un 3x2 y dos iguales una al 50%')
prenda3=int(input('¿Cual es la tercer prenda que desea? remera(0), camisa(1), pantalon(2), falda(3), vestido(4), abrigo(5), calzado(6).'))
if prenda3>7:
				 print('No ingresaste un numero del 1 al 7')
print('Eligió:',pprendas[prenda3])
precioprenda3=float(input('¿Cual es su valor?'))
print('Eligió: ',pprendas[prenda3])
super3=int(input('¿Participa de los SuperPuntos?Si(0) o no(1)'))
pp1=precioprenda1
pp2=precioprenda2
pp3=precioprenda3
#promociones:
#promo 3X2
if prenda1==prenda2 and prenda2==prenda3:
				promo3x2=1
				
				if precioprenda1<precioprenda2 and precioprenda1<precioprenda3:
								precioprenda1=0 
				if precioprenda2<precioprenda1 and precioprenda2<precioprenda3:
								precioprenda2=0     
				if precioprenda3<precioprenda2 and precioprenda3<precioprenda1:
									precioprenda3=0
else:   
				 promo3x2=0
				 promocion3x2='La promocion de 3x2 no esta incluida en tu compra'
#promocion 50% off
if promo3x2==0 and prenda1==prenda2 or prenda1==prenda3 or prenda3==prenda2:
				 promocion50='haz sido beneficiado por la promocion del 50% en '
				 if precioprenda1<precioprenda2 and precioprenda2>precioprenda3:
								promo50=2
								promocion1=precioprenda2//50*100
								precioprenda2=precioprenda2-promocion1

				if precioprenda2<precioprenda1 and precioprenda3<precioprenda1: 
						promo50=1
						promocion1=precioprenda1//50*100
						precioprenda1=precioprenda1-promocion1
				if precioprenda3>precioprenda2 and precioprenda1<precioprenda3:
								promo50=3
								promocion=precioprenda3//50*100
				 precioprenda3=precioprenda3-promocion1
else:
				 promo50=0
				 promocion50='La promocion del 50% no esta incluida en tu compra'
if precioprenda1==0:
				 descuento1='Tu',prendas[prenda1],'tubo un descuento por la compra de 3',prendas[prenda1],'iguales.'
else:
				 descuento1=' '
if precioprenda2==0:
				 descuento2='Tu',prendas[prenda2],'tubo un descuento por la compra de 3',prendas[prenda2],'iguales.'
else:
				 descuento2=' '    
if precioprenda3==0:
				 descuento3='Tu',prendas[prenda3],'tubo un descuento por la compra de 3',prendas[prenda3],'iguales.'
else:
				 descuento3=' '
if promo50==1:
				 descuento1='Tu',prendas[prenda1],'tubo un descuento por la compra de 1',prendas[prenda1],'iguales.'
else:
				 descuento1=' '
if promo50==2:
				 descuento2='Tu',prendas[prenda2],'tubo un descuento por la compra de 2',prendas[prenda2],'iguales.'
else:
				 descuento2=' '    
if promo50==3:
				 descuento3='Tu',prendas[prenda3],'tubo un descuento por la compra de 4',prendas[prenda3],'iguales.'
else:
				 descuento3=' '
#Detalles de la compra
print('Usted ha comprado: \n1.',pprendas[prenda1],' ',precioprenda1,'$ ',descuento1,'\n2.',pprendas[prenda2],' ',precioprenda2,'$ ',descuento2,'\n3.',pprendas[prenda3],' ',precioprenda3,'$ ',descuento3)
	 #pago de la compra
pago=('contado', 'tarjeta')
fpago=int(input('¿Desea pagar en efectivo(0) o con tarjeta de credito(1)'))
if fpago==1:
		cuotas=float(input('¿Con cuantas cuotas desea pagar?'))
		
				 
 

