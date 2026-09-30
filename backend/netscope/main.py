from fastapi import FastAPI

# traemos las 3 funciones

from netscope.scanner.arp import (
    obtener_ip_con_mascara,
    calcular_subred,
    escanear_red,
)

# creamos la app "app" que es el objeto que uvicorn
# arranca y al que le llegan las petciones

app = FastAPI()

# la linea del @ le dice a FastAPI
# que cuando llegue una petición GET a la ruta "/scan"
# ejecute la función scan()

@app.get("/scan")
def scan():
    # obtenemos la ip con mascara de la interfaz que usa scapy
    ip_con_mascara = obtener_ip_con_mascara()

    # calculamos la subred a partir de esa ip con mascara
    subred = calcular_subred(ip_con_mascara)

    # escaneamos la red y obtenemos la lista de dispositivos
    dispositivos = escanear_red(subred)

    return {"subred": subred, "dispositivos": dispositivos}