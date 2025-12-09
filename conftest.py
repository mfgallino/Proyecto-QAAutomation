"""
NOTA: 'conftest.py' tiene la particularidad de que todo lo definido acá 
       se hace globalmente. Por lo tanto, no requerirán importarse para
       llamarlos desde otros archivos, sino que las reconocen directamente. 
       Sirve para compartir configuraciones globales, es decir, centralizar las configuraciones que utilizan los tests.
       Este archivo tiene que estar en la raiz o por lo menos en un nivel superior a los archivos de tests.
"""

import pytest
from selenium import webdriver
from pages.login_page import LoginPage # Importar la clase LoginPage
from selenium.webdriver.chrome.options import Options

import pathlib
from datetime import datetime  # para usar el formato de fecha/hora en la captura de error
import time  # para usar el formato de Unix en la captura de error

# Crear variable para la carpeta de captura de errores
target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)

"""
'target' es una variable que va generar la carpeta donde se van a guardar las capturas de pantalla
se crea al principio de este archivo

'parents' significa que va a crear todas las carpetas intermedias entre reports y screens
exist_ok es para que no la cree si ya existe
"""

#Inicializar el navegador a través de una función:
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito") 
    driver = webdriver.Chrome(options=options)

    #Utilizar 'yield' para insertar acá la ejecución del test
    yield driver
    driver.quit()

#Ejecutar el login e insertar el driver
@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver

# url
@pytest.fixture
def url_base():
    return  "https://reqres.in/api/users"

# header
@pytest.fixture
def header_request():
    return {"x-api-key": "reqres_6c03c23b70da46c2b9b9b9d01723cd87"}

# hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    """
    'item' representa el test, texto y todos sus fixtures
    'call' tiene toda la ejecución interna del test
    'yield' pone en pausa la función, guarda el valor y continua luego, permitiendo hacer la captura de pantalla
    """

    report = outcome.get_result()

    if report.when in ("setup", "call") and report.failed:

        """
        Fases del ciclo de producción de la prueba:
        - setup (preparación del test)
        - call (ejecución del test)
        - teardown (cierre del test, reseteo de los datos , desconexión de las APIS)
        
        El test puede fallar:
        - entre el setup y el call o
        - cdo da failed

        Queremos hacer la captura en cualquiera de los dos casos.
        """

        # Guardar la información del test (item) en una variable
        driver = item.funcargs.get("driver", None)

        """
        Con esta linea se recupera el momento en que el test falló.
        si el test tiene el fixture "driver" se va a guardar dentro de esta variable 'driver',
        si no va a devolver 'None'.
        """

        if driver:
            timestamp_comun = datetime.now().strftime("%Y%m%D_%H%M%S")
            timestamp_unix = int(time.time())
            file_name = target / f"{report.when}_{item.name}.{timestamp_comun}.png"
            driver.save_screenshot(str(file_name))

