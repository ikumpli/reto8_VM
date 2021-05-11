
from datetime import datetime

from geopy.extra.rate_limiter import RateLimiter
import random
import requests
import json
import numpy as np


class generar_datos:
        
    def __init__(self, provincia, coordenadas):
        self.coordenadas = coordenadas
        self.provincia = provincia
        api_con = "3c59b4cb36f2e57db2f4dd1eb44d752d"
        url0 = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric"
        #geolocator = Nominatim(user_agent="geoapiExercises")
        #location = geolocator.geocode(self.provincia)
        #lat, lon = 37.992241, -1.130654 #location.latitude, location.longitude
        lat, lon = coordenadas.latitude, coordenadas.longitude
        url = url0 % (lat, lon, api_con)
        response = requests.get(url)
        data = json.loads(response.text)
        data['ubicacion'] = self.provincia
        self.data = data


    def agua(self):
        prob_lluvia = int([(lluvia['precipitation']) for lluvia in self.data['minutely']][-1])
        agua = bool(np.where(prob_lluvia == 0, False, True))
        return agua

    def nivel_agua(self):
        prob_lluvia = int(int([(lluvia['precipitation']) for lluvia in self.data['minutely']][-1]))

        if prob_lluvia == 0:
            nivel = 0
        elif prob_lluvia <= 20:
            nivel = 1
        elif (prob_lluvia > 20 & prob_lluvia <= 40):
            nivel = 2
        elif (prob_lluvia > 40 & prob_lluvia <= 60):
            nivel = 3
        elif (prob_lluvia > 60 & prob_lluvia <= 80):
            nivel = 4
        else:
            nivel = 5
        return(nivel)

    def humedad(self):
        humedad = self.data['current']['humidity']
        return(humedad)

    def GPS(self):
        return(str((self.coordenadas.latitude, self.coordenadas.longitude)))

    def lugar_instalacion(self):
        if self.provincia == "barcelona":
            lugar = {'industrial': 'mediana', 'renovables': 'eolica', 'distribucion_publica': 'urbana'}
        if self.provincia == "caceres":
            lugar = {'industrial': 'grande', 'renovables': 'solar', 'distribucion_publica': 'urbana'}
            
        else:
            lugar = {'industrial': 'grande', 'renovables': 'solar', 'distribucion_publica': 'rural'} 
        return(json.dumps(lugar))

    def temperatura(self):
        temp = self.data['current']['temp']
        return(temp)


    def clima(self):
        clima = self.data['current']['weather'][0]['description']
        return(clima)

    def humo(self):
        humo = bool(random.getrandbits(1))
        return(humo)

    def puerta_abierta(self):
        booleano = bool(random.getrandbits(1))
        return(booleano)

    def tension(self):
        tension = random.randrange(220, 440)
        return(tension)
