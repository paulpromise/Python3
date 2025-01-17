
student_hight = input("Enter the list of student hight ")
#convert input data into list
student_hight = student_hight.split()



for n in range(0, len(student_hight)):
    student_hight[n] = int(student_hight[n])

 #Using for loop to add items in list   

Total_height = 0
for num in student_hight:
    Total_height += num
print(Total_height)

Average_number = Total_height / len(student_hight)

print(round(Average_number))



#student_lenght = len(student_hight)


""" 
#Using for loop and the range function
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