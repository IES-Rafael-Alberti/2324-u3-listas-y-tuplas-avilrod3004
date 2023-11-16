'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''

from src.Ejercicio_3_1_8 import pedir_palabra

def contar_vocales(palabra: str, vocales: tuple) -> list:
    '''Cuenta el númerod de veces que aparece cada vocal en la palabra

    Args:
        palabra (str): palabra dada por el usuario por consola
        vocales (tuple): vocales

    Return:
        list: veces que se repite cada vocal en la palabra
    '''
    num_vocales = []
    longitud = len(palabra)
    palabra = palabra.lower()

    for i in range(0, 5):
        num = 0
        
        for j in range(0, longitud):
            if vocales[i] == palabra[j]:
                num += 1

            j += 1

        i += 1
        num_vocales.append(num)

    return num_vocales

def main():
    vocales = ('a', 'e', 'i', 'o', 'u')
    palabra = pedir_palabra()

    num_vocales = contar_vocales(palabra, vocales)

    # imprimir el número de veces que aparece cada vocal en la palabra
    for i in range(0, 5):
        print(f'La vocal {vocales[i]} aparece {num_vocales[i]} veces')
        i += 1


if __name__ == '__main__':
    main()