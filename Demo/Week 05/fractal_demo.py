def menu():
    menu = '1. Press 1 to draw a triangle fractal!\n\n2. Press 2 to draw a rectangle fractal!\n\n3. press 3 to draw a hexa fractal!\n\n4. Press X to exit!\n'
    print(menu)
menu()

def create_fractal():
    while True:
        try:
            choise = input('Give the number of the chosen menupoint: ')
            if choise == 'X':
                break
            elif choise == '1':
                from triangle import draw_triangle_fractal
                continue
            elif choise == '2':
                from rectangle import draw_rectangle_fractal
                continue
            elif choise == '3':
                from hexa import draw_hexa_fractal
                continue
            else:
                raise ValueError('The value is incorrect!')
                continue
        except ValueError:
            print('\nThis value is INCORRECT, please try again!\n')

create_fractal()
