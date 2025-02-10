import shutil
import pyautogui
import os, webbrowser

#esse codigo foi feito por um fresco

senha = ""#não ta obvio o que é pra ser aqui?
senha2 = input("digite sua senha:")
caminho = ''#botar o caminho do arquivo

if senha == senha2:
    print('acesso concedido')
    os.path.exists(caminho)
    webbrowser.open(os.path.realpath(caminho))
else:
    print("acesso negado")