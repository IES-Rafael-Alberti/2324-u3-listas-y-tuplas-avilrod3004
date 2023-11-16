import pytest
from src.Ejercicio_3_1_13 import calcular_media, calcular_desviacion

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ([10, 40, 5, 6, 1], 12.4),
        ([10, 15, 20, 40], 21.25),
        ([0, 4, 7, 8, 9, 6], 5.666666666666667),
        ([9, 5, 1, 7, 5], 5.40)
    ]
)

def test_calcular_media_params(input_x, expected):
    assert calcular_media(input_x) == expected


@pytest.mark.parametrize(
    'input_y, input_z, expected',
    [
        ([10, 40, 5, 6, 1], 12.4, 14.093970341958295),
        ([10, 15, 20, 40], 21.25, 11.388041973930374),
        ([0, 4, 7, 8, 9, 6], 5.666666666666667, 2.9814239699997196),
        ([9, 5, 1, 7, 5], 5.40, 2.65329983228432)
    ]
)

def test_calcular_desviacion_params(input_y, input_z, expected):
    assert calcular_desviacion(input_y, input_z) == expected