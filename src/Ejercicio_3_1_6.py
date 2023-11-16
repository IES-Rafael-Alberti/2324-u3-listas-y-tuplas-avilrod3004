'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
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
        try:
            nota = int(input(f'¿Qué nota has sacado en {curso[i]}? '))
        except ValueError:
            print('**ERROR** - INTRODUCE UN NÚMERO ENTERO')
        except:
            print('**ERROR**')
        finally:
            notas.append(nota)

        i += 1

    return notas


def eliminarAprobadas(curso: list, notas: list, num: int) -> list:
    '''Recorre la lista de las notas y crear una lista nueva a la que se añaden las asignaturas suspendidas

    Args:
        curso (list): lista con las asignaturas
        notas (list): lista con las notas
        num (int): número de asignaturas guardadas

    Return:
        list: lista con las asignaturas suspendidas
    '''
    curso_suspendidas = []
    for i in range(0, num):
        if notas[i] < 5:
            curso_suspendidas.append(curso[i])

        i += 1

    return curso_suspendidas


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

    # pedir las notas de cada asignatura
    notas = pedirNotas(curso, num)

    # guardar en una nueva lista las asignaturas suspendidas
    curso_suspendidas = eliminarAprobadas(curso, notas, num)
    num_suspendidas = len(curso_suspendidas)

    # comprobar si todas las asignaturas están aprobadas
    if len(curso_suspendidas) == 0:
        print('¡Has aprobado todas!')

    # muestra por pantalla y en una linea distinta cada asignatura introducida la nota correspondiente
    for i in range(0, num_suspendidas):
        print(f'Tienes que repetir {curso_suspendidas[i]}')
        i += 1


if __name__ == '__main__':
    main()        