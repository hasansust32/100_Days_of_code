
#Treasure map creation 

row1 = ["😀 " , " 🙂 " ," 🙂"]
row2 = ["😥 " , " 😀 " ," 🙂"]
row3 = ["😡 " , " 😥 " , " 😀"]

map = [row1, row2, row3]

print(f"{row1} \n{row2}\n{row3} ")
position = input("where you want to put the treasures ? :")

horigental = int(position[0])
verticle = int(position[1])

map[verticle-1][horigental-1]="X"

# selected_row = map[verticle -1]
# selected_row [horigental -1 ] = "x"

print(f"{row1} \n{row2}\n{row3} ")