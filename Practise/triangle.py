def draw_triangle_or_diamond(line):
    i = 0
    while i == 0:
        choise = input('Adjon meg 0-t a haromszoghoz, 1-et a diamondhoz: \n')
        if choise == 'exit':
            return
        elif choise < '0' or choise > '1':
            print ('HIBA!!! A megadott ertek 0 vagy 1 lehet.\n')
            continue
        else:
            break

    while i == 0:
        character = input('Adjon meg egy karaktert, amivel ki szeretne rajzolni a format: \n')
        if character == 'exit':
            return
        elif len(character) == 1:
            break
        else:
            print('HIBA!!! A karakter hossza nem lehet 1nel nagyobb! \n')
            continue


    for i in range(line + 1):
        print((line - i) * ' ' + i * str(character)+ str(character) + i * str(character))

    if choise == '1':
        for i in range(1,line + 1):
            print(i * ' ' + (line - i) * str(character) + str(character) +(line - i) * str(character))

draw_triangle_or_diamond(7)
