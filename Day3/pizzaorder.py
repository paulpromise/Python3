#A simple program to order pizza

pizza_price  = 0
extral_pepproni = 0
extral_cheese = 0
Total_bill = 0

print("Welcome to Python order Deliveries!")
print("Small pizza: 15$")
print("Medium pizza: 25$")
print("Large pizza: 20$")
print()

# User Input for Pizza size
size = input("What size of pizza do you want? (S, M or L)  ").lower()
print()

if size == "s":
    Total_bill = 15

    # User input for extral   cheese
    print("Extral cheese for small size: +1$")
    extral_cheese = input("Do you want extral chesse (Y or N)  ").lower()

    if extral_cheese == "y":
        Total_bill += 1

    print()
    #input for pepproni small size
    print("pepperroni for smaill pizza: +2$")
    extral_pepproni = input("Do you want pepperoni (Y or N) ").lower()


    if extral_pepproni == "y":
       Total_bill += 2
    print(f"Oder Total: ${Total_bill}")
    
    
elif size == "m":
    Total_bill = 25

    # User input for extral   cheese
    print("Extral cheese for Medium and large size: +2$")
    extral_cheese = input("Do you want extral chesse (Y or N)  ").lower()

    print()
    if extral_cheese == "y":
        Total_bill += 2

    #input for pepproni medium size

    print("pepperroni for medium or large pizza: +3$")
    extral_pepproni = input("Do you want pepperoni (Y or N) ").lower()

    if extral_pepproni == "y":
        Total_bill += 3

    print(f"Oder Total: ${Total_bill}")


elif size == "l":
    pizza_price = 30
    Total_bill = pizza_price

    # User input for extral cheese
    print("Extral cheese for Medium and large size: +2$")
    extral_cheese = input("Do you want extral chesse (Y or N)  ").lower()
    print()
    if extral_cheese == "y":
        Total_bill += 2
    

    print("pepperroni for medium or large pizza: +3$")
    extral_pepproni = input("Do you want pepperoni (Y or N) ").lower()

    if extral_pepproni == "y":
        Total_bill += 3

    print(f"Oder Total: ${Total_bill}")


else:
    print("invalid input! Please try again")


#...............................................................









