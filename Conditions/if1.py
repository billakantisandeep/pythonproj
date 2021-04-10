# Usage of is-operator

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(id(a))
print(id(b))

if a is b:
    print("True")
else:
    print("Change the ID")

# If you want to see the memory ID
b = a
print(id(a))
print(id(b))
if a is b:
    print("True")
else:
    print("Check the id")
