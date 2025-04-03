import pytest


class TestParentPokemonProperties:
    def test_initialises_with_attributes(self, pokemon):
        assert pokemon.name == "Eevee"
        assert pokemon.hitpoints == 55
        assert pokemon.attack_damage == 18
        assert pokemon.move == "Headbutt"

class TestChildPokemonProperties:
    def test_fire_pokemon(self, fire_pokemon):
        assert fire_pokemon.type == "fire"
        # assert fire_pokemon.name == "Flareon"
        assert fire_pokemon.strong_against == ["grass"]
        assert fire_pokemon.weak_against == ["water"]

    def test_water_pokemon(self, water_pokemon):
        assert water_pokemon.type == "water"
        # assert water_pokemon.name == "Vaporeon"
        assert water_pokemon.strong_against == ["fire"]
        assert water_pokemon.weak_against == ["grass"]

    def test_grass_pokemon(self, grass_pokemon):
        assert grass_pokemon.type == "grass"
        # assert grass_pokemon.name == "Leafeon"
        assert grass_pokemon.strong_against == ["water"]
        assert grass_pokemon.weak_against == ["fire"]

    def test_normal_pokemon(self,normal_pokemon):
        assert normal_pokemon.type == "normal"
        # assert normal_pokemon.name == "Eevee"
        assert normal_pokemon.strong_against == []
        assert normal_pokemon.weak_against == []

class TestPokemonUseMoveMethod:
    def test_use_move_returns_string(self, pokemon):

        assert pokemon.use_move() == "Eevee used Eevee's move"

class TestPokemonTakeDamageMethod:
    def test_take_damage_reduces_health(self, pokemon):
        assert pokemon.hitpoints == 55
        pokemon.take_damage(20) 
        assert pokemon.hitpoints == 35          
        pokemon.take_damage(20) 
        assert pokemon.hitpoints == 15  

class TestPokemonHasFaintedMethod:
    def test_for_health_above_zero_returns_false(self, pokemon):

        assert pokemon.has_fainted() is False

    def test_for_health_at_zero_returns_true(self, pokemon):
        # HP at 55
        pokemon.take_damage(60)

        assert pokemon.has_fainted() is True

class TestPokemonGetMultiplierMethod:
    def test__returns_1_point_5_for_weaker_pokemon(self,
                                   fire_pokemon,
                                   grass_pokemon):
               
        multiplier_1_point_5 = fire_pokemon.get_multiplier(pokemon=grass_pokemon)

        assert multiplier_1_point_5 == 1.5

    def test__returns_1_for_neutral_pokemon(self,
                                   fire_pokemon,
                                   normal_pokemon):
               
        multiplier_1= fire_pokemon.get_multiplier(pokemon=normal_pokemon)

        assert multiplier_1 == 1

    def test__returns_0_point_5_for_stronger_pokemon(self,
                                   fire_pokemon,
                                   water_pokemon):

        multiplier_0_point_5 = fire_pokemon.get_multiplier(pokemon=water_pokemon)

        assert multiplier_0_point_5 == 0.5



