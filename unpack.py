#Normal
items = ( 1, 2)
print(items)

#unpacking
a, b =(1 ,2)
print(a)
print(b)

#now we just want to ignore b we just want a.
a, _ =(1, 2)
print(a)

# _ is the way of telling we are not using the variable anywhere in the code.

#More variables or more values is causing the issue.

a, b, *c = ( 1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

#If we are not using the values other than the first two 

a, b, *_ = (1,2,3,4,5,6,7)  #to just take the first two values and ignore the remaining in the code
print(a)
print(b)
