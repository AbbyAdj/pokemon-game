from src.pokemon import FirePokemon, GrassPokemon, NormalPokemon, WaterPokemon, Pokemon
from src.pokeball import Pokeball
from src.trainer import Trainer
import pytest

# We have fixtures returning instances of classes except Battle because it requires pokemon instances as inputs

@pytest.fixture
def pokemon():
    pokemon = Pokemon(name="Eevee",
                      hitpoints=55,
                      attack_damage=18,
                      move="Headbutt")
    return pokemon

@pytest.fixture
def fire_pokemon():
    fire_pokemon = FirePokemon(name="Flareon",
                        hitpoints=65,
                        attack_damage=20,
                        move="Fire blast")
    return fire_pokemon

@pytest.fixture
def grass_pokemon():
    grass_pokemon = GrassPokemon(name="Leafeon",
                            hitpoints=65,
                            attack_damage=17,
                            move="Giga drain")
    return grass_pokemon

@pytest.fixture
def normal_pokemon():
    normal_pokemon = NormalPokemon(name="Eevee",
                    hitpoints=55,
                    attack_damage=18,
                    move="Headbutt")
    return normal_pokemon

@pytest.fixture
def water_pokemon():
    water_pokemon = WaterPokemon(name="Vaporeon",
                    hitpoints=70,
                    attack_damage=19,
                    move="Hydro pump")
    return water_pokemon

@pytest.fixture
def pokeball():
    pokeball = Pokeball()
    return pokeball

@pytest.fixture
def trainer():
    trainer = Trainer()
    return trainer
