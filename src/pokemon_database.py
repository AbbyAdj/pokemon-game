from pokemon import FirePokemon, GrassPokemon, NormalPokemon, WaterPokemon



class Flareon(FirePokemon):
    def __init__(self):
        super().__init__(name="Flareon", 
                         hitpoints=65, 
                         attack_damage=20, 
                         move="Fire Blast")

class Charmander(FirePokemon):
    def __init__(self,):
        super().__init__(name="Charmander", 
                         hitpoints=44, 
                         attack_damage=17, 
                         move="Flame Thrower")

class Leafeon(GrassPokemon):
    def __init__(self):
        super().__init__(name="Leafeon", 
                         hitpoints=65, 
                         attack_damage=17, 
                         move="Giga Drain")

class Bulbasaur(GrassPokemon):
    def __init__(self):
        super().__init__(name="Bulbasaur", 
                         hitpoints=45 ,
                         attack_damage=16, 
                         move="Razor Leaf")

class Eevee(NormalPokemon):
    def __init__(self):
        super().__init__(name="Eevee", 
                         hitpoints=55, 
                         attack_damage=18, 
                         move="Head Butt")

class Vaporeon(WaterPokemon):
    def __init__(self):
        super().__init__(name="Vaporeon", 
                         hitpoints=70, 
                         attack_damage=19, 
                         move="Hyrdo Pump")

class Squirtle(WaterPokemon):
    def __init__(self):
        super().__init__(name="Squirtle", 
                         hitpoints=44, 
                         attack_damage=16, 
                         move="Surf")
