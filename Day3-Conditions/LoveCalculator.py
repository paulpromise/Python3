#A simple app to calculate love score between two individuals
#
print("""Love is a word that has a variety of different meanings within different contexts. It is generally defined as a strong affection for another person, be it maternal, sexual, or based on admiration, and is sometimes even extended to objects or even food. There are differences in the concept of love even between cultures and countries, making it difficult to arrive at a "universal" definition of love.""")

# Take user input from name1 and name2
print("Welcome to Love calculator")
name1 = input("What is your name?\n")
name2 = input("What is your Partner's name? \n")



""" 
#convert to lower case
name1_lower = name1.lower()
name2_lower = name2.lower()

#true_Love
t_count_name1 = name1_lower.count("t")
r_count_name1 = name1_lower.count("r")
u_count_name1 = name1_lower.count("u")
e_count_name1 = name1_lower.count("e")

name1_total_count = t_count_name1 + r_count_name1 + u_count_name1 + e_count_name1
#love

l_count_name1 = name1_lower.count("l")
o_count_name1 = name1_lower.count("o")
v_count_name1 = name1_lower.count("v")
e_count_name1 = name1_lower.count("e")


name1_total_love = l_count_name1 + o_count_name1 + v_count_name1 + e_count_name1
Total_Name1_Value = name1_total_count + name1_total_love

#Name2

#true_Love
t_count_name2 = name2_lower.count("t")
r_count_name2 = name2_lower.count("r")
u_count_name2 = name2_lower.count("u")
e_count_name2 = name2_lower.count("e")
#love

name2_total_count = t_count_name2 + r_count_name2  + u_count_name2 + e_count_name2

o_count_name2 = name2_lower.count("o")
l_count_name2 = name2_lower.count("l")
v_count_name2 = name2_lower.count("v")
e_count_name2 = name2_lower.count("e")

name2_total_love = l_count_name2  + o_count_name2 + v_count_name2 + e_count_name2 
Total_Name2_Value = name2_total_count + name2_total_love

#........................................

#Percentage calculation
Percentage_calculation = str(Total_Name1_Value) + str(Total_Name2_Value)
love_Score = int(Percentage_calculation)

if love_Score <= 10 or love_Score >= 90:
    print(f"Your score {love_Score}, You go togather like coke and mentos")
elif love_Score >= 40 or love_Score <= 50:
    print(f"Your score is {love_Score}, You are alright togather")
else:
    print(f"Your score is {love_Score}")



 """
#Another Method
both_Partner_names = name1 + name2
lower_case_string = both_Partner_names.lower()

print(both_Partner_names)

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

true_love = str(true) + str(love)

love_Score = int(true_love)



if (love_Score < 10) or (love_Score > 90):
    print(f"Your score {love_Score}, You go togather like coke and mentos")
elif (love_Score) >= 40 and (love_Score) <= 50:
    print(f"Your score is {love_Score}, You are alright togather")
else:
    print(f"Your score is {love_Score}")