import pytest

#Lista de archivos de tests a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_cart_json.py",
    "tests/test_login_faker.py",
    "tests/test_api_reqres.py"
]
# Argumentos para ejecutar los tests:
# Concatenamos los archivos y los parámetros para generar el reporte de pytest
#  (el reporte ppiamente dicho, 'self-contained...' para que los estilos sean generados dentro del mismo html,
#   y -v para que muestre los detalles de los resultados del test)
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

if __name__ == "__main__":
    pytest.main(pytest_args)