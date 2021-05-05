#password generation python file is here.
import random

letter = [ 'a', 'b',  'c', 'd', 'e' , 'f' , 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r' ,'s', 't', 'u', 'v', 'w', 'x', 'y', 'z',  
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

numbers = ['0' ,'1', '2', '3', '4', '5', '6', '7', '8', '9', '10' ]
symbols = ['!', '@', '$', '%', '^', '&', '*', '(', ')', '+']


print("Welcome to the pypassword Generator!")

nr_letter = int(input("How many letters would you like in your password ? : \n"))
nr_symbol= int (input("How many symbols would you like  ? : \n"))
nr_numbers = int (input("How many numbers would you like ? : \n"))


password_list = []

for char in range (1, nr_letter+1 ):
    password_list += random.choice(letter)
for char in range (1, nr_symbol+1):
    password_list += random.choice(symbols)
for char in range (1, nr_numbers+1):
    password_list += random.choices(numbers)


print(password_list)

for char in password_list:
    random.shuffle(password_list)

print(password_list)

password = " "
for char in password_list:
    password+= char

print(password)












