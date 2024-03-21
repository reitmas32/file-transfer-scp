import os
import time
from dotenv import load_dotenv
import structlog
import subprocess

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Logger de structlog
logger = structlog.get_logger()

def transferir_archivos(ip_remota, usuario, password, carpeta_local, carpeta_remota):
    while True:
        try:
            # Ejecutar scp para copiar archivos recursivamente
            comando_scp = f'scp -r {carpeta_local} {usuario}@{ip_remota}:{carpeta_remota}'
            subprocess.run(comando_scp, shell=True, check=True)

            logger.info("Contenido de la carpeta local copiado a la carpeta remota", carpeta_local=carpeta_local, carpeta_remota=carpeta_remota)

            # Verificar cambios en la carpeta local cada 5 segundos
            time.sleep(5)
            # Obtener archivos locales modificados
            archivos_modificados = [os.path.join(root, file) for root, _, files in os.walk(carpeta_local) for file in files if os.stat(os.path.join(root, file)).st_mtime > time.time() - 5]
            # Transferir archivos modificados
            for archivo_modificado in archivos_modificados:
                comando_scp = f'scp {archivo_modificado} {usuario}@{ip_remota}:{carpeta_remota}'
                subprocess.run(comando_scp, shell=True, check=True)

                logger.info("Archivo modificado copiado a la carpeta remota", archivo_modificado=archivo_modificado, carpeta_remota=carpeta_remota)

        except subprocess.CalledProcessError as e:
            logger.error("Error durante la transferencia de archivos", error=str(e))

# Leer variables de entorno desde el archivo .env
ip_remota = os.getenv("IP_REMOTA")
usuario = os.getenv("USUARIO")
password = os.getenv("PASSWORD")
carpeta_local = os.getenv("CARPETA_LOCAL")
carpeta_remota = os.getenv("CARPETA_REMOTA")

# Verificar si la carpeta local existe
if not os.path.exists(carpeta_local):
    os.makedirs(carpeta_local)
    logger.info("Carpeta local creada", carpeta_local=carpeta_local)

# Llamar a la función para transferir archivos
transferir_archivos(ip_remota, usuario, password, carpeta_local, carpeta_remota)
