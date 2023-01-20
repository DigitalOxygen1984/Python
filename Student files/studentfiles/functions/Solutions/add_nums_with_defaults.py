def add_nums(num1, num2, num3=0, num4=0, num5=0): # Datgeen wat tussen haakjes staat, is een parameter. De =0 achter de laatste 3 cijfers is een DEFAULT getal wat Python dan meegeeft, mochten  deze niet gebruikt worden
    total = num1 + num2 + num3 + num4 + num5
    print(num1, '+', num2, '+', num3, '+', num4, '+', num5, ' = ', total)

def main():
    add_nums(1, 2)
    add_nums(1, 2, 3, 4, 5)
    add_nums(11, 12, 13, 14)
    add_nums(101, 201, 301)

main()