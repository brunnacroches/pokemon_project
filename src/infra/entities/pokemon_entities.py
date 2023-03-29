from sqlalchemy import Column, String, Integer
from src.infra.configs.base import Base

class Pokemon(Base):
    __tablename__ = "pokemon"

    id_pokemon =  Column(Integer, primary_key=True, autoincrement=True)
    name_pokemon =  Column(String(50), nullable=False)
    attack_force =  Column(String(100), nullable=False)
    attack_value =  Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "id_pokemon": self.id_pokemon,
            "name_pokemon": self.name_pokemon,
            "attack_force": self.attack_force,
            "attack_value": self.attack_value,
        }
