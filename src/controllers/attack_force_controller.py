from src.controllers.register_pokemon_controller import RegisterPokemonController
from src.infra.repository.pokemon_repository import PokemonRepository
from src.infra.configs.connection import DBConnectionHandler


class AtackForceController:
    def __init__(self):
        self.db_repository = PokemonRepository(DBConnectionHandler)
    
    def _is_force_attack_pokemon(self):
        pass
    
    def attack_combat(self):
        pass
