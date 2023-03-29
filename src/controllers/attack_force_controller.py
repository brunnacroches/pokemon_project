from src.infra.repository.pokemon_repository import PokemonRepository
from src.infra.configs.connection import DBConnectionHandler


class AtackForceController:
    def __init__(self):
        self.db_repository = PokemonRepository(DBConnectionHandler)

    def calculate_attack_force(self, pokemon_first, pokemon_second):
            pokemon_1 = self.db_repository.find_by_name(pokemon_first)
            pokemon_2 = self.db_repository.find_by_name(pokemon_second)
            if pokemon_1 and pokemon_2:
                if pokemon_1.attack_value > pokemon_2.attack_value:
                    return f"{pokemon_first} wins!"
                elif pokemon_2.attack_value > pokemon_1.attack_value:
                    return f"{pokemon_second} wins!"
                else:
                    return "It's a tie!"
            else:
                return "One or both Pokemons not found."
