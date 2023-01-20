_getal = 10 # Globale variabele (omdat deze NIET in een functie staat)

def say_hello():
    your_name = input("What is your name? ") # Lokate variabele (Omdat deze IN de functie say_hello staat)
    insert_separator()
    print("Hello, ", your_name, "!", sep="")

def insert_separator():
    print("===")
    getal = 20 # Getal 20 overruled nu de global variabele, omdat deze in de functie staat
    global _getal # Door 'global getal te gebruiken en daarna weer de variabele 'getal' aanspreekt, pakt hij wel weer de globale variabele
    print(_getal)

def recite_poem():
    print("How about a Monty Python poem?")
    insert_separator()
    print("Much to his Mum and Dad's dismay")
    print("Horace ate himself one day.")
    print("He didn't stop to say his grace,")
    print("He just sat down and ate his face.")

def say_goodbye():
    print("Goodbye!")

def main():
    say_hello()
    insert_separator()
    recite_poem()
    insert_separator()
    say_goodbye()

main()