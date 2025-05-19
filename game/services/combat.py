import random

def hack_battle(player, enemy):
    log = []

    while player.health > 0 and enemy.health > 0:
        player_damage = max(0, player.level + random.randint(1, 8) - enemy.defense)
        enemy.health -= player_damage
        log.append(f">> You breach {enemy.name}'s defenses for {player_damage} damage.")

        if enemy.health <= 0:
            log.append(f"!! {enemy.name} has been derezzed.")
            player.syscred += enemy.syscred_drop
            player.gain_experience(enemy.xp_drop)
            log.append(f"+ {enemy.syscred_drop} SysCred earned.")
            log.append(f"+ {enemy.xp_drop} XP earned.")
            break

        enemy_damage = max(0, enemy.attack + random.randint(1, 6) - player.level)
        player.health -= enemy_damage
        log.append(f"<< {enemy.name} counterattacks for {enemy_damage} damage!")

        if player.health <= 0:
            log.append("!! You’ve been firewalled into oblivion.")
            break

    return log
