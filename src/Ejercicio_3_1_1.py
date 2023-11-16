'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
'''
def pedirNumero(msj: str) -> int:
    '''Pide un número entero al usuario por consola

    Args:
        msj (str): texto a mostrar en el input

    Return:
        int: número dado por el usuario
    '''
    num = None

    try:
        num = int(input(msj))
    except ValueError:
        print('**ERROR** - INTRODUCE UN NÚMERO ENTERO')
    except:
        print('**ERROR**')

    return num


def pedirAsignatura() -> str:
    '''Pide al usuario que introduzca el nombre de una asignatura por consola

    Return:
        str: asignatura dada por el usuario
    '''
    asignatura = input('Introduce una asignatura: ')

    return asignatura


def main():
    num = pedirNumero('Número de asignaturas que vas a almacenar: ')

    # pide num hasta que sea un número entero
    while num == None:
        num = pedirNumero('Número de asignaturas que vas a almacenar: ')

    curso = []

    # hace un input pididendo una asignatura mientras la longitud de la lista sea menor al número dado por el usuario
    while len(curso) < num:
        asignatura = pedirAsignatura()
        curso.append(asignatura)

    # muestra por pantalla y en una linea distinta cada asignatura introducida
    print('\nAsignaturas guardadas: ')
    for i in range(0, num):
        print(f'- {curso[i]}')
        i += 1


if __name__ == '__main__':
    main()        