import paho.mqtt.client as paho
import logging
import sensores_publish as sp
import api_openweathermap as api
from threading import Thread
from geopy.geocoders import Nominatim


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s > %(name)s > %(levelname)s: %(message)s')
broker = "localhost" 

client = paho.Client("client-publish", clean_session = True)
client.username_pw_set(username = "ama", password = "ama") #por defecto, hay que cambiarla

logging.debug(f'Connecting to broker {broker}')
client.connect(broker)

#datos = api.generar_datos('murcia')

provincia = "barcelona"
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode(provincia)
c1 = sp.publicar(provincia,location, "temperatura", client, logging)
t1 = Thread(target = c1.run) 

c2 = sp.publicar(provincia, location,"humedad", client, logging)
t2 = Thread(target = c2.run) 

c3 = sp.publicar(provincia,location, "nivel_agua", client, logging)
t3 = Thread(target = c3.run) 

c4 = sp.publicar(provincia, location,"tension", client, logging)
t4 = Thread(target = c4.run) 

c5 = sp.publicar(provincia, location,"GPS", client, logging)
t5 = Thread(target = c5.run) 

c6 = sp.publicar(provincia, location,"lugar_instalacion", client, logging)
t6 = Thread(target = c6.run) 

c7 = sp.publicar(provincia,location, "clima", client, logging)
t7 = Thread(target = c7.run) 

c8 = sp.publicar(provincia, location,"agua", client, logging)
t8 = Thread(target = c8.run) 

c9 = sp.publicar(provincia,location, "humo", client, logging)
t9 = Thread(target = c9.run) 

c10 = sp.publicar(provincia,location, "puerta_abierta", client, logging)
t10 = Thread(target = c10.run) 



provincia = "sevilla"
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode(provincia)
c11 = sp.publicar(provincia,location, "temperatura", client, logging)
t11 = Thread(target = c11.run) 

c12 = sp.publicar(provincia, location,"humedad", client, logging)
t12 = Thread(target = c12.run) 

c13 = sp.publicar(provincia,location, "nivel_agua", client, logging)
t13 = Thread(target = c13.run) 

c14 = sp.publicar(provincia, location,"tension", client, logging)
t14 = Thread(target = c14.run) 

c15 = sp.publicar(provincia, location,"GPS", client, logging)
t15 = Thread(target = c15.run) 

c16 = sp.publicar(provincia, location,"lugar_instalacion", client, logging)
t16 = Thread(target = c16.run) 

c17 = sp.publicar(provincia,location, "clima", client, logging)
t17 = Thread(target = c17.run) 

c18 = sp.publicar(provincia, location,"agua", client, logging)
t18 = Thread(target = c18.run) 

c19 = sp.publicar(provincia,location, "humo", client, logging)
t19 = Thread(target = c19.run) 

c20 = sp.publicar(provincia,location, "puerta_abierta", client, logging)
t20 = Thread(target = c20.run) 



for x in range(1, 21):
   func = f"t{x}.start()"
   eval(func) #ejecuta el string

#c.terminate() 

#client.disconnect() #para desconectar hacer un desconet, deberia de estar conectado
