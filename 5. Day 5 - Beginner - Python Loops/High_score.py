#dont chnge the code bellow:

student_scores = input("Input a list of some students  : ").split()

for n in range (0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

height_score =0
for score in student_scores:
    if score > height_score:
        height_score= score
print(f"The height score is : {height_score} ")












