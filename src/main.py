from pokemon_database import *
from trainer import Trainer
from battle import Battle, PokemonHasFainted
from pokemon_game import PokemonGame
import random

# Ask users for input / Ask user for input to play against the computer (use random module) (done)
# Ask users for names for their trainers (players) (done)
# We can use random to decide who chooses pokemon first and plays first
# Ask users to pick a pokemon (they can't pick the same pokemon)
user_two_input = input("User 2, What would you like your trainer to be called?\n")
user_one_input = input("User 1, What would you like your trainer to be called?\n")


trainer_one = Trainer(user_one_input)
trainer_two = Trainer(user_two_input)
computer = Trainer("computer")

if __name__ == "__main__":
    new_game = PokemonGame()
    new_game.register_players()
    new_game.decide_starting_player()
    new_game.start_battle()
    new_game.show_winner()
