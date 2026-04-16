import random

from player.players import Hero
from monsters.A_grunt.gremlins import GruntGoblin
from battle.battle_logic import attack_sequence
from battle.action_key_mapper import offensive_card_actions, defensive_card_actions, special_card_effects
from cards.cards import HeroDeck, CommonCard


""" def get_basic_actions()->dict:
    actions={
        "attack":{"cost":1,"increment":1},
        "defend":{"cost":1,"increment":1},
        "double-attack":{"cost":2,"increment":2}
    }
    return actions """


def roll_dice()->int:
    dice_roll = random.randrange(1,6)
    return dice_roll


def draw_cards_from_deck(playable_cards:list[dict], base_deck:HeroDeck, number_of_cards:int = 5)->list[dict]:
    """_summary_

    Args:
        playable_cards (list[dict]): _sublist of all available cards for this session._
        base_deck (HeroDeck): _default deck of all available cards for this session._
        number_of_cards (int, optional): _default of 5_.

    Returns:
        list[dict]: _list length will be 5 to represent 5 cards._
        
    Description:
        This function will draw 5 cards from the playable cards and remove each card from the playable deck after it is drawn.
    """
    drawn_cards = []
    for i in range(number_of_cards):
        if len(playable_cards) == 0:
            print('No more cards to draw, shuffling deck...')
            playable_cards=base_deck.shuffle_deck()
        drawn_card = playable_cards.pop(0)
        drawn_cards.append(drawn_card)
    return drawn_cards


def player_turn(Ironclad:Hero, drawn_cards:list[CommonCard], base_deck:HeroDeck):
    def _show_hand(hand_of_cards:list[CommonCard]):
        for index, card in enumerate(hand_of_cards):
            print(f'Card {index + 1}: {card}')
        
    player_actions={}
    energy=Ironclad.energy
    list_keys = drawn_cards

    while energy > 0:
        _show_hand(list_keys)
        chosen_position = int(input(f'Pick a card: '))
        if chosen_position-1 not in range(len(list_keys)):
            print('Invalid card position, please choose a valid card.')
            continue
        chosen_card = list_keys[chosen_position-1]
        print(chosen_card)
        energy_cost = chosen_card.energy
        if energy_cost>energy:
            print(f'Not enough energy to perform {chosen_card.title}. Please choose another action.')
            continue
        else:
            energy-=energy_cost
            print(f'You have {energy} energy left.')
        # remove the selected card from the drawn cards.
        list_keys.remove(chosen_card)
        
        tactical_event = chosen_card.increment
        # add the tactical event to the player actions, if the player already has an action, add the tactical event to the existing action
        if chosen_card.type in player_actions:
            player_actions[chosen_card.type] += tactical_event
        else:
            player_actions[chosen_card.type] = tactical_event
            
    return player_actions


def enemy_turn(Enemy:GruntGoblin):
    enemy_actions = {}
    energy = Enemy.energy
    enemy_default_actions = Enemy.tactical_events
    enemy_action_list = list(enemy_default_actions.keys())

    while energy > 0:
        if len(enemy_action_list) > 1:
            random_selected_index = random.randrange(start=1, stop=len(enemy_action_list))
        else:
            random_selected_index = len(enemy_action_list)
            
        selected_action = enemy_action_list[random_selected_index-1]
        print(f'Enemy performed action `{selected_action}`')
        
        tactical_decision =  enemy_default_actions[selected_action]
        energy_cost = tactical_decision['cost']
        if energy_cost>energy:
            print(f'Cannot perform action, not enough energy!')
        else:
            energy -= energy_cost
        
        tactical_event = tactical_decision['increment']        
        # add the tactical event to the player actions, if the player already has an action, add the tactical event to the existing action
        if selected_action in enemy_actions:
            enemy_actions[selected_action] += tactical_event
        else:
            enemy_actions[selected_action] = tactical_event        
        
    return enemy_actions


def apply_defense(player_actions: dict, enemy_actions: dict, Ironclad: Hero, EnemyGoblin: GruntGoblin):
    if 'defend' in player_actions:
        Ironclad.block += player_actions['defend']
        
    if 'defend' in enemy_actions:
        EnemyGoblin.block += enemy_actions['defend']
        
        
def apply_attack(player_actions: dict, enemy_actions: dict, Ironclad: Hero, EnemyGoblin: GruntGoblin):     
    for player_action in player_actions:
        if player_action.lower() in offensive_card_actions:
            attack_sequence(player_actions[player_action], Ironclad.weak, EnemyGoblin.vulnerable, EnemyGoblin)
            
        elif player_action == 'double-attack':
            attack_sequence(player_actions[player_action], Ironclad.weak, EnemyGoblin.vulnerable, EnemyGoblin)
        
    for enemy_action in enemy_actions:
        if enemy_action.lower() in offensive_card_actions:
            attack_sequence(enemy_actions[enemy_action], EnemyGoblin.weak, Ironclad.vulnerable, Ironclad)


def apply_special_effects(player_actions: dict, enemy_actions: dict, Ironclad: Hero, EnemyGoblin: GruntGoblin):
    if 'bash' in player_actions:
        EnemyGoblin.vulnerable = True


def start_game():
    dice_roll = roll_dice()
    # load hero.
    Ironclad = Hero(hp = 10, position = 1)
    deck_of_cards = HeroDeck()
    deck_of_cards.set_common_deck()
    deck_of_cards.shuffle_deck()
    playable_cards = deck_of_cards.deck
    Ironclad.deck = deck_of_cards
    
    # load enemies.
    EnemyGoblin = GruntGoblin(hp = 5, energy=2, attack = 2)
    turn_number=1
    
    # begin combat loop.
    while Ironclad.hp > 0 and EnemyGoblin.hp > 0:
        drawn_cards = draw_cards_from_deck(playable_cards, deck_of_cards)
        
        Ironclad.block = 0
        EnemyGoblin.block = 0
        print("########################################")
        print(f'Combat Turn: {turn_number}')
        
        print(f'IronClad HP = {Ironclad.hp}')
        print(f'EnemyGoblin HP = {EnemyGoblin.hp}')
        print("---------------------------------------")
        player_actions = player_turn(Ironclad, drawn_cards, deck_of_cards)
        print("---------------------------------------")
        print(f'Player actions: {player_actions}')
        print("---------------------------------------")
        
        enemy_actions = enemy_turn(EnemyGoblin)
        print(f'Enemy actions: {enemy_actions}')
        print("---------------------------------------")
        # combat phase resolution.
        apply_defense(player_actions, enemy_actions, Ironclad, EnemyGoblin)
        apply_attack(player_actions, enemy_actions, Ironclad, EnemyGoblin)
        #apply_special_effects(player_actions, enemy_actions, Ironclad, EnemyGoblin)
        
        turn_number+=1
         
    if Ironclad.hp <= 0:
        print('You have been defeated!')
    else:
        print('You have defeated the enemy!')
        
    print(f'IronClad HP = {Ironclad.hp}')
    print(f'EnemyGoblin HP = {EnemyGoblin.hp}')
        
if __name__ == "__main__":
    start_game()