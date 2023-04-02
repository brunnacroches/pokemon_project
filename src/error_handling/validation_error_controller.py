from typing import Optional
from src.error_handling.validation_error import ControllerError

class ValidationErrorController(Exception):
    def __init__(self, message, errors=None) -> None:
        super().__init__(message)
        self.message = message
        self.errors = errors
        self.error_type = 'Controller Error'

    @staticmethod
    def validate_input_is_not_empty(*inputs):
        return all(len(input) > 0 for input in inputs)

    @staticmethod
    def validate_no_spaces_in_inputs(*inputs):
        return all(' ' not in input for input in inputs)

    @staticmethod
    def validate_values_are_not_null(*values):
        return all(value is not None for value in values)

    @staticmethod
    def validate_names_found(*names):
        return all(name is not None for name in names)

    @staticmethod
    def validate_pokemon_fields(name_pokemon: str, attack_force: str, attack_value: Optional[int]):
        if not ValidationErrorController.validate_input_is_not_empty(name_pokemon, attack_force) or not ValidationErrorController.validate_no_spaces_in_inputs(name_pokemon, attack_force):
            raise ControllerError("Error: Invalid input(s)")
        if not ValidationErrorController.validate_values_are_not_null(attack_value):
            raise ControllerError("Error: Attack value not found")
        try:
            int(attack_value)
        except ValueError:
            raise ControllerError("Error: Invalid attack value")

    @staticmethod
    def validate_attack_fields(pokemon_name_1: str, pokemon_name_2: str, pokemon_data_1, pokemon_data_2) -> str:
        if not ValidationErrorController.validate_input_is_not_empty(pokemon_name_1, pokemon_name_2) or not ValidationErrorController.validate_no_spaces_in_inputs(pokemon_name_1, pokemon_name_2):
            return "Invalid input(s)."

        if not ValidationErrorController.validate_values_are_not_null(pokemon_name_1, pokemon_name_2, pokemon_data_1, pokemon_data_2):
            return "Value(s) cannot be null."

        if not ValidationErrorController.validate_names_found(pokemon_data_1, pokemon_data_2):
            return "One or both Pokemons not found."

        return ""
