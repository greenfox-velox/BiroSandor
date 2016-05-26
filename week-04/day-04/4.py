# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def powerup(base, n):
    if n<=1:
        return base
    else:
        return base * powerup(base, n-1)

print(powerup(3, 4))
