#Medidor de nivel de cisterna de la escuela reportando a Thingspeak
#Proyecto de 5B 2023 (Damaris, Sabrina y Maxi)

from pyTrainer import *

import network, urequests, time
from  hcsr04 import HCSR04

#Medidas de la cisterna
ancho = 3
largo = 5.7
H1 = 0.7
supBase = ancho * largo


def conectaWiFi (red, password): 
    global miRed
    miRed = network.WLAN(network.STA_IF)
    if not miRed.isconnected():
        miRed.active(True)
        miRed.connect(red, password)
        print('Conectando la red', red +"...")
        timeout = time.time ()
        while not miRed.isconnected():
            #wdt.feed ()
            if (time.ticks_diff (time.time (), timeout) > 10):
                return False
    return True
    
red ="Estudiantes"
password ="educar_2018"



while (True):

    time.sleep (30*1)
    
    if conectaWiFi (red, password):
       
        print ("Conexión exitosa!")
        print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    
        url= "https://api.thingspeak.com/update?api_key=XZVCKWET0TLWMIKG"
      
    
        distancia_m = distancia_cm() / 100
        
        print (distancia_m) 
    
        H2 = H1 - distancia_m
    
        volumen = H2*supBase
    
        cantLitros = volumen * 1000
    
        print ("Tenemos = ", cantLitros)
    
        try:
        
            respuesta = urequests.get(url+"&field1="+str(cantLitros))

        except:
            
            print ("Error al enviar datos")
    
        else:
            print (respuesta.text)
            print (respuesta.status_code)
            respuesta.close ()
    
    else:
        print ("Error")
    
        #DistanciaMetros = distancia/100
    
        #if (DistanciaMetros > Profundidad):
        #DistanciaMetros = Profundidad

