from unittest.mock import MagicMock
from src.controllers.register_pokemon_controller import RegisterPokemonController

class TestRegisterPokemonController:
    def test_register_pokemon_controller(self):
        # Cria um mock do repositório de Pokemon para testar o controller
        mock_repo = MagicMock()
        mock_pokemon = {"name_pokemon": "Pikachu", "attack_force": "Thunderbolt", "attack_value": 8}
        mock_repo.insert.return_value = mock_pokemon

        # Cria uma instância do controller
        controller = RegisterPokemonController(mock_repo)

        # Chama o método de registro de um novo Pokemon e verifica se o resultado é o esperado
        result = controller.register_pokemon_controller("Pikachu", "Thunderbolt", 8)
        assert result == mock_pokemon

        # Verifica se o método 'insert' do repositório foi chamado corretamente com os argumentos corretos
        mock_repo.insert.assert_called_once_with("Pikachu", "Thunderbolt", 8)
