import random
import string 

cs = int(input('adicione a quantidade de caracteres para a senha'))
q1 = str(input('deve conter caracteres especiais? [y][n]'))
q2 = str(input('deve conter numeros?[y][n]'))

senhap = []
cha1 = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
cha2 = string.ascii_lowercase + string.ascii_uppercase

if q1 and q2 == 'y':
    for _ in range(cs):
        ran = random.randint(1,2)
        if ran == 1:
            senha = random.choice(cha1)
        else:
            senha = str(random.randint(0,9))
        senhap.append(senha)

if q1 == 'n' and q2 == 'y':
    for _ in range(cs):
        ran = random.randint(1,2)
        if ran == 1:
            senha = random.choice(cha2)
        else:
            senha = str(random.randint(0,9))
        senhap.append(senha)

if q1 =='y' and q2 == 'n':
    for _ in range(cs):
        ran = random.randint(1,2)
        senha = random.choice(cha1)
        senhap.append(senha)

if q1 and q2 == 'n':
    for _ in range(cs):
        ran = random.randint(1,2)
        if ran == 1:
            senha = random.choice(cha2)
        else:
            senha = str(random.randint(0,9))
        senhap.append(senha)

print(''.join(senhap))