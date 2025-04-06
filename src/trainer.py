from src.pokeball import Pokeball
from src.pokemon import Pokemon

class Trainer:
    """The trainer initialises with 6 empty pokeballs. 
    They can throw empty pokeballs to catch a new pokemon"""
    def __init__(self, name="Player"):
        self.name = name
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

    def __len__(self):
        """Return total number of occupied pokeballs in the belt"""
        occupied_pokeballs = len([ball for ball in self.belt if not ball.is_empty()])
        return occupied_pokeballs
    
    def __str__(self):
        return f"My name is {self.name}. I have {len(self)} occupied pokeballs"
    
    def __iter__(self):
        for pokeball in self.belt:
            yield pokeball.pokemon
    
if __name__ == "__main__":
    trainer = Trainer()
    print(trainer)
    pokemon = Pokemon(name="Vaporeon",
                    hitpoints=70,
                    attack_damage=19,
                    move="Hydro pump")    
    trainer.throw_pokeball(pokemon)

    print(trainer)