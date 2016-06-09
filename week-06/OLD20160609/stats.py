from random import randint



# Hero
# HP: 20 + 3 * d6
# DP: 2 * d6
# SP: 5 + d6
# Monster Lvl x (if boss)
# HP: 2 * x * d6 (+d6)
# DP: x/2 * d6 (+d6/2)
# SP: x * d6 (+x)

def dice(times):
    dice = []
    for i in range(times):
        i = randint(1,6)
        dice.append(i)
    return dice

print(hero_stat(3))


# def hero_hp():
#     hp = 20+3*randint(1,6)
#
# def hero_dp():
#     dp = 2*randint(1,6)
#
# def hero_sp():
#     sp = 5 + randint(1,6)
#
# def monster_hp():
#     hp = 2 * x * randint(1.6)
# def monster_dp():
#     dp = x/2 * randint(1.6)
# def monster_sp():
#     sp = x*randint(1.6),


def hero_stat():
    dice = dice(3)
    hp = 20+3*dice[0]
    dp = 2*dice[1]
    sp = 5 + dice[2]

def monster_stat():
