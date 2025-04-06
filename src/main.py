from pokemon_database import *
from trainer import Trainer
from pokemon_game import PokemonGame
import random, time

def wait(seconds):
    time.sleep(seconds)

if __name__ == "__main__":

    user_one_input = input("User 1, What would you like your trainer to be called?\n")
    user_two_input = input("User 2, What would you like your trainer to be called?\n")

    trainer_one = Trainer(user_one_input)
    trainer_two = Trainer(user_two_input)
    computer = Trainer(name="computer")

    for _ in range(6):
        trainer_one.throw_pokeball(pokemon_factory())
        trainer_two.throw_pokeball(pokemon_factory())

    new_game = PokemonGame(trainer_one, trainer_two)
    first_player_decision = random.randint(1,2)

    if first_player_decision == 2:
        new_game.decide_starting_player(num=2)

    pokemon_1 = new_game.player_one.belt[0].pokemon
    pokemon_2 = new_game.player_two.belt[0].pokemon

    print(f"{new_game.player_one.name} is player one with the pokemon {pokemon_1.name}......")
    wait(2)
    print(f"{new_game.player_two.name} is player two the pokemon {pokemon_2.name}......\n")

    learn_more = input("Would you like to know more about your pokemon??")
    if learn_more.lower() in ["y", "yes", "yeap"]:
        print(f"{pokemon_1}")
        wait(3)
        print(f"{pokemon_2}")
        wait(5)

    # TODO: Option for them to view all pokemon in their belt
    # TODO: Option for them to decide which pokemon to fight with
    # TODO: Ensure that pokemon that faints leaves the pokeball (or check rules) 
    
    wait(1)
    print(f"Players have caught their pokemon")

    wait(2)
    print("The game is starting........")

    wait(2)
    new_game.start_battle(pokemon_1, pokemon_2)

    wait(3)
    


