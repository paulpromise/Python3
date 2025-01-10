""" Fruits = ["Banana", "Mango", "Apple", "Orange"]
a = [1, "mclean", True, [1, 4, "list"]]
b = [1, 3, 7, 10]
c = ["name_student" , ["promise", "paul", "Angela"]]

print(f"list{a} and {b}")

Name_favorite_color = list((1, 3, 5, 'apple' , 3.5)) """


States_of_America = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
    "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", 
    "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", 
    "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", 
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", 
    "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", 
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", 
    "New Mexico", "Arizona", "Alaska", "Hawaii"
]

# change the name of a specific item in the list
States_of_America[1]= "NewMclean City"
#print(States_of_America)

#Add item to the list
States_of_America.append("AmericanLand")

#Add multiple items to the list
States_of_America.extend(["AmericanLand", "Kedjebi", "Atakrom"])
#print(States_of_America)

#insect an item into the list
States_of_America.insert(0, "Jasikan")
#print(States_of_America)


#remove item from the list
States_of_America.remove("Atakrom")
print(States_of_America)

 

