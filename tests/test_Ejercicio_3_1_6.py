import pytest
from src.Ejercicio_3_1_6 import eliminarAprobadas

@pytest.mark.parametrize(
    'input_x, input_y, input_z, expected',
    [
        (['prog', 'bd', 'edes', 'lm'], [3, 5, 6, 9], 4, ['prog']),
        (['mates', 'lengua', 'ingles', 'fisica'], [6, 8, 2, 2], 4, ['ingles', 'fisica']),
        (['mates', 'lengua', 'ingles', 'fisica'], [9, 8, 7, 6], 4, []),
        (['prog', 'bd', 'edes', 'lm'], [6, 5, 6, 9], 4, [])
    ]
)

def test_eliminarAprobadas(input_x, input_y, input_z, expected):
    assert eliminarAprobadas(input_x, input_y, input_z) == expected