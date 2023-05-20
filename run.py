from src.main.server.server_flask import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# http://localhost:5000/register_pokemon/atack_force/?pokemon_first=Fyredra&pokemon_second=Aqualynx