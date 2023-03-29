from cerberus import Validator
from src.validators.validate_register_pokemon import validate_register_pokemon_request_body
from pokemon_project.src.validators.validate_register_pokemon import validate_register_pokemon_request_body
from src.controllers.register_pokemon_controller import RegisterPokemonController
from src.error_handling.validation_error import ValidationError

class RegisterPokemonViews:
    def register_pokemon_view(self, request):
        try:
            validation_response = validate_register_pokemon_request_body(request.json)
            if not validation_response["is_valid"]:
                raise ValidationError("Invalid request body", validation_response["error"])
            
            body = request.json
            name_pokemon = body["name_pokemon"]
            attack_force = body["attack_force"]
            attack_value = body["attack_value"]

            # chama o controller para criar o registro
            register_pokemon_controller = RegisterPokemonController()
            register_pokemon_controller.register_pokemon_controller(name_pokemon, attack_force, attack_value)

            return {
                "status_code": 200,
                "data": {
                    "name_pokemon": name_pokemon,
                    "attack_force": attack_force,
                    "attack_value": attack_value
                },
                "success": True
            }
            

        except Exception as e:
            # Registre o erro e retorne um dicionário com uma mensagem de erro e um código de status de erro
            print(f"Erro ao registrar o Pokemon: {e}")
            return {"data": {"error": "Ocorreu um erro ao registrar o Pokemon."}, "status_code": 500}
