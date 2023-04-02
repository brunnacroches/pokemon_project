import pytest
from unittest.mock import MagicMock
from src.view.register_pokemon_view import RegisterPokemonViews

# Classe que representa o Pokemon com um unico atributo
class Pokemon:
    def __init__(self, attack) -> None:
        self.attack_value = attack

# Classe MockController que simula o comportamento de um controller
class MockController:
    def __init__(self) -> None:
        self.register_pokemon_controller_attributes = []

    # Metodo que simula a funcao register_pokemon_controller do controlador real
    def register_pokemon_controller(self, name_pokemon, attack_force, attack_value):
        self.register_pokemon_controller_attributes.append((name_pokemon, attack_force, attack_value))

# Testar registro de Pokemon valido
def test_register_pokemon_view_valid():
    controller = MockController()
    test_register_pokemon_view = RegisterPokemonViews(controller)
    request = MagicMock()
    request.json = {
        "name_pokemon": "Pikachu",
        "attack_force": "Electric",
        "attack_value": 100
    }
    response = test_register_pokemon_view.register_pokemon_view(request)

    # Verificando se os valores corretos foram registrado
    assert controller.register_pokemon_controller_attributes[0] == ('Pikachu', 'Electric', 100)

    # Verificando se a resposta e a resposta
    assert response["status_code"] == 200
    assert response["data"] == {
        "name_pokemon": "Pikachu",
        "attack_force": "Electric",
        "attack_value": 100
    }
    assert response["success"] == True

def test_register_pokemon_view_invalid():
    controller = MockController()
    register_pokemon_view = RegisterPokemonViews(controller)
    request = MagicMock()
    request.json = {
        "name_pokeon": "",
        "attack_force": "Electric",
        "attack_value": 100
    }
    response = register_pokemon_view.register_pokemon_view(request)

    # Verificando se a resposta e a esperada
    assert response["status_code"] == 400
    expected_error_message = {
        "message": "Invalid request body",
        "errors": {
            "name_pokemon": ["required field"],
            "name_pokeon": ["unknown field"]
        }
    }
    assert response["error_message"] == str(expected_error_message)