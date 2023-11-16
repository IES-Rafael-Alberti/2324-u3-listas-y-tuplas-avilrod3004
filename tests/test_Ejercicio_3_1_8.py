import pytest
from src.Ejercicio_3_1_8 import es_palindromo

@pytest.mark.parametrize(
    'input_x, input_y, expected',
    [
        (['h', 'o', 'l', 'a'], ['a', 'l', 'o', 'h', ], False),
        (['s', 'a', 'l', 'a', 's'], ['s', 'a', 'l', 'a', 's'], True),
        (['s', 'o', 'm', 'e', 't', 'e', 'm', 'o', 's'], ['s', 'o', 'm', 'e', 't', 'e', 'm', 'o', 's'], True),
        (['p', 'y', 't', 'h', 'o', 'n'], ['n', 'o', 'h', 't', 'y', 'p'], False)
    ]
)

def test_es_palindromo_params(input_x, input_y, expected):
    assert es_palindromo(input_x, input_y) == expected