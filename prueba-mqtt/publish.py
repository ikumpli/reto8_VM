import time
import paho.mqtt.client as paho
import logging

# Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s > %(name)s > %(levelname)s: %(message)s')

broker = "localhost" #aquí deberíamos indicar si hay otra maquina

client = paho.Client("client-publish", clean_session=True)
client.username_pw_set(username="user", password="user") #CAMBIAR CONTRA

logging.debug(f'Connecting to broker {broker}')
client.connect(broker)


message = "33 grados" #mensaje
logging.info(f"publishing: {message}")
client.publish("temperatura", message) #TOPIC

time.sleep(4)

message = "Soleado"
logging.info(f"publishing: {message}")
client.publish("tiempo", message)
time.sleep(4)

message = "32 grados"
logging.info(f"publishing: {message}")
client.publish("temperatura", message)

time.sleep(4)

message = "Soleado"
logging.info(f"publishing: {message}")
client.publish("tiempo", message)

time.sleep(4)

message = "28 grados"
logging.info(f"publishing: {message}")
client.publish("temperatura", message)

time.sleep(4)

message = "Nuboso"
logging.info(f"publishing: {message}")
client.publish("tiempo", message)


client.disconnect() #aquí desconecto el servidor, pero podría dejarlo funcionando
