'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
'''

def pedir_palabra() -> str:
    '''Pedir una palabra por consola al usuario

    Return:
        str: cadena de texto dada por el usuario
    '''
    try:
        palabra = input('Introduce una palabra: ')
    except ValueError:
        print('**ERROR** - INTRODUCE UNA PALABRA')
    except:
        print('**ERROR**')

    return palabra


def es_palindromo(derecha: list, invertida: list) -> bool:
    '''Comprueba si la palabra al derecho y al revés son la misma

    Args:
        derecha (list): palabra dada por el usuario
        invertida (list): palabra dada por el usuario al revés

    Return:
        bool: True si es un palindromo // False si no es un palindromo
    '''
    num = len(derecha)
    comp = True

    for i in range(0, num):
        if derecha[i] != invertida[i]:
            comp = False
        
        i += 1

    return comp


def main():
    palabra = None

    while palabra == None:
        palabra = pedir_palabra()

        # comprobar si el string tiene espacios o es un número
        if palabra.count(' ') >= 1 or palabra.isdecimal():
            palabra = None
    
    palabra_al_reves = palabra[::-1]
    palabra_lista = list(palabra)
    palabra_invertida_lista = list(palabra_al_reves)

    # comprobar si es un palindromo
    palindromo = es_palindromo(palabra_lista, palabra_invertida_lista)

    if palindromo == True:
        print('Es un palindromo')
    else:
        print('No es un palindromo')

    
if __name__ == '__main__':
    main()