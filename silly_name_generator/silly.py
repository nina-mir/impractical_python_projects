import sys, random

print('Welcome to the name picker project!')

first = ("Nina 'Bonina'", 'Goat Jackson', "Tina 'O-Nina'", 'Cadillac Joe',
        'Shampoo Doug', 'Treebird')
last = ('Torabi', 'Schlect','Richtig', 'dortdorf', 'Nottoday',
            'MaybeLater')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input('Try again? Press Enter or n to quit. ')
    if try_again.lower() == 'n':
        break

input("press Enter to exit! ")
