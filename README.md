# Transferencia Recursiva de Archivos Usando SCP

Este script de Python te permite transferir archivos entre máquinas locales utilizando el protocolo SCP (Secure Copy Protocol). Puedes especificar las carpetas locales y remotas entre las cuales deseas transferir archivos, y el script verificará periódicamente si hay cambios en la carpeta local para transferirlos a la carpeta remota.


### Requisitos
- Python 3.x
- Instalación de paquetes Python: paramiko, structlog, python-dotenv

Puedes instalar los paquetes requeridos ejecutando el siguiente comando:


```bash
pip install -r requirements.txt
```

### Generación de Claves SSH

Para utilizar la autenticación SSH sin contraseña, puedes generar un par de claves SSH en tu máquina local y copiar la clave pública a la máquina remota. A continuación, se muestran los pasos para hacerlo:

1. Genera un par de claves SSH en tu máquina local:

```bash
ssh-keygen -t rsa
```

2. Copia la clave pública a la máquina remota:

```bash
ssh-copy-id usuario@direccion_ip_remota
```

Reemplaza **usuario** con tu nombre de usuario en la máquina remota y **direccion_ip_remota** con la dirección IP de la máquina remota

### Configuración

1. Crea un archivo **.env** en la carpeta **src** con las siguientes variables de entorno:

```bash
IP_REMOTA=192.168.1.100
USUARIO=nombre_usuario_remoto
CARPETA_LOCAL=/ruta/a/carpeta_local
CARPETA_REMOTA=/ruta/a/carpeta_remota
```


Asegúrate de reemplazar los valores con la dirección IP de la máquina remota, tu nombre de usuario remoto y las rutas de las carpetas locales y remotas.

2. Asegúrate de que el script principal **main.py** se encuentre en la carpeta **src**.

### Uso

Para ejecutar el script, simplemente ejecuta el siguiente comando en tu terminal:

```bash
cd src
python main.py
```

Esto iniciará la transferencia de archivos entre las carpetas locales y remotas especificadas en el archivo .env.