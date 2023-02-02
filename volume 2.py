import time
import random
#global moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,tiempo,mayor,nueva,patente,tipo,forma,precio
letras=('abcdefghijklmnñopqrstuvwxyz')
numeros=('0123456789')
def manual():
   moto,auto,efectivo,telepeaje,camion,cantefe,canttelep=0,0,0,0,0,0,0
   letras=('abcdefghijklmnñopqrstuvwxyz')
   numeros=('0123456789')
   tiempo=time.time()
   while (time.time()-tiempo)<=240:
      global tipo,forma,patente
      tipo=input("¿Que tipo de vehiculo es, moto, auto o camion")
      forma=input("¿Forma de pago? efectivo o telepeaje")
      if forma=='2':
         patente=input("¿Cual es la patente del vehiculo?")
      control_ok=control(tipo,forma,patente)




def control():
   global tipo, forma, patente
   letras=('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
   numeros=('0123456789')
   while tipo!=moto and tipo!=auto and tipo!=camion:
      tipo=input("Ingresaste mal el tipo de vehiculo, por favor ingreselo de nuevo((1)moto,(2)auto o (3)camion)")
   while forma!=efectivo and forma!=telepeaje:
      forma=input("Ingresaste mal la forma de pago, por favor ingreselo de nuevo((1)efectivo o (2)telepeaje")
   if forma=='2':
      while (patente[0]!=letras and patente[1]!=letras and patente[2]!=letras and patente[3]!=numeros and patente[4]!=numeros and patente[5]!=numeros) or (patente[0]!=letras and patente[1]!=letras and patente[2]!=numeros and patente[3]!=numeros and patente[4]!=numeros and patente[5]!=letras and patente[6]!=letras):
         patente=input("Ingreso mal la patente,por favor ingresela de nuevo")
   
      



def automatico():
   global moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,tiempo,mayor,nueva,patente,tipo,forma,precio,numeros,printt,printf
   moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,hora=0,0,0,0,0,0,0,0
   primera=True
   vehiculos=('moto','auto','camion')
   pat=('efectivo','telepeaje')
   mayor='aaa000'
   patente='aaa000'
   tiempo=time.time()
   nueva=True
   banderas=(True,False)
   printt=''
   printf=''
   while (time.time()-tiempo)<=240:
      paso=random.choice(banderas)
      print(paso)
      if paso:
         printt=''
         printf=''
         precio=0
         tipo=random.choice(vehiculos)
         forma=random.choice(pat)
         if forma=='telepeaje':
            patentes=random.choice(banderas)
            if patentes:
               patente=str(random.choice(letras))+str(random.choice(letras))+str(random.choice(letras))+str(random.choice(numeros))+str(random.choice(numeros))+str(random.choice(numeros))
               printeo=str('con patente: ')+str(patente)
            else:
               patente=str(random.choice(letras))+str(random.choice(letras))+str(random.choice(numeros))+str(random.choice(numeros))+str(random.choice(numeros))+str(random.choice(letras))+str(random.choice(letras))
               printeo=str('con patente: ')+str(patente)
         else:
            printeo=""
         pase_ok=pase()
         pante_ok=patemayor()
         print("pasó un ",tipo,printeo,"pagó con ",forma,)
      time.sleep(5)


def patemayor():
   global hora,tiempo,numeros,nueva,mayor
   if nueva:
      if len(mayor)<len(patente):
         nueva=False
         mayor=patente
         hora=time.time()-tiempo
      elif mayor<patente:
         mayor=patente
         hora=time.time()-tiempo
         
   elif len(mayor)==len(patente) and mayor<patente:
      mayor=patente
      hora=time.time()-tiempo
   

def pase():
    global moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,tipo,forma,mayor,hora,patente,tiempo,numeros,primera,printt,printf
    if tipo=='moto':
        moto+=1
        precio=20
        printt=str("auto")
    elif tipo=='auto':
        precio=40
        auto+=1
        printt=str("moto")
    else:
        precio=80
        camion+=1
    if forma=='1':
        cantefe+=1
        efectivo+=precio
        printf=str("por efectivo")
    else:
        canttelep+=1
        telepeaje+=precio  
        printf=str("por telepeaje")
        patente_ok=patemayor()



numeros=('0123456789')
print("Menú de opciones:")
print("1.Definir forma de carga de datos")
print("2.Procesar las pasadas")
print("3.Ver los resultados")
print("4.Salir")
menu=input()

if menu!=1:
   manera=input("¿Desea que la carga de datos sea (0)manual o (1)automatica?")
   if manera==0:
      manu=manual()
   else:
      auto=automatico()
elif menu==3:
    printiar=resultados()
    
        
                
                
                
            
                






    
