print("welcome to the rollar coster ride:  ")
height = int(input("What is your height in cm? : "))

if height >= 120:
    print("You can ride rollarcoster!")
    age = int (input("what is your age ? : "))
    photo =(input("Do you want to take photos ? Y or N  :  "))
    
    bill = 0


    if age < 12:
        bill = 5
    elif age < 18:
        bill = 7
    elif age >=45 and age<=55:
        print("Everything is okay. Your ride is free now ")
    else:
        bill = 12


    if photo== "Y":
        bill += 3
    else:
        bill +=  0

    print(f"Your total bill is {bill} ")   
    
    
    
    # if photo == "y":
    #     if age< 12:
    #         print("Please pay 8 dollar")
    #     elif age<=18:
    #         print("Please pay 10 dollar.")
    #     else:
    #         print("please pay 15 dollar. ")

    # else:
    #     if age< 12:
    #         print("Please pay 5 dollar")
    #     elif age<=18:
    #         print("Please pay 7 dollar.")
    #     else:
    #         print("please pay 12 dollar. ")




else: 
    print("Sorry , you can not ride: before you grew up !!!")

