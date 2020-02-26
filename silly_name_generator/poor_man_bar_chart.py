"""
Practice project #2 of chapter.1 of Impractical Python Projects book

"""

from pprint import pprint
from collections import defaultdict

def main():
    """
    Creates a bar chart out of the frequency of letters used in the input text string
    and shows it using pprint function of pprint module using collections.defaultdict 
    data structure.
    """
    text = input('Please enter a text/sentence/paragraph! ')
    text = text.lower()

    d = defaultdict(list)

    for i in text:
        if i.isalpha and not i.isspace():
            d[i].append(i)

    pprint(d)

if __name__ ="__main__":
    main()