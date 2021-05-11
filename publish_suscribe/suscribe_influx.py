from datetime import datetime
from influxdb import InfluxDBClient
import logging
import paho.mqtt.client as paho
 
 # Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s > %(name)s > %(levelname)s: %(message)s') 

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe('#')
 
#client.get_list_database()
influx_client = InfluxDBClient('localhost', 8086, database='ormazabal')
influx_client.create_database('ormazabal')
  	
    	
def on_message(client, userdata, message):
    #current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if message.topic.split('/')[1] == 'ambiente':
        valor = float(message.payload.decode('utf-8'))
    if message.topic.split('/')[1] == 'ubicacion':
        valor = message.payload.decode('utf-8')
    if message.topic.split('/')[1] == 'elementos':
        if message.payload.decode('utf-8') == "True":
            valor = bool(1)
        else:
            valor = bool(0)
        
    json_body = [
    {
        "measurement": message.topic.split('/')[1],
        "tags": {
            "CT": message.topic.split('/')[0],
            "sensor": message.topic.split('/')[2]
        },
     
        "fields": {
            "time": datetime.now().timestamp(),
    
            "value": valor
        }
    }
    ]
    
    influx_client.write_points(json_body)
    logging.info(f'On message:\n\nMessage: {message.payload.decode("utf-8")}\nTopic: {message.topic}\n')






 
 
# Connection
broker = "localhost"
client = paho.Client("client-subscribe") 
client.username_pw_set(username="ama", password="ama") 
client.on_connect = on_connect
client.on_message = on_message
logging.debug(f'Connecting to broker {broker}')
client.connect(broker)
logging.debug("Start loop")
client.loop_forever() 
