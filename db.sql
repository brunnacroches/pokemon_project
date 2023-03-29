CREATE DATABASE battle_pokemons_db;

USE battle_pokemons_db;

CREATE TABLE pokemon (
    id_pokemon INT AUTO_INCREMENT PRIMARY KEY,
    name_pokemon VARCHAR(50) NOT NULL,
    attack_force VARCHAR(100) NOT NULL,
    attack_value INT NOT NULL
);

INSERT INTO pokemon(name_pokemon, attack_force, attack_value)
VALUES
    ('Fyredra', 'SolarBlast', 10),
    ('Aqualynx', 'SlashingWind', 9),
    ('Electrobeet', 'WaterJet', 8),
    ('Florixie', 'LightningStrike', 7);