# Print out the name and score of the student with maximum score
# Print out the name and score of the student with minimum score

student_score={
    'Ivan': 5.00,
    'Maria': 5.50,
    'Alex': 3.50,
    'Georgi': 5.00
}


max_score=max(student_score.values())
# print(max_score)

min_score=min(student_score.values())
# print(min_score)


for k, v in student_score.items():
    if v== min_score:   # min(student_score.values()):       
        k_min=k
        v_min=v
print('The student with minimum score is ' f'{k_min} - {v_min}')
    
for k1, v1 in student_score.items():
    if v1 == max_score:
        k_max=k1
        v_max=v1
print('The student with maximum score is ' f'{k_max} - {v_max}')


    
