    
    
class Hero():
    def __init__(self, hp:int = 9, energy:int = 3, block:int = 0, position:int=0):
        self.hp = hp
        self.energy = energy
        self.block = block
        self.position= position
        self.deck = None # list of dictionaries
        self.end_of_combat = None 
        self.weak = None # deals half damage (rate)
        self.vulnerable = None # takes double damage (rate)
        self.buff = None
        self.debuff = None
    