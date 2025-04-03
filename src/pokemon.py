
class Pokemon:
    def __init__(self, 
                 name:str,
                 hitpoints:int,
                 attack_damage:int, 
                 move:str):
        self.name = name
        self.hitpoints = hitpoints
        self.attack_damage = attack_damage
        self.move = move
        # TODO change self.health to private and refactor
        # TODO change strong against and weak against to private
        self.strong_against = []
        self.weak_against = []

    def use_move(self)-> str:
        return f"{self.name} used {self.name}'s move"

    def take_damage(self, amount:int):
        self.hitpoints -= amount

    def has_fainted(self) -> bool:
        """Returns true if health has hit zero and false otherwise"""
        if self.hitpoints <= 0:
            return True
        return False

    def get_multiplier(self, pokemon) -> float:
        """Returns 1.5 if pokemon in weak against list
        Returns 0.5 if pokemon in strong against list
        Returns 1 if pokemon isn't found in either list"""
        if pokemon.type in self.strong_against:
            return 1.5
        if pokemon.type in self.weak_against:
            return 0.5
        return 1

class FirePokemon(Pokemon):
    def __init__(self, name, hitpoints, attack_damage, move):
        super().__init__(name, hitpoints, attack_damage, move)
        self.type = "fire"
        self.strong_against = ["grass"]
        self.weak_against = ["water"]

class WaterPokemon(Pokemon):
    def __init__(self, name, hitpoints, attack_damage, move):
        super().__init__(name, hitpoints, attack_damage, move)
        self.type = "water"
        self.strong_against = ["fire"]
        self.weak_against = ["grass"]

class GrassPokemon(Pokemon):
    def __init__(self, name, hitpoints, attack_damage, move):
        super().__init__(name, hitpoints, attack_damage, move)
        self.type = "grass"
        self.strong_against = ["water"]
        self.weak_against = ["fire"]

class NormalPokemon(Pokemon):
    def __init__(self, name, hitpoints, attack_damage, move):
        super().__init__(name, hitpoints, attack_damage, move)
        self.type = "normal"

class Pokeball:
    """These contain pokemon"""
    def __init__(self):
        self.pokemon = None
    
    def catch(self,pokemon):
        if self.pokemon == None:
            self.pokemon = pokemon
        else:
            raise Exception("This pokeball has already a pokemon")
    
    def is_empty(self)->bool:
        if not self.pokemon:
            return True
        return False

class Trainer:
    def __init__(self):
        # On the belt, they have pokeballs, not pokemon
        self.belt = []
        for _ in range(6):
            new_pokeball = Pokeball()
            self.belt.append(new_pokeball)
        
    def throw_pokeball(self, pokemon):
        """Uses available empty pokeballs to catch pokemon"""
        for pokeball in self.belt:
            if pokeball.is_empty():
                try:
                    pokeball.catch(pokemon)
                except Exception:
                    continue
                return
        raise Exception("No available pokeballs")

    def get_occupied_pokeballs(self) -> int:
        """Return total number of occupied pokeballs in the belt"""
        occupied = len([ball for ball in self.belt if not ball.is_empty()])
        return occupied

class Battle:
    def __init__(self,pokemon_1,pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2

    def take_turn(self):
        pass
    
    def get_winner(self):
        pass

