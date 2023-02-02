class automoviles():
    def __init__(self,codigo,marca,precio,tipo,pais):
        self.codigo=codigo
        self.marca=marca
        self.precio=precio
        self.tipo=tipo
        self.pais=pais
def write(x):
    print('Codigo:',x.codigo,end=', ')
    print('Marca:',x.marca, end=', ')
    print('Precio:',x.precio,end=', ')
    print('Tipo:',x.tipo,end=', ')
    print('Pais:',x.pais)
