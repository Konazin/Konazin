import socket

def check_port(host, port, timeout=0.1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        sock.close()
        return True
    except Exception:
        return False

def scan(host, start, end, timeout=0.1):
    open_ports = []
    for port in range(start, end+1):
        if check_port(host, port, timeout):
            print(f"[*] port open = {port}")
            open_ports.append(port)
    if open_ports == []:
        print("[*] no open ports")

def main():
    scan("187.19.226.192", 1, 2048, timeout=0.1)

if __name__ == '__main__':
    main()