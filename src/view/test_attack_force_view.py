from src.view.attack_force_view import AttackForceViews

# Classe MockController que simula o comportamento de um controller
class MockController:
    def __init__(self) -> None:
        self.calculate_attack_force_attributes = []

    # Método que simula a função calculate_attack_force do controlador real
    def calculate_attack_force(self, pokemon_first, pokemon_second):
        self.calculate_attack_force_attributes.append((pokemon_first, pokemon_second))
        return {
            "pokemon_first": pokemon_first,
            "pokemon_second": pokemon_second,
            "winner": pokemon_first
        }

def test_attack_force_view_valid():
    controller = MockController()
    test_attack_force_view = AttackForceViews(controller)
    
    # Simular os argumentos da requisição
    request_args = {
        "pokemon_first": "Pikachu",
        "pokemon_second": "Bulbasaur"
    }
    
    response = test_attack_force_view.attack_force_views(request_args)

    # Verificando se os valores corretos foram registrados
    assert controller.calculate_attack_force_attributes[0] == ("Pikachu", "Bulbasaur")

    # Verificando se a resposta é a esperada
    assert response["status_code"] == 200
    assert response["data"] == {
        "pokemon_first": "Pikachu",
        "pokemon_second": "Bulbasaur",
        "winner": "Pikachu"
    }
    assert response["success"] == True
