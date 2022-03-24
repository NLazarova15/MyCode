import datetime as dt

# 1)
# today=dt.datetime.today()
# user_birth=dt.datetime(year=2022, month=5, day=14, hour=0) 
# time_diff=user_birth-today
# print(time_diff)

# 2)
today=dt.datetime.today().date()
# print(today)
user_birth=dt.datetime(year=2022, month=5, day=14).date() 
# print(user_birth)
time_diff=user_birth - today
print(time_diff)

