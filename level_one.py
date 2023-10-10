#Create an input loop that asks for a letter and confirms whether that letter exists in the chosen word or not on each round. 
#Once the whole word has been revealed, you win the game.

word = "crunk"
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
