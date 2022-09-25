import json

f = open('school.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
print(data["classes"]["students"]["2"]["spes"][1])
f.close()