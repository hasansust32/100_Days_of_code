#Age calculation


age = input("What is your current age ? :\n")

age = int (age)

year= 73- age
week = (73*52)- (age* 52)
days = (73*365 )- (age*365)

print(f"You have {year} year left, {week} week left, {days} days left")