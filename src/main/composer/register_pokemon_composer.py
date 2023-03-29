from src.infra.repository.pokemon_repository import PokemonRepository
from src.controllers.register_pokemon_controller import RegisterPokemonController
from src.view.register_pokemon_view import RegisterPokemonViews
from src.infra.configs.connection import DBConnectionHandler


def register_pokemon_composer():
    model = PokemonRepository(DBConnectionHandler)
    controller = RegisterPokemonController(model)
    view = RegisterPokemonViews(controller)

    return view