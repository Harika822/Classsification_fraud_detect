import random
#import pandas as pd
#word_list=pd.read_csv("words.csv")
from words import word_list
print("Starting a game of Hangman...")
#validation for incorrect attempts
while True:
    k = input("How many incorrect attempts do u want?[1-25] ")
    try:
        tries = int(k)
        if tries > 25:
            raise Exception
        if tries < 26:
            print(tries)
            break
    except:
        print(k, 'is not an integer between 1 and 25')
#validation for word length
y=int(input("enter min range[4-16]"))
z=[w for w in word_list if len(w)>=y]
#word choosing
word = random.choice(z)
word_completion="*"*len(word)
guessed = False
guessed_letters = [' ']
print("Selecting a word...")
#main code
while not guessed and tries>0:
    print(word_completion)
    print("Attempts remaining:", tries)
    print("Previous Guessed:",guessed_letters[-1])
    guess=input("Choose the letter: ")
    if len(guess)==1 and guess.isalpha():
        if guess in guessed_letters:
            print("You already guessed the letter", guess)
            print('\n')
        elif guess not in word:
            print(guess, "is not in the word.")
            print("\n")
            tries -= 1
            guessed_letters.append(guess)
        else:
            print(guess, "is in the word!")
            print("\n")
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "*" not in word_completion:
                guessed = True
    elif len(guess) > 1 or guess.isnumeric():
        print('Not a valid guess')
        tries -= 1
        print('\n')
if guessed==True:
    print("Congrats, you guessed the word")
else:
    print("Ran out of tries")

