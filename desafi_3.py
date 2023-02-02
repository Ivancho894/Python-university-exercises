from desafio3 import *
def elmodal(c):
    modal,masgrande,igual=0,0,0
    for posi in range(len(c)):
        if c[posi]>masgrande:
            masgrande=c[posi]
            modal=posi

    for posis in range(len(c)):
        if c[posis]==masgrande:
            igual+=1
    if igual>=2:
        modal=0
    return modal
def test():
    n=300000
    frecu,compara=0,0
    v=vector_known_range(n)
    c=[0]*n
    #print(v)
    cantidad=0
    for posi in range(len(v)):
        compara+=1
        if v[posi]==6:
            print(frecu)
            frecu=0
        else:
            frecu+=1
        c[v[posi]]+=1
    for posi in range(len(v)):
        if c[posi]!=0:
            cantidad+=1
    modal=elmodal(c)
    print(cantidad)
    print(c)
    print(modal)
    print(compara)


test()
