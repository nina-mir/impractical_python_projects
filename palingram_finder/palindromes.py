"""Find panlindromes (letter palingrams) in dictionary file."""
import load_dictionary as ldict
eng_dict = ldict.load('/home/nina/Impractical_Python_Projects/env/palingram_finder/2of4brif.txt')
palindromes = list()

for word in eng_dict:
    if len(word) > 1 and word == word[::-1]:
        palindromes.append(word)

print("\nNumber of palindromes founs: {}".format(len(palindromes)))
print(*palindromes, sep='\n')