class cine():
    def __init__(self,id,titulo,importe,tipo,pais):
        self.id=id
        self.titulo=titulo
        self.importe=importe
        self.tipo=tipo
        self.pais=pais
def write(x):
    print('id',x.id,end=' ')
    print('titulo:',x.titulo,end=' ')
    print('importe:',x.importe,end=' ')
    print('tipo:',x.tipo,end=' ')
    print('pais:',x.pais)
