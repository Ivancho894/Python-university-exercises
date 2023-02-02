def test():
    primera=True
    a=False
    s=False
    e=True
    t=False
    n=False
    r=False
    re=False
    palabrascont=False
    cantletras,eje1,letrast,palabrast,eje4,ultima,sae,promedio=0,0,0,0,0,0,0,0
    texto=input('ingrese un texto')
    for letra in texto:
        if letra!=' ' and letra!='.':
            cantletras+=1            
            if letra=='n' or letra=='N':
                n=True
            if primera and letra=='t' or letra=='T':
                t=True
                palabrast+=1
                palabrascont=True
            else:
                primera=False
            if t:
                letrast+=1
            if letra in 'sS':
                s=True
            if letra in 'Aaá':
                a=True
            if letra=='r' or letra=='R':
                r=True
            if letra in 'eEé':
                e=False
                if r:
                    re=True
            else:
                r=False
            ultima=letra
        else:
            if cantletras>4 and n:
                eje1+=1
            if s and a and e:
                sae+=1
            if re and ultima=='o':
                eje4+=1
            s=False
            a=False
            e=True
            re=False
            t=False
            r=False
            cantletras=0
            unicavez=True
            n=False
            primera=True
    if palabrascont:
        promedio=letrast//palabrast
    print("palabras con cantidad mayor a 4 y con n: ",eje1)
    print("promedio de letras por palabra que tienen una t:",promedio)
    print("palabras que contienen la letra 's' y la 'a' pero no una 'e': ",sae)
    print("palabras que contenian por lo menos una vez la expresion 're' y no termina con 'o': ",eje4)
test()
    
