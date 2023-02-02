def init():
    pila=[]
    return pila

def apilar(num,pila):
    pila.append(num)
    return pila
def printeo(pila):
    for posi in range(len(pila)):
        if pila[-1]!=pila[posi]:
            print(pila[posi],end=';')
        else:
            print(pila[posi])
def vacia(pila):
    n=len(pila)
    return n==0
def desapilar(pila):
    x=None
    if vacia(pila)==False:
        x=pila[-1]
        del pila[-1]
    return x
def test():
    p1=init()
    apilar(7,p1)
    apilar(3,p1)
    apilar (5,p1)
    apilar(2,p1)
    printeo(p1)
    while vacia(p1)== False:
        x=desapilar(p1)
        print('Desapilado: ',x)
test()
