def draw_triangle_or_diamond(line):
    while True:
        choise = input('Press the 0 for the triangle or 1 to the diamond: \n')
        if choise == 'exit':
            return
        elif choise < '0' or choise > '1':
            print ('ERROR!!! The input can only be 0 or 1.\n')
            continue
        else:
            break

    while True:
        character = input('Adjon meg egy karaktert, amivel ki szeretne rajzolni a format: \n')
        if character == 'exit':
            return
        elif len(character) == 1:
            break
        else:
            print('HIBA!!! The length of the character can be 1! \n')
            continue


    for i in range(line + 1):
        print((line - i) * ' ' + i * str(character)+ str(character) + i * str(character))

    if choise == '1':
        for i in range(1,line + 1):
            print(i * ' ' + (line - i) * str(character) + str(character) +(line - i) * str(character))

draw_triangle_or_diamond(7)
