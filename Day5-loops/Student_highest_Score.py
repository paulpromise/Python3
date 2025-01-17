Student_score = input("Enter the list of student score ")

print(type(Student_score))
#convert input data into list
Student_score = Student_score.split()

for n in range(0, len(Student_score)):
    Student_score[n] = int(Student_score[n])

print(type(Student_score[n]))

#print(max(Student_score))
#print(min(Student_score))
highest_score = 0

for score in Student_score:
    if score > highest_score:
        highest_score = score
    
print(f"highest score in the class is {highest_score}")


