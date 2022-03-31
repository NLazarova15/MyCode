#  Given is next JSON file: pythonbooks.revolunet.com.issues.json, 
# which contains information about the books listed in pythonbooks.revolunet.com

# Make a program, that will extract from these data only the "title", "author" and "url" fields for the books labeled
# as "Advanced", and will print the extracted information, as shown in sample output

import json

# JSON file
f = open ('.\pythonbooks.json', "r")
 
# Reading from file
data = json.loads(f.read())
 
# Iterating
for i in data['books']:
    for key, value in i.items():
        if key=='level' and value=='Advanced':
            print(i['title'],',',i['author'],',',i['url'])
 
# Closing file
f.close()