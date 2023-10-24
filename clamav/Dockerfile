# Utilizamos una imagen base de Ubuntu
FROM ubuntu:latest

# Instalamos ClamAV y las herramientas necesarias
RUN apt-get update && apt-get install -y clamav clamav-daemon clamav-freshclam

# Actualizamos la base de datos de virus de ClamAV
RUN freshclam

# Exponer el puerto 3310 que es el puerto por defecto de clamd
EXPOSE 3310

# Copiar un archivo de configuración personalizado de clamd (si lo tienes)
COPY clamd.conf /etc/clamav/clamd.conf

# Iniciar el demonio clamd
CMD ["clamd"]
