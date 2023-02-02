
class Estudiante:
    # método constructor
    def __init__(self, leg, nom, prom):
        self.legajo = leg
        self.nombre = nom
        self.promedio = prom

def write(est):
    print('\n Legajo: ', est.legajo, '-', end=' ')
    print('Nombre: ', est.nombre, '-', end=' ')
    print('Promedio: ', est.promedio, '-', end=' ')
