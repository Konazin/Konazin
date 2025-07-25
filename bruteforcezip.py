from zipfile import *
import string
import random

arq = str(input('adicione o caminho do zip'))
force = []
senha = string.ascii_uppercase + string.ascii_lowercase + string.punctuation

def brute():
    for _ in range(6):
            cho = random.randint(1,2)
            if cho == 1:
                  force = random.choice(senha)
            else:
                  random.randint(0,9)
with ZipFile(arq, 'r') as zpref:
    pause = False
    while pause == False:
        brute()
        bt = ''.join(force)
        def ext():
             zpref.extractall(path=arq, pwd=bt)
             return True
        if ext == True:
             pause = True
print('Pasta violada')