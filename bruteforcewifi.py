import random
import scapy
from scapy.all import *
from multiprocessing import pool, cpu_count

wifi = str(input("adicione o ip da rede: "))
dist = int(input("adicione a quantidade de digitos da senha: "))
mac = str(input("digite o endereço mac"))

def cheiro():
    