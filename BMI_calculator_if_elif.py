weight = input("Enter Weight = ")
height = input("Enter Higth = ")
print(type(weight))
print(type(height))

bmi = (float(weight) / (float(height) ** 2))
print(type(bmi))
print("Your BMI = ", bmi)
if bmi <= 18.5:
    print("your underweight")
elif bmi >= 18.5 and bmi <= 25:
    print("Normal weight")
    else bmi >= 25:
    print("over weight")