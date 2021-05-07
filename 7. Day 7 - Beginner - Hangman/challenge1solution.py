#Hangman solution in python 

word_list = ["ardvark" , "baboon" , "camel"]

import random

chosen_word = random.choice(word_list)

# print(chosen_word)

guess = input("guess a world : ").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")








