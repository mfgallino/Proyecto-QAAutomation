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

import time

# <> Interacción con Productos


def test_shopping(login_in_driver):
    try:
        driver = login_in_driver

        # Guardar en una variable la lista de productos presentes en la página
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        # > Añadir un producto al carrito:
        # Hacer click en el primer item de la lista
        productos[0].find_element(By.TAG_NAME, "button").click()
        
        # Guardar el nombre del producto en una variable
        titulo_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
       
        # > Verificar que el contador del carrito haya aumentado en una unidad
        wait = WebDriverWait(driver,10)
        carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text
        assert carrito == "1", "No se ha agregado el producto al carrito."
        
        # > Navegar al carrito de compras  
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(5)

        # Guardar el nombre del producto en el carrito en una variable
        titulo_producto_carrito = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text

        # Verificar que los nombres de los productos coincidan
        assert titulo_producto == titulo_producto_carrito, "El producto no coincide."

    finally:
        driver.quit()