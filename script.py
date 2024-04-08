import webbrowser # Librería para automatizar en navegador
import pyperclip # Sirve para copiar y pegar cosas en python
import pyautogui # Automatizar que se ejecute una tecla por ej el espacio
import time # Nos va a ayudar a evitar errores
from colorama import Fore, Style # Colores

try:
    with open('addresses.txt','r') as f:
        f = f.read().split('\n')
except FileNotFoundError:
    raise FileNotFoundError("No se ha encontrado el archivo con las direcciones IP")

election = input(Fore.GREEN + "Escribe el nombre de la herramienta que quieras utilizar para analizar las direcciones IP: "
+ Fore.YELLOW + """\n1 - Symantec
2 - AbuseIP
3 - VirusTotal: \n""" + Style.RESET_ALL + "Su elección --> ")

election = int(election)

def open_browser(url,tab=0):    
    webbrowser.open_new(url)
    time.sleep(3)
    for i in range(tab):
        pyautogui.press('tab')
    pyperclip.copy(ip)
    pyautogui.hotkey('ctrl','v', interval=0.15)
    pyautogui.press('enter')

 # El usuario elige Symantec
if election == 1:
    for ip in f:
        open_browser("https://sitereview.bluecoat.com/#/")
 # El usuario elige AbuseIP
elif election == 2:
    for ip in f:
        open_browser("https://www.abuseipdb.com/",15)
           
 # El usuario elige VirusTotal
elif election == 3:
    for ip in f:
        open_browser("https://www.virustotal.com/gui/home/search",5)
    
else:
    raise ValueError("Debe insertar numeros del 1 al 3 inclusive.")