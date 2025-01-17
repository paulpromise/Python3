import random

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
user_num = int(input("enter number "))

password = random.sample(symbols, user_num)
word = ''

for i in password:
   word += i

print(word)

