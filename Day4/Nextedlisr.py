box1 = ["null1", "null2", "null3"]
box2 = ["null4", "null5", "null6"]
box3 = ["null7", "null8", "nulll9"]

all_boxes = [box1, box2, box3]
#print(f" {box1}\n {box2}\n {box3}")
possition = input("Which box will you like to insect item  " )

column = (int(possition[0]) - 1)
row = (int(possition[1]) - 1)

all_boxes[column][row] = "item"
print(f"{box1} {box2} {box3}")
#print(f" {box1}\n {box2}\n {box3}")

print(type(column))
print(type(row))

