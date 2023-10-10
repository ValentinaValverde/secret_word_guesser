import random

# word_list = ["crunk", "hype", "phat", "pumped"]


easy_list = ["one", "dog", "cat"]
medium_list = ["aggressive", "imagine", "diverse"]
hard_list = ["onomatopoeia", "mischievous", "quiescence"]





choose_list = input("to pick a list, type 'easy,' 'medium,' or 'hard' -> ")

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
