def tree_maker(input, type, character):
    if type < 0 or type > 1:
        print ('hiba: masodik parameter erteke 0 vagy 1 lehet.')
        return

    for i in range(input + 1):
        print((input - i) * ' ' + i * str(character)+ str(character) + i * str(character))

    if type == 1:
        for i in range(1,input + 1):
            print(i * ' ' + (input - i) * str(character) + str(character) +(input - i) * str(character))

tree_maker(7, 1, 7)
