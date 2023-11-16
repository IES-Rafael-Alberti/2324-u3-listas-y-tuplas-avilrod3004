import pytest
from src.Ejercicio_3_1_11 import producto_escalar

@pytest.mark.parametrize(
    'input_a, input_b, expected',
    [
        ((1, 2, 3), (-1, 0, 2), 5),
        ((0, 3, 5), (-4, 0 , -8), -40),
        ((3, 1, 2), (3, 7, 8), 32),
        ((0, 4, 8), (5, 3, 1), 20)
    ]
)

def test_producto_escalar_params(input_a, input_b, expected):
    assert producto_escalar(input_a, input_b) == expected