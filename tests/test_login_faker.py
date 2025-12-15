
from selenium import webdriver
from selenium.webdriver.common.by import By   #Atajo para usar el método By
import pytest

from pages.login_page import LoginPage

from faker import Faker # Importar la librería (Antes, instalar faker con pip install.)

from utils.logger import logger

#Inicializar faker
fake = Faker()


@pytest.mark.parametrize("usuario, password, debe_funcionar", [
    (fake.user_name(), fake.password(length=8, special_chars=True, upper_case=True, lower_case=True, digits=True), False),
    (fake.user_name(), fake.password(), False)
])
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):
    logger.info("'Iniciando prueba de Login con Faker.'") # log
    logger.info("Completando los datos de usuario.") # log
    driver = login_in_driver
    LoginPage(driver).login_completo(usuario,password)
        
    if debe_funcionar == True:
        logger.info("Validando redireccionamiento al Inventario.") # log
        # <> Validar la redirección a inventario.html
        assert '/inventory.html' in driver.current_url, "No se redirigió al inventario."   # Buscar una parte del url en el url de la web que estamos
        logger.info("Login completado.") # log 
    else:
        mensaje_error = LoginPage(driver).obtener_error()
        assert "Epic sadface" in mensaje_error, "El mensaje de error no se está mostrando."
        logger.info("Prueba de login con datos incorrectos completada.") # log
