'''
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
'''

def precio_mayor(precios: tuple, num: int) -> int:
    '''Bucle que compara los números, guardando el mayor en cada comparación

    Args:
        precios (tuple): tupla con los precios
        num (int): número de precios que contiene la tupla

    Return:
        int: precio mayor de la tupla
    '''
    mayor = 0
    for i in range(0, num):
        if precios[i] > mayor:
            mayor = precios[i]
        
        i += 1

    return mayor


def precio_menor(precios: tuple, num: int, mayor: int) -> int:
    '''Bucle que compara los precios, guardando el menor en cada comparación

    Args:
        precios (tuple): tupla con los precios
        num (int): número de precios que contiene la tupla
        mayor (int): precio mayor de la tupla

    Return:
        int: precio menor de la tupla

    '''
    menor = mayor
    for i in range(0, num):
        if precios[i] < menor:
            menor = precios[i]

        i += 1

    return menor


def main():
    precios = (50, 75, 46, 22, 80, 65, 8)

    longitud = len(precios)

    # calcular el precio mayor
    mayor = precio_mayor(precios, longitud)

    # calcular el precio menor
    menor = precio_menor(precios, longitud, mayor)

    # mostrar por pantalla cual es el menor precio y cual es el mayor
    print(f'El mayor de los precios es {mayor} y el menor de los precios es {menor}')


if __name__ == '__main__':
    main()