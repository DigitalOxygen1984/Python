from voertuig import Voertuig

class Auto(Voertuig):
    def __init__(self, merk):
        self.kenteken=''
        self.merk = merk
        self.apk_keuringsdatum = ''
    def rijden(self):
        self.snelheid = 50
    def stoppen(self):
        self.snelheid = 0