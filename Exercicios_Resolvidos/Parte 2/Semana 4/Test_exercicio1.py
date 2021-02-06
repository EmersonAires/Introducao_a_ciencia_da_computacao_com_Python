import exercicio1
import pytest

class Test_:

    @pytest.mark.parametrize("lista, valor_esperado", [([1, 4, 2, 5], False),
    ([1, 2, 3, 4, 5], True), (["a", "b", "c", "d", "e"], True)])

    def testa_ordenada(self, lista, valor_esperado):
        assert exercicio1.ordenada(lista) == valor_esperado

