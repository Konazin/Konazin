from scapy.all import IP, TCP, Raw, sniff
from datetime import datetime
import string  


def para_binario(payload):
    return ' '.join(format(byte, '08b') for byte in payload)


def log(origem, destino, porta_o, porta_d, content):
    with open("sniffer_payload.log", "a", encoding="utf-8") as f:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{agora}] {origem}:{porta_o} -> {destino}:{porta_d}\n")
        f.write(f"payload {content}\n\n")

def tratar_pacote(pacote):
    if IP in pacote and TCP in pacote and Raw in pacote:
        src = pacote[IP].src
        dst = pacote[IP].dst
        sport = pacote[TCP].sport
        dport = pacote[TCP].dport
        payload_raw = pacote[Raw].load

        try:
            texto = payload_raw.decode('utf-8')
            formato = "UTF-8"
        except UnicodeDecodeError:
            
            try:
                
                printable_part = "".join(chr(b) if chr(b) in string.printable else '.' for b in payload_raw)
                hex_part = payload_raw.hex()
                
                
                texto = f"ASCII (tentativa): {printable_part}\nHEX: {hex_part}"
                formato = "ASCII/HEX"
            
            except Exception:
                
                try:
                    texto = payload_raw.hex()
                    formato = "HEX"
                except:
                    
                    texto = para_binario(payload_raw)
                    formato = "BIN"
            

        log(src, dst, sport, dport, texto)

print("Sniffando... Ctrl+C para parar")
sniff(filter="tcp", prn=tratar_pacote, store=0)