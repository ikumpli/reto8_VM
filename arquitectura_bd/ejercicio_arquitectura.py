import pandas as pd
import datetime
import random
import time

df = pd.DataFrame(columns = ["fecha","tension", "temperatura"])
while True:
        tension = random.randrange(220, 440)
        temperatura = random.randrange(25, 30)
        fecha = datetime.datetime.now()
        
        fila = [fecha, int(tension), int(temperatura)]
        fila = pd.Series(fila, index = df.columns)
        df = df.append(fila, ignore_index = True)
        
        df.to_csv("arquitectura.csv", index = False)

        time.sleep(5)
