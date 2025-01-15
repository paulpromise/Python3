#create a fizzbuzz game using loops

for num_item in range(1, 101):
    #check if the number can be divided by 3 and 5 and print fizzbuzz
    if (num_item % 3 == 0) and (num_item % 5 == 0):
       print("fizzbuzz")
    #check if the number can be devided by 5 and print buzz
    elif (num_item % 5 == 0):
        print("buzz")
     #check if the number can be devided by 3 and print fizz
    elif (num_item % 3 == 0):
        print("fizz")
    #print the rest of the number
    else:
        print(num_item)
 


