import string
import pyzipper
from itertools import product
from multiprocessing import Pool, cpu_count

esc1 = str((input('incluir letras?[y][n] ')))
esc2 = str(input('incluir numeros? [y][n] '))
esc3 = str(input('incluir caracteres especiais?[y][n] '))
cs = int(input('tamanho estimado da senha?: '))
arq = str(input('adicione o caminho do zip: '))

senha = ''
if esc1 == 'y':
    senha += string.ascii_letters
if esc2 == 'y':
    senha += string.digits
if esc3 == 'y':
    senha += string.punctuation
if not senha:
    print('sem seleção, encerrando...')
    exit()

def ext(sen):
    try:
        with pyzipper.AESZipFile(arq, 'r') as zp:
            zp.extractall(pwd=sen.encode())
        return (sen, True)
    except:
        return (sen, False)

def res():
    for sla in product(senha, repeat=cs):
        yield ''.join(sla)

if __name__ == "__main__":
    with Pool(cpu_count()) as pool:
        for comb, sus in pool.imap_unordered(ext, res(), chunksize=500):
            print(f'Testando: {comb}')
            if sus:
                print(f'violado com: {comb}')
                pool.terminate()
                break