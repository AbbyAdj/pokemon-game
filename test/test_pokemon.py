from src.pokemon import Pokemon, FirePokemon, WaterPokemon, GrassPokemon, NormalPokemon,Pokeball
import pytest

class TestParentProperties:
    def test_initialises_with_attributes(self):
        pokemon = Pokemon(name="Eevee",
                          hitpoints=55,
                          attack_damage=18,
                          move="Headbutt")
        
        assert pokemon.name == "Eevee"
        assert pokemon.hitpoints == 55
        assert pokemon.attack_damage == 18
        assert pokemon.move == "Headbutt"

class TestChildProperties:
    def test_fire_pokemon(self):
        fire_pokemon = FirePokemon(name="Eevee",
                        hitpoints=55,
                        attack_damage=18,
                        move="Headbutt")

        assert fire_pokemon.type == "fire"
        assert fire_pokemon.name == "Eevee"
        assert fire_pokemon.strong_against == ["grass"]
        assert fire_pokemon.weak_against == ["water"]

    def test_water_pokemon(self):
        fire_pokemon = WaterPokemon(name="Eevee",
                        hitpoints=55,
                        attack_damage=18,
                        move="Headbutt")

        assert fire_pokemon.type == "water"
        assert fire_pokemon.name == "Eevee"
        assert fire_pokemon.strong_against == ["fire"]
        assert fire_pokemon.weak_against == ["grass"]

    def test_grass_pokemon(self):
        fire_pokemon = GrassPokemon(name="Eevee",
                        hitpoints=55,
                        attack_damage=18,
                        move="Headbutt")

        assert fire_pokemon.type == "grass"
        assert fire_pokemon.name == "Eevee"
        assert fire_pokemon.strong_against == ["water"]
        assert fire_pokemon.weak_against == ["fire"]

    def test_normal_pokemon(self):
        fire_pokemon = NormalPokemon(name="Eevee",
                        hitpoints=55,
                        attack_damage=18,
                        move="Headbutt")

        assert fire_pokemon.type == "normal"
        assert fire_pokemon.name == "Eevee"
        assert fire_pokemon.strong_against == []
        assert fire_pokemon.weak_against == []

class TestUseMoveMethod:
    def test_use_move_returns_string(self):
        pokemon = Pokemon(name="Eevee",
                          hitpoints=55,
                          attack_damage=18,
                          move="Headbutt")
        
        assert pokemon.use_move() == "Eevee used Eevee's move"

class TestTakeDamageMethod:
    def test_take_damage_reduces_health(self):
        pokemon = Pokemon(name="Eevee",
                          hitpoints=55,
                          attack_damage=18,
                          move="Headbutt")
        pokemon.take_damage(20) 
        assert pokemon.health == 80          
        pokemon.take_damage(20) 
        assert pokemon.health == 60   

class TestHasFaintedMethod:
    def test_for_health_above_zero(self):
        pokemon = Pokemon(name="Eevee",
                        hitpoints=55,
                        attack_damage=18,
                        move="Headbutt")
        
        assert pokemon.has_fainted() is False

    def test_for_health_at_zero(self):
        pokemon = Pokemon(name="Eevee",
                        hitpoints=55,
                        attack_damage=18,
                        move="Headbutt")
        
        pokemon.take_damage(100)

        assert pokemon.has_fainted() is True

class TestGetMultiplierMethod:
    def test_get_multiplier_method(self):
        
        fire = FirePokemon(name="Flareon",
                           hitpoints=65,
                           attack_damage=20,
                           move="Fire blast")
        
        grass = GrassPokemon(name="Leafeon",
                             hitpoints=65,
                             attack_damage=17,
                             move="Giga drain")
        
        normal = NormalPokemon(name="Eevee",
                        hitpoints=55,
                        attack_damage=18,
                        move="Headbutt")
        
        water = WaterPokemon(name="Vaporeon",
                        hitpoints=70,
                        attack_damage=19,
                        move="Hydro pump")
        
        multiplier_1_point_5 = fire.get_multiplier(pokemon=grass)
        multiplier_1= fire.get_multiplier(pokemon=normal)
        multiplier_0_point_5 = fire.get_multiplier(pokemon=water)

        assert multiplier_1_point_5 == 1.5
        assert multiplier_1 == 1
        assert multiplier_0_point_5 == 0.5

class TestPokeballProperties:
    def test_pokemon_initialise_with_none(self):
        pokeball = Pokeball()
        assert pokeball.pokemon == None

class TestCatchMethod:
    def test_for_empty_and_occupied_pokeball(self):
        pokeball = Pokeball()
        fire = FirePokemon(name="Flareon",
                           hitpoints=65,
                           attack_damage=20,
                           move="Fire blast")
        fire_2 = FirePokemon(name="Flareon",
                           hitpoints=65,
                           attack_damage=20,
                           move="Fire blast")       
        assert pokeball.pokemon == None
        pokeball.catch(fire)
        assert pokeball.pokemon == fire
        assert pokeball.pokemon.name == "Flareon"
        with pytest.raises(Exception):
            pokeball.catch(fire_2)

class TestIsEmptyMethod:
    def test_for_empty_pokeball(self):
        pokeball = Pokeball()
        fire = FirePokemon(name="Flareon",
                           hitpoints=65,
                           attack_damage=20,
                           move="Fire blast")
      
        assert pokeball.is_empty() == True
        pokeball.catch(fire)
        assert pokeball.is_empty() == False
       
        
