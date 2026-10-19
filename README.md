# Practica Ransomware Seguridad Informatica

Este es un ransomware de prueba para la materia de seguridad informática.

El objetivo de este programa es completamente educativo para enteneder como funciona un software de este estilo y poder aplicar tacticas de proteccion frente a estos casos.

## Como funciona

Este software se compone de 4 fases: 

1. El cifrado de los archivos
2. El cifrado de la clave que se uso para cifrar
3. El descifrado de la clave de cifrado
4. El descifrado de los archivos

En estas fases se usan 2 algoritmos: `ChaCha20` y `RSA`.

El primer algoritmo `ChaCha20` es el usado para cifrar los datos debido a que es simetrico y solo necesita una llave para esto.

El segundo algoritmo `RSA` se usa para cifrar la llave de `ChaCha20` para evitar que rompan facilmente nuestro Malware.

## Como hacer uso del software

0. Se necesita tener un entorno virtual en el cual vamos a instalar los paquetes dentro de `requirements.txt` mediante el comando:

```bash
python -m venv venv
pip install -r requirements.txt
```

1. Primero necesitamos setear la ruta a la que vamos a atacar (posteriormente se busca añadir un arreglo de rutas base para atacar).
2. Despues se setea el tiempo de tolerancia que se le va a dar a la victima para poder pagar.
3. Se tiene que ejecutar el archivo `generate_keys.py` el cual genera 2 llaves, una publica con la cual se cifra la llave de `ChaCha20` y la privada la cual es la que debemos conservar y no darle a la victima.
4. Ya se puede ejecutar el archivo `main.py`.


## Anexo

El objetivo es poder enviar la llave desde un servidor el cual va a estar en otro repositorio, este unicamente tiene el objetivo de recibir un pago y entonces liberar la llave.
