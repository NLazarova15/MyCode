# user_data={
#     'id':
#     'name':
# }

user_data={
    '1': ["Maria", "+39587111111"],
    '2': ["Ivan","+39587222222"],
    '3': ["Asen", "+39587333333"]
}

user_bills={
    '1': 25.50,
    '2': 30.48,
    '3': 5.98
}

max_bill=max(user_bills.values())
min_bill=min(user_bills.values())
# print(max_bill)

for k1,v1 in user_bills.items():
    if v1 == max_bill:    #  max(user_bills.values()): 
        v_max=v1 
        k_max=k1
# print(k_max, v_max)
print('The user with highest bill - ' f'{max_bill}'' is ' f'{user_data[k_max][0]}')   

for k2,v2 in user_bills.items():
    if v2 == min_bill:    #  max(user_bills.values()): 
        v_min=v2 
        k_min=k2
# print(k_min, v_min)
print('The user with lowest bill - ' f'{min_bill}' ' is ' f'{(user_data[k_min][0])}')
    