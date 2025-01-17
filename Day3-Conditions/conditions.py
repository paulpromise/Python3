#Roller costa game
print("Welcome to the roller coster!")
height = int(input("What is your height in CM? "))

if height >= 120:
    print("you can ride the roler coster")
    Age = int(input("What is your age? "))
    if Age < 12:
        print("Please pay 5$")
    elif Age <= 18:
        print("Please pay 7$")
    else:
        print("Please pay 22$")
else:
    print("Am Sorry you can't ride! Goodbye!")