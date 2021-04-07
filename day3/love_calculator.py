#lover calculator creation


print("Welcome to the love calculator : ")
name1 = input("What is your name ? : \n")
name2 = input("What is your lover name ?  : \n")

combine_namae = name1 + name2
combine_namae = combine_namae.lower()

t = combine_namae.count("t")
r = combine_namae.count("r")
u = combine_namae.count("u")
e = combine_namae.count("e")

true = t+r+u+e 

l = combine_namae.count("l")
o = combine_namae.count("o")
v = combine_namae.count("v")
e = combine_namae.count("e")

love= l+o+v+e

love_score = str(true) + str(love)

#print(f"your love score is {love_score} ")
# print ("love score is : " + love_score)

love_score = int(love_score)

if (love_score <= 10) or (love_score>= 90):
    print(f"Your love score is {love_score}. You go together like coke and mentos")
if (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}. You are alright together ")
else:
    print(f"your score is : {love_score} . You are not bad.")

