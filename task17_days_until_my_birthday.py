import datetime as dt

#  How days are to your next birthday?
def next_birthday():
    user_next_birth=dt.datetime.strptime(input("Inser your next birthday: dd.mm.YYYY  "), '%d.%m.%Y').date()
    today=dt.datetime.today().date()
    time_diff=user_next_birth - today
    print(time_diff.days)

next_birthday()
