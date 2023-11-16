'''
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
'''

def eliminar_multiplos_de_tres(abecedario: list) -> list:
    '''Añade a una lista nueva las letras con posiciones que no sean múltiplo de 3

    Args:
        abecedario (list): abecedario

    Return:
        list: lista con las las letras con posiciones que no sean múltiplo de 3
    '''

    nuevo_abecedario = []

    for i in range(0, len(abecedario)):
        if i % 3 != 0:
            nuevo_abecedario.append(abecedario[i])

        i += 1

    return nuevo_abecedario


def main():
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    nuevo_abecedario = eliminar_multiplos_de_tres(abecedario)

    print(nuevo_abecedario)

if __name__ == '__main__':
    main()