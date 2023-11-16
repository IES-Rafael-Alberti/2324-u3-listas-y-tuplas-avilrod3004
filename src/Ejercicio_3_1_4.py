'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

from src.Ejercicio_3_1_1 import pedirNumero

def main():
    numeros = []
    
    # pide los 6 números
    for i in range(0, 6):
        num_ganadores = pedirNumero('Introduce un número: ')
        numeros.append(num_ganadores)
        i += 1

    # ordena los números de menor a mayor
    numeros.sort()
    print(numeros)


if __name__ == '__main__':
    main()