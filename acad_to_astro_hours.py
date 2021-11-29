# Print out how many astronomical hours a python course should take, if it consists of 64 academical hours, including the respective brakes
# For each 3 academical hours there are 15 minutes brake
astro_hour=60
acad_hours=40
brake_min=15
all_acad_hours=64
all_astro_hour=(all_acad_hours*40+(all_acad_hours*15)/3)/60
print(f'All astronomical hours = {all_astro_hour}')