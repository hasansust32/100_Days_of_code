print("welcome to the rollar coster ride:  ")
height = int(input("What is your height in cm? : "))

if height >= 120:
    print("You can ride rollarcoster!")
else: 
    print("Sorry , you can not ride: before you grew up !!!")




#nested loop statement : 

print("welcome to the rollar coster ride:  ")
height = int(input("What is your height in cm? : "))

if height >= 120:
    print("You can ride rollarcoster!")
    age = int(input("what is your age ? : "))
    if age<= 18:
        print("please pay 18 dollar .")
    else: 
        print("please pay 25 dollar. ")
else: 
    print("Sorry , you can not ride: before you grew up !!!")


# possibility are given bellow:
# <12 $5 
# 12-18 pay $7
# >18 pay $ 12


#nested loop statement : 

print("welcome to the rollar coster ride:  ")
height = int(input("What is your height in cm? : "))

if height >= 120:
    print("You can ride rollarcoster!")
    age = int(input("what is your age ? : "))
    if age< 12:
        print("please pay 5 dollar.")
    elif age<=18:
        print("Please pay 7 dollar.")
    else: 
        print("please pay 12 dollar. ")
else: 
    print("Sorry , you can not ride: before you grew up !!!")












