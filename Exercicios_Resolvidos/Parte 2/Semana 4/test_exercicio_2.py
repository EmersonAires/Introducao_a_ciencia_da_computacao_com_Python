from exercicio_2 import busca
import pytest

class Test_:


    @pytest.mark.parametrize("lista, elemento, resultado_esperado",
    [([1, 2, 3, 4, 5], 3, 2), (["a", "b", "c"], "d", False), 
    ([12, 125, 15, 17], 17, 3)])

    def testa_busca(self, lista, elemento, resultado_esperado):
        assert busca(lista, elemento) == resultado_esperado
