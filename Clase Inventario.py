#Clase Inventario.

class Inventario:
    lista=[]
    contador=0
    def __init__(self,Constructor):
        if Constructor=="Bebida" or Constructor=="Alimentos" or Constructor=="Ferreteria":
            self.Constructor=Constructor
            Inventario.contador+=1
        else:
            return "Error ha seleccionado un tipo no existente"
        
    def asignarInformacion(self):
        if self.Constructor=="Bebida":
            n=input("Ingrese el nombre del producto: ")
            if n=="":
                return "No ingresó ningún nombre"
            try:
                p=float(input("Ingrese el precio del producto: "))
            except:
                return "Error, el precio debe ser de tipo flotante"
            try:
                v=int(input("Ingrese el volumen del producto: "))
            except:
                return "Error, el volumen debe ser de tipo entero"
            Inventario.lista+=[[n,p,v]]
        if self.Constructor=="Alimentos":
            n2=input("Ingrese el nombre del producto: ")
            if n2=="":
                return "No ingresó ningún nombre"
            try:
                p2=float(input("Ingrese el precio del producto: "))
            except:
                return "Error, el precio debe ser de tipo flotante"
            try:
                ps=int(input("Ingrese el peso del producto: "))
            except:
                return "Error, el volumen debe ser de tipo entero"
            Inventario.lista+=[[n2,p2,ps]]
        if self.Constructor=="Ferreteria":
            n3=input("Ingrese el nombre del producto: ")
            if n3=="":
                return "No ingresó ningún nombre"
            try:
                p3=float(input("Ingrese el precio del producto: "))
            except:
                return "Error, el precio debe ser de tipo flotante"
            try:
                m=input("Ingrese el nombre del material: ")
            except:
                return "Error, el volumen debe ser de tipo string"
            Inventario.lista+=[[n3,p3,m]]
    def mostrarArticulo(self):
        nomb=input("ingrese el nombre del articulo: ")
        filas=0
        while filas<len(Inventario.lista):
            if Inventario.lista[filas][0]==nomb:
                print(Inventario.lista[filas])
                filas+=1
            else:
                filas+=1
    def mostrarInventario(self):
        return(Inventario.contador)
    
