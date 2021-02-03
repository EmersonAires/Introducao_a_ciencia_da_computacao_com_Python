class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return (self.a + self.b + self.c)
    
    def tipo_lado(self):
        if self.a == self.b != self.c :
            return "isósceles"
        
        if self.a != self.b == self.c :
            return "isósceles"
        
        if self.b != self.a == self.c :
            return "isósceles"


        elif self.a == self.b  == self.c:
            return "equilátero"
            
        elif self.a != self.b  != self.c != self.a:
            return "escaleno"

