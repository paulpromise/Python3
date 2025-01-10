#A simple app to caculate BMI
# Asked the user to Enter their height and weight
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

Bmi = weight / (height ** 2)
FinalBMI = round(Bmi)

if FinalBMI <= 18:
    print(f"You BMI is {FinalBMI}, You are underweight!")

elif FinalBMI <= 25:
    print(f"You BMI is {FinalBMI}, You are Normal.")
elif FinalBMI <= 30:
    print(f"You BMI is {FinalBMI}, You are Overweight")
elif FinalBMI <= 35:
    print(f"You BMI is {FinalBMI}, You are Obese")
else:
    print(f"You BMI is {FinalBMI}, You are clinicaly obese")