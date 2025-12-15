from selenium import webdriver
from selenium.webdriver.common.by import By     # #Atajo para usar el método By
from selenium.webdriver.support.ui import WebDriverWait     #Espera explícita
from selenium.webdriver.support import expected_conditions as EC     #Condiciones para espera explícita
import pytest

from pages.login_page import LoginPage

from pages.inventory_page import InventoryPage

from utils.logger import logger

@pytest.mark.parametrize("usuario, password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver, usuario, password):
    logger.info("'Iniciando prueba de Inventario.'") # log
    try:
        logger.info("Completando los datos de usuario.") # log
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)

        # Instanciar el driver para ejecutar las funciones 
        inventory_page = InventoryPage(driver)

        # Verificar que hay productos en el inventario
        logger.info("Verificando que hay productos en el inventario.") # log
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "No hay productos en el inventario."

        # Verificar que el carrito está vacío
        logger.info("Verificando que el carrito está vacío") # log
        assert inventory_page.obtener_conteo_carrito() == 0

        # Agregar el primer producto al carrito
        logger.info("Agregando un producto al carrito") # log
        inventory_page.agregar_primer_producto()

        #Verificar el contador del carrito
        logger.info("Verificando que se agregó un producto al carrito.") # log
        assert inventory_page.obtener_conteo_carrito() == 1

    # Guardamos en una variable (e) el error qué tuvo en el momento de la ejecución 
    except Exception as e:
        logger.info("Informando error detectado durante el test de inventario.") # log
        # y lo mostramos con un print:
        print(f"Error en test_inventory: {e}")
        # Utilizamos raise para avisar a pytest que hubo un error
        raise


