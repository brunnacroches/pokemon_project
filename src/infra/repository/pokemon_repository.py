from src.infra.entities.pokemon_entities import Pokemon

class PokemonRepository:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler

    def select(self):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Pokemon).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, name_pokemon: str, attack_force: str, attack_value: int) -> Pokemon:
        with self.__ConnectionHandler() as db:
            try:
                data_insert = Pokemon(
                    name_pokemon=name_pokemon,
                    attack_force=attack_force,
                    attack_value=attack_value
                )
                db.session.add(data_insert) 
                db.session.commit()
                return data_insert
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id_pokemon: int):
        with self.__ConnectionHandler() as db:
            try:
                deleted_rows = db.session.query(Pokemon).filter(
                    Pokemon.id_pokemon == id_pokemon
                ).delete()
                db.session.commit()
                if deleted_rows > 0:
                    return id_pokemon
                else:
                    return None  # Para levantar uma exceção
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, id_pokemon:int, new_id_pokemon: int):
        with self.__ConnectionHandler() as db:
            try:
                db.session.query(Pokemon).filter(
                    Pokemon.id_pokemon == id_pokemon
                ).update(
                    {"id_pokemon": new_id_pokemon}
                )
                db.session.commit()
                return new_id_pokemon
            except Exception as exception:
                db.session.rollback()
                raise exception

    def find_by_name(self, name_pokemon: str) -> Pokemon:
        with self.__ConnectionHandler() as db:
            try:
                pokemon = db.session.query(Pokemon).filter(
                    Pokemon.name_pokemon == name_pokemon
                ).one_or_none()
                print(f"find_by_name result for {name_pokemon}: {pokemon}")
                return pokemon
            except Exception as exception:
                db.session.rollback()
                raise exception