from selenium import webdriver
from selenium.webdriver.common.by import By     # #Atajo para usar el método By
import pytest

from pages.login_page import LoginPage

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.logger import logger

@pytest.mark.parametrize("usuario, password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver, usuario, password):
    logger.info("'Iniciando prueba de Carrito.'") # log
    try:
        logger.info("Completando los datos de usuario.") # log
        driver = login_in_driver

        LoginPage(driver).login_completo(usuario, password)  # Traer el driver y ejecutar la función de login_completo con usuario/contraseña parametrizados

        inventory_page = InventoryPage(driver)   # Instanciar el driver para ejecutar las funciones 

        # Agregar el primer producto al carrito
        logger.info("Agregando un producto al carrito.") # log
        inventory_page.agregar_primer_producto() 

        # Abrir el carrito
        logger.info("Abriendo el carrito.") # log
        inventory_page.abrir_carrito()

        # Validar el producto
        cartPage = CartPage(driver)   # Instanciar el CartPage 

        productos_en_carrito = cartPage.obtener_productos_carrito()
        logger.info("Validando que hay un producto en el carrito.") # log
        assert len(productos_en_carrito) == 1

        # Activar solamente para probar la instancia de fallo:
        # assert False, "Fallo de prueba forzado"

# Guardar en una variable (e) el error que tuvo en el momento de la ejecución 
    except Exception as e:
        logger.info("Informando error detectado durante el test de carrito.") # log
        print(f"Error en test_cart: {e}")   # Mostrarlo con un print:
        raise     # Avisar a pytest que hubo un error
    
    
