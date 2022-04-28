import json

# users={'name':'',
# 'age':'',
# 'city':''}
# l=[]
# while input("Enter new user data [y/n]?: y") =='y':
#     user_name=input("Enter your name")
#     user_age=input('Enter your age') 
#     user_city=input("Enter your city")
#     users['name']=user_name
#     users['age']=user_age
#     users['city']=user_city
    
# print(users)

users=[
    {'name': 'Pier', 
    'age':40,
    'city':'Paris'},

    {'name': 'Jon', 
    'age':25,
    'city':'New York'},

    {'name': 'Sara', 
    'age':45,
    'city':'London'},

    {'name': 'Mary ', 
    'age':30,
    'city':'Paris'},

    {'name': 'Bob', 
    'age':35,
    'city':'London'},

    {'name': 'Mike', 
    'age':50,
    'city':'London'},
]

print(json.dumps(users))
output_file='users.json'

with open(output_file, mode='w') as f:
    json.dump(users, f, indent=2)  