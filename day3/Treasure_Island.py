#treasure island puzzel:

print("welcome to the treasure island:")
print("Your mission is to find out the treasure.")
print("lets go \n")

step1 = input("You are at a cross road. Where do you want to go? \n Type 'left' or 'right'  : ")
if step1 == "left":
    step2 = input("You came to a a lake.  There is a island in the lake.\n Type 'wait' to waiting for a boat or \ntype 'swim' to swiming in the lake  : ")
    if step2 == "wait":
        step3= input("You arrived at the island unharmed. There is a house with three doors. \n Which door you want to chose?? \n Type 'red' or 'yellow'  or 'blue' ")
        if step3== "yellow":
            print("You are welcome. You win the game")
        else:
            print("You are in the 3rd hole. Game Over. ")

    else:
        print("You are in the 2nd hole. Game Over. ")


else:
    print("You are in the hole. Game Over. ")




