from selenium import webdriver
from selenium.webdriver.common.by import By     # #Atajo para usar el método By
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos

# Definir constante con la ruta del archivo Json
RUTA_JSON = "datos/productos.json"

"""OPTATIVO: VER hacer archivo data_default_login.csv para parametrizar el usuario/login general
              para las demás pruebas en vez de que esté hardcodeado."""

@pytest.mark.parametrize("usuario, password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto", leer_json_productos(RUTA_JSON))  # Valores de los nombres que da el JSON
def test_cart_json(login_in_driver, usuario, password, nombre_producto):
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)

        # Instanciar el driver para ejecutar las funciones 
        inventory_page = InventoryPage(driver)

        # Agregar al carrito los productos que están en el JSON
        inventory_page.agregar_producto_por_nombre(nombre_producto)

        # Abrir el carrito
        inventory_page.abrir_carrito()

        # Validar el producto
        cartPage = CartPage(driver)   # Instanciar el CartPage 
        assert cartPage.obtener_nombre_producto_carrito() == nombre_producto

# Guardar en una variable (e) el error que tuvo en el momento de la ejecución 
    except Exception as e:
        print(f"Error en test_cart: {e}")   # Mostrarlo con un print:
        raise     # Avisar a pytest que hubo un error
        
    finally:
        driver.quit()