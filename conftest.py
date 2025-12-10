"""
Conceptos
- Conftest.py: 
  tiene la particularidad de que todo lo definido acá 
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
target = pathlib.Path("reports/screens")  # ruta de la carpeta de captura de errores 
target.mkdir(parents=True, exist_ok=True) # parámetros para crear la carpeta

"""
Conceptos:
- target: es una variable que va generar la carpeta donde se van a guardar las capturas de pantalla.
  Se crea al principio de este archivo (acá arriba antes de los fixtures).

- parents=True: significa que Python va a crear este directorio (reports/screens) entre la raíz y el destino, en caso de que no existan.
- exist_ok=True: es para que Python no tire error en caso de que la carpeta ya exista y no la cree si ya existe.
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

# Captura de pantalla (hook)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    """
    Conceptos:
    - item: representa el test, el nombre del test, el concepto y todos sus fixtures
    - call: tiene la información de la ejecución interna del test
    - yield: pone en pausa la función, devuelve un valor pero, además, guarda el estado de la ejecución
      y continua luego donde se quedó, permitiendo hacer la captura de pantalla en el medio.
    """

    # Obtener reporte con los resultados de la prueba
    report = outcome.get_result()
    
    # Condición para la captura
    if report.when in ("setup", "call") and report.failed:

        # Guardar la información del test (item) en una variable
        driver = item.funcargs.get("driver", None)

        """
        Conceptos:
        Fases del ciclo de ejecución de la prueba:
          - setup (preparación del test): fase previa donde se definen y crean los fixtures, se inicializa los drivers, se inicializa selenium, hace la conexión, prepara los datos de prueba y arma el entorno del test.
          - call (ejecución del test): desde que se define el test y se tiene toda la información de la prueba (lo que está dentro del archivo de test, ej test_login.py)
          - teardown (limpieza del test): cierre del test, reseteo de los datos , desconexión de las APIS.
        
        Captura de la prueba: 
        Al capturar la prueba, se capturan las 3 etapas del test.
          
        * Disparador:
          En el 'if', se define cuándo deben hacerse las capturas: 
          - durante el setup (antes de la ejecución), 
          - durante el call (durante la ejecución)
          - y cdo el resultado del test es 'failed'
          Queremos hacer la captura en cualquiera de los dos casos.
          Esta condición if, va a ser el disparador de la captura.

        * Guardado:
          - funcargs: es como un diccionario donde están los fixtures del test.
          Con esta linea se recupera el momento en que el test falló en el webdriver.
            - si el test tiene el fixture "driver" se va a guardar dentro de esta variable 'driver',
            - si no va a devolver 'None'.
        """
        # Si driver tiene un valor distinto de None:
        if driver:
            timestamp_comun = datetime.now().strftime("%Y%m%d_%H%M%S") # Guardar la fecha y hora en una variable
            timestamp_unix = int(time.time())  # Otra opción (no usada acá): guardar el momento de la captura en una variable (con nomenclatura unix epoch): segundos transcurridos desde 1/01/1970 hasta las 00:00 UTC )
            file_name = target / f"{report.when}_{item.name}_{timestamp_comun}.png"  # definir nombre y ruta del archivo de captura de pantalla
            driver.save_screenshot(str(file_name)) # guardado de la captura de pantalla

"""
Concepto:
- Nomenclatura UNIX Epoch): serie de números (irrepetibles) que representa los segundos transcurridos desde 1/01/1970 hasta las 00:00 UTC.
  Se usa mucho en informática. 
"""
