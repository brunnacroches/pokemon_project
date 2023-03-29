from src.infra.repository.pokemon_repository import PokemonRepository
from src.controllers.attack_force_controller import AttackForceController
from src.view.attack_force_view import AttackForceViews
from src.infra.configs.connection import DBConnectionHandler

def attack_force_composer():
    model = PokemonRepository(DBConnectionHandler)
    controller = AttackForceController(model)
    view = AttackForceViews(controller)
    
    return view

