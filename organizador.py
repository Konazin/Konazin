import os
import shutil

camin = str(input('adicione o caminho da pasta corretamente'))
faz = str(input('o que quer fazer? [copiar][apagar]'))

def copia():
    arquivo = str(input('adicione o caminho com o arquivo que deseja copiar'))
    try:
        shutil.copy(arquivo, camin)
        print('arquivo copiado para o diretório:' + camin)
    except shutil.SameFileError:
        print('já existe um arquivo com o mesmo nome')

def apagar():
    os.remove(camin)
    print('arquivo apagado')
if faz == 'copiar':
    copia()
elif faz == 'apagar':
    apaga()
