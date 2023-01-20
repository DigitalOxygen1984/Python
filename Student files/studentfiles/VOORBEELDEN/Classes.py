class Student():
    klas = 5
    def __init__(self, naam):
        self.naam = naam
        self.adres= ''
        self.telefoonnummer = ''
    def layout(self):
        print('Student', self.naam, 'woont aan', self.adres)

s1 = Student('Jan')
s2 = Student('Piet')

# print(s1.klas)
# print(s2.klas)

# print(s1.naam)
# print(s2.naam)

# print(s1.adres)
# print(s2.telefoonnummer)

s1.adres = 'Hobbemakade 5'

# print(s1.adres)
# print(s2.adres)

print(s1.layout())
print(s2.layout())