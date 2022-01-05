# Refine the BMI program form the (last lab)
# Ask the user to enter his/her weight_in_kilogram and height_in_meters
# Now, the output of your program should be the BMI category, corresponding to the BMI index (given in next slide)


user_weit=float(input("Insert your weit in kilogram:"))
user_height=float(input("Insert your height in meter:"))
user_bmi=round(user_weit/(user_height*user_height), 2)
# print(f'BMI = {user_bmi}')
if user_bmi <= 18.5:
    print(f'BMI = {user_bmi}'', Category = Underweight')
if user_bmi >= 30:
    print(f'BMI = {user_bmi}'', Category = Obesity')
if user_bmi >= 18.5 and user_bmi<= 24.9: 
    print(f'BMI = {user_bmi}'', Category = Normal')
if user_bmi >= 25 and user_bmi<= 29.9: 
    print(f'BMI = {user_bmi}'', Category = Overweight')    