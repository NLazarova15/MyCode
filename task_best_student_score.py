#From student_scores data, create a new data structure named best_students_scores, 
# storing the information (name and score) only for students with scores greater than 4.00

student_score={
    'Ivan': 5.00,
    'Alex': 3.50,
    'Maria': 5.50,
    'Georgi': 5.00
}

for k,v in student_score.items():
    if v>4.00:
        best_students_scores = print(f'{k} - {v}')     

