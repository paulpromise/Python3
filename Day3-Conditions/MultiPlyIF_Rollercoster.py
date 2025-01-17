#Roller costa game
print("Welcome to the roller coster!")
height = int(input("What is your height in CM? "))
bill = 0

if height >= 120:
    print("you can ride the roler coster")
    Age = int(input("What is your age? "))
    if Age < 12:
        bill = 5
        print(f"Please tickets price is {bill}$")
    elif Age <= 18:
        bill = 7
        print(f"Please tickets price is {bill}$")
    elif Age >= 45 and Age <= 55:
        print("Everything is going to be okay, Have a free ride on us!")
    else:
        bill = 12
        print(f"Please tickets price is {bill}$")
        
    wants_photo = input("Do you want photo? (Y or N)  ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
    print(f"Your final bill is {bill}$")


else:
    print("Am Sorry you can't ride! Goodbye!")