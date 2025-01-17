#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your Password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""



for letter in range(0, nr_letters):
    password += random.choice(letters)
print(password)


#Use a for loop to generate random  password
for number in range(0, nr_numbers):
    password += random.choice(numbers)
print(password)

for symbol in range(0, nr_symbols):
    password += random.choice(symbols)
print(password)

#convert password string into list
password_list = list(password)

#convert back into password
print(password_list)
random.shuffle(password_list)
print(password_list)

New_Password = ''

for char in password_list:
    New_Password += char
print(New_Password)


#
# for char in range(1, nr_letters + 1):
#    password += random.choice(letters)
#
#print(password)
# 
#
#    password += random.choice(letters)
#    print(char)
#print(password)