import pyautogui
import random
import os
import webbrowser
#roleta russa doida pra krl

jogador = int(input("escolha um numero e tente sobreviver:[1] [2] [3] [4] [5] [6]:"))

bala = random.choice([1,2,3,4,5,6])

if jogador >= 7:
    print("mano, tem que ser de 1 a 6 seu merda")
    webbrowser.open_new_tab(url=('Xvideos.com'))
    exit()

if jogador == bala:
    print("Parabéns, contra todas as possibilidades você conseguiu")
    exit()

else:
    print("parabéns, veja o que acontecerá")
    webbrowser.open_new_tab(url='')#dá pra por um ip logger aqui ou algum comando OS