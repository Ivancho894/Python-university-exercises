def init():
    cola=[]
    return cola
def add(cola,n):
    cola.append(n)
    return cola
def vacia(cola):
    n=len(cola)
    return n==0
def desapilar(cola):
    x=None
    if vacia(cola)==False:
        x=cola[-1]
        del cola[-1]
    return x
def test():
    c1=init()
    add(cola,1)
    add(cola,54)
    add(cola,3)
    add(cola,9)
