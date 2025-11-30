from selenium import webdriver
from selenium.webdriver.common.by import By     # #Atajo para usar el método By
import time
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.parametrize("usuario, password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver):
    try:
        driver = login_in_driver
        inventory_page = InventoryPage(driver)   # Instanciar el driver para ejecutar las funciones 

        # Agregar el primer producto al carrito
        inventory_page.agregar_primer_producto() 

        # Abrir el carrito
        inventory_page.abrir_carrito()

        # Validar el producto
        cartPage = CartPage(driver)   # Instanciar el CartPage 

        productos_en_carrito = cartPage.obtener_productos_carrito()
        assert len(productos_en_carrito) == 1


# Guardar en una variable (e) el error que tuvo en el momento de la ejecución 
    except Exception as e:
        print(f"Error en test_cart: {e}")   # Mostrarlo con un print:
        raise     # Avisar a pytest que hubo un error
        
    finally:
        driver.quit()