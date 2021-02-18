import soma_lista
import pytest


class Test_recursao:


    @pytest.mark.parametrize("entrada, valor_esperado", [
        ([1, 2, 3], 6),
        ([7, 8, 9], 24),
        ([0, 0, 0], 0),
    ])


    def test_soma_lista(self, entrada, valor_esperado):
        assert soma_lista.soma_lista(entrada) == valor_esperado