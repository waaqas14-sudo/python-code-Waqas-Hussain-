#calculate  the BMI
#input weight (kg) and height(m)then calculate
weight=float(input("Enter the weight in kg:",))
height=float(input("Enter the height in metre:",))
BMI=weight/(height**2)
if BMI<18.5:
    print("underweight")
    elifBMI<30:
    print("normal weight")
else:
    print()