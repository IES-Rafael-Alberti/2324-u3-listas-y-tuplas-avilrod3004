'''
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
'''
from src.Ejercicio_3_1_1 import pedirNumero
import math

def calcular_media(muestra: list) -> float:
    '''Calcula la media de los números dados

    Args:
        media (list): números de los que se va a calcular la media

    Return:
        float: media de los números
    '''
    suma = 0
    cantidad = len(muestra)
    for i in range(0, cantidad):
        suma += muestra[i]

        i += 1

    media = suma / cantidad

    return media


def calcular_desviacion(muestra: list, media: float) -> float:
    '''Calcular la desviación típica de los numeros dados

    Args:
        muestra (list): números de los que se va a calcular la desviación típica
        media (float): media los números de la tupla

    Return:
        float: desviación típica de los números
    '''
    cantidad = len(muestra)
    suma = 0

    for i in range(0, cantidad):
        media_diferencia = (muestra[i] - media) ** 2

        suma += media_diferencia

        i += 1

    media = suma / cantidad

    desviacion = math.sqrt(media)

    return desviacion

    
def main():
    muestra = []

    num = pedirNumero('¿Cuántos números tendrá la muestra?: ')

    while num == None:
        num = pedirNumero('¿Cuántos números tendrá la muestra?: ')

    for i in range(0, num):
        numero = pedirNumero('Añade un número -> ')
        muestra.append(numero)

    # calcular la media de los números
    media = calcular_media(muestra)
    print(f'La media es => {media:.2f}')

    # calcular la desviación típica
    desviacion = calcular_desviacion(muestra, media)
    print(f'La desviación típica es => {desviacion:.2f}')


if __name__ == '__main__':
    main()