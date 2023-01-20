# with gebruik ik om de opdracht meteen na uitvoering te sluiten

with open("../data/1880-boys.txt") as f:
    boys = f.read()

with open("../data/1880-girls.txt") as f:
    girls = f.read()

# Hier heb ik geen "with statement" gebruikt en heb ik de opdracht 'handmatig' gesloten
f2 = open("../data/girls-boys.txt","w")
f2.write(boys + "\n" + girls)
f2.close()