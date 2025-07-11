import random
import string

cs = int(input('input here how many characters you want on password'))
cha = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
nome = []

for _ in range(cs):
    ica = random.randint(1,2)
    if ica == 1:
        senha = random.choice(cha)
    else:
        senha = str(random.randint(0,9))
    nome.append(senha)
print(''.join(nome))