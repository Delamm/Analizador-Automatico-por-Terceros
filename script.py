import webbrowser # Librería para automatizar en navegador
import pyperclip # Sirve para copiar y pegar cosas en python
import pyautogui # Automatizar que se ejecute una tecla por ej el espacio
import time # Nos va a ayudar a evitar errores
from colorama import Fore, Style # Colores

with open('addresses.txt','r') as f:
    f = f.read().split('\n')

election = input(Fore.GREEN + "Escribe el nombre de la herramienta que quieras utilizar para analizar las direcciones IP: "
+ Fore.YELLOW + """\n1 - Symantec
2 - AbuseIP
3 - VirusTotal: \n""" + Style.RESET_ALL + "Su elección --> ")

election = int(election)
 # El usuario elige Symantec
if election == 1:
    for ip in f:
        webbrowser.open_new("https://sitereview.bluecoat.com/#/")
        time.sleep(3)
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl','v', interval=0.05)
        pyautogui.press('enter')
 # El usuario elige AbuseIP
elif election == 2:
    for ip in f:
        webbrowser.open_new("https://www.abuseipdb.com/")
        time.sleep(2.5)
        # Para poder pegar algo primero tenemos que llegar al input apretando 15 veces TAB
        for i in range(15):
            pyautogui.press('tab')
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl','v', interval=0.15)
        pyautogui.press('enter')
 # El usuario elige VirusTotal
elif election == 3:
    for ip in f:
        webbrowser.open_new("https://www.virustotal.com/gui/home/search")
        time.sleep(2.5)
        for i in range(6):
            pyautogui.press('tab')
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl','v', interval=0.15)
        pyautogui.press('enter')
else:
    raise ValueError("Debe insertar numeros del 1 al 3 inclusive.")