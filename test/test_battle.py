from src.battle import Battle
import pytest


class TestBattleProperties:
    def test_battle_attributes_check(self,grass_pokemon, water_pokemon):
        battle = Battle(grass_pokemon, water_pokemon)

        assert battle.pokemon_1 == grass_pokemon
        assert battle.pokemon_2 == water_pokemon

class TestBattleTakeTurnMethod:
    def test_switches_attacker_and_defender_after_each_turn(self,fire_pokemon, grass_pokemon):
        battle = Battle(pokemon_1 = fire_pokemon ,pokemon_2 = grass_pokemon)

        assert battle.current_player == fire_pokemon

        battle.take_turn()
        assert battle.current_player == grass_pokemon
        
        battle.take_turn()
        assert battle.current_player == fire_pokemon
            

    def test_method_calculates_damage_to_the_opponent_and_subtracts_from_HP(self):
        pass
    
    def test_raises_exception_if_a_pokemon_has_fainted(self):
        pass

