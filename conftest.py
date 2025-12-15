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

#Inicializar el navegador a través de una función:
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito") 
    options.add_argument("--no-sandbox") # github (principal)
    options.add_argument("--disable-gpu") # github (deshabilitar gpu)
    options.add_argument("--window-size=1920,1080") # github (definir tamaño de pantalla)
    options.add_argument("--headless=new") # github (correr sin ventana, en segundo plano)
    
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

    # Obtener reporte con los resultados de la prueba
    report = outcome.get_result()
    
    # Condición para la captura
    if report.when in ("setup", "call") and report.failed:

        # Guardar la información del test (item) en una variable
        driver = item.funcargs.get("driver", None)

        # Si driver tiene un valor distinto de None:
        if driver:
            timestamp_comun = datetime.now().strftime("%Y%m%d_%H%M%S") # Guardar la fecha y hora en una variable
            # timestamp_unix = int(time.time())  # Esta es otra opción (no usada acá): guardar el momento de la captura en una variable (con nomenclatura unix epoch): segundos transcurridos desde 1/01/1970 hasta las 00:00 UTC )
            file_name = target / f"{report.when}_{item.name}_{timestamp_comun}.png"  # definir nombre y ruta del archivo de captura de pantalla
            driver.save_screenshot(str(file_name)) # guardado de la captura de pantalla


