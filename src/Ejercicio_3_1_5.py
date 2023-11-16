'''
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
'''
def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    serie = ''

    for i in range(0, 10):
        if i == 9:
            serie = serie + f'{numeros[9 - i]}'
        else:
            serie = serie + f'{numeros[9 - i]}, '
        
        i += 1

    print(serie)


if __name__ == '__main__':
    main()