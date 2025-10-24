""" 
CONSIGNA
1. Automatización de Login:
•	Navegar a la página de login de saucedemo.com
•	Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
•	Validar login exitoso verificando que se haya redirigido a la página de inventario	
Criterios mínimos:
Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.
"""

from selenium import webdriver
import time

# 'By' Permite seleccionar el elemento según una característica
from selenium.webdriver.common.by import By

# Definir la función para llamarla luego desde pytest.
def test_login():
    driver = webdriver.Chrome()

    # Para que selenium espere 5seg a que el elemento aparezca antes de dar error
    # Esto es una Buena Práctica (es un tiempo máximo de espera entre acciones)
    driver.implicitly_wait(5)

    try:
        # >> LOGIN 
        
        # >> Ingresar a la página
        driver.get("https://www.saucedemo.com/")

        # Agregar pausa (solamente para poder verificar visualmente qué hace)
        time.sleep(2)

        # >> Ingresar credenciales válidas (usuario y contraseña) y presiona el botón 'Login'
         
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        
        """  >>  ¡¡FALTA AGREGAR ESPERA EXPLICITA!!!  <<   """

        # >> Verificar que se haya redirigido a la página de inventario.html
        
        # Buscar una parte del url en el url de la web que estamos
        assert '/inventory.html' in driver.current_url
        
        # >> Validar el Título ("SWAG LABS") y el Subtítulo ("PRODUCTS") de la página
        
        # Buscar cada elemento y compararlo con el texto del título/subtítulo para verificar que coincida
        assert driver.title == "Swag Labs", f"El título de la página es incorrecto: {driver.title}"
        assert driver.find_element(By.CLASS_NAME,"title").text == "Products", f"l subtítulo de la página es incorrecto: {driver.find_element(By.CLASS_NAME,"title").text}"

    # Guardar en una variable (e) el error qué tuvo en el momento de la ejecución 
    except Exception as e:
        # Mostrar el mensaje de error con un print:
        print(f"Error en test_login: {e}")
        # Utilizar raise para avisar a pytest que hubo un error
        raise

    #Finalmente, cerrar la página (cualquiera sea el resultado del test)
    finally:
        driver.quit()