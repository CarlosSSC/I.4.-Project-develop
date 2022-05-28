from http import client
from iiot_device import Sensor
import json
import time

#Creacion de un objeto de la clase HTTPConnetion
_conn = client.HTTPConnection('localhost', port=5000)

#Creacion de un objeto de la clase Sensor
s = Sensor()
h = {'Content-type': 'application/json'}  

while True:
    data = {
        'id': 1,
        'name': 'Temp Sensor',
        'value': s.get_random_number()
    }

    json_data = json.dumps(data)

    _conn.request('POST', '/devices', json_data, headers=h)
    _conn.close()
    _conn.request('GET', '/devices', json_data, headers=h)
    _conn.close()


    value = data['value']
    if value >= 15:
        print(value ," -- Its more or equal to 15°")
    else:
        print(value ," -- Its less than 15°")

    time.sleep(1)