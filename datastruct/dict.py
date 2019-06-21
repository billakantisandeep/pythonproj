student = {"Name": "Sandeep", "Age": 25, "courses": ["Math", "Compsci"]}
student["phone"] = 5555
student["Name"] = "udvi"
student.update({"Name": "teju", "Age": 28})
print(student)
print(student["courses"])
print(
    student.get("phone1", "Notfound")
)  # It gives the output as none if key doesnt exist instead of errror
print(len(student))
print(student.values())
print(student.keys())
print(student.items())
# For printing either key or values in the dict
# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)

for key, value in student.items():
    print(key, value)
# Key-values paris can be anything like integers,strings, list etc..
