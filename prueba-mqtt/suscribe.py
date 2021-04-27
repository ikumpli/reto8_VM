import time
import paho.mqtt.client as paho
import logging

# Logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s > %(name)s > %(levelname)s: %(message)s')


def on_connect(client, userdata, flags, rc):
    logging.debug(f'Connected with result code {rc}')
    logging.debug("Subscribing")
    client.subscribe("#")  # Warning! (read comment below)
    logging.debug("Subscribed")
    """
    Good and bad practices (https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices):
    - Usually subscribing just to the multilevel wildcard (#) is a bad practice, too much load.
    - Never use a leading slash => /kaixo/mundua/mezuak adds an unnecessary topic level.
    - Never use spaces in a topic => leads to confusion.
    - Keep the topic short and concise => it is sent in every single message.
    - Use only ASCII characters => Otherwise is difficult to find typos as when printing the topic they do not show.
    - Use specific topics, not general ones. For example, if you have three sensors in your living room, 
      create topics for myhome/livingroom/temperature, myhome/livingroom/brightness and myhome/livingroom/humidity. 
      Do not send all values over myhome/livingroom. Use of a single topic for all messages is a anti pattern. 
    
    Other subscription examples:
    - client.subscribe(kaixo/mundua/mezuak).
    - client.subscribe(kaixo/+/mezuak) # single level wildcard (+).
    - client.subscribe(kaixo/#) # multilevel wildcard (#).
    
    There are topics beggining with $, they are reserved for internal statistics of the MQTT broker:
    - $SYS/broker/clients/connected
    - $SYS/broker/clients/disconnected
    - $SYS/broker/clients/total
    - $SYS/broker/messages/sent
    - $SYS/broker/uptime
    """


def on_message(client, userdata, message):
    logging.info(f'On message:\n\nMessage: {message.payload.decode("utf-8")}\nTopic: {message.topic}\n')


# Connection
broker = "localhost"
client = paho.Client("client-subscribe")
client.username_pw_set(username="mosquitto", password="mosquitto")
client.on_connect = on_connect
client.on_message = on_message
logging.debug(f'Connecting to broker {broker}')
client.connect(broker)
logging.debug("Start loop")
client.loop_forever()
