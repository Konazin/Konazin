import string
import pyzipper
from itertools import product

arq = str(input('adicione o caminho do zip:'))
force = []
senha = string.digits

def ext(sen):
    try:
        with pyzipper.AESZipFile(arq, 'r') as zp:
            zp.extractall(pwd=sen.encode())
        return True
    except:
        return False

for comb in product(senha, repeat=3):
    res = ''.join(comb)
    print(f'Testando: {res}')
    if ext(res):
        print(f'violado com: {res}')
        break