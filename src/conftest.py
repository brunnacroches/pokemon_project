import pytest
from src.infra.configs.base import Base
from src.infra.configs.connection import DBConnectionHandler
from src.main.server.server_flask import app

@pytest.fixture(scope="session")
def test_app():
    app.config["TESTING"] = True
    return app

@pytest.fixture(scope="session")
def test_database():
    # Criando uma instância do manipulador de conexão do banco de dados
    db_handler = DBConnectionHandler()
    # Obtendo o objeto 'engine' a partir do manipulador
    engine = db_handler.get_engine()

    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)