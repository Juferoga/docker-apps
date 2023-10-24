# CLAMAV
Este software es básicamente un antivirus el cual tiene como objetivo detectar si hay amlware en un archivo.
El presente repositorio permite crear un contenedor de Docker el cual podrá ser usado como servicio para verificar si un archivo tiene o no virus.

## Datos generales

- Puerto : 3310

## Dockerfile
Este archivo permite crear una imagen de CLAMAV, para crear la imagen usar el siguiente comando:

```bash
docker build -t my-clamav .
```

Para probar el contenedor usar:
```bash
docker run -d -p 3310:3310 --name my-clamav-container my-clamav
```


## Docker-compose
Este archivo permite la automatización de la creación del contenedor, exposición de puertos y creación de volúmenes necesarios para su funcionamiento.

Para ejecutar el Docker composé usar el comando:
```bash
docker-compose up --build -d
```
## Ejemplo Python 

En el archivo ```main.py``` se mostrará un ejemplo de cómo usar el contenedor desde otro contenedor de Docker

### Instalar las dependencias

```bash
pip install pyclamd
```

Se debe revisar que ambos contenedores estén sobre la misma red y con una conexión tipo bridge.

```yml
version: '3.1'

services:
  clamav:
    networks:
      - mynetwork

  python:
    networks:
      - mynetwork

networks:
  mynetwork:
    driver: bridge
```

