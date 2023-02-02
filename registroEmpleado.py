class Empleado:
    # método constructor
    def __init__(self, leg, nom, direc, sue, ant):
        self.legajo = leg
        self.nombre = nom
        self.direccion = direc
        self.sueldo = sue
        self.antiguedad = ant

def write(empleado):
    print(' Legajo: ', empleado.legajo,'-', end=' ')
    print('Nombre: ', empleado.nombre, '-', end =' ')
    print('Direccion: ', empleado.direccion,'-', end =' ')
    print('Sueldo: ', empleado.sueldo, '-', end =' ')
    print('Antiguedad: ', empleado.antiguedad)

e1 = Empleado(1,'juan','calle a',10000,2)
e2 = Empleado(2,'matias','calle b',20000,7)
write(e1)
write(e2)




