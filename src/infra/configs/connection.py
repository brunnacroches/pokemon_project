from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    # construtor da classe
    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://root:keyspace@localhost:3306/battle_pokemons_db'
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :parram - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member