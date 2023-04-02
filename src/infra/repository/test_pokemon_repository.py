from faker import Faker
from src.infra.configs.connection import DBConnectionHandler
from src.infra.entities.pokemon_entities import Pokemon
from src.infra.repository.pokemon_repository import PokemonRepository
from sqlalchemy.orm import Session, session

faker = Faker()
pokemon_repository = PokemonRepository(DBConnectionHandler)
db_connection_handler = DBConnectionHandler()

def test_insert_pokemon():
    """Should insert a Pokemon in Pokemon table and return it"""

    name_pokemon = faker.name()
    attack_force = "Electric"
    attack_value = faker.random_number(digits=3)

    # Inserir o novo Pokémon
    new_pokemon = pokemon_repository.insert(name_pokemon, attack_force, attack_value)

    # Obter o engine e criar uma sessão separada para a consulta de teste
    engine = db_connection_handler.get_engine()
    test_session = Session(bind=engine)

    # Adicionar o objeto new_pokemon à sessão de teste e sincronizar com o banco de dados
    test_session.add(new_pokemon)
    test_session.flush()

    # Consultar o Pokémon inserido
    query_pokemon = test_session.query(Pokemon).filter_by(id_pokemon=new_pokemon.id_pokemon).first()

    assert new_pokemon.id_pokemon == query_pokemon.id_pokemon
    assert new_pokemon.name_pokemon == query_pokemon.name_pokemon
    assert new_pokemon.attack_force == query_pokemon.attack_force
    assert new_pokemon.attack_value == query_pokemon.attack_value

    # Remover o Pokémon e fechar a sessão de teste
    test_session.delete(new_pokemon)
    test_session.commit()
    test_session.close()

def test_select_pokemon():
    """Should select all Pokemon from the Pokemon table"""

    # Inserir 2 novos Pokémon
    name_pokemon_1 = faker.name()
    attack_force_1 = "Electric"
    attack_value_1 = faker.random_number(digits=3)
    new_pokemon_1 = pokemon_repository.insert(name_pokemon_1, attack_force_1, attack_value_1)

    name_pokemon_2 = faker.name()
    attack_force_2 = "Water"
    attack_value_2 = faker.random_number(digits=3)
    new_pokemon_2 = pokemon_repository.insert(name_pokemon_2, attack_force_2, attack_value_2)

    # Obter o engine e criar uma sessão separada para a consulta de teste
    engine = db_connection_handler.get_engine()
    test_session = Session(bind=engine)

    # Adicionar os objetos new_pokemon à sessão de teste e sincronizar com o banco de dados
    test_session.add(new_pokemon_1)
    test_session.add(new_pokemon_2)
    test_session.flush()

    # Selecionar todos os Pokémon
    all_pokemon = pokemon_repository.select()

    # Verificar se os dois novos Pokémon estão na lista de todos os Pokémon
    assert any(pokemon.id_pokemon == new_pokemon_1.id_pokemon for pokemon in all_pokemon)
    assert any(pokemon.id_pokemon == new_pokemon_2.id_pokemon for pokemon in all_pokemon)

    # Remover os Pokémon inseridos e fechar a sessão de teste
    test_session.delete(new_pokemon_1)
    test_session.delete(new_pokemon_2)
    test_session.commit()
    test_session.close()

def test_delete_pokemon():
    """Should delete a Pokemon from the Pokemon table by id"""

    # Inserir um novo Pokémon
    name_pokemon = faker.name()
    attack_force = "Electric"
    attack_value = faker.random_number(digits=3)
    new_pokemon = pokemon_repository.insert(name_pokemon, attack_force, attack_value)

    # Obter o engine e criar uma sessão separada para a consulta de teste
    engine = db_connection_handler.get_engine()
    test_session = Session(bind=engine)

    # Adicionar o objeto new_pokemon à sessão de teste e sincronizar com o banco de dados
    test_session.add(new_pokemon)
    test_session.flush()

    # Consultar o Pokémon inserido
    inserted_pokemon = test_session.query(Pokemon).filter_by(id_pokemon=new_pokemon.id_pokemon).first()

    # Deletar o Pokémon inserido
    deleted_pokemon_id = pokemon_repository.delete(inserted_pokemon.id_pokemon)

    # Verificar se o Pokémon foi deletado corretamente
    assert deleted_pokemon_id == inserted_pokemon.id_pokemon

    # Fechar a sessão de teste
    test_session.close()

    # Criar uma nova sessão de teste para consultar o

def test_update_pokemon():
    """Should update a Pokemon's id_pokemon in the Pokemon table"""

    # Inserir um novo Pokémon
    name_pokemon = faker.name()
    attack_force = "Electric"
    attack_value = faker.random_number(digits=3)
    new_pokemon = pokemon_repository.insert(name_pokemon, attack_force, attack_value)

    # Obter o engine e criar uma sessão separada para a consulta de teste
    engine = db_connection_handler.get_engine()
    test_session = Session(bind=engine)

    # Adicionar o objeto new_pokemon à sessão de teste e sincronizar com o banco de dados
    test_session.add(new_pokemon)
    test_session.flush()

    # Consultar o Pokémon inserido
    inserted_pokemon = test_session.query(Pokemon).filter_by(id_pokemon=new_pokemon.id_pokemon).first()

    # Atualizar o id_pokemon do Pokémon inserido
    new_id_pokemon = inserted_pokemon.id_pokemon + 100
    updated_pokemon_id = pokemon_repository.update(inserted_pokemon.id_pokemon, new_id_pokemon)

    # Confirmar as alterações no banco de dados
    test_session.commit()

    # Verificar se o id_pokemon foi atualizado corretamente
    assert updated_pokemon_id == new_id_pokemon

    # Consultar o Pokémon atualizado
    updated_pokemon = test_session.query(Pokemon).filter_by(id_pokemon=updated_pokemon_id).first()

    # Verificar se o Pokémon foi atualizado corretamente
    assert updated_pokemon is not None

    # Fechar a sessão de teste
    test_session.close()

def test_find_by_name_pokemon():
    """Should find a Pokemon in the Pokemon table by name."""

    # Inserir um novo Pokémon
    name_pokemon = faker.name()
    attack_force = "Electric"
    attack_value = faker.random_number(digits=3)
    new_pokemon = pokemon_repository.insert(name_pokemon, attack_force, attack_value)

    # Obter o engine e criar uma sessão separada para a consulta de teste
    engine = db_connection_handler.get_engine()
    test_session = Session(bind=engine)

    # Adicionar o objeto new_pokemon à sessão de teste e sincronizar com o banco de dados
    test_session.add(new_pokemon)
    test_session.flush()

    # Consultar o Pokémon inserido pelo nome
    found_pokemon = pokemon_repository.find_by_name(new_pokemon.name_pokemon)

    # Verificar se o Pokémon foi encontrado corretamente pelo nome
    assert found_pokemon is not None
    assert found_pokemon.name_pokemon == new_pokemon.name_pokemon
    assert found_pokemon.attack_force == new_pokemon.attack_force
    assert found_pokemon.attack_value == new_pokemon.attack_value

    # Remover o Pokémon inserido para limpar o banco de dados
    test_session.delete(new_pokemon)
    test_session.commit()
