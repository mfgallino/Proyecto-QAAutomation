
from selenium import webdriver
from selenium.webdriver.common.by import By   #Atajo para usar el método By
import pytest

from pages.login_page import LoginPage

from faker import Faker # Importar la librería (Antes, instalar faker con pip install.)

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
    try:
        driver = login_in_driver

        if debe_funcionar == True:

            # <> Validar la redirección a inventario.html
            assert '/inventory.html' in driver.current_url, "No se redirigió al inventario."   # Buscar una parte del url en el url de la web que estamos
        
        else:
            mensaje_error = LoginPage(driver).obtener_error()
            assert "Epic sadface" in mensaje_error, "El mensaje de error no se está mostrando."

        """FALTA VOLVER A AGREGAR ESTO:
        # <> Validar el Encabezado ("SWAG LABS") y el Subtítulo ("PRODUCTS") de la página
        assert driver.find_element(By.CLASS_NAME,"app_logo").text == "Swag Labs", f"El Encabezado de la página es incorrecto: {driver.find_element(By.CLASS_NAME,"app_logo").text}"
        assert driver.find_element(By.CLASS_NAME,"title").text == "Products", f"El subtítulo de la página es incorrecto: {driver.find_element(By.CLASS_NAME,"title").text}"
        """

    # Guardar en una variable (e) el error qué tuvo en el momento de la ejecución 
    except Exception as e:
        print(f"Error en test_login: {e}")   # Mostrar el mensaje de error con un print
        raise    # Utilizar raise para avisar a pytest que hubo un error

    #Finalmente, cerrar la página (cualquiera sea el resultado del test)
    finally:
        driver.quit()