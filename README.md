### [[ README en Desarrollo - Versión Borrador ]]


# Proyecto de Automatización - Talento Tech

Proyecto desarrollado como parte del curso QA Automation con Python - Talento Tech

## Propósito del Proyecto
El objetivo de este Proyecto Final automatizar pruebas de UI y de API, aplicando los conocimientos adquiridos sobre:
- Page Object Model (POM), 
- Manejo de datos externos, 
- Generación de reportes HTML, 
- Logging y 
- Captura automática de pantalla.

El sitio objetivo utilizado para las pruebas UI es **saucedemo.com (https://www.saucedemo.com/)**, una aplicación web demo especialmente diseñada para prácticas de testing. 
Por su parte, las pruebas de API se realizaron sobre el sitio  **reqres.in (https://reqres.in/api/users)**, que está diseñado para realizar prácticas de este tipo.


## Repositorio del proyecto: 
https://github.com/mfgallino/Proyecto-QAAutomation


## Tecnologías Utilizadas
- Lenguaje:             Python 3.x 
- Navegador:            Google Chrome   
- Framework de testing: Pytest  
- Automatización UI:    Selenium WebDriver  
- Reportes:             Pytest HTML (plugin `pytest-html`)
- Logging de ejecución: Logging
- Datos aleatorios:     Faker
- Formatos de datos:    CSV / JSON
- Solicitud HTTP:       Requests


## Requisitos Previos
Antes de instalar el proyecto, tener instalados:

- Python 3.8 o superior (https://www.python.org/downloads/)
- Google Chrome actualizado
- Git (https://git-scm.com/install/) (seguir las intrucciones de la página)
- Acceso a internet (para ejecutar sobre **saucedemo.com** y **reqres.in/eqres/user**)


## Instalación del Proyecto
Clonar el repositorio de Github, siguiendo los siguientes pasos: 

Escribir las siguientes sentencias desde Git Bash, en la carpeta raíz:
1. Convertir la carpeta raíz del proyecto en un repositorio Git local:
git init
2. Descargar una copia del proyecto:
git clone https://github.com/mfgallino/Proyecto-QAAutomation.git 


## Instalación de Dependencias
- Pytest (`pip install pytest pytest-html`)
- Selenium (`pip install selenium`)
- Webdriver (ChromeDriver o versión compatible con el navegador) (`pip install webdriver-manager`)
- Faker (`pip install Faker`)
- Requests (`pip install requests`)


## Estructura del Proyecto
El proyecto está estructurado de la siguiente, siguiendo el POM:

**Carpeta raíz del proyecto/**
- **pages/**
    - `login_page.py`
    - `inventory_page.py`
    - `cart_page.py`

- **tests/** (Carpeta de tests automatizados)
    - `test_login.py`     
    - `test_inventory.py` (Valida la carga del catálogo y los elementos del inventario)
    - `test_cart.py` (Comprueba la funcionalidad del carrito y la coincidencia de los productos agregados)


- **utils/** (Carpeta con funciones de soporte reutilizables)
    - `datos.py`
    - `lector_json.py`
    - `logger.py`

- **reports/screens/** (Directorio de carpetas para archivos de captura de pantalla)
    -  archivos `.png` (Capturas de pantalla ante fallos durante las pruebas)

- `conftest.py` (Configuración global de fixtures y setup)

- **`run_tests.py`** (Ejecuta todas las pruebas y genera reporte de resultados)

- `report.html` (Reporte de resultados)

- `README.md`  (Resumen del proyecto)


## Pruebas incluidas
El proyecto incluye:
- Pruebas de login (exitoso y fallido) - `test_login.py`
- Pruebas de login fallido utilizando 'Faker' - `test_login_faker.py`
- Pruebas de navegación del inventario - `test_inventory.py`
- Pruebas de interacción con el carrito de compras - `test_cart.py` y `test_cart_json.py`
- Pruebas de API: Peticiones (GET users, POST create users, DELETE user), validaciones de códigos HTTP, validaciones de estructura JSON. - `test_api_reqres.py`



## Ejecución de Pruebas
Todas las pruebas y el reporte de resultados se ejecutan, al ejecutar el siguiente archivo: 
`run_tests.py`
que corre todos los tests y genera el reporte HTML, guardándolo en la carpeta raíz del proyecto. 


## Resultados
Los resultados de las pruebas se guardan como **report.html** en la carpeta raíz del proyecto.
Incluyen el detalle cada test, su resultado (passed / failed) y su tiempos de duración.