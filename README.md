# PROYECTO DE AUTOMATIZACION - TALENTO TECH

Proyecto desarrollado como parte del curso QA Automation con Python - Talento Tech

## Propósito del Proyecto
El objetivo de esta Pre-Entrega es aplicar los conocimientos adquiridos en *Testing Automation*, utilizando *Python* y *Selenium WebDriver* para automatizar flujos básicos de navegación. 

Así se pone en práctica lo aprendido sobre:
- Interacción con elementos web (inputs, botones, menús), 
- Estrategias de localización (By.ID, By.CLASS_NAME, etc.) y 
- Validaciones de navegación, texto y estados de página. 

El sitio objetivo utilizado para esta automatización es **saucedemo.com (https://www.saucedemo.com/)**, una aplicación web demo especialmente diseñada para prácticas de testing.

El proyecto incluye:
- Pruebas de login
- Pruebas de navegación del inventario
- Pruebas de interacción con el carrito de compras


## Repositorio del proyecto: 
https://github.com/mfgallino/Proyecto-QAAutomation


## Tecnologías Utilizadas
- Lenguaje:             Python 3.8 o superior 
- Navegador:            Google Chrome   
- Framework de testing: Pytest  
- Automatización:       Selenium WebDriver  
- Reportes:             Pytest HTML (plugin `pytest-html`)  


## Requisitos Previos
Antes de instalar el proyecto, tener instalados:

- Python 3.8 o superior **(https://www.python.org/downloads/)**
- Google Chrome actualizado
- Git **(https://git-scm.com/install/)** (seguir las intrucciones de la página)
- Acceso a internet (para ejecutar sobre *saucedemo.com*)


## Instalación del Proyecto
Clonar el repositorio de Github, siguiendo los siguientes pasos: 

Escribir las siguientes sentencias desde Git Bash, en la carpeta raíz:
1. Convertir la carpeta raíz del proyecto en un repositorio Git local:
git init
2. Descargar una copia del proyecto:
git clone https://github.com/mfgallino/Proyecto-QAAutomation 


## Instalación de Dependencias
- Pytest **(pip install pytest pytest-html)**
- Selenium **(pip install selenium)**
- Webdriver (ChromeDriver o versión compatible con el navegador) **(pip install webdriver-manager)**


## Estructura del Proyecto
El proyecto está estructurado de la siguiente manera:

- **Carpeta raíz del proyecto/**
- **tests/** (Carpeta de tests automatizados)
- - **test_login.py** (Verifica el inicio de sesión exitoso/fallido)    
- - **test_inventory.py** (Valida la carga del catálogo y los elementos del inventario)
- - **test_shopping.py** (Comprueba la funcionalidad del carrito y la coincidencia de los productos agregados)
- **run_tests.py** (Ejecuta todas las pruebas y genera reporte de resultados)
- **utils.py** (Funciones de soporte reutilizables)
- **conftest.py** (Configuración global de fixtures y setup)
- **report.html** (Reporte de resultados)
- **README.md**



## Ejecución de Pruebas
Todas las pruebas y el reporte de resultados se ejecutan, al ejecutar el siguiente archivo: 
run_tests.py
que corre todos los tests y genera el reporte HTML, guardándolo en la carpeta raíz del proyecto. 


## Resultados
Los resultados de las pruebas se guardan como **report.html** en la carpeta raíz del proyecto.
Incluyen el detalle cada test, su resultado (passed / failed) y su tiempos de duración.