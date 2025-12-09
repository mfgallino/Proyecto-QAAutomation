#LOGGER
"""
Script que sirve como una herramienta que permite registrar información 
durante la ejecución de cualquier test.
Permite dejar registro de lo que pasó, lo qué se ejecutó, en qué orden, errores que se encontraron, etc.
Se usa bastante para UI porque las acciones suceden muy rápido.
El log permite después auditar qué pasó línea por línea.
Es útil también para trabajar en equipo porque se puede consultar qué pasó para entender qué hacer.
"""

import logging
import pathlib # Librería que interpreta la ruta de un archivo desde la raíz del proyecto

# Crear carpeta 'logs'
audit_dir = pathlib.Path('logs')

# Evaluar si la carpeta 'logs' ya existe 
audit_dir.mkdir(exist_ok=True)

# Crear archivo
log_file = audit_dir/ 'suite.log'

# Definir el archivo creado como logger (inicializar el logger)
logger = logging.getLogger("TalentoTech")

# Definir el tipo de logger (tipo:'INFO')
logger.setLevel(logging.INFO)

# Verificar que no exista un archivo logger con el mismo nombre (para no duplicar)
if not logger.handlers:
    # Definir formato del archivo
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")

    """modo "a": append (agrega un log abajo de otro, no sobreescribe)"""

    # Definir formatter
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    """
    - asctime   -> fecha/hora
    - levelname -> nivel de log (INFO, ERROR…)
    - name      -> nombre del logger
    - message   -> texto del mensaje
    La s indica que ese valor debe formatearse como string. 
    """

    # Setear formato del archivo
    file_handler.setFormatter(formatter)

    # Agregar lo anterior al logger
    logger.addHandler(file_handler)
