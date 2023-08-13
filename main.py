import json
import requests
import time


Base_URL= "https://127.0.0.1:58000/api/v1/ticket"

data = {

    "aaaUser": {

        "attributes": {

            "name": "admin",

            "pwd": "admin123!"

        }

    }

}

cabecera = {"content-type": "application/json"}

requests.packages.urllib3.disable_warnings()
respuesta = requests.post(url, json.dumps(data), headers=cabecera, verify=False)

respuesta_json = respuesta.json()

# print(respuesta.json())

API_Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
# print("***************************************")

print("API-Token :" + API_Token)

url1 = "https://127.0.0.1:58000/api/v1/network-device"
cabecera = {
    "Content-Type": "application/json"
}

WebToken = {
    "APIC-Cookie": API_Token
}

respuesta1 = requests.get(url1, headers=cabecera, cookies=WebToken,verify=False)
print(respuesta1.json())

def obtener_cantidad_dispositivos(BSASE_URL=None, HEADERS=None):
    response = requests.get(f'{BASE_URL}/obtenerInventario', headers=HEADERS)
    data = response.json()
    cantidad_dispositivos = data.get("cantidad_dispositivos")
    return cantidad_dispositivos

def monitorear_estado(BASE_URL=None, HEADERS=None):
    response = requests.get(f'{BASE_URL}/monitorearEstado', headers=HEADERS)
    data = response.json()
    estado = data.get("estado")
    return estado

def generar_alarma(mensaje):
    print(f"¡Alarma! {mensaje}")

while True:
    try:

        cantidad_actual = obtener_cantidad_dispositivos()

        estado_actual = monitorear_estado()

if cantidad_actual > cantidad_previa:
    generar_alarma("Se detectó un posible dispositivo malicioso agregado a la red.")

if estado_actual != "normal":
    generar_alarma("Se detectó un problema en el estado de la red.")

    cantidad_previa = cantidad_actual

time.sleep(300)

print(f"Error: {e}")
time.sleep(300)