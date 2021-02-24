'''
Elenca proprietà e metodi della classe Prodotto.
Definisci il metodo assegna prezzo alla classe Prodotto. 
'''
class Prodotto:
    def __init__(self, name, colour, material, use):
        self.name = name
        self.colour = colour
        self.material = material
        self.use = use

    def assegnazione_prezzo(self, price):
        self.price = price

    def informazioni(self):
        print("L'oggetto",self.name,",di colore",self.colour,",di",self.material,",che serve a",self.use,",")
        print("costa",self.price,"euro.")

p1 =  Prodotto("Tavolo","marrone chiaro","legno di betulla","arredo")
p1.assegnazione_prezzo(200)
p1.informazioni()
p2 =  Prodotto("Vaso","rosso","ceramica","soprammobile")
p2.assegnazione_prezzo(50)
p2.informazioni()