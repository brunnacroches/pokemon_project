import pytest
from unittest.mock import MagicMock
from src.controllers.attack_force_controller import AttackForceController
from src.infra.entities.pokemon_entities import Pokemon

class TestAttackForceController:
    @pytest.fixture
    def model_mock(self):
        mock = MagicMock()
        mock.find_by_name.side_effect = lambda name: {
            "Fyredra": Pokemon(name_pokemon="Fyredra", attack_value=9),
            "Aqualynx": Pokemon(name_pokemon="Aqualynx", attack_value=1),
        }.get(name)
        return mock

    @pytest.fixture
    def controller(self, model_mock):
        return AttackForceController(model_mock)

    def test_calculate_attack_force_win(self, controller):
        result = controller.calculate_attack_force("Fyredra", "Aqualynx")
        assert result == "Fyredra wins!"

    def test_calculate_attack_force_lose(self, controller):
        result = controller.calculate_attack_force("Aqualynx", "Fyredra")
        assert result == "Fyredra wins!"

    def test_calculate_attack_force_tie(self, controller):
        result = controller.calculate_attack_force("Fyredra", "Fyredra")
        assert result == "It's a tie!"

    def test_calculate_attack_force_not_found(self, controller):
        result = controller.calculate_attack_force("Fyredra", "Non-existent")
        assert result == "One or both Pokemons not found."
