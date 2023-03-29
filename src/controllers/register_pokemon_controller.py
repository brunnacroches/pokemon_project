class RegisterPokemonController:
    def __init__(self, model) -> None:
        self.db_repository = model

    def register_pokemon_controller(self, name_pokemon: str, attack_force: str, attack_value: int):
        return self.db_repository.insert(name_pokemon, attack_force, attack_value)
