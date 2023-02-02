#datos
pal=input('ingrese la palabara a ser codificada')
#proceso
primera=pal[0]
media='*'*(len(pal)-2)
ultima=pal[-1]
enmascarada=primera+media+ultima
#resultados
print('la palabra enmascarda es:',enmascarada,)
#informacion de los resultados
print('Su palabra tiene',len(pal),'letras, de las cuales', len(media),'fueron enmascaradas')
