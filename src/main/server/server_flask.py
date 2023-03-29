from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.infra.configs.connection import DBConnectionHandler

# Criando uma instância do manipulador de conexão do banco de dados
db_handler = DBConnectionHandler()
# Obtendo o objeto 'engine' a partir do manipulador
engine = db_handler.get_engine()

app = Flask(__name__)
from .routes import *

app.config['SQLALCHEMY_DATABASE_URI'] = db_handler.get_connection_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)