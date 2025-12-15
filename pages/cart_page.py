from selenium.webdriver.common.by import By  #Atajo para usar el método By
from selenium.webdriver.support.ui import WebDriverWait  #Espera explícita
from selenium.webdriver.support import expected_conditions as EC  #Condiciones para espera explícita


class CartPage:

    #Selectores (Localizadores):
    
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")  # Productos en el carrito
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")  # Nombre de producto en el carrito


    def __init__(self, driver):  
        self.driver = driver  # Inicializar el driver
        self.wait = WebDriverWait(driver,10)  # Definir la espera

    # Obtener los productos del carrito
    def obtener_productos_carrito(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        return productos
    
    #Obtener nombre de producto en el carrito
    def obtener_nombre_producto_carrito(self):
        nombre_producto = self.wait.until(EC.visibility_of_element_located(self._CART_ITEM_NAME))
        return nombre_producto.text
    
