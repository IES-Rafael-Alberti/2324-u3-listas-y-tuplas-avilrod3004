import pytest
from src.Ejercicio_3_1_10 import precio_mayor, precio_menor

@pytest.mark.parametrize(
    'input_x, input_y, expected',
    [
        ((30, 12, 5, 6, 9, 39), 6, 39),
        ((14, 2, 4, 7, 80), 5, 80),
        ((45, 1, 8, 34, 29, 100), 6, 100),
        ((1, 14, 11, 20, 23), 5, 23)
    ]
)

def test_precio_mayor_params(input_x, input_y, expected):
    assert precio_mayor(input_x, input_y) == expected



@pytest.mark.parametrize(
    'input_z, input_a, input_b, expected',
    [
        ((30, 12, 5, 6, 9, 39), 6, 39, 5),
        ((14, 2, 4, 7, 80), 5, 80, 2),
        ((45, 1, 8, 34, 29, 100), 6, 100, 1),
        ((1, 14, 11, 20, 23), 5, 23, 1)
    ]
)

def test_precio_menor_params(input_z, input_a, input_b, expected):
    assert precio_menor(input_z, input_a, input_b) == expected