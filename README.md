# NetScope

Escáner y mapeador de redes LAN para Linux.

NetScope analiza tu red local, muestra los dispositivos conectados (IP, MAC, fabricante, puertos abiertos y SO probable), dibuja un mapa de la topología y guarda un histórico de escaneos para avisar de cambios.

> Proyecto en desarrollo · Proyecto Intermodular SMX

![Captura de NetScope](docs/img/banner.jpeg)


## Características

- [ ] Descubrimiento de dispositivos (ARP)
- [ ] Identificación del fabricante (OUI)
- [ ] Escaneo de puertos y detección de SO
- [ ] Mapa visual de la topología
- [ ] Histórico de escaneos (SQLite)
- [ ] Detección de dispositivos nuevos y cambios

## Stack

| Capa | Tecnología |
|------|-----------|
| Escritorio | Electron |
| Interfaz | Next.js + Tailwind CSS |
| Backend | Python, FastAPI |
| Escaneo | Scapy, python-nmap |
| Datos | SQLite |

## Requisitos

- Linux
- Python 3.10 o superior
- Node.js 18 o superior
- nmap

```bash
sudo apt install nmap python3-venv
```

## Instalación

```bash
git clone https://github.com/<tu-usuario>/netscope.git
cd netscope

# Backend
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ..

# Frontend y Electron
cd frontend && npm install && cd ..
cd electron && npm install && cd ..
```

## Uso

Aplicación completa (Electron arranca el backend y abre la ventana):

```bash
cd electron
npm start
```

Modo desarrollo, cada parte por separado:

```bash
# Terminal 1: backend
cd backend && source .venv/bin/activate
uvicorn netscope.main:app --host 127.0.0.1 --port 8000

# Terminal 2: frontend
cd frontend && npm run dev
```

Scapy necesita permisos de red. En desarrollo puedes lanzar el backend con `sudo` o dar capacidades a Python:

```bash
sudo setcap cap_net_raw,cap_net_admin+eip $(readlink -f $(which python3))
```

Estas instrucciones se ajustarán cuando la app esté construida.

## Licencia

MIT
EOF