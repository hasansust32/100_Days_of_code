#Welcome to the tip calculator
#What was the total bill ? $124.54
#How many people to split the bill ? 5
#What percentage tip would you like to give ? 10 12 or 15?
#Each person should pay : $27.9


print("Welcome to the tip calculator")
bill = input("What was the total bill ? :")
tip = input("What Percentage tip would you like to give ? 10, 12 or 15 ? : ")
people = input("How many people to split the bill? :")

bill= float(bill)
tip= float(tip)
people = int(people)


total_tip = (bill* tip/100)
total_bill = bill + total_tip

cost= (total_bill/ people)
cost= round(cost , 2)

message= f"Each person should pay: {cost} "

print(message)



