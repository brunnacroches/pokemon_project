from src.validators.validate_register_pokemon import validate_register_pokemon_request_body
from src.validators.validate_register_pokemon import validate_register_pokemon_request_body
from src.error_handling.validation_error_view import ViewError

class RegisterPokemonViews:
    def __init__(self, controller) -> None:
        self.__controller = controller

    def register_pokemon_view(self, request):
        try:
            validate_register_pokemon_request_body(request.json)

            body = request.json
            name_pokemon = body["name_pokemon"]
            attack_force = body["attack_force"]
            attack_value = body["attack_value"]

            # chama o controller para criar o registro
            self.__controller.register_pokemon_controller(name_pokemon, attack_force, attack_value)

            return {
                "status_code": 200,
                "data": {
                    "name_pokemon": name_pokemon,
                    "attack_force": attack_force,
                    "attack_value": attack_value
                },
                "success": True
            }

        except Exception as exception:
            # Envia a exceção para a função de tratamento de erros
            response = ViewError.handler_error(exception, error_type="register")
            return response
