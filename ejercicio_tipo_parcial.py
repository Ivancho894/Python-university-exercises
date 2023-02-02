class agencia:
    def __init__(self,numip,des,tipo,dias,impo):
        self.numeroip=numip
        self.descripcion=des
        self.tipodepa=tipo
        self.diasde=dias
        self.importe=impo
def write(age):
    print('\nNumero de identificacion del paquete:',age.numeroip,end=' ')
    print('Descripcion del paquete: ',age.descripcion,end=' ')
    print('Tipos de pasajes: ',age.tipodepa,end=' ')
    print('Cantidad de dias: ',age.diasde,end=' ')
    print('Importe: ',age.importe)
