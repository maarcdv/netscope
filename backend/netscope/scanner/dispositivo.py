# traemos el dataclass de la libreria de python
from dataclasses import dataclass

# El "@dataclass" de arriba es un decorador: le dice a Python que esta clase
# es una ficha de datos. Con solo eso, Python genera por nosotros el código
# para crear fichas, mostrarlas por pantalla y compararlas.
@dataclass

# una class es una clantilla para crear objetos. La plantilla
# se llama dispositivo, y cada dispositivo encontrado en la red sera un objeto

class Dispositivo:
    # estas son las propiedades de la clase, que seran los datos que guardaremos
    # de cada dispositivo encontrado en la red
    ip: str
    mac: str