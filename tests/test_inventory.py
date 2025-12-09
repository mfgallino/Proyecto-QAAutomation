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

        

        """ -------------ELIMINO ESTO!!!

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

        """

    # Guardamos en una variable (e) el error qué tuvo en el momento de la ejecución 
    except Exception as e:
        # y lo mostramos con un print:
        print(f"Error en test_inventory: {e}")
        # Utilizamos raise para avisar a pytest que hubo un error
        raise


