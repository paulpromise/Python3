#create a program that checks if a number is old or not

#create a variable for number
number = int(input("Which number do you want to check? "))

if number % 2 != 0:
    print("Not Even Number!")
else:
    print("This is an even number")