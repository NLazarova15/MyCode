import datetime as dt

#  1) How days are to your next birthday?
# def next_birthday():
#     user_next_birth=dt.datetime.strptime(input("Insert your next birthday: dd.mm.YYYY  "), '%d.%m.%Y').date()
#     today=dt.datetime.today().date()
#     time_diff=user_next_birth - today
#     print(f'{time_diff.days} days have to your next birtday')

# next_birthday()

# 2)  When were you born? How days are to your next birthday?
def user_next_birth():
    user_birth=dt.datetime.strptime(input("Insert your birthday: dd.mm.YYYY  "), '%d.%m.%Y').date()
    # print(user_birth)
    user_dt_m = user_birth.month  
    user_dt_d = user_birth.day                   
    
    today=dt.datetime.today().date()
    today_y=dt.datetime.today().date().year    
    
    if today.month<user_birth.month:
        user_next_birth=dt.datetime(year=today_y, month=user_dt_m, day=user_dt_d, hour=0).date()
        # print (user_next_birth)
        time_diff=user_next_birth - today
        print(f'There is/are {time_diff.days} day/days to your next birthday.')
    elif today.month>user_birth.month:
        user_next_birth=dt.datetime(year=today_y+1, month=user_dt_m, day=user_dt_d, hour=0).date()
        # print (user_next_birth)
        time_diff=user_next_birth - today
        print(f'There is/are {time_diff.days} day/days to your next birthday.')
        #The birtday is in current month:
    elif today.month == user_birth.month and today.day < user_dt_d: 
        user_next_birth=dt.datetime(year=today_y, month=user_dt_m, day=user_dt_d, hour=0).date()
        time_diff=user_next_birth -today
        print(f'There is/are {time_diff.days} day/days to your next birthday.')
    else:
        user_next_birth=dt.datetime(year=today_y+1, month=user_dt_m, day=user_dt_d, hour=0).date()
        # print (user_next_birth)
        time_diff=user_next_birth - today
        print(f'There is/are {time_diff.days} day/days to your next birthday.')

user_next_birth()