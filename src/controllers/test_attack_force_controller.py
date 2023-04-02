import pytest
from src.controllers.attack_force_controller import AttackForceController
from src.error_handling.validation_error import ControllerError

# Classe que representa um Pokemon com um único atritubo
class Pokemon:
    def __init__(self, attack) -> None:
        self.attack_value = attack

# Classe MockModel que simula o comportamento de um modelo real
class MockModel:
    def __init__(self) -> None:
        self.find_by_name_atrributes = []
        self.register_pokemon_controller_attributes = []
    
    # Método que simula a função find_by_name do modelo real
    def find_by_name(self, name):
        if name is None:
            return None

        self.find_by_name_atrributes.append(name)
        if name.lower() == 'element1':
            return Pokemon(1)
        if name.lower() == 'element2':
            return Pokemon(2)
        return None

# Classe para o Model inválido
class InvalidModel:
    pass

#  1- Testar para verificar se o resultado é empate
def test_calculate_attack_force_tie():
    model = MockModel()
    attack_force_controller = AttackForceController(model) # injeção de dependencia
    response = attack_force_controller.calculate_attack_force('element1', 'element1')

    # Verificando se os elementos corretos foram buscados
    assert model.find_by_name_atrributes[0] == 'element1'
    assert model.find_by_name_atrributes[1] == 'element1'

    # Verificando se a resposta é a esperada
    assert isinstance(response, str)
    assert response == "It's a tie!"

    # print()
    # print(response)

# 2- Testar para verificar se o resultado é uma vitória
def test_calculate_attack_force_win():
    model = MockModel()
    attack_force_controller = AttackForceController(model)
    response = attack_force_controller.calculate_attack_force('element1', 'element2')
    
    # Verificando se os elementos corretos foram buscados
    assert model.find_by_name_atrributes[0] == 'element1'
    assert model.find_by_name_atrributes[1] == 'element2'
    
    # Verificando se a resposta é a esperada
    assert isinstance(response, str)
    assert response == 'element2 wins!'
    
    # print()
    # print(response)

# 3- Testar com diferentes valores de ataque para os Pokemons
def test_calculate_attack_force_varying_attack_values():
    model = MockModel()
    attack_force_controller = AttackForceController(model)    
    response = attack_force_controller.calculate_attack_force('element1', 'element2')

    assert isinstance(response, str)
    assert response == 'element2 wins!'

    # print()
    # print(response)

# 4- Testar os casos em que apenas o primeiro não é encontrado
def test_calculate_attack_force_first_not_found():
    model = MockModel()
    attack_force_controller = AttackForceController(model)    
    response = attack_force_controller.calculate_attack_force('', 'element2')
    
    assert isinstance(response, str)
    assert response == 'Invalid input(s).'

    # print()
    # print(response)

# # 5- Testar os casos em que apenas o segundo não é encontrado
def test_calculate_attack_force_second_not_found():
    model = MockModel()
    attack_force_controller = AttackForceController(model)    
    response = attack_force_controller.calculate_attack_force('element1', '')
    
    assert isinstance(response, str)
    assert response == 'Invalid input(s).'

    # print()
    # print(response)

# # 6- Testar inicialização da Lógica do Controller com um objeto ´model´ inválido
def test_calculate_attack_force_invalid_model():
    invalid_model = InvalidModel()
    attack_force_controller = AttackForceController(invalid_model)

    with pytest.raises(AttributeError):
        response = attack_force_controller.calculate_attack_force('element1', 'element2')
        # print()
        # print(response)

# # 7- Testar com entradas vazias
def test_calculate_attack_force_empty_inputs():
    model = MockModel()
    attack_force_controller = AttackForceController(model)    
    response = attack_force_controller.calculate_attack_force('', '')
    
    assert isinstance(response, str)
    assert response == 'Invalid input(s).'

    # print()
    # print(response)

# # 8- Testar com entradas nulas
# def test_calculate_attack_force_null_inputs():
#     model = MockModel()
#     attack_force_controller = AttackForceController(model)    
#     response = attack_force_controller.calculate_attack_force(None, None)
    
#     assert isinstance(response, str)
#     assert response == 'One or both Pokemons not found.'

#     # print()
#     # print(response)

# 9- Testar com entradas inválidas ou incorretas
def test_calculate_attack_force_invalid_inputs():
    model = MockModel()
    attack_force_controller = AttackForceController(model)    
    response = attack_force_controller.calculate_attack_force('!@#$', '1234')
    
    assert isinstance(response, str)
    assert response == 'Value(s) cannot be null.'
    
    # print()
    # print(response)

# # 10- Testar com entradas contendo espaços
def test_calculate_attack_force_space_inputs():
    model = MockModel()
    attack_force_controller = AttackForceController(model)    
    response = attack_force_controller.calculate_attack_force('element 1', 'element 2')
    
    assert isinstance(response, str)
    assert response == 'Invalid input(s).'

    # print()
    # print(response)

# # 11- Testar com nomes em diferentes combinações de letra maiúsculas e minísculas 
# def test_calculate_attack_force_case_insensitive_inputs():
    model = MockModel()
    attack_force_controller = AttackForceController(model)
    response = attack_force_controller.calculate_attack_force('Element1', 'ElEmEnT2')

    # Verificando se os elementos corretos foram buscados
    assert model.find_by_name_atrributes[0] == 'Element1'
    assert model.find_by_name_atrributes[1] == 'ElEmEnT2'
    
    # Verificando se a resposta é a esperada
    assert isinstance(response, str)
    assert response == 'ElEmEnT2 wins!'
    # print()
    # print(response)