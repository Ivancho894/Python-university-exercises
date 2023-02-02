class resultado:
    def __init__(self,cp,p,ug,e,cd,pde):
        self.codigo_de_publicacion=cp
        self.precio=p
        self.ubicacion_geografica=ug
        self.estado=e
        self.cantidad_disponible=cd
        self.puntuacion_del_vendedor=pde
def write(res):
    print("\nCodigo de publicacion",res.codigo_de_publicacion,end=' ')
    print("Precio",res.precio,end='')
    print("Ubicacion geografica",res.ubicacion_geografica,end=' ')
    print("Estado",res.estado,end=' ')
    print("Cantidad disponible",res.cantidad_disponible,end=' ')
    print("Puntuacion del vendedor",res.puntuacion_del_vendedor,end=' ')
