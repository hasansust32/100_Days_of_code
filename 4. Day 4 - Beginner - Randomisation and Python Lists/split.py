import random
#split string method 

nameAsCSV = input("Give me everybody's name separated by comma :")
names = nameAsCSV.split(", ")
print(names)

strlen = (len(names))
randigit = random.randint(0, strlen-1)
ranname= names[randigit]

print(f" {ranname} will pay the bill. ")



