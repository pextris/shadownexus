import random

def hack_battle(player, enemy):
    log = []

    player_attack = random.randint(10, 25)
    enemy_attack = random.randint(5, enemy.damage)

    # Player attacks first
    log.append(f"> You attack the {enemy.name} and deal {player_attack} damage.")

    enemy.health -= player_attack
    if enemy.health <= 0:
        log.append(f"> {enemy.name} has been neutralized.")
        player.syscred += enemy.syscred_drop
        level_ups = player.gain_xp(enemy.xp_reward)
        player.save()
        log.append(f"> You gained {enemy.syscred_drop} SysCred and {enemy.xp_reward} XP.")
        if level_ups > 0:
            log.append(f"> LEVEL UP! You are now Level {player.level}. Max health increased.")
        return log

    # Enemy survives and counter-attacks
    log.append(f"> {enemy.name} counter-attacks and deals {enemy_attack} damage.")
    player.health -= enemy_attack
    if player.health <= 0:
        player.health = 0
        log.append("> You have been defeated. Disconnect and recover.")

    player.save()
    return log
