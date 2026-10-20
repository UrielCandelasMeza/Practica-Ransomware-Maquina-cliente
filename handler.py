from datetime import datetime

class Handler:
  def __init__(self, date_delete, eliminar_archivos, descifrar_directorios, descifrar_llave):
    self.date_delete = date_delete
    self.eliminar_archivos = eliminar_archivos
    self.descifrar_directorios = descifrar_directorios
    self.descifrar_llave = descifrar_llave