'''
Crea una classe Quadrato con l'attributo lato e i metodi per calcolare il perimetro e l'area.
'''
class Quadrato:
    
    def __init__(self, lato):
        self.lato = lato

    def perimetro(self):
        perimetro = self.lato * 4
        print("Il perimetro del quadtrato è uguale a",perimetro)
    
    def area(self):
        area = self.lato * self.lato
        print("L'area è uguale a",area)


dom= Quadrato(int(input("Quanto misura il lato del quadrato?")))
dom.perimetro()
dom.area()