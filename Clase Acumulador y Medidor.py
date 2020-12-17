#Clase Acumulador y Medidor.

#Acumulador
class Acumulador:
        def __init__(self):
                self.valor=0
        def tipo(self):
                return ("Acumulador")
        def actualizador(self, valor):
                self.valor+=valor
                return self.valor
        def mostrar(self):
                return self.valor
        def reset(self):
                self.valor=0
                return self.valor
#Medidor
class Medidor(Acumulador):
        def tipo(self):
                return ("medidor")
        def arriba(self):
                self.valor+=1
                return self.valor
        def abajo(self):
                self.valor-=1
                return self.valor
            
