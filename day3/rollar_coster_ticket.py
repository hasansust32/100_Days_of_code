print("welcome to the rollar coster ride:  ")
height = int(input("What is your height in cm? : "))

if height >= 120:
    print("You can ride rollarcoster!")
    age = int (input("what is your age ? : "))
    photo =str(input("Do you want to take photos ? y/n  :  "))
    

    if photo == "y":
        if age< 12:
            print("Please pay 8 dollar")
        elif age<=18:
            print("Please pay 10 dollar.")
        else:
            print("please pay 15 dollar. ")

    else:
        if age< 12:
            print("Please pay 5 dollar")
        elif age<=18:
            print("Please pay 7 dollar.")
        else:
            print("please pay 12 dollar. ")




else: 
    print("Sorry , you can not ride: before you grew up !!!")

