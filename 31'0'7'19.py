import random

def seleccion_sort(v):
    n=len(v)
    for i in range (n-1):
        for j in range(i +1, n):
            if v[i]>v[j]:
                v[i],v[j]=v[j],v[i]
def credor():
    v=[0]
    cant=int(input('ingrese cantidad de casillas'))
    v=cant*[0]
    for posi in range (len(v)):
        v[posi]=random.randint(0,100)
    return v
def buscar(v):
    x=int(input('Ingrese numero a buscar'))
    for posi in range (len(v)):
        if v[posi]==x:
            print('El numero "x"('+str(x)+'esta en la posiscion v['+str(posi)+']')

            return posi
    return True
def impares(posicion,v):
    impares=0
    for posi in range(posicion+1,len(v)):
        if v[posi]%2!=0:
            impares+=1
    return impares
def test():
    v=credor()
    seleccion_sort(v)
    posicion=buscar(v)
    if posicion:
#        print('El numero "x"('+str(x)") no ha sido encontrado")
    else:
        impares=impares(posicion,v)
    print(impares)
test()
