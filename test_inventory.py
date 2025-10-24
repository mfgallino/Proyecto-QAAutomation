"""
CONSIGNA DE PREENTREGA
2.	Navegación y Verificación del Catálogo: (Clases 6 a 8)
•	Caso de Prueba de Navegación:
    o	Verificar que el título de la página de inventario sea correcto
    o	Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
    o	Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
Criterios mínimos:
•	Valida título
•	Valida presencia de productos 
•	Lista nombre/precio del primero.

"""
from selenium import webdriver
import time

# #Atajo para usar el método By
from selenium.webdriver.common.by import By


def test_inventory():
    try:
        driver = webdriver.Chrome()

        # LOGIN
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # >> Verificar que el título de la página de inventario sea correcto
        assert driver.title == "Swag Labs", f"El título de la página es incorrecto: {driver.title}"

        # >> Comprobar que existan productos visibles en la página

        # Creamos una variable, donde capturamos en una lista, todos los elementos de la página.
        # Usamos la clase, que es común a todos los elementos
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

        # Chequeamos si la longitud de la variable es > 0
        assert len(productos) > 0, "No existen productos visibles en la página"

    # Guardamos en una variable (e) el error qué tuvo en el momento de la ejecución 
    except Exception as e:

        # y lo mostramos con un print:
        print(f"Error en test_inventory: {e}")
        # Utilizamos raise para avisar a pytest que hubo un error
        raise
        
    finally:
        driver.quit()



""" >>>  FALTA VALIDAR QUE ELEMENTOS IMPORTANTES DE LA INTERFAZ ESTEN PRESENTES, 
MENU, FILTROS, ETC.   <<< """