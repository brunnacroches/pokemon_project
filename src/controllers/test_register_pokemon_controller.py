import pytest
from src.controllers.register_pokemon_controller import RegisterPokemonController
from src.error_handling.validation_error import ControllerError

class Pokemon:
    def __init__(self, name_pokemon, attack_force, attack_value) -> None:
        self.name_pokemon == name_pokemon
        self.attack_force == attack_force
        self.attack_value == attack_value

class MockModel:
    def __init__(self) -> None:
        self.find_by_name_attibutes = []
        self.register_pokemon_controller_attributes = []
        self.insert_pokemons = []

    def insert(self, name_pokemon, attack_force, attack_value):
        self.register_pokemon_controller_attributes.append((name_pokemon, attack_force, attack_value))
        self.insert_pokemons.append({
            'name_pokemon': name_pokemon,
            'attack_force': attack_force,
            'attack_value': attack_value
        })
        return True

class InvalidModel:
    pass

def test_register_pokemon_controller_varying_values():
    model = MockModel()
    register_pokemon_controller = RegisterPokemonController(model)
    response = register_pokemon_controller.register_pokemon_controller("Bulbasaur", "Grass", 49)
    
    assert model.register_pokemon_controller_attributes[0] == ("Bulbasaur", "Grass", 49)
    assert model.insert_pokemons[0] ==  {"name_pokemon": "Bulbasaur", "attack_force": "Grass", "attack_value": 49}
    
    assert response == True
    # print()
    # print(response)

def test_register_pokemon_controller_name_not_found():
    model = MockModel()
    register_pokemon_controller = RegisterPokemonController(model)

    with pytest.raises(ControllerError) as exc_info:
        register_pokemon_controller.register_pokemon_controller("", "Grass", 49)
    assert str(exc_info.value) == "Error: Invalid input(s)"

    # print()
    # print(response)

def test_register_pokemon_controller_attack_force_not_found():
    model = MockModel()
    register_pokemon_controler = RegisterPokemonController(model)
    
    with pytest.raises(ControllerError) as exc_info:
        register_pokemon_controler.register_pokemon_controller("Bulbasaur", "", 49)
    assert str(exc_info.value) == "Error: Invalid input(s)"

    # print()
    # print(response)   

def test_register_pokemon_controller_attack_valule_not_found():
    model = MockModel()
    register_pokemon_controller = RegisterPokemonController(model)
    
    with pytest.raises(ControllerError) as exc_info:
        register_pokemon_controller.register_pokemon_controller("Bulbasaur", "Grass", None)
    assert str(exc_info.value) == "Error: Attack value not found"

    # print()
    # print(response)
 
def test_register_pokemon_controller_invalid_model():
    model = InvalidModel()
    register_pokemon_controller = RegisterPokemonController(model)
    
    with pytest.raises(AttributeError):
        response = register_pokemon_controller.register_pokemon_controller("Bulbasaur", "Grass", 49)
        print()
        print(response)
        assert response == 'Error: Not found'

def test_register_pokemon_controller_empty_inputs():
    model = MockModel()
    register_pokemon_controller = RegisterPokemonController(model)
    with pytest.raises(ControllerError) as exc_info:
        register_pokemon_controller.register_pokemon_controller('', '', '')
    assert str(exc_info.value) == "Error: Invalid input(s)"

def test_register_pokemons_controller_invald_inputs():
    model = MockModel()
    register_pokemons_controller = RegisterPokemonController(model)
    with pytest.raises(ControllerError) as exc_info:
        register_pokemons_controller.register_pokemon_controller('!@#$', '!@#$', '!@#$')
    assert str(exc_info.value) == 'Error: Invalid attack value'

def test_register_pokemons_controller_space_inputs():
    model = MockModel()
    register_pokemons_controller = RegisterPokemonController(model)
    with pytest.raises(ControllerError) as exc_info:
        register_pokemons_controller.register_pokemon_controller("Bulbas aur", "Gra ss", 49)
    assert str(exc_info.value) == 'Error: Invalid input(s)'

def test_register_pokemons_controller_case_insensitive_inputs():
    model = MockModel()
    register_pokemon_controller = RegisterPokemonController(model)
    
    try:
        response_upper = register_pokemon_controller.register_pokemon_controller("BULBASAUR", "GRASS", 49)
        response_lower = register_pokemon_controller.register_pokemon_controller("bulbasaur", "grass", 49)
        response_mixed = register_pokemon_controller.register_pokemon_controller("BuLbAsAuR", "GrAsS", 49)
    except ControllerError:
        pytest.fail("ControllerError raised unexpectedly")
    
    assert model.register_pokemon_controller_attributes[0] == ("BULBASAUR", "GRASS", 49)
    assert model.insert_pokemons[0] == {"name_pokemon": "BULBASAUR", "attack_force": "GRASS", "attack_value": 49}
    assert response_upper == True
    
    assert model.register_pokemon_controller_attributes[1] == ("bulbasaur", "grass", 49)
    assert model.insert_pokemons[1] == {"name_pokemon": "bulbasaur", "attack_force": "grass", "attack_value": 49}
    assert response_lower == True
    
    assert model.register_pokemon_controller_attributes[2] == ("BuLbAsAuR", "GrAsS", 49)
    assert model.insert_pokemons[2] == {"name_pokemon": "BuLbAsAuR", "attack_force": "GrAsS", "attack_value": 49}
    assert response_mixed == True
