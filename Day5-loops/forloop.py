
#create a list of fruits
# For Loop on List
# Creating a list of fruits
fruits = ["Apple","Banana","Orange","Mango","Grape","Pineapple","Strawberry","Blueberry" "Watermelon","Peach","Pear","Cherry","Kiwi","Papaya","Pomegranate","Lemon","Lime","Raspberry","Blackberry","Coconut"]

#use loop to print all elements in fruits
#for fruit in fruits:
    #print(fruit)

#create a loop that convert the loop item into a list
fruit_list = ""
for i in fruits:
    fruit_list = fruit_list + " " +  i
print(fruit_list.split())
