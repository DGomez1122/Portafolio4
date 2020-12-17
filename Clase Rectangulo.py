# Clase Rectangulo-

class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        
    def calcularArea(self):
        return self.base*self.altura

    def calcularPerimetro(self):
        return 2*(self.base+self.altura)

