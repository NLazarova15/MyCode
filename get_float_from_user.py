def get_float_from_user(msg):
    try:
        user_in=float(input(msg))

    except ValueError as e:
        print("You did not enter a number!" )
    except KeyboardInterrupt:
        print("\n***Oops, something went wrong! Try again!\n")
    else:
        # print(user_in)
        return user_in

def user_data():
    user_number = get_float_from_user("***Enter a number, please!   ")
    user_height = get_float_from_user("I need to know your height in centimetres: ")
    user_weight = get_float_from_user("And your weight in kilograms: ") 
     
    try:
        print("Your height is: {:5.2f}cm. and you weight {:.2f}kg.".format(user_height, user_weight)) 
    except:
        print("\n***Oops, something went wrong! Try again!\n")

user_data()