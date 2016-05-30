def triangle():
    print('Kirjazolja a haromszog fractalt')

def rectangle():
    print('Kirajzolja a negyzet fractalt')
def hexa():
    print('kirajzolja a hexa fractalt')



def creat_fractal():
    print('1. Nyomja meg az 1 gombot haromszog fractal kirajzolasahoz!')
    print('2. Irja be a recta szot a negyzet fractal kirajzolasahoz!')
    print('3. Irja be a hexa szot a hatszog fractal kirajzolasahoz!')
    print('4. Nyomja meg az X gombot a kilepeshez!')

    choise = input('Adja meg a kivalasztott menupont szamat: ')


    if choise == 1:
        print('Kirjazolja a haromszog fractalt')
creat_fractal()
