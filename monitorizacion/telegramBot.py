import telebot
import requests
from elasticsearch import Elasticsearch 


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
TOKEN = "1819664958:AAG-U2mevCGWAlnIy62FhgVnIBPtsORBBtc"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola!")

@bot.message_handler(commands = ['cti1'])
def send_ct1(message2):

    #res = es.get(index = "pub_sus_elastic", id="UqvYVnkBznQBBrkeSIfm")
    res = es.search(index = "pub_sus_elastic", body={"size":1}, sort='@timestamp:desc')
    msg = "Los valores del cti1 son: %s" %(res["hits"]["hits"][0]["_source"])
    bot.reply_to(message2, msg)
    
bot.polling()
