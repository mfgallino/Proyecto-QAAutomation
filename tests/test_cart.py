from selenium import webdriver
from selenium.webdriver.common.by import By     # #Atajo para usar el método By
import pytest

from pages.login_page import LoginPage

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.parametrize("usuario, password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver, usuario, password):
    try:
        driver = login_in_driver

        LoginPage(driver).login_completo(usuario, password)  # Traer el driver y ejecutar la función de login_completo con usuario/contraseña parametrizados

        inventory_page = InventoryPage(driver)   # Instanciar el driver para ejecutar las funciones 

        # Agregar el primer producto al carrito
        inventory_page.agregar_primer_producto() 

        # Abrir el carrito
        inventory_page.abrir_carrito()

        # Validar el producto
        cartPage = CartPage(driver)   # Instanciar el CartPage 

        productos_en_carrito = cartPage.obtener_productos_carrito()
        assert len(productos_en_carrito) == 1

        # Activar solamente para probar la instancia de fallo:
        # assert False, "Fallo de prueba forzado"

# Guardar en una variable (e) el error que tuvo en el momento de la ejecución 
    except Exception as e:
        print(f"Error en test_cart: {e}")   # Mostrarlo con un print:
        raise     # Avisar a pytest que hubo un error
    
    
