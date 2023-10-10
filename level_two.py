#Let's start using some of those cool data structures!
#create a data structure that can hold a series of words, 
#and let the game randomly select a word at the beginning of the game.

import random

word_list = ["crunk", "hype", "phat", "pumped"]
word = random.choice(word_list)
guess = input("type a word! -> ")

# function to check string
def check(guess, word):
    result = []
    for x in word:      #otherwise, "for each letter in word"
        if x in guess:
            result.append(x)
        else:
            result.append("")
    return result


while guess != word:
    print(check(guess, word))
    guess = input("type a word! -> ")
else:
    print("WOW! You guessed correctly! Congrats!")