import random

#my lists
easy_list = ["one", "dog", "cat"]
medium_list = ["aggressive", "imagine", "diverse"]
hard_list = ["onomatopoeia", "mischievous", "quiescence"]

#prompts user to choose a list
choose_list = input("to pick a list, type 'easy,' 'medium,' or 'hard' -> ")

#assigns list to word_lsit
if choose_list == "easy":
    word_list = easy_list
elif choose_list == "medium":
    word_list = medium_list
elif choose_list == "hard":
    word_list = hard_list
else:
    print("please type a proper list: 'easy,' 'medium,' or 'hard")
    choose_list = input("to pick a list, type 'easy,' 'medium,' or 'hard' -> ")
    #struggling with how to restart this loop after this point

#picks a random word from said list
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

#while the guess is incorrect, run specified steps until it is (correct)
while guess != word:
    print(check(guess, word))
    guess = input("type a word! -> ")
else:
    print("WOW! You guessed correctly! Congrats!")
