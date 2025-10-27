"""Parte Lógica, usada solamente para interactuar con la página."""

#Atajo para usar el método By
from selenium.webdriver.common.by import By 

#Espera explícita
from selenium.webdriver.support.ui import WebDriverWait 

#Condiciones para espera explícita
from selenium.webdriver.support import expected_conditions as EC

import time

# <> LOGIN 
def login(driver):
    # <> Ingresar a la página
    driver.get("https://www.saucedemo.com/")
    
    # Agregar pausa (solamente para poder verificar visualmente qué hace)
    time.sleep(2)
            
    # Espera explícita (espera a que sea visible el user_name)
    # Si el elemento no aparece en el tiempo especificado, devuelve un error.
    wait = WebDriverWait(driver,10)
    usuario = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    
    # <> Ingresar credenciales válidas (usuario y contraseña) 
    usuario.send_keys("standard_user") 
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    time.sleep(2)
    
    # <> Presionar el botón 'Login'  
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

