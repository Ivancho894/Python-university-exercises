import time
import random
#global moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,tiempo,mayor,nueva,patente,tipo,forma,precio
letras=('abcdefghijklmnñopqrstuvwxyz')
numeros=('0123456789')
primer=0
segundo=0
tercero=0
cuerto=0

moto,auto,sonlas,efectivo,telepeaje,camion,cantefe,canttelep,hora,ti=0,0,0,0,0,0,0,0,0
def manual():
   letras=('abcdefghijklmnñopqrstuvwxyz')
   numeros=('0123456789')
   tiempo=time.time()
   while (time.time()-tiempo)<=240:
      global tipo,forma,patente
      a=input("Enter para ingresar nuevo vehiculo")
      tipo=input("¿Que tipo de vehiculo es, moto, auto o camion")
      forma=input("¿Forma de pago? efectivo o telepeaje")
      if forma=='2':
         patente=input("¿Cual es la patente del vehiculo?")
      control_ok=control(tipo,forma,patente)
      pase_ok=pase()




def control():
   letras=('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
   numeros=('0123456789')
   while tipo!='1' and tipo!='2' and tipo!='3':
      tipo=input("Ingresaste mal el tipo de vehiculo, por favor ingreselo de nuevo((1)moto,(2)auto o (3)camion)")
   while forma!='1' and forma!='2':
      forma=input("Ingresaste mal la forma de pago, por favor ingreselo de nuevo((1)efectivo o (2)telepeaje")
   if forma=='2':
      while (patente[0]!=letras and patente[1]!=letras and patente[2]!=letras and patente[3]!=numeros and patente[4]!=numeros and patente[5]!=numeros) or (patente[0]!=letras and patente[1]!=letras and patente[2]!=numeros and patente[3]!=numeros and patente[4]!=numeros and patente[5]!=letras and patente[6]!=letras):
         patente=input("Ingreso mal la patente,por favor ingresela de nuevo")
   
      



def automatico():
   primera=True
   vehiculos=('una moto','un auto','un camion')
   pat=('efectivo','telepeaje')
   mayor='aaa000'
   patente='aaa000'
   tiempo=time.time()
   nueva=True
   banderas=(True,False)
   while (time.time()-tiempo)<=5:
      sonlas=time.time()
      paso=random.choice(banderas)
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
         print("Pasó",tipo,printeo,"que pagó con",forma,)
         print(tiempo)
         #time.sleep(5)
   print_ok=printeos()


def patemayor():

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
    global moto,auto,efectivo,telepeaje,camion,cantefe,canttelep,tipo,forma,mayor,hora,patente,tiempo,numeros,primera,primer,segundo,tercero,cuerto
   
    if sonlas-tiempo==240:
       cuerto=auto+moto+camion-tercero
    elif sonlas-tiempo==180:
       tercero=auto+moto+camion-segundo
    elif sonlas-tiempo==120:
       segundo=auto+moto+camion-primer
    else:
       primer=auto+moto+camion
    if tipo=='una moto'or tipo=='1':
        moto+=1
        precio=20
        printt=str("auto")
    elif tipo=='un auto' or tipo=='2':
        precio=40
        auto+=1
        printt=str("moto")
    else:
        precio=80
        camion+=1
    if forma=='efectivo'or forma=='1':
        cantefe+=1
        efectivo+=precio
    else:
        canttelep+=1
        telepeaje+=precio  
        patente_ok=patemayor()
def printeos():
   print("Cantidad de autos: ",auto)
   print("Cantidad de camiones: ",camion)
   print("Cantidad de motos: ",moto)
   print("Recaudación de efectivo: $",efectivo)
   print("Recaudación por telepeaje: $",telepeaje)
   total=efectivo+telepeaje
   print("Total recaudado con efectivo y telepeaje: $",total)
   totalpases=moto+auto+camion
   print("Total de pases en el turno: ",totalpases)
   
   if efectivo<telepeaje:
      print("Las pasadas con telepeaje fueron mayores que con efectivo")
   else:
      print("Las pasadas con efectivo fueron matores que con telepeaje")
   print("La patente mas nueva fue: ",mayor," y paso a los ",hora,"minutos desde que empezo el turno")
   if primer>segundo and primer>tercero and primer>cuerto:
      horapico=str("primera")
   elif segundo>tercero and segundo>cuerto:
      horapico=str("segunda")
   elif tercero>cuerto:
      horapico=str("tercera")
   else:
      horapico=str("cuerta")
   print("La hora pico fue en la ",horapico,"hora")

   
   print("La hora pico horapico fue en la ",horapico,"hora del turno")
   


  
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
    
        
                
                
                
            
                






    
