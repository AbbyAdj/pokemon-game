from src.pokemon import  *
import pytest

# TODO implement fixtures for the testing and object creation
# @pytest.fixture(params=["water", "fire", "normal", "grass"])
# def pokemon_factory(pokemon_type:str):
#     fire = FirePokemon(name="Flareon",
#                        hitpoints=65,
#                        attack_damage=20,
#                        move="Fire blast")
    
#     grass = GrassPokemon(name="Leafeon",
#                          hitpoints=65,
#                          attack_damage=17,
#                          move="Giga drain")
    
#     normal = NormalPokemon(name="Eevee",
#                     hitpoints=55,
#                     attack_damage=18,
#                     move="Headbutt")
    
#     water = WaterPokemon(name="Vaporeon",
#                     hitpoints=70,
#                     attack_damage=19,
#                     move="Hydro pump")
 
#     pokemon_dict = {"fire": fire,
#                     "grass": grass,
#                     "normal": normal,
#                     "water": water,
#                     }
#     return pokemon_dict[pokemon_type]

class TestParentPokemonProperties:
    def test_initialises_with_attributes(self):
        pokemon = Pokemon(name="Eevee",
                          hitpoints=55,
                          attack_damage=18,
                          move="Headbutt")
        
        assert pokemon.name == "Eevee"
        assert pokemon.hitpoints == 55
        assert pokemon.attack_damage == 18
        assert pokemon.move == "Headbutt"

class TestChildPokemonProperties:
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

class TestPokeballProperties:
    def test_pokemon_initialise_with_none(self):
        pokeball = Pokeball()
        assert pokeball.pokemon == None

class TestTrainerProperties:

    def test_pokeballs_are_different_instances(self):
        trainer = Trainer()
        for i in range(len(trainer.belt)):
            assert trainer.belt[i].is_empty() is True
            if i == 0:
                continue
            assert trainer.belt[i] is not trainer.belt[i-1] 

# class TestBattleProperties:
#     def test_battle_attributes_check():
        


class TestPokemonUseMoveMethod:
    def test_use_move_returns_string(self):
        pokemon = Pokemon(name="Eevee",
                          hitpoints=55,
                          attack_damage=18,
                          move="Headbutt")
        
        assert pokemon.use_move() == "Eevee used Eevee's move"

class TestPokemonTakeDamageMethod:
    def test_take_damage_reduces_health(self):
        pokemon = Pokemon(name="Eevee",
                          hitpoints=55,
                          attack_damage=18,
                          move="Headbutt")
        pokemon.take_damage(20) 
        assert pokemon.hitpoints == 35          
        pokemon.take_damage(20) 
        assert pokemon.hitpoints == 15  

class TestPokemonHasFaintedMethod:
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

class TestPokemonGetMultiplierMethod:
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

class TestPokeballCatchMethod:
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

class TestPokeballIsEmptyMethod:
    def test_for_empty_pokeball(self):
        pokeball = Pokeball()
        fire = FirePokemon(name="Flareon",
                           hitpoints=65,
                           attack_damage=20,
                           move="Fire blast")
      
        assert pokeball.is_empty() == True
        pokeball.catch(fire)
        assert pokeball.is_empty() == False
       
class TestTrainerThrowPokeballMethod:
    def test_at_least_one_empty_pokeball_on_the_belt(self):
        trainer = Trainer()
        fire_pokemon = FirePokemon(name="Flareon",
                           hitpoints=65,
                           attack_damage=20,
                           move="Fire blast")
        
        initial = trainer.get_occupied_pokeballs()
        
        trainer.throw_pokeball(pokemon=fire_pokemon)
  
        final = trainer.get_occupied_pokeballs()

        assert initial != final
        assert final == initial + 1
        
    def test_no_empty_pokeballs_on_the_belt(self):
        pass

class TestBattleTakeTurnMethod:


    def test_switches_attacker_and_defender(self):

        fire = FirePokemon(name="Flareon",
                        hitpoints=65,
                        attack_damage=20,
                        move="Fire blast")
        
        grass = GrassPokemon(name="Leafeon",
                            hitpoints=65,
                            attack_damage=17,
                            move="Giga drain")  
        battle = Battle(pokemon_1 = fire,pokemon_2 = grass)
        assert battle.current_player == fire
        battle.take_turn()
        assert.battle.current_player == grass
            

    def test_method_calculates_damage_to_the_opponent_and_subtract_from_HP(self):
        pass
    
    def test_raises_exception_if_a_pokemon_has_fainted(self):
        pass



