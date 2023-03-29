from src.infra.repository.pokemon_repository import PokemonRepository
from src.infra.configs.connection import DBConnectionHandler


class RegisterPokemonController:
    def __init__(self) -> None:
        self.db_repository = PokemonRepository(DBConnectionHandler)

    def register_pokemon_controller(self, name_pokemon: str, attack_force: str, attack_value: int):
        return self.db_repository.insert(name_pokemon, attack_force, attack_value)
