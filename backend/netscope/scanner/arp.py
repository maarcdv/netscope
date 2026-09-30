import re # permite buscar un trozo de texto dentro de otro texto
import subprocess # permite ejecutar comandos del sistema desde python
import ipaddress # herramienta de python para trabajar con ips

from scapy.all import conf # de la lbreria solo sacamos conf que es donde guarda la config
# como la interfaz de red que se usa

from scapy.all import ARP, Ether, srp
from netscope.scanner.dispositivo import Dispositivo

def obtener_ip_con_mascara():
    interfaz = conf.iface
    salida = subprocess.run(
        ["ip", "-4", "-o", "addr", "show", "dev", str(interfaz)],
        capture_output=True,
        text=True,
    ).stdout
    coincidencia = re.search(r"inet (\S+)", salida)
    return coincidencia.group(1)


def calcular_subred(ip_con_mascara):
    interfaz = ipaddress.ip_interface(ip_con_mascara)

    return str(interfaz.network)

## Descubrir MAC de cada Dispositivo

def escanear_red(subred):

    ## AI

    # Construimos el paquete que vamos a enviar, en dos capas unidas con "/":
    #   Ether(dst="ff:ff:ff:ff:ff:ff") -> la capa de enlace. Esa MAC de destino
    #       especial significa "a todos los equipos de la red" (broadcast).
    #   ARP(pdst=subred) -> la pregunta ARP. "pdst" es la IP por la que
    #       preguntamos. Al darle una subred entera, Scapy genera una pregunta
    #       para cada IP (192.168.1.0, .1, .2 ... .255).
    peticion = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=subred)

    # srp envía los paquetes y recoge las respuestas ("sr" = send/receive,
    # la "p" indica que trabaja a nivel de enlace, donde viven las MAC).
    #   timeout=2 -> espera 2 segundos a las respuestas y se rinde
    #   verbose=False -> que Scapy no llene la pantalla de mensajes
    # Devuelve dos cosas: las preguntas que tuvieron respuesta y las que no.
    # Solo nos interesan las primeras; la "_" es la forma habitual de decir
    # "esta segunda parte la ignoro".
    respuestas, _ = srp(peticion, timeout=3, retry=2, verbose=False)
    # las ips que no contestan vuelven a preguntar 2 veces mas

    # Lista vacía donde iremos guardando los dispositivos encontrados.
    dispositivos = []

    for enviado, recibido in respuestas:
        # recibido.psrc -> la IP de quien contesta (source IP)
        # recibido.hwsrc -> la MAC de quien contesta (source hardware address)
        # Con esos dos datos rellenamos la ficha y la añadimos a la lista.
        dispositivos.append(Dispositivo(ip=recibido.psrc, mac=recibido.hwsrc))

    # Devolvemos la lista completa.
    return dispositivos

# El programa pregunta a 256 direcciones para tratar de encontrar dispositivos.