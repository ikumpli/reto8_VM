
import paho.mqtt.client as paho
import logging
import time
import random
import api_openweathermap as api



class publicar:

    
      
    def __init__(self, provincia, coordenadas, sensor, client, logging):
        self._running = True
        self.sensor = sensor
        self.provincia = provincia
        self.client = client
        self.logging = logging
        self.coordenadas = coordenadas
        #self.datos = datos
        
        

    def run(self): 
    	
             
        while self._running:  #while true
            
            datos = api.generar_datos(self.provincia, self.coordenadas)
            #funcion = f"api_openweathermap.sensores('{self.ubicacion}').{self.sensor}()"
            funcion = f"datos.{self.sensor}()"
            valor = eval(funcion)
            #valor = random.randint(4, 8)
            #valor2 = 'a'
            #self.client.publish("elementos/nivel_agua", None, retain = True) 
            if self.sensor in (['temperatura', 'humedad', 'nivel_agua', 'tension']): 
                self.logging.info(f"publishing {self.sensor}: {valor}")
                #valor = random.randint(4, 7)
                self.client.publish(datos.data['ubicacion'] + "/ambiente/"+self.sensor, valor)
                time.sleep(20)
                
            if self.sensor in (['GPS', 'lugar_instalacion', 'clima', 'nivel_agua']): 
                self.logging.info(f"publishing {self.sensor}: {valor}")               
                self.client.publish(datos.data['ubicacion'] + "/ubicacion/"+self.sensor, valor)
                time.sleep(60)
                
            if self.sensor in (['agua', 'humo', "puerta_abierta"]): 
                self.logging.info(f"publishing {self.sensor}: {valor}")               
                self.client.publish(datos.data['ubicacion'] + "/elementos/"+self.sensor, valor)
                time.sleep(30)
                
