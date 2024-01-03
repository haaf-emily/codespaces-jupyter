import random

print("hangman in python")
words= 'Hund Gold Auto Rose Kind'.split( )
foundletters=[]
userinput=""
choiceword= random.choice(words)

# in print can use only parameter print(" ", end='_')
# print the letter numbers for the word

for letters in choiceword:
    print(" ", end='_')
    foundletters.append('_')

while userinput != "bye":
    for output in foundletters:
        print(output, end=' ')
    print()
    userinput = input("Ihr Vorschlag: ")
    for letters in choiceword:
        if letters.lower() == userinput.lower():
            print ("hit")
