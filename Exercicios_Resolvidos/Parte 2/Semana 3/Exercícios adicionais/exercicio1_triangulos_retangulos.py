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
    
    def retangulo(self):

        hipotenusa = max(self.a, self.b, self.c)

        if hipotenusa == self.c:

            if hipotenusa**2 == (self.a**2) + (self.b**2):
                return True
            else:
                return False
        if hipotenusa == self.b:

            if hipotenusa**2 == (self.a**2) + (self.c**2):
                return True
            else:
                return False
        if hipotenusa == self.a:

            if hipotenusa**2 == (self.b**2) + (self.c**2):
                return True
            else:
                return False
