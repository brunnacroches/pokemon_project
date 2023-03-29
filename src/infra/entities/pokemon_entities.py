from sqlalchemy import Column, String, Integer
from src.infra.configs.base import Base

class Pokemon(Base):
    __tablename__ = "pokemon"

    id_pokemon =  Column(Integer, primary_key=True, autoincrement=True)
    name_pokemon =  Column(String(50), nullable=False)
    attack_force =  Column(String(100), nullable=False)
    attack_value =  Column(Integer, nullable=False)

    def __repr__(self):
        return (f' Pokemon(\n'
                f' id_pokemon={self.id_pokemon},\n' 
                f' name_pokemon={self.name_pokemon},\n'
                f' attack_force={self.attack_force})\n'
                f' attack_value={self.attack_value}\n'
    )

    __table_args__ = {"extend_existing": True}
