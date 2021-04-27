import time
import paho.mqtt.client as paho
import logging

# Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s > %(name)s > %(levelname)s: %(message)s')

broker = "localhost" #aquí deberíamos indicar si hay otra maquina

client = paho.Client("client-publish", clean_session=True)
client.username_pw_set(username="mosquitto", password="mosquitto") #CAMBIAR CONTRA

logging.debug(f'Connecting to broker {broker}')
client.connect(broker)


message = "Mi primer mensaje"
logging.info(f"publishing: {message}")
client.publish("kaixo/mundua/mezuak", message)

time.sleep(4)

message = "Mi segundo mensaje"
logging.info(f"publishing: {message}")
client.publish("kaixo/mundua/mezuak", message)
time.sleep(4)

message = "Mi tercer mensaje"
logging.info(f"publishing: {message}")
client.publish("kaixo/mundua/mezuak", message)

time.sleep(4)

message = "Mi cuarto mensaje"
logging.info(f"publishing: {message}")
client.publish("kaixo/mundua/mezuak", message)

time.sleep(4)

message = "Mi quinto mensaje"
logging.info(f"publishing: {message}")
client.publish("kaixo/mundua/mezuak", message)

time.sleep(4)

message = "Mi sexto mensaje"
logging.info(f"publishing: {message}")
client.publish("kaixo/mundua/mezuak", message)


client.disconnect() #aquí desconecto el servidor, pero podría dejarlo funcionando
