# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def bunny(n):
    if n <= 1:
        return 2
    else:
        return 2 + bunny(n - 1)

print(bunny(3)) 
