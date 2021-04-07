#pizza order app

print("welcome to python pizza delevary app !! ")

size = input("What  is your pizza size ? S, M or L ? : ")
pepperony = input("Do you want pepperony ?? Y or N  ? :")
chese = input("Do you want extra chese ? Y or N : ")

bill = 0

if size == "S":
    bill += 15
if size == "M":
    bill += 20
if size == "L":
    bill += 25

if pepperony == "Y":
    if size== "S":
        bill +=2
    else:
        bill += 3
else: 
    bill==0

if chese == "Y":
    bill += 1


print(f"Your total  Bill is {bill} ")





