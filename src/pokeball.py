
class Pokeball:
    """These contain pokemon"""
    def __init__(self):
        self.pokemon = None
    
    def catch(self,pokemon):
        """Cathces a pokemon only if it is empty. Raises an exception otherwise"""
        if self.pokemon == None:
            self.pokemon = pokemon
        else:
            raise Exception("This pokeball has already a pokemon")
    
    def is_empty(self)->bool:
        """Returns true if the pokeball is empty and false otherwise"""
        if not self.pokemon:
            return True
        return False
    