from src.validators.validator_attack_force import validate_attack_force_query_params
from src.error_handling.validation_error_view import ViewError

class AttackForceViews:
    def __init__(self, controller) -> None:
        self.__controller = controller

    # Método para tratar a requisição da rota e retornar a resposta da pesquisa de combinação de signos
    def attack_force_views(self, request_args):
        try:
            # Converte os argumentos da requisição em um dicionário
            query_params = dict(request_args)

            # Valida os parâmetros de consulta recebidos
            validate_attack_force_query_params(query_params)

            # Obtém os nomes dos pokemons a partir dos parâmetros de consulta
            pokemon_first = request_args.get("pokemon_first")
            pokemon_second = request_args.get("pokemon_second")

            # Cria uma instância do controlador de pesquisa de combinação e verifica a força dos Pokemons
            attack_result = self.__controller.calculate_attack_force(pokemon_first, pokemon_second)

            # Retorna a resposta bem-sucedida com os dados da pesquisa do combate
            return {
                "status_code": 200,
                "data": attack_result,
                "success": True
            }
            
        except Exception as exception:
            response = ViewError.handler_error(exception, error_type="attack")
            return response