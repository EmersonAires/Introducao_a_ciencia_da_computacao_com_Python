import exercicio1_triangulos_retangulos
import pytest

class Test_exercio_1:

    @pytest.mark.parametrize("a, b, c, valor_esperado", [(1, 2, 3, False),(3,2, 5, False), (8, 6, 10, True), (3, 4, 5, True)])

    def test_triangulo_retangulo(self, a, b, c, valor_esperado):

        t1 = exercicio1_triangulos_retangulos.Triangulo(a, b, c)
        assert t1.retangulo() == valor_esperado
    
    @pytest.fixture
    def t1(self):
        t1 = exercicio1_triangulos_retangulos.Triangulo(2, 2, 2)
        return t1

    @pytest.mark.parametrize("a, b, c, valor_esperado", [(1, 2, 3, False),(3,2, 5, False), (8, 8, 8, True), (4, 4, 4, True)])

    def test_triangulos_semelhantes(self, t1, a, b, c, valor_esperado):
        t2 = exercicio1_triangulos_retangulos.Triangulo(a, b, c)
        assert t1.semelhantes(t2) == valor_esperado
