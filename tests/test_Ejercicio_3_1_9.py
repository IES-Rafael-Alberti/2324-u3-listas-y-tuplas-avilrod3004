import pytest
from src.Ejercicio_3_1_9 import contar_vocales

@pytest.mark.parametrize(
    'input_x, input_y, expected',
    [
        ('hola', ('a', 'e', 'i', 'o', 'u'), [1, 0, 0, 1, 0]),
        ('murcielago', ('a', 'e', 'i', 'o', 'u'), [1, 1, 1, 1, 1]),
        ('python', ('a', 'e', 'i', 'o', 'u'), [0, 0, 0, 1, 0]),
        ('Ejercicios', ('a', 'e', 'i', 'o', 'u'), [0, 2, 2, 1, 0])
    ]
)

def test_contar_vocales_params(input_x, input_y, expected):
    assert contar_vocales(input_x, input_y) == expected