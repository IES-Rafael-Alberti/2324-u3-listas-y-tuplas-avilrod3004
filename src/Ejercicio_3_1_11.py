'''
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
'''

def producto_escalar(a: tuple, b:tuple) -> int:
    '''Calcular el producto escalar de dos vectores

    Args:
        a (tuple): vector 1
        b (tuple): vector 2

    Return:
        int: producto escalar de los vectores 1 y 2
    '''
    producto = 0
    for i in range(0, 3):
        producto += (a[i] * b[i])

        i += 1

    return producto


def main():
    a = (1, 2, 3)
    b = (-1, 0, 2)

    # calcular el producto escalar de los vectores a y b
    producto = producto_escalar(a, b)

    print(f'El producto escalar es => {producto}')


if __name__ == '__main__':
    main()