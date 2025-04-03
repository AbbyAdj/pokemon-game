import pytest


class TestPokeballProperties:
    def test_pokemon_initialises_with_no_pokemon(self, pokeball):

        assert pokeball.pokemon == None

class TestPokeballCatchMethod:
    def test_for_empty_and_occupied_pokeball(self,
                                             pokeball,
                                             fire_pokemon,
                                             grass_pokemon):

        assert pokeball.pokemon == None

        pokeball.catch(fire_pokemon)

        assert pokeball.pokemon == fire_pokemon
        assert pokeball.pokemon.name == "Flareon"

    def test_for_occupied_pokeball(self,
                                   pokeball,
                                   fire_pokemon,
                                   grass_pokemon):
        pokeball.catch(fire_pokemon)

        assert pokeball.pokemon == fire_pokemon

        with pytest.raises(Exception):
            pokeball.catch(grass_pokemon)
        

class TestPokeballIsEmptyMethod:
    def test_for_empty_pokeball(self, pokeball):
        assert pokeball.is_empty() == True

    def test_for_occupued_pokeball(self, pokeball, fire_pokemon):
        assert pokeball.is_empty() == True
        pokeball.catch(fire_pokemon)
        assert pokeball.is_empty() == False
        
