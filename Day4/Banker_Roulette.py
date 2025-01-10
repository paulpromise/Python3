import random
# Take names of all people sitting non the table
User_Names = input("Enter everyone's name sitting on the table\n ")

""" list_Names = ["Paul", "Promise", "Mclean" , "Etornam", "Angela"]
list_random = random.choice(list_Names)
print(list_random)"""


# convert the  names to list
Names = User_Names.split(',')
print(Names)


""" User_Name_length = len(Names)

print(User_Name_length)
Random_User = random.choice(Names)
print(Random_User)
print(f"{Random_User} is going to pay the bills")
 """

#Another Method

#Get the total number of items in the list
Num_Items = len(Names)

#Print the list 
print(Num_Items)

#Generate random numbers from the list items
random_choice = random.randint(0, Num_Items - 1)

#Print the random number generated from the list
print(random_choice)

Random_Person = Names[random_choice]
print(Random_Person, "is going to buy and pay the bill")