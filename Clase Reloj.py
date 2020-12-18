#Clase Reloj.

class reloj:
     minutos=58
     horas=10
     def __init__(self,tipo):
          self.indice="AM"
          self.tipo=tipo
     def mostrar(self):
          if self.minutos<10:
               print("La hora y minutos que marca el reloj es:", reloj.horas,"con","0",reloj.minutos,"minutos",self.indice)
          else:
               print("La hora y minutos que marca el reloj es:", reloj.horas,"con",reloj.minutos,"minutos",self.indice)
               
     def AvanzarMinutos(self):
          if reloj.minutos==59:
               reloj.minutos=0
               reloj.horas+=1
          reloj.minutos+=1
     def AvanzarHoras(self):
          
          if reloj.horas>12:
               self.indice="PM"
          if reloj.horas>24:
               reloj.horas=1
               self.indice="AM"
          reloj.horas+=1
     def set(self):
          minn=int(input("Indique los minutos:"))
          hor=int(input("Indice la hora:"))
          indi=input("indice:")
          reloj.horas=hor
          reloj.minutos=minn
          self.indice=indi
