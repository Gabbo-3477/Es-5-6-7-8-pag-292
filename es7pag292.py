'''
Elenca proprietà e metodi della classe Motociclo.
'''
class Motociclo:
    
    def __init__(self, modello, colore, velocita_massima, accelerazione_massima, prezzo):
        self.modello = modello
        self.colore = colore
        self.velocita_massima = velocita_massima
        self.accelerazione_massima = accelerazione_massima
        self.prezzo = prezzo
    
    def informazioni(self):
        print("Il motociclo del modello",self.modello,"che costa",self.prezzo,"euro, è di colore",self.colore,".")
        print("Può raggiungere la velocita massima di",self.velocita_massima,"km/h e può raggiungere l'accelerazione massima di",self.accelerazione_massima,"m/s^2.")

modello = input("Inserire modello del motociclo: ")
colore = input("Inserire colore: ")
velocita_massima = int(input("Inserisci velocità massima (Esprimere la misura in km/h) :"))
accelerazione_massima = int(input("Inserire accellerazione massima(Esprimere la misura in m/s^2) :"))
prezzo = int(input("Inserire prezzo: "))
m1 = Motociclo(modello, colore, velocita_massima, accelerazione_massima, prezzo)
m1.informazioni()