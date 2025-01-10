 #Creat a progrM that checks for a leep year
year = int(input("Which year do you want to check? "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leep Year")
        else:
            print("Not Leep")

    else:
        print("Leep Year")
else:
    print("Not Leep")