def main():
    vakken = {}
    vakken['Engels'] = int(8)
    vakken['Wiskunde'] = int(7)
    vakken["Aardrijkskunde"] = int(6)
    vakken["Kunst"] = int(9)
    vakken["Muziek"] = int(9)
    

    punten = vakken.values()

    gemiddelde = (sum(punten)/len(punten))

    print("Je gemiddelde cijfer is: ", gemiddelde, "Zou je het cijfer voor Aardrijkskunde willen veranderen naar een 8? ")

    vakken["Aardrijkskunde"] = int(input("Voer hier het nieuwe cijfer in: "))

    gemiddelde = (sum(punten)/len(punten))
    
    print("Je gemiddelde cijfer is nu weer up-to-date ",gemiddelde)
   

main()