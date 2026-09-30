import re # permite buscar un trozo de texto dentro de otro texto
import subprocess # permite ejecutar comandos del sistema desde python
import ipaddress # herramienta de python para trabajar con ips

from scapy.all import conf # de la lbreria solo sacamos conf que es donde guarda la config
# como la interfaz de red que se usa

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