from desafio3 import *
def numdiferentes(v):
    num=[]
    cont=[]
    frecu,compara=0,0
    noesta=True
    for posi in range(len(v)):
        if v[posi]==547:
            print(frecu)
            frecu=0
        else:
            frecu+=1
        
        for posinum in range(len(num)):

            if v[posi]==num[posinum]:
                noesta=False
                cont[posinum]+=1
        if noesta:
            num.append(v[posi])
            cont.append(1)
        else:
            noesta=True
    print(compara)
    return num,cont
def elmodal(cont,num):
    masgrande,modal,igual=0,0,0
    for posi in range(len(cont)):
        if cont[posi]>masgrande:
            masgrande=cont[posi]
            modal=num[posi]
    for posis in range(len(cont)):
        if cont[posis]==masgrande:
            igual+=1
    if igual>=2:
        modal=0
    return modal
def test():
    v=vector_unknown_range(300000)
    num,cont=numdiferentes(v)
    modal=elmodal(cont,num)
    #print(v)
    print("valor modal:",modal)
    #print(num)
    #print(cont)
    #print(len(num))
test()
