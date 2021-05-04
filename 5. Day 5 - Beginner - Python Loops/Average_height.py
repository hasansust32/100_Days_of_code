#average height calculator

student_height = input("input a list of students height : ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)


total_height = 0
for height in student_height:
    total_height += height
print(total_height)

total_len = 0
for length in student_height:
    total_len += 1
print(total_len)

# total_height = sum(student_height)
# length= len(student_height)

average_height = total_height/ total_len

print(average_height)















