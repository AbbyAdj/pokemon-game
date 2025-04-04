from pokemon_database import *
from trainer import Trainer
from pokemon_game import PokemonGame
import random, time


user_one_input = input("User 1, What would you like your trainer to be called?\n")
user_two_input = input("User 2, What would you like your trainer to be called?\n")

trainer_one = Trainer(user_one_input)
trainer_two = Trainer(user_two_input)
computer = Trainer(name="computer")

list_of_pokemon1 = [Flareon(), Charmander(), Leafeon(), Bulbasaur(), Eevee(), Vaporeon(), Squirtle()]
list_of_pokemon2 = [Flareon(), Charmander(), Leafeon(), Bulbasaur(), Eevee(), Vaporeon(), Squirtle()]
list_of_pokemon3 = [Flareon(), Charmander(), Leafeon(), Bulbasaur(), Eevee(), Vaporeon(), Squirtle()] #computer

for _ in range(6):
    trainer_one.throw_pokeball(list_of_pokemon1.pop(random.randint(0, len(list_of_pokemon1)-1)))
    trainer_two.throw_pokeball(list_of_pokemon2.pop(random.randint(0, len(list_of_pokemon2)-1)))


if __name__ == "__main__":
    new_game = PokemonGame(trainer_one, trainer_two)
    first_player_decision = random.randint(1,2)

    if first_player_decision == 2:
        new_game.decide_starting_player(num=2)
    else:
        new_game.decide_starting_player()

    pokemon_1 = new_game.player_one.belt[0].pokemon
    pokemon_2 = new_game.player_two.belt[0].pokemon
    if pokemon_2.name == pokemon_1.name:
        pokemon_2 = new_game.player_two.belt[1].pokemon

    print(f"{new_game.player_one.name} is player one with the pokemon {pokemon_1.name}......")
    time.sleep(2)
    print(f"{new_game.player_two.name} is player two the pokemon {pokemon_2.name}......\n")

    learn_more = input("Would you like to know more about your pokemon??")
    if learn_more.lower() in ["y", "yes", "yeap"]:
        print(f"{pokemon_1}")
        time.sleep(3)
        print(f"{pokemon_2}")
        time.sleep(5)
        
    # Assigning randomly
    # new_game.players_catch_pokemon(pokemon_1, pokemon_2)
    
    time.sleep(1)
    print(f"Players have caught their pokemon")

    time.sleep(2)
    print("The game is starting........")

    time.sleep(2)
    new_game.start_battle(pokemon_1, pokemon_2)

    time.sleep(3)
    print("Getting results......")
    
    new_game.show_winner()


