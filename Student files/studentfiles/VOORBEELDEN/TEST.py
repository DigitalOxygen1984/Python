aantal_namen = 0
namen = []

while True:
    ingegeven_namen = input("voer een naam in: ")
    namen.append(ingegeven_namen)

    
    if ingegeven_namen == "":
            print(f"aantal namen {aantal_namen}")
            namen.remove('')
            
            break

    aantal_namen += 1

for naam in namen:
    print(naam, end=', ')
