
class Battle:
    def __init__(self,pokemon_1,pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.current_player = self.pokemon_1

    def pokemon_1_turn(self):
        self.current_player = self.pokemon_2

    def pokemon_2_turn(self):
        self.current_player = self.pokemon_1

    def calculate_damage(self, attacker, defender):
        pass

    def take_turn(self):
        if self.current_player == self.pokemon_1:
            self.pokemon_1_turn()
            return
        if self.current_player == self.pokemon_2:
            self.pokemon_2_turn()
            return
        raise Exception("Pokemon(insert name) has fainted. No more turns")
        
        
    
    def get_winner(self):
        pass

