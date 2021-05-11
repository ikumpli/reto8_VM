import time
import paho.mqtt.client as paho
import logging
from datetime import datetime, timezone
from elasticsearch import Elasticsearch

# Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s > %(name)s > %(levelname)s: %(message)s')

def on_connect(client, userdata, flags, rc):
    logging.debug(f'Connected with result code {rc}')
    logging.debug("Subscribing")
    client.subscribe("#")
    logging.debug("Subscribed")



def on_message(client, userdata, message):
    logging.info(f'On message:\n\nMessage: {message.payload.decode("utf-8")}\nTopic: {message.topic}\n')
    tension = int(message.payload.decode('utf-8').split('_')[0])
    temperatura = int(message.payload.decode('utf-8').split('_')[1])
    
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    doc = {
        '@timestamp':  datetime.now(timezone.utc),
        'tension': tension,
        'temperatura': temperatura}
    res = es.index(index="pub_sus_elastic", body=doc)

# Connection
broker = "localhost"
client = paho.Client("client-subscribe")
client.username_pw_set(username="iker", password="iker")
client.on_connect = on_connect
client.on_message = on_message
logging.debug(f'Connecting to broker {broker}')
client.connect(broker)
logging.debug("Start loop")
client.loop_forever()
