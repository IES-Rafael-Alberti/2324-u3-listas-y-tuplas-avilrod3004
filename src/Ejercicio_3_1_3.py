'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
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


def pedirNotas(curso: list, num: int) -> list:
    '''Pide una nota para cada asignatura introducida

    Args:
        curso (list): lista con las asignaturas
        num (int): número entero con la cantidad de asignaturas introducidas

    Return:
        list: lista con las notas ordenadas en el mismo orden que las asiganturas en su correspondiente lista
    '''
    notas = []

    for i in range(0, num):
        nota = input(f'¿Qué nota has sacado en {curso[i]}? ')
        notas.append(nota)
        i += 1

    return notas



def main():
    # ENTRADA
    num = pedirNumero('Número de asignaturas que vas a almacenar: ')

    # pide num hasta que sea un número entero
    while num == None:
        num = pedirNumero('Número de asignaturas que vas a almacenar: ')

    curso = []

    # hace un input pididendo una asignatura mientras la longitud de la lista sea menor al número dado por el usuario
    while len(curso) < num:
        asignatura = pedirAsignatura()
        curso.append(asignatura)

    # pedir las notas de cada asignatura
    notas = pedirNotas(curso, num)


    # SALIDA
    # muestra por pantalla y en una linea distinta cada asignatura introducida la nota correspondiente
    for i in range(0, num):
        print(f'En {curso[i]} he sacado {notas[i]}')
        i += 1


if __name__ == '__main__':
    main()        