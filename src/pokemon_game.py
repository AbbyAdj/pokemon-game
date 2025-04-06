from src.battle import Battle, PokemonHasFainted

class PokemonGame:
    def __init__(self, trainer_one, trainer_two):
        self.trainer_one = trainer_one
        self.trainer_two = trainer_two

        self.player_one = self.trainer_one
        self.player_two = self.trainer_two

    def decide_starting_player(self,num=1):
        """Only invokes if second player is to start. Otherwise the normal order is followed"""
        if num == 2:
            self.player_one = self.trainer_two
            self.player_two = self.trainer_one
    
    def players_catch_pokemon(self, first_pokemon, second_pokemon) -> bool:
        """Only invoke if players do not have any pokemon in their belt"""
        self.player_one.throw_pokeball(first_pokemon)
        self.player_two.throw_pokeball(second_pokemon)
    
    def start_battle(self, player_one_pokemon, player_two_pokemon):
        """This invokes a battle object taking the two starting pokemon as args.
        Once a pokemon faints, the show_winner method is called and the winner is announced."""
        game = Battle(pokemon_1=player_one_pokemon,
                      pokemon_2=player_two_pokemon)

        while True:
            try:
                game.take_turn()
            except PokemonHasFainted:
                winning_pokemon = game.get_winner()
                print("Getting results......")
                self.show_winner(winning_pokemon=winning_pokemon)
                return winning_pokemon
            else:
                pass
                # communicate trainer who won
    
    def show_winner(self, winning_pokemon):
        winner_pokemon = winning_pokemon
        winner = self.player_one


        if winner_pokemon in self.player_two:
            winner = self.player_two

        print(f"{winner_pokemon.name} pokemon has won. {winner.name} is the winner.")
        return winner
        