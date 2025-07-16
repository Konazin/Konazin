import os
import shutil

camin = str(input('adicione o caminho da pasta corretamente'))
faz = str(input('o que quer fazer? [copiar][apagar]'))
arquivo = 

def copia():
    shutil.copy(dst=camin, )
    print('arquivo copiado')

def copiadir():
    try:
         shutil.copy(arquivo, )
    except shutil.SameFileError:

def apagar():
    os.remove(camin)
    
if faz == 'copiar':
    copia()
elif faz == 'apagar':
    apaga()
