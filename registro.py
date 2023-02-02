gen = ['Infantil', 'Comedia', 'Romantico', 'Drama', 'Ciencia Ficcion', 'Otros']
peliculas = ['Capitan America', 'El Hombre Araña', 'Iron Man', 'Los Ilusionistas', 'Star Wars', 'Titanic',
             'Volver al Futuro']
leng = ['Español', 'Ingles', 'Frances', 'Portugues', 'Otros']


class Pelicula:
    def __init__(self, titulo, genero, idioma):
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma


def write(x):
    print('Titulo:', peliculas[x.titulo], end=', ')
    print('Genero:', gen[x.genero], end=', ')
    print('Idioma:', leng[x.idioma])


def to_string(x):
    renglon = ''
    renglon += '{:>10}'.format('Titulo:' + str(peliculas[x.titulo] + ', '))
    renglon += '{:>10}'.format('Genero:' + str(gen[x.genero] + ', '))
    renglon += '{:>5}'.format('Idioma:' + str(leng[x.idioma]))
    return renglon
