def main():
    zin = input('voer hier een zin in: ')
    print('U heeft de volgende zin ingevoerd: ', zin)
    nummer = int(input('voer hier nu een nummer tussen de 1 en 9 in: '))
    print('Uw ingevoerde nummer, staat gelijk aan de volgende letter:', (str.capitalize(zin[nummer-1])))

    

main()