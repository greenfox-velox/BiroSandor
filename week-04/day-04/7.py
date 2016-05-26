# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def changer(n):
    if len(n) <= 1:
        if n[0] == 'x':
            return 'y'
        else:
            return n[0]
    else:
        if n[0] == 'x':
            return 'y' + changer(n[1:])
        else:
            return n[0] + changer(n[1:])

print(changer('Axlxmxa'))
