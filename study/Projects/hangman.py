import random

print("hangman in python")
words= 'Hund Gold Auto Rose Kind'.split( )
foundletters=[]
userinput=""
choiceword= random.choice(words)

# in print can use only parameter print(" ", end='_')
# print the letter numbers for the word

for letters in choiceword:
    foundletters.append('_')

while userinput != "bye":
    for output in foundletters:
        print(output, end=' ')
    print()
    userinput = input("Ihr Vorschlag: ")
    
    # Serche for letters hits
    x=0
    for letters in choiceword:
        if letters.lower() == userinput.lower():
            print("hit")
            foundletters[x]= letters
        x+=1
    print()
    # Check if won or lost
    if '_' in foundletters:
        tryfail= 7
        tryfail= tryfail- 1
        if tryfail == 0:
            print("Lost! No more tries left")
            break
    else:
        print("You won")
        break
