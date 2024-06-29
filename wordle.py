import nltk
import random
from colorama import Fore, Style


words = nltk.corpus.words.words()

# Read words from the file
with open('word.txt') as word_file:
    word_list = word_file.readlines()

word_list = [word.strip() for word in word_list]

# Select a random word
randw = random.choice(word_list)
print(randw)

# Main game loop
while(True):
    x = input("Enter your guess: ")
    if x == randw:
        print("Wow you have gussed it right!!")
        break
    if x in words and len(x) == 5:
        for i in range(5):
            if x[i] == randw[i]:
                print(Fore.GREEN + x[i] + Style.RESET_ALL, end="")
            elif x[i] in randw:
                print(Fore.RED + x[i] + Style.RESET_ALL, end="")
            else:
                print(x[i], end="")
    else:
        print("Invalid word. Please enter a valid 5-letter word.")
    print()
