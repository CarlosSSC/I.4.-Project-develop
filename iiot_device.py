from random import randint
 
# POO en Python
# Definición de la clase
class Sensor:
 
    # Constructor de la clase
    def __init__(self):
        # Funciona pa' Linux
        #self._sensor = psutil.sensors_temperatures()
        # Funciona pa' Windows... ojalá
        #self._wmi = wmi.WMI(namespace='root/OpenHardwareMonitor')
        pass
    def get_temp(self):
        return self._sensor['coretemp']
    
    # Simular 'la toma de algún valor de otro sensor'
    def get_random_number(self):
        return randint(0, 99)
 
#def get_temp_for_windows(self):
 #   return self._wmi