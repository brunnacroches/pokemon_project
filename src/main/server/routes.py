from flask import request, jsonify, make_response
from src.main.server.server_flask import app
from src.view.register_pokemon_view import RegisterPokemonViews
from src.view.attack_force_view import AttackForceViews
from src.main.composer.register_pokemon_composer import register_pokemon_composer
from src.main.composer.attack_force_composer import attack_force_composer

@app.route("/register_pokemon", methods=["POST"])
def register_pokemon_route():
    pokemon_route = register_pokemon_composer()
    
    http_response = pokemon_route.register_pokemon_view(request)
    
    response = make_response(jsonify(http_response["data"]), http_response["status_code"])
    return response

@app.route("/register_pokemon/atack_force/", methods=["GET"])
def search_person_route():
    attack_route = attack_force_composer()

    http_response = attack_route.attack_force_views(request.args)

    print(f"http_response: {http_response}")

    return jsonify(http_response["data"]), http_response["status_code"]
