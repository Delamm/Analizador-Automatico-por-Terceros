import webbrowser # Librería para automatizar en navegador
import pyperclip # Sirve para copiar y pegar cosas en python
import pyautogui # Automatizar que se ejecute una tecla por ej el espacio
import time # Nos va a ayudar a evitar errores
from colorama import Fore, Style # Colores

with open('adresses.txt','r') as f:
    f = f.read().split('\n')

election = input(Fore.GREEN + "Escribe el nombre de la herramienta que quieras utilizar para analizar las direcciones IP: "
+ Fore.YELOW + """\n1 - Symantec
2 - AbuseIP
3 - VirusTotal: \n""" + Style.RESET_ALL + "Su elección --> ")
