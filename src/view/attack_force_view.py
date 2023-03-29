from cerberus import Validator
import traceback
from src.validators.validator_attack_force import validate_attack_force_query_params
from src.controllers.attack_force_controller import AtackForceController
from src.error_handling.validation_error import ValidationError

class AttackForceViews:
    # Método para tratar a requisição da rota e retornar a resposta da pesquisa de combinação de signos
    def attack_force_views(self, request_args):
        try:
            # Converte os argumentos da requisição em um dicionário
            query_params = dict(request_args)
            
            # Valida os parâmetros de consulta recebidos
            validation_response = validate_attack_force_query_params(query_params)
            if not validation_response["is_valid"]:
                raise ValidationError("Invalid query params: {}".format(validation_response["error"]))

            # Obtém os nomes dos pokemons a partir dos parâmetros de consulta
            pokemon_first = request_args.get("pokemon_first")
            pokemon_second = request_args.get("pokemon_second")

            # Cria uma instância do controlador de pesquisa de combinação e verifica a força dos Pokemons
            attack_force_controller = AtackForceController()
            attack_result = attack_force_controller.calculate_attack_force(pokemon_first, pokemon_second)

            # Retorna a resposta bem-sucedida com os dados da pesquisa do combate
            return {
                "status_code": 200,
                "data": attack_result,
                "success": True
            }
            
        except Exception as e:
            # Registre o erro e retorne um dicionário com uma mensagem de erro e um código de status de erro
            traceback.print_exc()
            print(f"Erro ao calcular o combate entre os Pokemons: {e}")
            return {"data": {"error": "Ocorreu um erro ao calcular o combate entre os Pokemons."}, "status_code": 500}  
