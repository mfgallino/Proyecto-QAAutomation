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
    
    # Setear formato del archivo
    file_handler.setFormatter(formatter)

    # Agregar lo anterior al logger
    logger.addHandler(file_handler)
