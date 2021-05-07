word_list = ["ardvark" , "baboon" , "camel"]

import random

chosen_word = random.choice(word_list)
world_length = len(chosen_word)

end_of_game = False
lives = world_length


# print(chosen_word)

# guess = input("guess a world : ").lower()

# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print("wrong")

print(f'The solution is {chosen_word}')



display = []
for _ in range (world_length):
    display += "_"
print(display)

guess = input("Guess a letter : \n").lower()



while not end_of_game:
    guess = input("Guess a letter : \n").lower()

    
    for position in range (world_length):
        letter = chosen_word[position]
        print(f'Current position :{position} \n  current letter: {letter} \n Guessed letter : {guess} ')
        if letter == guess:
            display[position]= letter


    print(display)

if "_" not in display:
    end_of_game= True
    print("You win")
