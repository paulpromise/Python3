
response = input("Do you want to play a game [y/n]: ").lower()

while response != "y" and response != "n":
    response = input("Do you want to play a game [y/n]: ").lower()

if response == "y":
    print("Welcome to a simple game")
    print("this is to test while loop")
else:
    print("Good bye! see you later!")


    