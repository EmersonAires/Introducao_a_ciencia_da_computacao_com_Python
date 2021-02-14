import ordena
import pytest

class Test_ordena:

    @pytest.fixture
    def b (self):
        return ordena.ordenacao()

    @pytest.mark.parametrize("entrada, valor_esperado", [([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])]


    def test_bolha(self, entrada, valor_esperado):
        assert b.bolha(entrada) == valor_esperado


    def test_bolha_otimizado(self, entrada, valor_esperado):
        assert b.bolha_otimizado(entrada) == valor_esperado
