"""
NOTA: 'conftest.py' tiene la particularidad de que todo lo definido acá 
       se hace globalmente. Por lo tanto, no requerirán importarse para
       llamarlos desde otros archivos, sino que las reconocen directamente. 
       Sirve para compartir configuraciones globales.
       Este archivo tiene que estar en la raiz o por lo menos en un nivel superior a los archivos de tests.
"""

import pytest
from selenium import webdriver
from utils import login

#Inicializar el navegador a través de una función:
@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    #Utilizar 'yield' para insertar acá la ejecución del test
    yield driver

    driver.quit()

#Ejecutar el login e insertar el driver
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
