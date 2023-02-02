texto=input("ingrese")
def principal(texto):
    e=False
    for letra in texto:
        if letra!=' ' or letra!='.':
        
            letras+=1            
            if letra in numeros:
                numero+=1
            if letra=='e':
                e=True
            else:
                e=False
        elif (letras%2)!=0:
            promedio=1
        else:
            letras=0
            
            
