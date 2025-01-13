
student_hight = input("Enter the list of student hight ")
student_hight = student_hight.split()

total_sum = 0

for n in range(0, len(student_hight)):
    student_hight[n] = int(student_hight[n])

 #Using for loop to add items in list   
for num in student_hight:
    total_sum += num
print(total_sum)

Average_number = total_sum / len(student_hight)

print(round(Average_number))



#student_lenght = len(student_hight)


""" 
for n in range(0, student_lenght):
    student_hight[n] = int(student_hight[n])

total_hight = sum(student_hight)
Student_average = total_hight / student_lenght
print(round(Student_average))

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

print(student_heights[n])
#Write your code below this row 👇 """