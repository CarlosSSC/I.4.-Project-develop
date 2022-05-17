"""
@author Carlos Salazar
@since 2022-05-17
@descrip I.1. Aplicación Cliente-Servidor
"""

# Inclusion de modulos

from flask import Flask, request

app = Flask('__main__')


device = {
    "code": "12312414",
    "descrip": "Temp, sensor",
    "value": 67
}

@app.route('/devices', methods=['GET'])
def go_home():
    return device
    
    #Save an user
@app.route('/users', methods=['POST'])
def save_users():
    user = request.json
    print(user)
    return user
    
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    return device



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')