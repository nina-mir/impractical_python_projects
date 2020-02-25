
def isVowel(x):
    vowels = ['a','o','u','e','i']
    flag = False
    for i in vowels:
        if x.lower() == i:
            flag = True
            break
    return flag


print("this code will conver any English word into its pig Latin equivalent!")
word = input("Enter a word: ")

if isVowel(word[0]):
    translated = word[1:].lower()
    print("{}{}{}".format(translated.capitalize(),word[0].lower(),'ay' )) 