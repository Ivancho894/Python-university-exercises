import time
import random
global moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,tiempo,mayor,nueva,patente,tipo,forma,precio

def manual():
   moto,auto,efectivo,telepeaje,camion,cantefe,canttelep=0,0,0,0,0,0,0
   letras=('abcdefghijklmnñopqrstuvwxyz')
   numeros=('0123456789')
   tiempo=time.time()
   while (time.time()-tiempo)<=240:
      global tipo,forma,patente
      tipo=input("¿Que tipo de vehiculo es, (1)moto,(2)auto o (3)camion")
      forma=input("¿Forma de pago?(1)efectivo o (2)telepeaje")
      if forma=='2':
         patente=input("¿Cual es la patente del vehiculo?")
      control_ok=control(tipo,forma,patente)




def control(tipo, forma, patente):
   letras=('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
   numeros=('0123456789')
   while tipo!=1 and tipo!=2 and tipo!=3:
      tipo=input("Ingresaste mal el tipo de vehiculo, por favor ingreselo de nuevo((1)moto,(2)auto o (3)camion)")
   while forma!=1 and forma!=2:
      forma=input("Ingresaste mal la forma de pago, por favor ingreselo de nuevo((1)efectivo o (2)telepeaje")
   if forma=='2':
      while (patente[0]!=letras and patente[1]!=letras and patente[2]!=letras and patente[3]!=numeros and patente[4]!=numeros and patente[5]!=numeros) or (patente[0]!=letras and patente[1]!=letras and patente[2]!=numeros and patente[3]!=numeros and patente[4]!=numeros and patente[5]!=letras and patente[6]!=letras):
         patente=input("Ingreso mal la patente,por favor ingresela de nuevo")
      
   return tipo, forma , patente
   
      



def automatico():
   global moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,tiempo,mayor,nueva,patente,tipo,forma,precio
   letras=('abcdefghijklmnñopqrstuvwxyz')
   numeros=('0123456789')
   moto,auto,efectivo,telepeaje,camion,cantefe,canttelep=0,0,0,0,0,0,0
   primera=True
   vehiculos=(1,2,3)
   pat=('1','2')
   mayor='aaa000'
   patente='aaa000'
   hora=0
  
   tiempo=time.time()
   nueva=True
   while (time.time()-tiempo)<=240:
      print(primera)  
      numeros=('0123456789')
      precio=0
      tipo=random.choice(vehiculos)
      forma=random.choice(pat)
      if forma=='2':
         patentes=random.choice(pat)
         if patentes=='1':
            patente=str(random.choice(letras))+str(random.choice(letras))+str(random.choice(letras))+str(random.choice(numeros))+str(random.choice(numeros))+str(random.choice(numeros))
            printeo=str('patente: ')+str(patente)
         else:
            patente=str(random.choice(letras))+str(random.choice(letras))+str(random.choice(numeros))+str(random.choice(numeros))+str(random.choice(numeros))+str(random.choice(letras))+str(random.choice(letras))
            printeo=str('patente: ')+str(patente)
      else:
         printeo=""

      pase_ok=pase(moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,tipo,forma,mayor,hora,patente,tiempo,numeros,primera)
      pante_ok=patemayor(hora,tiempo,numeros,nueva,mayor)
      print(printeo,"tipo: ",tipo,"forma: ",forma,"mayor: ",mayor, "minutos desde que empezo el turno: ",hora,primera)
      time.sleep(1)

def patemayor(pmhora,pmtiempo,pmnumeros,pmnueva,pmmayor):
   print("1. mayor: ", pmmayor,"nueva es: ",pmnueva,"patente: ",pmpatente)
   a=input()
   if pmnueva:
     # if mayor[2] not in numeros and patente[2] in numeros:
      if len(pmmayor)<len(pmpatente):
         print("2. mayor: ", pmmayor,"nueva es: ",pmnueva,"patente: ",pmpatente)
         a=input()
         pmnueva=False
         pmmayor=pmpatente
         pmhora=time.time()-pmtiempo
      elif pmmayor<pmpatente:
         print("3. mayor: ", pmmayor,"nueva es: ",pmnueva,"patente: ",pmpatente)
         a=input()
         pmmayor=pmpatente
         pmhora=time.time()-pmtiempo
         
   elif len(pmmayor)<len(pmpatente) and pmmayor<pmpatente:
      print("4. mayor: ", pmmayor,"nueva es: ",pmnueva,"patente: ",pmpatente)
      a=input()
      pmmayor=pmpatente
      pmhora=time.time()-pmtiempo
   print("5. mayor: ", pmmayor,"nueva es: ",pmnueva,"patente: ",pmpatente)
   

      
   
#   if patente[2] in numeros and mayor<patente:
#      mayor=patente
#      hora=time.time()-tiempo
#   elif mayor<patente:
#      mayor=patente
#      hora=time.time()-tiempo
   return hora,mayor,nueva



def pase(moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,tipo,forma,mayor,hora,patente,tiempo,numeros,primera):
    if tipo==1:
        moto+=1
        precio=20
    elif tipo==2:
        precio=40
        auto+=1
    else:
        precio=80
        camion+=1
    if forma=='1':
        cantefe+=1
        efectivo+=precio
    else:
        canttelep+=1
        telepeaje+=precio
    if forma=='2':  
       patente_ok=patemayor(hora,tiempo,numeros,nueva, mayor)
    return hora,moto,auto,precio,efectivo,telepeaje,canttelep,cantefe,mayor


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
    
        
                
                
                
            
                






    
