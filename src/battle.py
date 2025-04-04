from src.pokemon import FirePokemon, GrassPokemon

class PokemonHasFainted(Exception):
    pass


class Battle:
    def __init__(self,pokemon_1,pokemon_2):
        """Takes in two pokemon as arguments to start a battle between them"""
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        # might need to refactor and use self.pokemon1 and self.pokemon2 directly.
        self.attacker = self.pokemon_1
        self.defender = self.pokemon_2

    def pokemon_1_turn(self):
        """Invokes pokemon 1's turn and has it inflict damage on pokemon 2
        Turns switch at the end of invocation"""
        self.calculate_damage()
        # at the end of the turn........
        self.attacker = self.pokemon_2
        self.defender = self.pokemon_1

    def pokemon_2_turn(self):
        """Invokes pokemon 2's turn and has it inflict damage on pokemon 1
        Turns switch at the end of invocation"""
        self.calculate_damage()
        # at the end of the turn........
        self.attacker = self.pokemon_1
        self.defender = self.pokemon_2

    def calculate_damage(self):
        """Calculates the total damage the attack deals on the defender's hitpoints"""
        # We might need to take out the two parameters above and use the self ones directly
        # call take damage for the defender. 
        # Use the attackers multiplier to check the total damage the attacker will infict
        
        total_attacker_damage = self.attacker.attack_damage * self.attacker.get_multiplier(self.defender)
        self.defender.take_damage(amount=total_attacker_damage)

        # Call this method at the beginning of each pokemon's turn method, 

    def take_turn(self):
        """Assigns and manages the turns per round and raises an exception if a pokemon has fainted"""
        if self.attacker == self.pokemon_1:
            self.pokemon_1_turn()
        elif self.attacker == self.pokemon_2:
            self.pokemon_2_turn()
        if self.pokemon_1.has_fainted():
            raise PokemonHasFainted(f"{self.pokemon_1.name} has fainted. No more turns")        
        if self.pokemon_2.has_fainted():
            raise PokemonHasFainted(f"{self.pokemon_2.name} has fainted. No more turns")
        
    def get_winner(self):
        """Returns winner if other pokemon has fainted"""
        if self.pokemon_1.has_fainted():
            return self.pokemon_2
        if self.pokemon_2.has_fainted():
            return self.pokemon_1
        return None

    def __str__(self):
        return f"pokemon {self.pokemon_1.name} is fighting with pokemon {self.pokemon_2.name}"




if __name__ == "__main__":
    fire_pokemon = FirePokemon(name="Flareon",
                    hitpoints=65,
                    attack_damage=20,
                    move="Fire blast")
    grass_pokemon = GrassPokemon(name="Leafeon",
                    hitpoints=65,
                    attack_damage=17,
                    move="Giga drain")
    battle = Battle(pokemon_1 = fire_pokemon ,pokemon_2 = grass_pokemon) 
    # battle.take_turn()
    # print(battle.pokemon_2.hitpoints)

    # battle.take_turn() 
    # battle.take_turn() 
    # print(battle.pokemon_2.hitpoints)
    # battle.take_turn() 
    # battle.take_turn() 
    # print(battle.pokemon_2.hitpoints)

    print(battle)


    