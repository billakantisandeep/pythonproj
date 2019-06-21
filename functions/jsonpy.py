import json
#some json
x = '{"name": John, "age":54, "city":"Newyork"}'

#Parse X
y = json.loads(x)

#The result is a python dict
print(y["age"])