# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.


def changer(n):
    if len(n) <= 1:
        if n[0] == 'x':
            return ''
        else:
            return n[0]
    else:
        if n[0] == 'x':
            return '' + changer(n[1:])
        else:
            return n[0] + changer(n[1:])

print(changer('Axlxmxa'))
