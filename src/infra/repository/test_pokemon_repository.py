import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import mock
from src.infra.entities.pokemon_entities import Pokemon
from src.infra.repository.pokemon_repository import PokemonRepository
import os

os.environ["SQLALCHEMY_WARN_20"] = "1"

class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(Pokemon),  # condição para acessar esses dados
                    ],
                    [Pokemon(id_pokemon=1234, name_pokemon="Fyredra", attack_force="SolarBlast")]
                )
            ]
        )

    # Método especial __enter__ é chamado ao entrar em um bloco 'with'
    def __enter__(self):
        return self

    # Método especial __exit__ é chamado ao sair do bloco 'with'
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Fechando a sessão atual
        self.session.close()

    def __call__(self):
        return self
        # Fechando a sessão atual
        self.session.close()


def test_select():
    pokemon_repository = PokemonRepository(ConnectionHandlerMock)
    response = pokemon_repository.select()
    print()
    print(response)
    assert isinstance(response, list)
    assert isinstance(response[0], Pokemon)
    assert response[0].name_pokemon == "Fyredra"

def test_insert():
    pokemon_repository = PokemonRepository(ConnectionHandlerMock)
    response = pokemon_repository.insert("Aqualynx", "SlashingWind", 9)
    print()
    print(response)
    assert isinstance(response, Pokemon)

def test_delete():
    pokemon_repository = PokemonRepository(ConnectionHandlerMock)
    response = pokemon_repository.delete(1234)
    print()
    print(response)
    assert response == 1234

def test_update():
    pokemon_repository = PokemonRepository(ConnectionHandlerMock)
    response = pokemon_repository.update(1234, 4321)
    print()
    print(response)
    assert response == 4321

def test_find_by_name():
    pokemon_repository = PokemonRepository(ConnectionHandlerMock)
    response = pokemon_repository.find_by_name("Fyredra")
    print()
    print(response)
    assert response.name_pokemon == "Fyredra"
