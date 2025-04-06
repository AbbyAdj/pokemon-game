from src.pokemon_game import PokemonGame
from src.trainer import Trainer
import pytest


class TestGameProperties:
    def test_initialises_with_both_players(self):
        trainer_1 = Trainer("A")
        trainer_2 = Trainer("B")
        new_game = PokemonGame(trainer_1,trainer_2)
        assert new_game.player_one == trainer_1
        assert new_game.player_two == trainer_2
    
class TestStartingPlayer:
    def test_trainer_one_starts(self):
        trainer_1 = Trainer("A")
        trainer_2 = Trainer("B")
        new_game = PokemonGame(trainer_1,trainer_2)
        new_game.decide_starting_player()
        assert new_game.player_one == trainer_1

    def test_trainer_two_starts(self):
        trainer_1 = Trainer("A")
        trainer_2 = Trainer("B")
        new_game = PokemonGame(trainer_1,trainer_2)
        new_game.decide_starting_player(num=2)
        assert new_game.player_one == trainer_2

class TestStartBattle:
    def test_players_have_pokemons(self,
                                   fire_pokemon,
                                   grass_pokemon):
        trainer_1 = Trainer("A")
        trainer_2 = Trainer("B")
        new_game = PokemonGame(trainer_1,trainer_2)
        new_game.players_catch_pokemon(fire_pokemon,grass_pokemon)
        assert new_game.player_one.belt[0].pokemon == fire_pokemon
        assert new_game.player_two.belt[0].pokemon == grass_pokemon

    def test_game_ends_with_the_winner(self,
                                   fire_pokemon,
                                   grass_pokemon):
        trainer_1 = Trainer("A")
        trainer_2 = Trainer("B")
        new_game = PokemonGame(trainer_1,trainer_2)
        new_game.players_catch_pokemon(fire_pokemon,grass_pokemon)
        winner = new_game.start_battle(fire_pokemon, grass_pokemon)
        assert winner== fire_pokemon
        
class TestShowWinnerMethod:
    def test_shows_the_winner(self,
                                   fire_pokemon,
                                   grass_pokemon,
                                   capsys):
        trainer_1 = Trainer("A")
        trainer_2 = Trainer("B")
        new_game = PokemonGame(trainer_1,trainer_2)
        new_game.players_catch_pokemon(fire_pokemon,grass_pokemon)
        winner = new_game.start_battle(fire_pokemon, grass_pokemon)
        winning_player = new_game.show_winner(winner)
        
        captured = capsys.readouterr()
        assert f"{winner.name} pokemon has won. {winning_player.name} is the winner.\n" in captured.out