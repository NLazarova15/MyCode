# Calculate a body mass index (BMI) 
# formula: BMI = W / (H*H)
# where:
# W = weight_in_kilogram
# H = height_in_meters
# the result rounded to 2 digits after the decimal point

# dict={}
def get_user_data(user_name, user_weit, user_height):
    """retrieves user data from the command line"""
    
    result={'name': user_name, 
    'weit':user_weit,
    'height': user_height,
    'BMI':round(user_weit/(user_height*user_height), 2)}
    print(result)
    return result

name=input('Insert your name: ')
weit = float(input("Insert your weit in kilogram:"))
height=float(input("Insert your height in meter:"))

get_user_data(name, weit, height)


# return round(user_weit/(user_height*user_height), 2)
# print(f'BMI = {round(user_weit/(user_height*user_height), 2)}')
