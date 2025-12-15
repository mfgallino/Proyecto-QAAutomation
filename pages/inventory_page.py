from selenium.webdriver.common.by import By  #Atajo para usar el método By
from selenium.webdriver.support.ui import WebDriverWait  #Espera explícita
from selenium.webdriver.support import expected_conditions as EC  #Condiciones para espera explícita

class InventoryPage:

    #Selectores (Localizadores):

    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")   # productos en el inventario
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".inventory_item button") # botón para agregar el producto al carrito
    _CART_COUNT = (By.CLASS_NAME,"shopping_cart_badge")    # contador del carrito
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")    # nombre de producto en inventario
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")     # botón de acceso al carrito



    def __init__(self, driver):  
        self.driver = driver  # Inicializar el driver
        self.wait = WebDriverWait(driver,10)  # Definir la espera
    
    # Capturar todos los productos
    def obtener_todos_los_productos(self):
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)
        return productos
    
    # Obtener los nombres de todos los productos
    def obtener_nombres_productos(self):
        productos = self.driver.find_elements(*self._ITEM_NAME)

        # Guardar en una lista los nombres de todos los productos
        return [producto_nombre.text for producto_nombre in productos]   # captura el nombre de cada producto y lo convierte en texto

    # Agregar primer producto al carrito
    def agregar_primer_producto(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))

        primer_boton_producto = productos[0].find_element(*self._ADD_TO_CART_BUTTON)
        primer_boton_producto.click()
       
    # Agregar producto por nombre al carrito
    def agregar_producto_por_nombre(self,nombre_producto):
        # Obtener todos los productos
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)   #llama a otra función y asigna el resultado a una variable
        
        # Capturar los nombres en el formato texto
        # Recorrer una lista buscando el nombre de cada producto
        for producto in productos:
            nombre = producto.find_element(*self._ITEM_NAME).text
            
            # Limpiar los espacios que podría haber (usando 'strip()') 
            # y comparar lo que tengo de mi página ('nombre') con el parámetro que le estoy pasando ('nombre_producto'), que sale del Json.
            if nombre.strip() == nombre_producto.strip():
                
                #Y agregar el producto
                boton = producto.find_element(*self._ADD_TO_CART_BUTTON)
                boton.click()
                return self
            
        raise Exception(f"No se encontró el producto {nombre_producto}")

    # Ir al carrito
    def abrir_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self._CART_LINK)).click()
        return self
    
    # Obtener el conteo del carrito
    def obtener_conteo_carrito(self):
        try:
            # Esperar a que aparezca
            self.wait.until(EC.visibility_of_element_located(self._CART_COUNT))
    
            # Capturar el carrito
            contador_carrito = self.driver.find_element(*self._CART_COUNT)
            return int(contador_carrito.text)   # Convertir a int
        
        except:
            return 0
        