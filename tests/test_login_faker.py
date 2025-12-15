
from selenium import webdriver
from selenium.webdriver.common.by import By   #Atajo para usar el método By
import pytest

from pages.login_page import LoginPage

from faker import Faker # Importar la librería (Antes, instalar faker con pip install.)

from utils.logger import logger

#Inicializar faker
fake = Faker()

"""
Luego, llamamos al faker al momento de pasarle los datos a través de la parametrización.
Vamos a crear una lista con tuplas, cada tupla va a tener un conjunto de datos distintos.
NOTA: para el caso de contraseñas que requieren ciertas condiciones, se puede agregar al faker
esos parámetros para que los cumpla, por ej:
fake.password(length=8, special_chars=True, upper_case=True, lower_case=True, digits=True)
"""

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

        """FALTA VOLVER A AGREGAR ESTO:
        # <> Validar el Encabezado ("SWAG LABS") y el Subtítulo ("PRODUCTS") de la página
        assert driver.find_element(By.CLASS_NAME,"app_logo").text == "Swag Labs", f"El Encabezado de la página es incorrecto: {driver.find_element(By.CLASS_NAME,"app_logo").text}"
        assert driver.find_element(By.CLASS_NAME,"title").text == "Products", f"El subtítulo de la página es incorrecto: {driver.find_element(By.CLASS_NAME,"title").text}"
        """


    