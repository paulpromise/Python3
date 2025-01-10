import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below this line 👇
print("Welcome to the rock, paper, and scissors game")
User_choice = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors ")

if not User_choice.isdigit() or int(User_choice) not in [0, 1, 2]:
    print("Invalid input! Please enter a number (0, 1, or 2). ")
    sys.exit()
else:
    User_choice = int(User_choice)



# Display the user's choice
game_image = [rock, paper, scissors]
print(game_image[User_choice])

""" 
if User_choice == 0:
    print(rock)
elif User_choice == 1:
    print(paper)
else:
    print(scissors) """

#Generate random number between 0 and 2
print("Computer Choice")
computer_choice = random.randint(0, 2)

game_image = [rock, paper, scissors]
print(game_image[computer_choice])


""" 
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors) """

if User_choice == 0 and computer_choice == 1:
    print("You loss!")
elif User_choice == 1 and computer_choice == 0:
    print("You Won!")
elif User_choice == 2 and computer_choice == 1:
    print("You Won!")
elif User_choice == 1 and computer_choice == 2:
    print("You loss!")
elif User_choice == 2 and computer_choice == 0:
    print("You loss!")
elif User_choice == 0 and computer_choice == 2:
    print("You Won!")
elif User_choice == computer_choice:
    print("Is a draw.")



