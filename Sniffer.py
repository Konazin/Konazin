from scapy.all import *

devices = ifaces
print(devices)
interface = input("digite o nome da interface que deseja utilizar: ")

def process_packet(packet):
    print(packet.summary())

sniff(iface=interface,prn=process_packet, store=False)