"""
CONSIGNA DE PREENTREGA
3.	Interacción con Productos: (Clase 8)
•	Caso de Prueba de Carrito:
    o	Añadir un producto al carrito haciendo clic en el botón correspondiente
    o	Verificar que el contador del carrito se incremente correctamente
    o	Navegar al carrito de compras
    o	Comprobar que el producto añadido aparezca correctamente en el carrito
Criterios mínimos:
•	Agrega primer producto 
•	Verifica ítem en carrito.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import info_producto

import time

# <> Interacción con Productos

def test_shopping(login_in_driver):
    try:
        driver = login_in_driver
        wait = WebDriverWait(driver, 10)

        # Esperar que se cargue la lista
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        # Obtener el primer producto de la lista y guardarla en una variable
        primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
        info_lista = info_producto(primer_producto)

        # <> Agregar el primer producto al carrito
        primer_producto.find_element(By.TAG_NAME, "button").click()
        
        # <> Verificar que el contador del carrito haya aumentado en una unidad
        wait = WebDriverWait(driver,10)
        carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text
        assert carrito == "1", "No se ha agregado el producto al carrito."

        # <> Navegar al carrito de compras
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
        
        # Validar la redirección a cart.html
        assert '/cart.html' in driver.current_url

        # Obtener la info del producto en el carrito y guardarla in una variable
        producto_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")[0]
        info_carrito = info_producto(producto_carrito)

        # <> Verificar que la info de ambos productos coincida
        assert info_lista == info_carrito, "Los productos no coinciden."
        
    except Exception as e:
        print(f"Error en test_shopping: {e}")

    finally:
        driver.quit()