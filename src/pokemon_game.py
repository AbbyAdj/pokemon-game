from src.trainer import Trainer
from src.battle import Battle, PokemonHasFainted
import random

class PokemonGame:
    def __init__(self, trainer_one, trainer_two):
        self.trainer_one = trainer_one
        self.trainer_two = trainer_two

        self.player_one = self.trainer_one
        self.player_two = self.trainer_two

    def decide_starting_player(self,num=1):
        # first_player_decision = random.randint(1,2)
        if num == 2:
            self.player_one = self.trainer_two
            self.player_two = self.trainer_one
    
    def players_catch_pokemon(self, first_pokemon, second_pokemon) -> bool:
        self.player_one.throw_pokeball(first_pokemon)
        self.player_two.throw_pokeball(second_pokemon)
    
    def start_battle(self):
        player_one_pokemon = self.player_one.belt[0].pokemon
        player_two_pokemon = self.player_two.belt[0].pokemon

        game = Battle(pokemon_1=player_one_pokemon,
                      pokemon_2=player_two_pokemon)
        
        game_ongoing = True
        
        while game_ongoing:
            try:
                game.take_turn()
            except PokemonHasFainted:
                winner = game.get_winner()
                return winner
                # game_ongoing = False
            else:
                pass
                # communicate trainer who won
    
    def show_winner(self):
        winner_pokemon = self.start_battle()
        winner = self.player_one

        if self.player_one.belt[0].pokemon.has_fainted():
            winner = self.player_two

        print(f"{winner_pokemon.name} pokemon has won. {winner.name} is the winner.")
        return winner
        