precio=float(input("cual es el total de su compra"))
pagar=(input("desea pagar con efectivo o con tarjeta de credito"))
efectivo=1
if pagar==efectivo:
    descuento=float(input("Cual es el descuento pagando en efectivo?"))
    descuentoapli=precio//descuento*100
    total=precio-descuentoapli 
    print("El precio final de su compra es: ",total,"$, teniendo en cuenta que se aplico un descuento del: ",descuento,"%")
else:
    recargo=float(input("Cuanto es el recargo aplicado pagando con credito?"))
    recargoapli=precio*recargo//100
    total=precio+recargoapli
    print("El precio final de su compra es: ",total,"$, teniendo en cuenta que se aplico un recargo del: ",recargo,"%")
