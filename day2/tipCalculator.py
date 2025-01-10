print("Welcome to the tip calculator.")
bill = float((input("What was the total bill? $")))
tip = int(input("What percentage tip will you like to give? 10, 12, 15?  "))

#Calculate the percentage tip given
tip /= 100

#Add percentage tip to the bill
bill += bill * tip
people = int(input("How many people to split the bill? "))

#Calculate the bill a person should pay
bill_per_person = bill / people

#round final amount to two decimal places
final_amount = round(bill_per_person, 2)

#round to exwctly two decimal places
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person will pay: ${final_amount}")
