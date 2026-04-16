
import random
from dataclasses import dataclass

@dataclass
class CommonCard:
    title: str
    energy: int
    action: str
    type: str
    increment: int
    description: str
    special_effect: str = None


class HeroDeck:
    # this function will return a list of cards that the hero can use in combat, it will return a list of dictionaries that represent the cards that the hero can use in combat.
    def __init__(self):
        self.deck = None
        self.set_common_deck()
        self.shuffle_deck()
    
    def set_common_deck(self, total_cards:int = 15, strike_cards:int = 6, defend_cards:int = 6, double_strike_cards:int = 3):
        common_deck = []
        # 6 strike cards, 6 defend cards, 3 double strike cards.
        for i in range(1, strike_cards + 1):
            TempCard = CommonCard(
                title = f"Strike {i}",
                energy = 1,
                action = "attack",
                type = "strike",
                increment = 1,
                description = f"Deal 1 damage to the enemy. (Card {i} of {total_cards})",
                special_effect=None
            )
            common_deck.append(TempCard)
        
        for i in range(1, defend_cards + 1):
            TempCard = CommonCard(
                title = f"Defend {i}",
                energy = 1,
                action = "defend",
                type = "defend",
                increment = 1,
                description = f"Gain 1 block. (Card {i} of {total_cards})",
                special_effect=None
            )
            common_deck.append(TempCard)
        
        for i in range(1, double_strike_cards + 1):
            TempCard = CommonCard(
                title = "Twin Strike",
                energy = 2,
                action = "double-attack",
                type = "strike",
                increment = 2,
                description = f"Deal 2 damage to the enemy. (Card {i} of {total_cards})",
                special_effect=None
            )
            common_deck.append(TempCard)
        SpecialCard = CommonCard(
                title = "Bash",
                energy = 2,
                action = "attack",
                type = "strike",
                increment = 2,
                description = f"Deal 2 damage to the enemy and apply 1 vulnerable. (Card {total_cards} of {total_cards})",
                special_effect="bash"
            )
        self.deck = common_deck
        
               
    def add_card(self, card):
        self.deck.append(card)
        
        
    def remove_card(self, card):
        self.deck.remove(card) 
    
        
    def shuffle_deck(self):
        random.shuffle(self.deck)