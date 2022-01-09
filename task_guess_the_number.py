#The Python program, implementing the "Guess the number" game
#The program will "think" of a number using the random module

# user input
user_guess=int(input("Insert your gess from 1 to 10:  "))

# mashine number
from random import randint
machine_number = randint(1,10)
print("machine_number={}".format(machine_number))

if 1 <= user_guess <=10:
    if user_guess==machine_number:
        print("Congratulation - you winn!")
    elif user_guess <= machine_number:
        print("Your guess is less than my number. Try again!")
    elif user_guess >= machine_number:
        print("Your guess is greater than my number. Try again!")
else:
    print("Your guess is out of range")





