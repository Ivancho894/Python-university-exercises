class resultado:
    def __init__(self,cp,p,ug,e,cd,pde):
        self.codigo=cp
        self.precio=p
        self.ubicacion_geografica=ug
        self.estado=e
        self.cantidad_disponible=cd
        self.calificacion=pde


def write(res):
    print("\nCodigo de publicacion",res.codigo,end=', ')
    print("Precio $"+str(res.precio),end=', ')
    print("Ubicacion geografica:",res.ubicacion_geografica,end=', ')
    print("Estado:",res.estado,end=', ')
    print("Cantidad disponible:",res.cantidad_disponible,end=', ')
    print("Puntuacion del vendedor:",res.calificacion)