# Proyecto de Automatización - Talento Tech

Proyecto desarrollado como parte del curso QA Automation con Python - Talento Tech.

## Propósito del Proyecto
El objetivo de este Proyecto Final es automatizar pruebas de UI y de API, aplicando los conocimientos adquiridos sobre:
- Page Object Model (POM), 
- Manejo de datos externos, 
- Generación de reportes HTML, 
- Logging,
- Captura automática de pantalla e
- Integración continua.

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
- Pytest / Pytest-html (`pip install pytest pytest-html`)
- Selenium (`pip install selenium`)
- Webdriver-manager (ChromeDriver o versión compatible con el navegador) (`pip install webdriver-manager`)
- Faker (`pip install Faker`)
- Requests (`pip install requests`)


## Estructura del Proyecto
El proyecto está organizado de la siguiente, aplicando el Page Object Model:

**Carpeta raíz del proyecto/**
- **pages/** (Archivos con lógica de interacción de la página -selectores y métodos)
    - `login_page.py`
    - `inventory_page.py`
    - `cart_page.py`

- **tests/** (Carpeta de tests automatizados)
    - `test_login.py` (Prueba de login exitoso y fallido)
    - `test_login_faker.py` (Prueba de login fallido con datos aleatorios)    
    - `test_inventory.py` (Valida la carga del catálogo y los elementos del inventario)
    - `test_cart.py` (Comprueba la funcionalidad del carrito)
    - `test_cart_json.py` (Comprueba la funcionalidad del carrito con varios productos)
    - `test_api_reqres.py` (Prueba de API -sobre el sitio 'Reqres.in')

- **utils/** (Carpeta con funciones de soporte reutilizables)
    - `datos.py`
    - `lector_json.py`
    - `logger.py`

- **Datos**
    - `data_login.csv` (Datos de entrada para prueba de login)
    - `productos.json` (Datos de entrada para prueba de cart)

- **Logs** 
    - `suite.log` (*se crea automáticamente al ejecutar los tests*)

- **reports/**
    - `report.html` (Reporte de resultados, *se crea automáticamente al ejecutar los tests*)
    
    - **screens/** (Carpeta para archivos de captura de pantalla)
       -  archivos `.png` (Capturas de pantalla ante fallos durante las pruebas, *se crean automáticamente*)

- `conftest.py` (Configuración global de fixtures y setup)

- **`run_tests.py`** (Ejecuta todas las pruebas y genera reporte de resultados)

- **.github/**
    - **workflows/**
        - `ci.yml`  (Realiza las acciones de integración continua dentro de Github)

- `requirements.txt` (Dependencias del proyecto)

- `README.md`  (Resumen del proyecto)


## Pruebas incluidas
El proyecto incluye:
- Pruebas de login (exitoso y fallido) - `test_login.py`
- Pruebas de login fallido utilizando 'Faker' - `test_login_faker.py`
- Pruebas de navegación del inventario - `test_inventory.py`
- Pruebas de interacción con el carrito de compras - `test_cart.py` y `test_cart_json.py`
- Pruebas de API: Peticiones (GET users, POST create users, DELETE user), validaciones de códigos HTTP, validaciones de estructura JSON. - `test_api_reqres.py`


## Ejecución de Pruebas
Todas las pruebas y los reportes de resultados se ejecutan al correr el siguiente archivo de Python: ```run_tests.py```. 


## Reportes de Resultados
### Reporte HTML: 
Los resultados de las pruebas se guardan en un reporte HTML (```report.html```), ubicado en la carpeta ```reports/```. El reporte incluye el detalle cada test, su resultado (passed / failed) y su tiempo de duración.

### Capturas de Pantalla:
También se realizan capturas de pantalla por cada falla ocurrida durante la ejecución de un test. Son archivos ` .png`  que se guardan en la siguiente ubicación: ```reports/screens/```.

### Logs de Ejecución:
Adicionalmente, se generan logs con información detallada de la ejecución de las pruebas en la siguiente ubicación: ```logs/suite.log```.


## Manejo de Datos de Prueba
Algunos tests utilizan datos de prueba parametrizados, ubicados en la carpeta ```datos/```:
- `data_login.csv` datos de usuario y contraseña, para pruebas de login.
- `productos.json` datos de producto de inventario, para pruebas de cart.

## Integración Continua
Cualquier cambio en el código se verifica en forma automática en el repositorio de Github, inmediatamente luego de cada push, dejando un reporte de resultado.
Si algún test falla, se marca y notifica. Por el contrario, si todos los testspasan exitosamente, la versión queda validada e integrada. 
Los comandos para esto, se encuentran en la siguiente ubicación: ```.github/workflows/ci.yml```.


## Conclusiones del proyecto
Este proyecto presenta una estructura organizada y escalable para automatizar pruebas de API utilizando Python y Pytest. 

A través de la ejecución de `run_test.py`, ofrece una forma simple de ejecución de todos los tests y la generación automática de reporte HTML, capturas de pantalla de fallas y logs de ejecución, que facilitan el análisis de las pruebas.

Además, la arquitectura del proyecto esta pensada para agregar nuevos casos de prueba y configuraciones sin modificar el nucleo del proyecto, manteniendo buenas prácticas y permitiendo su escalabilidad en el tiempo.

Adicionalmente, realiza el proceso de integración continua en el repositorio de Github, contribuyendo al aseguramiento de la calidad del código antes de la entrega a producción. 