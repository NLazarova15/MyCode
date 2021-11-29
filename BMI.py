# Calculate my body mass index (BMI) 
# formula: BMI = W / (H*H)
# where:
# W = weight_in_kilogram
# H = height_in_meters
# the result rounded to 2 digits after the decimal point

h=1.6
w=60.0
bmi=round(w/(h*h), 2)
print(f'BMI= {bmi}')

# OR

# Calculate a body mass index (BMI) 
# formula: BMI = W / (H*H)
# where:
# W = weight_in_kilogram
# H = height_in_meters
# the result rounded to 2 digits after the decimal point
user_weit=float(input("Insert your weit in kilogram:"))
user_height=float(input("Insert your height in meter:"))
user_bmi=round(user_weit/(user_height*user_height), 2)
print(f'BMI = {user_bmi}')