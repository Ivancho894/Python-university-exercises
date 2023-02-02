
def introducir_texto():
    global texto
    texto=input("ingrese un texto")
def eje_1():
    if letra=='n'or letra=='N':
        n=True
    if n and letras>4:
        tienen_n+=1
        n=False

def eje_2():
    if primera and letra=='t'or letra=='T':
        palabras_t+=1
        t=True
    if t:
        letras_t+=1
def eje_3():
    if letra=='a'or letra=='A' and unavez:
        a=True
        unavez=False
    if a and letra=='s'or letra=='S':
        s=True
        palabras_as+=1
        a=False
        
    if s and letra=='e'or letra=='E':
        s=False
        palabras_as-=1
def eje_4(letra):
    if letra=='r' or letra=='R':
        r=True
    if r and letra=='e'or letra=='E':
        r=False
    if ultimaletra and ultimaletra_es=='o' or letra=='O':
        palabras_re+=1
def test():
    global letra
    global letras,tienen_n,letras_t,palabras_t,palabras_as,palabras_re=0,0,0,0,0,0
    global n=False
    t=False
    a=False
    unavez=True
    a=False
    s=False
    ultimaletra=False
    introducir=introducir_texto()
    for letra in texto:
        if letra!=' ' or letra!='.':
            primer_ejercicio=eje_1()
            segundo_ejercicio=eje_2()
            tercer_ejercicio=eje_3()
            cuerto_ejercicio=eje_4()
            letras=+1
            ultimaletra_es=letra
            primera=False
        else:
            ultimaletra=True
            cuerto_ejercicio=eje_4()
            unavez=True
            primera=True
            t=False
            a=False
    promedio_t=letras_t//palabras_t

    print('Las palabras que contien al menos 4 letras y contienen al menos una "n" son:',tienen_n)
    print('El promedio de letras por palabras que comienzan con "t" son:',promedio)
    print('La cantidad de palabras que contienen una "a" y una "s" pero no contiene una "e" son:',palabras_as)
    print('La cantidad de palabras que contenian al menos una vez la expresion "re" pero terminan con "o" son:',palabras_re)
test()
    
