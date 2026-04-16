
def attack_sequence(incomming_attack_damage:int, attacker_weakened:bool, target_is_vulnerable:bool, Target):
    target_block = Target.block
    # if target has weak applied, halve the attack damage (round up)
    if attacker_weakened:
        incomming_attack_damage = round(incomming_attack_damage * 0.5)
        
    if target_is_vulnerable:
        incomming_attack_damage = round(incomming_attack_damage * 2)
        
    if target_block >= incomming_attack_damage:
        # if the block is greater than the attack, decrement the block.
        # if the attack and block cancel out, reset the block to 0.
        Target.block -= incomming_attack_damage
    elif target_block == incomming_attack_damage:
        Target.block = 0
    else:
        # subtract the remaining damage from the enemy hp
        damage = incomming_attack_damage - Target.block
        Target.block = 0
        Target.hp -= damage
