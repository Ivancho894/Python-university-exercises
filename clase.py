texto=input('ingrese texto: ')
cp,a,la,pl=0,0,0,0
paso=True
for q in texto:
    if q!=' ' or q!='.':
        la=q
        if q=='a' or q=='e' or q=='i' or q=='u' or q=='o' and paso:
                pl=q
                paso=False
        else:
            paso=False
    if q==' ' or q=='.':
        paso=True
        print(pl)
        #print(la)
        if la=='a' or la=='e' or la=='i' or la=='u' or a=='o':
            if pl=='a' or pl=='e' or pl=='i' or pl=='u' or pl=='o':
                a+=1
                print(a)
                print(pl)
                print(la)
           
            
