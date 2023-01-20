from auto import *
from auto_garage import *
import datetime

auto1 = Auto('Audi')
auto2 = Auto('Volkswagen')
auto1.apk_keuringsdatum = datetime.datetime.now()
auto1.kilometerstand = 70000
garage = Garage()

garage.bepaalOnderhoud(auto1)



# print('de APK keuringsdatum was', auto1.apk_keuringsdatum)

# print(auto1.merk, auto1.snelheid)
# print(auto2.merk, auto2.snelheid)

# auto1.rijden()

# print(auto1.merk, auto1.snelheid)
# print(auto2.merk, auto2.snelheid)

# auto1.stoppen()

# print(auto1.merk, auto1.snelheid)
# print(auto2.merk, auto2.snelheid)

