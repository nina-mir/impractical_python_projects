"""
Generates funny first and last names from 2 sepearte lists randomly.
1st project of the book of Impractical Python Projects.

"""

import sys
import random

def main():
    """
    Choose a name at random from two lists to print to screen in a loop
    untill the user quits.
    """

    print('Welcome to the name picker project!')
    first = ("Nina 'Bonina'", 'Goat Jackson', "Tina 'O-Nina'", 'Cadillac Joe',
             'Shampoo Doug', 'Treebird')
    last = ('Torabi', 'Schlecht', 'Richtig', 'dortdorf', 'Nottoday',
            'MaybeLater')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input('Try again? Press Enter or n to quit. ')
        if try_again.lower() == 'n':
            break

    input("press Enter to exit! ")

if __name__ == "__main__":
    main()
