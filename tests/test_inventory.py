from selenium import webdriver
from selenium.webdriver.common.by import By     # #Atajo para usar el método By
from selenium.webdriver.support.ui import WebDriverWait     #Espera explícita
from selenium.webdriver.support import expected_conditions as EC     #Condiciones para espera explícita
import pytest

from pages.login_page import LoginPage

from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("usuario, password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver, usuario, password):
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)

        # Instanciar el driver para ejecutar las funciones 
        inventory_page = InventoryPage(driver)

        # Verificar que hay productos en el inventario
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "No hay productos en el inventario."

        # Verificar que el carrito está vacío
        assert inventory_page.obtener_conteo_carrito() == 0

        # Agregar el primer producto al carrito
        inventory_page.agregar_primer_producto()

        #Verificar el contador del carrito
        assert inventory_page.obtener_conteo_carrito() == 1

    # Guardamos en una variable (e) el error qué tuvo en el momento de la ejecución 
    except Exception as e:
        # y lo mostramos con un print:
        print(f"Error en test_inventory: {e}")
        # Utilizamos raise para avisar a pytest que hubo un error
        raise


