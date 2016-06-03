from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600, bg= 'yellow')
canvas.pack()

def draw_triangle(x, y, size):
    h = ((3**0.5)/2)
    canvas.create_polygon(x, y, x + size, y, x + size / 2, y + h * size, fill = 'white', outline = 'black')


def draw_tringle_fractal(x, y, size):
    draw_triangle(x, y, size)

    if size > 5:
        h = (((3 ** 0.5) / 2) * size)
        draw_tringle_fractal(x, y, size/2)
        draw_tringle_fractal(x + size / 2, y, size / 2)
        draw_tringle_fractal(x + size / 4, y + h /2, size / 2)

def rectangle(x, y, size):
    canvas.create_rectangle(x + size, y, x + 2 * size, y + size)
    canvas.create_rectangle(x, y + size, x + size, y + 2 * size)
    canvas.create_rectangle(x + size, y + size, x + 2 * size, y + 2 * size)
    canvas.create_rectangle(x + 2 * size, y + size, x + 3 * size, y + 2 * size)
    canvas.create_rectangle(x + size, y + 2 * size, x + 2 * size, y + 3 * size)

    if size < 3:
        pass
    else:
        rectangle(x+size, y, size/3)
        rectangle(x, y + size, size/3)
        rectangle(x + 2 * size, y + size, size/3)
        rectangle(x +size, y + 2* size, size / 3)

def draw_hexa(x, y, size):
    h = (((3 ** 0.5) / 2) * size)
    canvas.create_polygon(x + size / 2, y, x + (size / 2 + size), y, x + 2 * size, y + h, x + (size / 2 + size), y + 2 * h, x + size / 2, y + 2 * h, x, y + h, fill = 'white', outline = 'black')


def draw_fractal(x, y, size):
    h = (((3 ** 0.5) / 2) * size)
    draw_hexa(x, y, size)

    if size > 5:
        draw_fractal(x + size / 3, y, size / 3)
        draw_fractal(x + size, y, size / 3)
        draw_fractal(x + size / 3, y + h + h / 3, size / 3)
        draw_fractal(x + size, y + h + h / 3, size / 3)
        draw_fractal(x, y + 2 * (h / 3), size / 3)
        draw_fractal(x+ size + size / 3, y + 2 * (h / 3), size / 3)



def create_fractal():
    print('1. Nyomja meg az 1 gombot haromszog fractal kirajzolasahoz!\n')
    print('2. Nyomja meg az 2 gombot a negyzet fractal kirajzolasahoz!\n')
    print('3. Nyomja meg az 3 gombot a hexa fractal kirajzolasahoz!\n')
    print('4. Nyomja meg az X gombot a kilepeshez!\n')

    while True:
        try:
            choise = input('Adja meg a kivalasztott menupont szamat: ')
            if choise == 'X':
                return
            if choise == '1':
                draw_tringle_fractal(0, 0, 300)
                break
            elif choise == '2':
                rectangle(0, 0, 200)
                break
            elif choise == '3':
                draw_fractal(5, 5, 150)
                break
            elif choise < '1' or choise > '3':
                raise ValueError('Az ertek nem helyes')
                continue
        except ValueError:
            print('A megadott ertek helytelen!')


create_fractal()
root.mainloop()
