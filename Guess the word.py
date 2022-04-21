import random

list = ["jigar","mahek","aman","ratan","dipesh"]
word = random.choice(list)
turns = 5
guesses = ""                 # ✨✨ (❁´◡`❁)

print("   ## Guess the word game ## ")
print("Guess the characters:")

while (turns > 0):
    fail = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            fail += 1              # ✨✨ (❁´◡`❁)

    if fail == 0:
        print("YOU WIN")
        print("The word is",word)
        break

    guess = input("Guess a character:")
    guesses += guess

    if guess not in word:
        print("Incorrect guess of character")
        turns -= 1
        print("No.of turns left:", turns)
        if turns == 0:
            print("YOU LOSE")