# Calculate a body mass index (BMI) 
# formula: BMI = W / (H*H)
# where:
# W = weight_in_kilogram
# H = height_in_meters
# the result rounded to 2 digits after the decimal point


def validate_name():
    name=input('Insert your name: ')

    while len(name)<=2:
        # print(len(name))
        print('User name must be at least 2 characters long')
        name=input('Insert your name: ')
        continue
    # print(name)
    return name 

def validate_weight():
    weight=float(input("Insert your weit in kilogram:"))
    
    while weight <= 5 or weight >=300:                  
        # print(weight)
        print("User's weight must be in the range: [5 - 300]")
        weight=float(input("Insert your weit in kilogram:"))
        continue
    # print(weight)
    return weight


def cm_to_meters(cm):
	# converts centimetres to meters
        print(cm)
        return float(cm/100)
	
def validate_height():
    height=int(input("Insert your height in centimeter:"))

    while height <= 50 or height >=250:                  
        # print(height)
        print("User's height must be in the range: [50 - 250]")
        height =int(input('Insert your height in centimeter: '))
        continue
    # print(height)
    return cm_to_meters(height)

def calc_BMI_category(w,h):
	# Calculates the BMI category
    user_bmi=round(w/(h*h), 2)
    return user_bmi


def print_results(user_bmi):
	
    if user_bmi <= 18.5:
        print(f'BMI = {user_bmi}'', Category = Underweight')
    if user_bmi >= 30:
        print(f'BMI = {user_bmi}'', Category = Obesity')
    if user_bmi >= 18.5 and user_bmi<= 24.9: 
        print(f'BMI = {user_bmi}'', Category = Normal')
    if user_bmi >= 25 and user_bmi<= 29.9: 
        print(f'BMI = {user_bmi}'', Category = Overweight') 

 

def get_user_data():
    name=validate_name()
    height=validate_height()
    weight=validate_weight()
    user_bmi=calc_BMI_category(weight, height)
    
    print_results(user_bmi)
    
    result= {
        'name': name,
        'weit':weight,
        'BMI':user_bmi
    }
    print(result)
    return print(result.items())
