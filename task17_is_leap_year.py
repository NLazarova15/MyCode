## Task Is a Leap year?

# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)

def leap_year(year_val):
    if year_val%4==0 and year_val%400==0:
        print(f"{year_val} is a leap year")
    elif year_val%100!=0 and year_val%4==0:
        print(f"{year_val} is a leap year")
    else:
        print(f"{year_val} is a common year")

user_year=int(input("Enter a year:   "))
leap_year(user_year)
