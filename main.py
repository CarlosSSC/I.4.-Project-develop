"""
@author Carlos Salazar
@since 2022-05-28
@descrip I.4. Project develop
"""

# Inclusion de modulos
from flask import Flask, request

import http.client
import json

class httpConecction:

    def __init__(self, host, port):
        try:
            self._conn=http.client.HTTPConnection(host, port)
        except Exception as ex:
            return ex
    def send_data(self, data):
        headers = {'Content-type': 'application/json'} 
        json_data = json.dumps(data)
        self._conn.request('POST', '/', json_data, headers)
        self._conn.close()
        return 'ok'

app = Flask('__main__')

device = {
    "code":"112233",
    "descrip":"Temp. Sensor",
    "value": 65
}

@app.route('/devices', methods=['GET'])
def get_device():
    if device['value'] > 15:
        num = device['value']
        return ' Its more than 15°'
    else:
       return 'Its less than 15°'
      

#Save an devices
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print(device)
    return device, 201

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')