#The Python program, implementing the "Guess the number" game
#The program will "think" of a number using the random module
# The user now will have 5 tries to guess.

i=1
# while i <=5:  # while variant
for i in range(1,6):
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
    # i=i+1    # while variant
if user_guess!=machine_number:
    print("You Loss! My number was " f'{machine_number}')
