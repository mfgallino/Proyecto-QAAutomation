""" 
CONSIGNA DE PREENTREGA
1. Automatización de Login:
•	Navegar a la página de login de saucedemo.com
•	Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
•	Validar login exitoso verificando que se haya redirigido a la página de inventario	
Criterios mínimos:
Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.
"""

from selenium import webdriver

#Atajo para usar el método By
from selenium.webdriver.common.by import By 

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        # <> Validar la redirección a inventario.html
        assert '/inventory.html' in driver.current_url   # Buscar una parte del url en el url de la web que estamos
        
        # <> Validar el Encabezado ("SWAG LABS") y el Subtítulo ("PRODUCTS") de la página
        assert driver.find_element(By.CLASS_NAME,"app_logo").text == "Swag Labs", f"El Encabezado de la página es incorrecto: {driver.find_element(By.CLASS_NAME,"app_logo").text}"
        assert driver.find_element(By.CLASS_NAME,"title").text == "Products", f"El subtítulo de la página es incorrecto: {driver.find_element(By.CLASS_NAME,"title").text}"

    # Guardar en una variable (e) el error qué tuvo en el momento de la ejecución 
    except Exception as e:
        print(f"Error en test_login: {e}")   # Mostrar el mensaje de error con un print
        raise    # Utilizar raise para avisar a pytest que hubo un error

    #Finalmente, cerrar la página (cualquiera sea el resultado del test)
    finally:
        driver.quit()

