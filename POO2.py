import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        area = math.pi * self.raio**2
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.raio
        return perimetro

# Criando uma instância da classe Circulo
circulo1 = Circulo(5)
area = circulo1.calcular_area()
perimetro = circulo1.calcular_perimetro()
print(f"Área: {area}, Perímetro: {perimetro}")