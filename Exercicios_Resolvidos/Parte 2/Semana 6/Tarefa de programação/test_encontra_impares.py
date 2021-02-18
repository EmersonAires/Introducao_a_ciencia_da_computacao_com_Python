import encontra_impares
import pytest


class Test_encontra_impares:


    @pytest.mark.parametrize("entrada, valor_esperado", [
        ([1, 2, 3], [1, 3]),
        ([7, 8, 9], [7, 9]),
        ([0, 0, 0], []),
    ])


    def test_encontra_impares(self, entrada, valor_esperado):
        assert encontra_impares.encontra_impares(entrada) == valor_esperado
        