def tabla(numero):
    print(f'elegiste la tabla del {numero} ')
    for x in range(0, 12):
        print(f'{x} x {numero} =' + str(int(x * 10)))


def run():
    menu = 'Vamos a visualizar la tabla del numero elegido: '
    numero = input(menu)
    tabla(numero)


if __name__ == '__main__':
    run()
