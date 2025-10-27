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

#Espera explícita
from selenium.webdriver.support.ui import WebDriverWait 

#Condiciones para espera explícita
from selenium.webdriver.support import expected_conditions as EC


def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        # <> Verificar el título de la página (pestaña)
        assert driver.title == "Swag Labs", f"El título de la página es incorrecto: {driver.title}"

        # <> Comprobar que existan productos visibles en la página

        # Creamos una variable, donde capturamos en una lista, todos los elementos de la página.
        # Usamos la clase, que es común a todos los elementos
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

        # Chequeamos si la longitud de la variable es > 0
        assert len(productos) > 0, "No existen productos visibles en la página."

        # <> Validar que los elementos importantes de la interfaz estén presentes (menú, filtro)

        # > Menú Hamburguesa
        # Le damos tiempo para que aparezca
        menu_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))

        # Verificamos que esté visible
        assert menu_btn.is_displayed(), "El menú hamburguesa no está visible."

        # > Filtro
        # Le damos tiempo para que aparezca
        sort_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))

        # Verificamos que esté visible
        assert sort_btn.is_displayed(), "El filtro no está visible."

    # Guardamos en una variable (e) el error qué tuvo en el momento de la ejecución 
    except Exception as e:

        # y lo mostramos con un print:
        print(f"Error en test_inventory: {e}")
        # Utilizamos raise para avisar a pytest que hubo un error
        raise
        
    finally:
        driver.quit()

