import math

# Clase Circulo.

class Circulo:
    def __init__(self,radio):
        self.radio=radio
    def calcularArea(self):
        return math.pi*self.radio**2
    def calcularPerimetro(self):
        return 2*math.pi*self.radio
