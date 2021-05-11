import time
import paho.mqtt.client as paho
import logging
import random
import datetime
# Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s > %(name)s > %(levelname)s: %(message)s')

broker = "localhost"

client = paho.Client("client-publish", clean_session=True)
client.username_pw_set(username="iker", password="iker")

logging.debug(f'Connecting to broker {broker}')
client.connect(broker)

while True:
    tension = str(random.randrange(220, 440))
    temperatura = str(random.randrange(25, 30))
    mensaje = str(tension+"_"+temperatura)
    
    logging.info(f"publishing: {mensaje}")
    client.publish("iker/prueba1", mensaje)
    
   
    time.sleep(10)

client.disconnect()
