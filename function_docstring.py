def print_max(x, y):
    ''' Prints max of the two numbers
    The two values should be the integers.  '''

    #Convert to the integers

    x = int(x)
    y = int(y)

    if x > y:
        print(x , 'is max')
    else: 
        print(y, ' is max')

print_max(3, 5)
print(print_max.__doc__)
