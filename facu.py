# tipo de prenda
prenda = "remera", "camisa", "pantalon", "falda", "vestido", "abrigo", "calzado"

# primer prenda

prenda_1 = int(input("ingrese el primer tipo de prenda: 0(remera), 1(camisa), 2(pantalon), 3(falda), 4(vestido), 5(abrigo), 6(calzado):"))
prenda_1 = prenda[prenda_1]

precio_1 = float(input("ingrese el valor de la prenda:"))

sp1 = int(input("participa del programa SuperPuntos? 0(si) 1(no):"))


# segunda prenda

prenda_2 = int(input("ingrese el tipo segundo de prenda: 0(remera), 1(camisa), 2(pantalon), 3(falda), 4(vestido), 5(abrigo), 6(calzado): "))
prenda_2 = prenda[prenda_2]

precio_2 = float(input("ingrese el valor de la prenda:"))

sp2 = int(input("participa del programa SuperPuntos? 0(si) 1(no):"))

# tercer prenda

prenda_3 = int(input("ingrese el tercer tipo de prenda: 0(remera), 1(camisa), 2(pantalon), 3(falda), 4(vestido), 5(abrigo), 6(calzado): "))
prenda_3 = prenda[prenda_3]

precio_3 = float(input("ingrese el valor de la prenda:"))

sp3 = int(input("participa del programa SuperPuntos? 0(si) 1(no):"))


# forma de pago
fpago = int(input('Desea pagar en 0(efectivo) o 1(tarjeta de credito)?:'))
if fpago == 1:
    cuotas = int(input('en cuantas cuotas desea realizarlo?:'))

# total a pagar sin promos

monto = precio_1 + precio_2 + precio_3

# menor#

if precio_1 <= precio_2 and precio_1 <= precio_3:
    men = precio_1
elif precio_2 <= precio_3:
    men = precio_2
else:
    men = precio_3

# promos:

# promo3x2

if prenda_1 == prenda_2 and prenda_2 == prenda_3:
    promo3x2 = 1
    if prenda_1 == prenda_2 and prenda_1 == prenda_3 and prenda_2 == prenda_3:
        promo32 = men
else:
    promo3x2 = 0
    promo32 = 0


# promo 50%

if promo3x2 == 0:
    if prenda_1 == prenda_2:
        if precio_1 >= precio_2:
            may = precio_1
            promo50 = may / 2
        else:
            may = precio_2
            promo50 = may / 2
    if prenda_1 == prenda_3:
        if precio_1 >= precio_3:
            may = precio_1
            promo50 = may / 2
        else:
            may = precio_3
            promo50 = may / 2
    if prenda_2 == prenda_3:
        if precio_2 >= precio_3:
            may = precio_2
            promo50 = may / 2
        else:
            may = precio_3
            promo50 = may / 2
else:
    promo50 = 0

# total con promos

montofinal = monto - promo50 - promo32

# ahorro

ahorro = promo32 + promo50


# super puntos
spf = 0
if sp1 == 0:
    spf = precio_1
if sp2 == 0:
    spf = spf + precio_2
if sp3 == 0:
    spf = spf + precio_3
if sp1 == 0 and sp2 == 0 and sp3 == 0:
    spf = spf * 2


# forma de pago

pago = ("contado", "tarjeta")
if fpago == 1:
    if  cuotas <= 3:
        ryd = "(2% de recargo)"
        recargo = 2 * montofinal / 100
        final = montofinal + recargo

    elif    cuotas > 3:
            ryd = "(5% de recargo)"
            recargo = 5 * montofinal / 100
            final = montofinal + recargo
else:
        ryd = "(10% de descuento)"
        descuento = 10 * montofinal / 100
        final = montofinal - descuento



print("----------------------------------------\nTIENDA ELEGANCIA\nTipo Precio SuperPuntos\n",prenda_1," ", precio_1 ,"$\n",prenda_2," ", precio_2 ,"$\n",prenda_3," ", precio_3 ,"$\nTotal sin Promo $", monto,"\nAhorro $", ahorro, "\nTotal con Promo $" , montofinal ,"\nForma de Pago:", pago[fpago] , ryd , "\nMonto a Pagar $", final ,"\nUsted obtiene", int(spf) , "SuperPuntos\n----------------------------------------")