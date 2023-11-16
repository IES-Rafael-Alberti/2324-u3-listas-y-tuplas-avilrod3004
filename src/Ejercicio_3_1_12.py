'''
Escribir un programa que almacene las matrices A=(123456) y B=(-100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
'''

def main():
    # Entrada
    matriz_a = [[1], [2], [3], [4], [5], [6]]
    matriz_b = [[-1], [0], [0], [1], [1], [1]]
    suma = 0

    # Proceso
    # multiplica cada vector de la matriz A por el la matriz B en la misma posición y suma los productos
    for i in range(0, len(matriz_a)):
        productos = 0
        productos = matriz_a[i][0] * matriz_b[i][0]

        suma += productos
        i += 1

    # Salida
    print(f'El producto de las dos matrices es => {suma}')


if __name__ == '__main__':
    main()