import string
import pyzipper
from itertools import product

esc1 = str((input('você quer que seja incluida letras?[y][n] ')))
esc2 = str(input('você quer que seja incluida numeros? [y][n] '))
esc3 = str(input('você quer que seja incluido caracteres especiais?[y][n] '))
cs = int(input('quantos digitos tem(ou você acredita que tenha) a senha?: '))
arq = str(input('adicione o caminho do zip: '))

if esc1 and esc2 and esc3 == 'y':
    senha = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
elif esc2 and esc3 == 'y':
    senha = string.digits + string.punctuation
elif esc1 and esc3 == 'y':
    senha = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
elif esc1 and esc2 == 'y':
    senha = string.digits + string.ascii_lowercase + string.ascii_uppercase
elif esc1 == 'y':
    senha = string.ascii_lowercase + string.ascii_uppercase
elif esc2 == 'y':
    senha = string.digits
elif esc3 == 'y':
    senha = string.punctuation
else:
    print('não foi uma escolha válida')
    exit()

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