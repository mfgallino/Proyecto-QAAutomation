
from selenium.webdriver.common.by import By  #Atajo para usar el método By
from selenium.webdriver.support.ui import WebDriverWait  #Espera explícita
from selenium.webdriver.support import expected_conditions as EC  #Condiciones para espera explícita

class LoginPage:

    # Enlace de la página web (URL)
    URL = "https://www.saucedemo.com/"  

    #Localizadores (_MAYUSCULAS)
    """
    Son la forma de identificar a elementos en la página web para interactuar con ellos
    a través de Selenium y poder utilizarlos. 
    Son variables internas.
    """
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")


    # Funciones

    def __init__(self, driver):  # self hace referencia a que vamos a trabajar con info que está dentro de la clase
        self.driver = driver  # Inicializar el driver
        self.wait = WebDriverWait(driver,10)  # Definir la espera
    
    # Inicializar la página
    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    # Login:
    """
    Se puede definir una función para cada paso: usuario, contraseña, botón login, 
    o hacer todo junto dentro de una misma función. 
    Se define en función de la complejidad del proyecto.
    """
    # Ingresar usuario
    def completar_user(self, usuario):
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        input.clear()
        input.send_keys(usuario)
        return self
    
    # Ingresar password
    def completar_pass(self, password):
        input = self.driver.find_element(*self._PASS_INPUT)   
        input.clear()
        input.send_keys(password)
        return self
    
    # Presionar botón de login
    def hacer_click_button(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    # Hacer login completo
    def login_completo(self, usuario, password):
        self.completar_user(usuario)
        self.completar_pass(password)
        self.hacer_click_button()
        return self
    
    # Obtener mensaje de error de login
    def obtener_error (self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container h3")))
        return div_error.text  #retornar el texto del mensaje de error del h3