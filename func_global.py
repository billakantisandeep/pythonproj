x = 50

def fun():
    global x 

    print('x value is ', x)

    x = 2 
    print('x value is ', x)

fun()
print ('the value of x is ', x)