import pyclamd

# Función para conectar con el servicio ClamAV
def connect_to_clamav():
    # El host debe coincidir con el nombre del servicio de ClamAV en tu archivo docker-compose.yml
    # El puerto debe coincidir con el puerto expuesto por el servicio ClamAV
    cd = pyclamd.ClamdNetworkSocket(host='clamav', port=3310)
    return cd

# Función para escanear un archivo
def scan_file(file_path):
    # Obtén la conexión a ClamAV
    cd = connect_to_clamav()
    # Escanea el archivo. La ruta del archivo debe ser accesible por el contenedor Django.
    result = cd.scan_file(file_path)
    return result

# Función de ejemplo para usar scan_file
def example_usage():
    # Ruta del archivo a escanear
    file_path = '/home/juferoga/virus/virus.sh'
    # Escanea el archivo
    result = scan_file(file_path)
    # Procesa el resultado
    if result is None:
        print("Archivo sin virus encontrados")
    else:
        print(f"Virus encontrados (resultado de escaneo): {result}")

# Llama a la función de ejemplo
if __name__ == "__main__":
    example_usage()
