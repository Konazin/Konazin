import string
import pyzipper
from itertools import product

cs = int(input('quantos digitos tem(ou você acredita que tenha) a senha?: '))
arq = str(input('adicione o caminho do zip: '))
senha = string.digits + string.ascii_lowercase + string.ascii_uppercase

def ext(sen):
    try:
        with pyzipper.AESZipFile(arq, 'r') as zp:
            zp.extractall(pwd=sen.encode())
        return True
    except:
        return False

for comb in product(senha, repeat= cs):
    res = ''.join(comb)
    print(f'Testando: {res}')
    if ext(res):
        print(f'violado com: {res}')
        break