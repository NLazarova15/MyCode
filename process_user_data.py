import json
from statistics import mean
from operator import itemgetter

input_file='users.json'

def print_all_users():
    f=open(input_file,mode='r')  
    data=json.load(f)
    # print(data)
    for el in data:
        print(el["name"])
    f.close()


def average_users():
    f=open(input_file,mode='r')   
    data=json.load(f)
    # print(data)
    for el in data:
        l=int(el['age'])
        # print(mean(str(l)))
        print(l)
    f.close()

def users_city(city):
    f=open(input_file,mode='r')   
    data=json.load(f)
    for el in data:
        if city==(el['city']):
            print(el)     
    f.close()


def users_sort():
    f=open(input_file,mode='r')   
    data=json.load(f)
    for el in sorted(data,key=itemgetter("name")):
        print(el)
    f.close()

x=int(input("input from 1 to 5: "))
if x==1:
    print_all_users()
elif x==2:
    average_users()
elif x==3:
    city='London' #input("input city: ") #
    users_city(city)
elif x==4:   
    users_sort()
elif x==5:
    exit
