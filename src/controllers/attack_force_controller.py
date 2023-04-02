from src.error_handling.validation_error_controller import ValidationErrorController

class AttackForceController:
    def __init__(self, model):
        self.db_repository = model

    def calculate_attack_force(self, pokemon_first: str, pokemon_second: str):
        pokemon_1 = self.db_repository.find_by_name(pokemon_first)
        pokemon_2 = self.db_repository.find_by_name(pokemon_second)

        validation_error = ValidationErrorController.validate_attack_fields(pokemon_first, pokemon_second, pokemon_1, pokemon_2)

        if validation_error:
            return validation_error

        if pokemon_1.attack_value > pokemon_2.attack_value:
            return f"{pokemon_first} wins!"
        elif pokemon_2.attack_value > pokemon_1.attack_value:
            return f"{pokemon_second} wins!"
        else:
            return "It's a tie!"
