import exercicio_1
import pytest

class Test_exercicio1:

    def teste_1(self):
        t1 = exercicio_1.Triangulo(1, 1, 1)
        assert t1.perimetro() == 3
    
    def teste_2(self):
        t2 = exercicio_1.Triangulo(2, 2, 2)
        assert t2.perimetro() == 6
    
    def teste_3(self):
        t3 = exercicio_1.Triangulo(2, 2, 2)
        assert t3.perimetro() == 6
    
  
