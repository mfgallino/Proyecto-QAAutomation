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

#Espera explícita
from selenium.webdriver.support.ui import WebDriverWait 

#Condiciones para espera explícita
from selenium.webdriver.support import expected_conditions as EC

import time


# Definir la función para llamarla luego desde pytest.
def test_login():
    driver = webdriver.Chrome()

    # Espera implicita: para que selenium espere 5seg a que el elemento aparezca antes de dar error
    # Esto es una Buena Práctica (es un tiempo máximo de espera entre acciones)
    # driver.implicitly_wait(5)

    try:
        # <> LOGIN 
        
        # <> Ingresar a la página
        driver.get("https://www.saucedemo.com/")

        # Agregar pausa (solamente para poder verificar visualmente qué hace)
        time.sleep(2)

        # <> Ingresar credenciales válidas (usuario y contraseña) y presiona el botón 'Login'   
                
        # Espera explícita 
        # Espera a que se ejecute una condición particular de un elemento particular)
        # Si el elemento no aparece en el tiempo especificado, devuelve un error.
        wait = WebDriverWait(driver,10)

        usuario = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        usuario.send_keys("standard_user") 
        
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        time.sleep(2)
        
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)
        

        # <> Validar la redirección a inventario.html
        assert '/inventory.html' in driver.current_url   # Buscar una parte del url en el url de la web que estamos
        
        # <> Validar el Encabezado ("SWAG LABS") y el Subtítulo ("PRODUCTS") de la página
        assert driver.find_element(By.CLASS_NAME,"app_logo").text == "Swag Labs", f"El Encabezado de la página es incorrecto: {driver.find_element(By.CLASS_NAME,"app_logo").text}"
        assert driver.find_element(By.CLASS_NAME,"title").text == "Products", f"El subtítulo de la página es incorrecto: {driver.find_element(By.CLASS_NAME,"title").text}"

    # Guardar en una variable (e) el error qué tuvo en el momento de la ejecución 
    except Exception as e:
        print(f"Error en test_login: {e}")       # Mostrar el mensaje de error con un print
        raise        # Utilizar raise para avisar a pytest que hubo un error

    
    # || No agregar esta sentencia porque se va a llamar a esta función para hacer otros tests ||
    #Finalmente, cerrar la página (cualquiera sea el resultado del test)
    #finally:
    #    driver.quit()