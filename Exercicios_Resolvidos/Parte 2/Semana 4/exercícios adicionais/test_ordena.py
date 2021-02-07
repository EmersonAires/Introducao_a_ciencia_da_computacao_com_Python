from ordena import ordena
import pytest

class Test_ordena:

    @pytest.mark.parametrize("lista, valor_esperado" , [([5, 4, 3, 2, 1], 
    [1, 2, 3, 4, 5]), ([7, 2, 9, 1, 10], [1, 2, 7, 9, 10])])

    def test_ordena(self, lista, valor_esperado):
        assert ordena(lista) == valor_esperado