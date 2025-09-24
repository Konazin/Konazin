import requests
import sys
import argparse

def get_ip(ip: str) -> dict:
    try:
        url = "https://ipwho.is/"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return {"error": f"Falha na requisição, status: {resposta.status_code}"}
    except Exception as e:
        return {"error": str(e)}
    
def main():
    args = str(input("ip: "))
    result = get_ip(args)
    if "error" in result:
        print(f"Erro: {result['error']}")
    else:
        print("""-----result-----""")
        print(f"IP: {result.get('query')}")
        print(f"País: {result.get('country')}")
        print(f"Região: {result.get('regionName')}")
        print(f"Cidade: {result.get('city')}")
        print(f"Provedor (ISP): {result.get('isp')}")
        print(f"Type: {result.get('type')}")
        print(f"domain: {result.get('domain')}")
        print(f"postal: {result.get('postal')}")
if __name__ == "__main__":
    main()