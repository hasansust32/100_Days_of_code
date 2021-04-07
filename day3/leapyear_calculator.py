#Enter a year you want to check !!!
#check the leapyear !!!



year = int(input("enter a year you want to check : "))

#okay this year is 2020

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year .")
        else:
            print("Not leap year .")
    else:
        print("This is leap year :")
else:
    print("This is not leap year. ")



