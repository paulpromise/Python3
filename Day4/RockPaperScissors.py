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
user_response = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors ")

if not user_response.isdigit() or int(user_response) not in [0, 1, 2]:
    print("Invalid input! Please enter a number (0, 1, or 2). ")
    sys.exit()
else:
    user_response = int(user_response)

# Display the user's choice
if user_response == 0:
    print(rock)
elif user_response == 1:
    print(paper)
else:
    print(scissors)

#Generate random number between 0 and 2
random_num = random.randint(0, 2)

if random_num == 0:
    print(rock)
elif random_num == 1:
    print(paper)
else:
    print(scissors)

if user_response == 0 and random_num == 1:
    print("You loss!")
elif user_response == 1 and random_num == 0:
    print("You Won!")
elif user_response == 2 and random_num == 1:
    print("You Won!")
elif user_response == 1 and random_num == 2:
    print("You loss!")
elif user_response == 2 and random_num == 0:
    print("You loss!")
elif user_response == 0 and random_num == 2:
    print("You Won!")
elif user_response == random_num:
    print("Is a draw.")



