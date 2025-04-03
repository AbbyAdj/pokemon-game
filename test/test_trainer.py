import pytest


class TestTrainerProperties:
    def test_pokeballs_initialised_on_belt_are_different_instances(self, trainer):
        for i in range(len(trainer.belt)):
            assert trainer.belt[i].is_empty() is True
            if i == 0:
                continue
            assert trainer.belt[i] is not trainer.belt[i-1] 

class TestTrainerThrowPokeballMethod:
    def test_at_least_one_empty_pokeball_on_the_belt(self,
                                                     trainer,
                                                     fire_pokemon):
        
        initial = len(trainer) #0 balls occupied
        trainer.throw_pokeball(pokemon=fire_pokemon)
        final = len(trainer) # 1 ball occupied

        assert initial != final
        assert final == initial + 1
        
    def test_no_empty_pokeballs_on_the_belt(self,
                                            trainer,
                                            fire_pokemon,
                                            grass_pokemon,
                                            normal_pokemon,
                                            water_pokemon):
        # We have 4 pokemon instances being used in this test
        # for the same of testing, we are allowing the last two pokeballs
        # on the balls to re use the same instances of pokeballs. This is simply
        # for testing. If a method/algorithm arises that needs this changed,
        # the test will be refactored.
        trainer.throw_pokeball(fire_pokemon)
        trainer.throw_pokeball(grass_pokemon)
        trainer.throw_pokeball(normal_pokemon)
        trainer.throw_pokeball(water_pokemon)
        trainer.throw_pokeball(fire_pokemon)
        trainer.throw_pokeball(grass_pokemon)

        assert len(trainer) == 6

