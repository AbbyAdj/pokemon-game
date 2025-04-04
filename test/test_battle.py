from src.battle import Battle, PokemonHasFainted
import pytest


class TestBattleProperties:
    def test_battle_attributes_check(self,grass_pokemon, water_pokemon):
        battle = Battle(grass_pokemon, water_pokemon)

        assert battle.pokemon_1 == grass_pokemon
        assert battle.pokemon_2 == water_pokemon

class TestBattleTakeTurnMethod:
    def test_switches_attacker_and_defender_after_each_turn(self,fire_pokemon, grass_pokemon):
        battle = Battle(pokemon_1 = fire_pokemon ,pokemon_2 = grass_pokemon)

        assert battle.attacker == fire_pokemon
        assert battle.defender == grass_pokemon

        battle.take_turn()

        assert battle.attacker == grass_pokemon
        assert battle.defender == fire_pokemon
                  
    def test_method_calculates_damage_to_the_opponent_and_subtracts_from_HP(self, fire_pokemon, grass_pokemon):
        battle = Battle(pokemon_1 = fire_pokemon ,pokemon_2 = grass_pokemon)
        # fire hp - 65
        # fire attack damage 20
        # fire multiplier 1.5
        # fire total damage = 30

        # grass hp 65
        # grass attack damage 17
        # grass multiplier 0.5
        # grass total damage 8.5

        # Beginning of the battle

        assert battle.pokemon_1.hitpoints == 65
        assert battle.pokemon_2.hitpoints == 65

        # round 1 - attacker : fire | defender : grass
        battle.pokemon_1_turn()

        assert battle.pokemon_1.hitpoints == 65
        assert battle.pokemon_2.hitpoints == 35

        # # round 2 - attacker : grass | defender : fire
        battle.pokemon_2_turn()

        assert battle.pokemon_1.hitpoints == 56.5
        assert battle.pokemon_2.hitpoints == 35

        # # round 3 - attacker : fire | defender : grass
        battle.pokemon_1_turn()

        assert battle.pokemon_1.hitpoints == 56.5
        assert battle.pokemon_2.hitpoints == 5

    def test_raises_exception_if_a_pokemon_has_fainted(self, fire_pokemon, grass_pokemon):
        battle = Battle(pokemon_1 = fire_pokemon ,pokemon_2 = grass_pokemon)

        # TODO use a while loop or a for loop for the take turns below:

        battle.take_turn() #1st round : fire attacks
        battle.take_turn() #2nd round : grass attacks
        battle.take_turn() #3rd round : fire attacks
        battle.take_turn() #4th round : grass attacks
        with pytest.raises(PokemonHasFainted) as err:
            battle.take_turn() #5th round : fire attacks (grass faints)
        assert str(err.value) == "Leafeon has fainted. No more turns"

class TestGetWinnerMethod:
    def test_returns_none_if_no_pokemon_has_fainted(self, fire_pokemon, grass_pokemon):
        battle = Battle(pokemon_1 = fire_pokemon ,pokemon_2 = grass_pokemon)

        battle.take_turn()

        assert battle.get_winner() is None

    def test_returns_winner_if_one_pokemon_has_fainted(self, fire_pokemon, grass_pokemon):
        battle = Battle(pokemon_1 = fire_pokemon ,pokemon_2 = grass_pokemon)
        try:
            battle.take_turn()
            battle.take_turn()
            battle.take_turn()
            battle.take_turn()
            battle.take_turn()
        except PokemonHasFainted:
            print("The fight ended.......checking winner")
        else:
            assert battle.get_winner() == grass_pokemon
