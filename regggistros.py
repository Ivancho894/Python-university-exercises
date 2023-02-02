class resultado:
    def __init__(self, cp, p, ug, e, cd, pde):
        self.codigo=cp
        self.precio=p
        self.ubicacion_geografica=ug
        self.estado=e
        self.cantidad_disponible=cd
        self.calificacion=pde

class compras:
    def __init__(self,cp, cant, p, env, mon, fec):
        self.codigo = cp
        self.cantidad = cant
        self.precio = p
        self.envio = env
        self.monto = mon
        self.fecha = fec


def write(res):
    print("\nCodigo de publicacion",res.codigo,end=', ')
    print("Precio $"+str(res.precio),end=', ')
    print("Ubicacion geografica:",res.ubicacion_geografica,end=', ')
    print("Estado:",res.estado,end=', ')
    print("Cantidad disponible:",res.cantidad_disponible,end=', ')
    print("Puntuacion del vendedor:",res.calificacion)

def write2(res):
    print("-" * 47)
    print("Compra #" + str(res.codigo) + " - " + res.fecha)
    print("Resumen de compra")
    print("Articulo: " + str(res.codigo) + "  $" + str(res.monto) + " (" + str(res.cantidad) + " x $" + str(res.precio) + ")")
    if res.envio == 0:
        print("Retira en sucursal")
    else:
        print("Cargo de envío $" + str(res.envio))
    print("Tu pago $" + str(res.monto))
    print("-" * 47)
