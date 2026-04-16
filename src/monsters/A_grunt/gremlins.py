    
    
class GruntGoblin():
    def __init__(self, hp:int = 5, energy = 1, attack: int = 1, block:int = 0, position:int = 0,
                 tactical_events={'attack':{'cost':1,'increment':1}}):
        self.hp = hp
        self.energy = energy
        self.attack = attack
        self.block = block
        self.position = position
        self.tactical_events = tactical_events
        self.strength = False # increment attack damage
        self.weak = False # deals half damage (rate)
        self.vulnerable = False # takes double damage (rate)
    
    
    def load_tactical_events(self):
        # this function will load the tactical events for the enemy, it will return a dictionary of the tactical events that the enemy can use
        moves = {
            "attack": {'cost': 1, 'increment': 1},
            "defend": {'cost': 1, 'increment': 1},
            "strong-attack": {'cost': 2, 'increment': 2},
        }
        self.tactical_events = moves
