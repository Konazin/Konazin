import pyautogui
import random
import os
#roleta russa doida pra krl

def jogador():
    int(input("digite um numero de 1 a 6"))
def bala():
    random.choice([1,2,3,4,5,6])

if jogador == bala:
    print("boa mano, ganhou dessa vez a roleta russa mais dificil do planeta")
    exit()

else:
    print("acho que fudeu")
    pyautogui.press('win')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.press('l')
    pyautogui.press('o')
    pyautogui.press('enter')