#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your Password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

number_letters = random.sample(letters, nr_letters)
num_symbols = random.sample(symbols, nr_symbols)
num_numbers = random.sample(numbers, nr_numbers)

all_gen_password = (number_letters + num_symbols +  num_numbers)

Password  = ''

for passwd in all_gen_password:
    Password += passwd


#Convert Password into a list
Password = list(Password)

#Reshuffle the password int the list
random.shuffle(Password)

#create a new variable to store the Password
New_Password = ""

#Use loop to put all the password togather and print it out 
for char in Password:
    New_Password += char


print(f"Your new password: {New_Password}")