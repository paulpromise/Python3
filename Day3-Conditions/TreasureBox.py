print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("""Welcome to Treasure Island!
Your mission is to find the treasure.""")

response = input('You\'re at a crossroad. Where do you want to go? Type "Left" or "Right": ').lower()
#response = User_response.lower()


# create a while loop to ask user to enter right or left if input is wrong

while response != "right" and (response != "left"):
        print("Invalid choice. Please type 'right' or 'left'")
        response = input('You\'re at a crossroad. Where do you want to go? Type "Left" or "Right": ').lower()


print()

if response == "right":
    print("You took the right path, but it leads to a dead end. Game Over!")

elif response == "left":
    response = input('You are at the edge of the water. Do you want to swim across or wait for the boat? Type "Swim" or "Wait": ').lower()

    print()
# create a while loop to ask user to enter wait or swim if input is wrong
    while response != "swim" and response != "wait":
        response = input("""You are at the edge of the water. Do you want to swim across or wait for the boat? Type "Swim" or "Wait": """)

    if (response == "swim"):
        print("You chose to swim, but unfortunately, the waters are too dangerous. Game Over!")

    elif response == "wait":
        print("You chose to wait, and a boat arrives to take you safely across. You proceed on your adventure!")
         
        print()

        response = input('You\'ve crossed the road and find three doors. One is red, one is blue, and one is yellow. Which door will you choose? Type "Red", "Blue", or "Yellow": ')

        if response.lower() == "red":
            print("You open the red door and find a room filled with fire. Game Over!")
        elif response.lower() == "blue":
            print("You open the blue door and enter a room full of beasts. Game Over!")
        elif response.lower() == "yellow":
            print("You open the yellow door and discover a treasure chest. Congratulations, you win!")
        else:
            print("Invalid choice. Please type 'Red', 'Blue', or 'Yellow'.")

    else:
        print("Invalid choice. Please type 'Swim' or 'Wait'.")




