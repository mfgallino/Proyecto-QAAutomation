import requests
import pytest

from utils.logger import logger

# Obtener usuario
def test_get_users(url_base, header_request):   
    # Hacer la petición
    logger.info("Realizando 'petición GET'.") # log
    response = requests.get(f"{url_base}/2", headers=header_request)
    
    # Verificar que la respuesta sea exitosa
    logger.info("Verificando el código de status (200).") # log
    assert response.status_code == 200
    
    data = response.json()

    # Verificar que la clave "data" está presente
    logger.info("Verificando la presencia de la clave data.") # log
    assert "data" in data

    # Verificar que el id es id=2  
    logger.info("Verificando el id.") # log
    assert data["data"]["id"] == 2

    # Verificar que haya al menos un usuario en la lista
    logger.info("Verificando que el listado de usuarios no esté vacío.") # log
    assert len(data["data"]) > 0

# Crear usuario
def test_create_user(url_base, header_request):
    # Guardar el dato en formato JSON en una variable ('payload')
    payload = {
        "name": "María",
        "job": "Ingeniera"
    }
    
    # Hacer la 
    logger.info("Realizando 'petición POST'.") # log
    response = requests.post(url_base, headers=header_request, json=payload)

    # Verificar que la respuesta sea exitosa
    logger.info("Verificando el código de status (201).") # log
    assert response.status_code == 201

    data = response.json()

    # Verificar que el nombre de la respuesta sea el mismo que el dato de entrada
    logger.info("Verificando que en nombre de la respuesta coincida con el nombre del dato de entrada del post.") # log
    assert data["name"] == payload["name"]

    # Verificar que la respuesta tenga id y 'createdAt'
    logger.info("Verificando la existencia de id y createdAt.") # log
    assert "id" and "createdAt" in data
    
# Eliminar usuario
def test_delete_user(url_base, header_request):
    # Hacer petición
    logger.info("Realizando 'petición DELETE'.") # log
    response = requests.delete(f"{url_base}/2", headers=header_request)

    # Verificar el status de la respuesta
    logger.info("Verificando el código de status (204).") # log
    response.status_code == 204

