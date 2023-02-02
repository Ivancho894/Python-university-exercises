#Desarrolle un programa en python sin usar las fucions predefinidas de min() y max(), que permita cargar
#por teclado los milimetros de lluvia caidos durante 3 meses consecutivos. Muestre la mayor de esas
#cantidades. Informe si al menos un mes no tuvo lluvias (es decir 0mm caidos).
mes1=float(input("ingrese los mm de lluvia caidos en el primer mes"))
mes2=float(input("ingrese los mm de lluvia caidos en el segundo mes"))
mes3=float(input("ingrese los mm de lluvia caidos en el tercer mes"))
if mes1>mes2:
    if mes3<mes1:
        print("El mes que mas llovio fue el primero con una cantidad de: ",mes1,"mm")
    else:
        print("El mes que mas llovio fue el tercero con una cantidad de: ",mes3,"mm")
elif mes2<mes3:
    print("El mes que mas llovio fue el tercero con una cantidad de: ",mes3,"mm")
else:
    print("El mes que mas llovio fue el segundo con una cantidad de: ",mes2,"mm")
if mes1==0 or mes2==0 or mes3==0:
    print("Hubo uno de los mese que no tuvo lluvias")

