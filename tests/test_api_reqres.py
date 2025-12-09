import requests
import pytest

# Obtener usuario
def test_get_users(url_base, header_request):   
    
    # Hacer la petición
    response = requests.get(f"{url_base}/2", headers=header_request)
    
    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200
    
    data = response.json()

    # Verificar que la clave "data" está presente
    assert "data" in data

    # Verificar que el id es id=2  
    assert data["data"]["id"] == 2

    # Verificar que haya al menos un usuario en la lista
    assert len(data["data"]) > 0

# Crear usuario
def test_create_user(url_base, header_request):
    
    # Guardar el dato en formato JSON en una variable ('payload')
    payload = {
        "name": "María",
        "job": "Ingeniera"
    }
    
    # Hacer la petición
    response = requests.post(url_base, headers=header_request, json=payload)

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 201

    data = response.json()

    # Verificar que el nombre de la respuesta sea el mismo que el dato de entrada
    assert data["name"] == payload["name"]

    # Verificar que la respuesta tenga id y 'createdAt'
    assert "id" and "createdAt" in data
    
# Eliminar usuario
def test_delete_user(url_base, header_request):
    
    # Hacer petición
    response = requests.delete(f"{url_base}/2", headers=header_request)

    # Verificar el status de la respuesta
    assert response.status_code == 204

