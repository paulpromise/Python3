import random

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
user_response = int(user_response)
print(type(user_response))

if user_response == 0:
    print(rock)
elif user_response == 1:
    print(paper)
elif user_response == 2:
    print(scissors)
else:
    print("Input not valid!")

#Generate random number between 0 and 2
random_num = random.randint(0, 2)

if random_num == 0:
    print(rock)
elif random_num == 1:
    print(paper)
else:
    print(scissors)




