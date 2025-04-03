
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
        # TODO change strong against and weak against to private
        self.strong_against = []
        self.weak_against = []

    def use_move(self)-> str:
        """Returns a string of the pokemon using their move"""
        return f"{self.name} used {self.name}'s move"

    def take_damage(self, amount:int):
        """Reduces hp by a certain amount"""
        self.hitpoints -= amount

    def has_fainted(self) -> bool:
        """Returns true if hp has hit zero and false otherwise"""
        if self.hitpoints <= 0:
            return True
        return False

    def get_multiplier(self, pokemon) -> float:
        """Returns 1.5 if pokemon in 'weak against' list
        Returns 0.5 if pokemon in 'strong against' list
        Returns 1 if pokemon isn't found in either list, i.e. normal types"""
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

