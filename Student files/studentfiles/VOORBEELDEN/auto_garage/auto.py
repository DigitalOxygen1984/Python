class Auto():
    def __init__(self, merk):
        self.merk = merk
        self.snelheid = 0
        self.kilometerstand = 0
    def rijden(self):
        self.snelheid = 50
    def stoppen(self):
        self.snelheid = 0